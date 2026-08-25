# Sending Mail via the Gmail API Instead of EmailJS

This replaces your EmailJS proxy call with a direct call to the Gmail API, authenticated
as your own Gmail account via OAuth 2.0.

**Note on approach:** Since you're sending *as* a personal Gmail address (not a Google
Workspace domain), the practical path is a one-time OAuth consent that produces a
long-lived **refresh token**, which your Flask app then uses forever after (no service
account / domain-wide delegation needed — that only works for Workspace accounts).

---

## 1. Create/select a Google Cloud project

1. Go to [console.cloud.google.com](https://console.cloud.google.com/)
2. Top-left project dropdown → **New Project** (or select an existing one)
3. Name it something like `project-alexander-mailer`

## 2. Enable the Gmail API

1. In the left sidebar: **APIs & Services → Library**
2. Search for **Gmail API**
3. Click it → **Enable**

## 3. Configure the OAuth consent screen

1. **APIs & Services → OAuth consent screen**
2. User type: **External** (unless you have Workspace)
3. Fill in required fields (app name, your email as support contact)
4. Scopes: add `https://www.googleapis.com/auth/gmail.send`
5. Test users: add the Gmail address you'll be sending *from* (your own address)
6. Save — you don't need Google's app verification since you're the only user

## 4. Create OAuth 2.0 credentials

1. **APIs & Services → Credentials → Create Credentials → OAuth client ID**
2. Application type: **Web application**
3. Under **Authorized redirect URIs**, add:
   `https://developers.google.com/oauthplayground`
4. Save. Copy the **Client ID** and **Client secret** — these become
   `GMAIL_CLIENT_ID` and `GMAIL_CLIENT_SECRET`.

No JSON download or local script needed for this route — the token is generated
entirely through Google's own OAuth Playground, no libraries installed on your
machine.

## 5. Generate a refresh token via the OAuth Playground (one-time)

You only do this once — it's how your server proves "I'm allowed to send from
Michael's Gmail" without ever asking anyone to log in again.

1. Open [developers.google.com/oauthplayground](https://developers.google.com/oauthplayground).
2. Click the ⚙️ gear (top right) → check **"Use your own OAuth credentials"**
   → paste in the Client ID and Client secret from step 4.
3. In the left panel, find **Gmail API v1** → select the scope
   `https://www.googleapis.com/auth/gmail.send` → **Authorize APIs**.
4. Sign in with the Gmail account you want to send *from* and accept.
5. Click **Exchange authorization code for tokens**.
6. Copy the **Refresh token** shown — this becomes `GMAIL_REFRESH_TOKEN`.
   It doesn't expire from just sitting unused, so you only need to do this once
   (see the troubleshooting table at the end for the one case where it does).

## 6. Store credentials as environment variables

Wherever you currently have `SERVICE_ID`, `TEMPLATE_ID`, etc. (locally in `.env`, and
in Vercel's project settings under **Environment Variables**), add:

```
GMAIL_CLIENT_ID=<from step 4>
GMAIL_CLIENT_SECRET=<from step 4>
GMAIL_REFRESH_TOKEN=<from step 5>
GMAIL_SENDER=<the Gmail address you're sending from>
GMAIL_RECEIVER=<the address you want the form submissions sent to>
```

`.gitignore` should already exclude `.env` — never commit the real file. If you
deploy to Vercel, set these same five as **environment variables in the Vercel
dashboard**, not in code — `.env` files aren't uploaded on most platforms.

You can delete the old `SERVICE_ID`, `TEMPLATE_ID`, `PUBLIC_KEY`, `PRIVATE_KEY` vars
once the migration is done.

## 7. Add the Python dependencies to your server

Add to `requirements.txt`:

```
google-auth
google-auth-httplib2
google-api-python-client
```

## 8. Update `server.py`

Add these imports near the top of your file:

```python
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
```

Add a helper to build an authenticated Gmail service from your stored refresh token:

```python
def get_gmail_service():
    """
    Rebuilds Gmail API credentials from the long-lived refresh token
    stored in environment variables, then returns an authorized
    Gmail API client.
    """
    creds = Credentials(
        token=None,
        refresh_token=os.environ['GMAIL_REFRESH_TOKEN'],
        client_id=os.environ['GMAIL_CLIENT_ID'],
        client_secret=os.environ['GMAIL_CLIENT_SECRET'],
        token_uri='https://oauth2.googleapis.com/token',
        scopes=['https://www.googleapis.com/auth/gmail.send'],
    )
    return build('gmail', 'v1', credentials=creds)
```

Add a helper to build the message from your form's raw data:

```python
def build_message(raw_data):
    """
    Formats the form submission into an email addressed to
    GMAIL_RECEIVER, with the submitter's email set as reply-to
    so you can just hit "reply" in your inbox.
    """
    body = (
        f"First name: {raw_data.get('first_name')}\n"
        f"Last name: {raw_data.get('last_name')}\n"
        f"Email: {raw_data.get('email_address')}\n"
        f"Phone: {raw_data.get('country_code')} {raw_data.get('mobile_num')}\n\n"
        f"Message:\n{raw_data.get('message')}"
    )

    message = MIMEText(body)
    message['to'] = os.environ['GMAIL_RECEIVER']
    message['from'] = os.environ['GMAIL_SENDER']
    message['subject'] = f"New form submission from {raw_data.get('first_name')} {raw_data.get('last_name')}"
    message['reply-to'] = raw_data.get('email_address')

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}
```

Replace your `send_mail` route body with:

```python
@app.route('/send-mail', methods=['POST'])
def send_mail():
    """
    Catches the HTTP POST request from the form in the front end
    and sends the submission as an email via the Gmail API.
    """
    raw_data = request.json
    print(type(raw_data))
    print(raw_data)

    try:
        service = get_gmail_service()
        message = build_message(raw_data)
        service.users().messages().send(userId='me', body=message).execute()

        print('submission successful')
        return json.dumps(({'success': True, 'message': 'submission successful'}, 200, {'Content-Type': 'application/text'}))

    except Exception as e:
        print(f'submission unsuccessful.\nerror: {e}')
        return json.dumps(({'success': False, 'message': 'submission unsuccessful'}, 500, {'Content-Type': 'application/text'}))
```

You can now remove the `requests`-based call to `api.emailjs.com` and the
`SERVICE_ID` / `TEMPLATE_ID` / `PUBLIC_KEY` / `PRIVATE_KEY` env vars entirely.

---

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| `invalid_grant` when refreshing the token | Refresh token was revoked, or the OAuth consent screen is still in "Testing" mode and fell out of authorization — re-add yourself as a test user (or publish to production) and re-run step 5 |
| `redirect_uri_mismatch` in the Playground | The redirect URI in your OAuth client doesn't exactly match `https://developers.google.com/oauthplayground` |
| Email never arrives | Check spam first; confirm `GMAIL_RECEIVER` is correct and the request actually reached `messages().send()` (check your server logs) |
| 401/403 from the Gmail API | `GMAIL_CLIENT_ID`/`SECRET` don't match the ones used to generate the refresh token in step 5 |
| Works locally, fails when deployed | Env vars weren't set in the Vercel dashboard — `.env` files aren't uploaded on most platforms |

A couple of things worth knowing beyond the table:

- **Sending address**: Gmail API sends as whatever Gmail account owns the refresh
  token (`GMAIL_SENDER`) — it can't spoof arbitrary "from" addresses like EmailJS'
  template variables could. The submitter's email goes in `reply-to` instead, which is
  the recommended pattern.
- **Vercel + Flask**: if your Flask app is deployed to Vercel as a serverless function,
  confirm `google-api-python-client`'s dependencies fit within Vercel's function size
  limits — it's a reasonably heavy library.
