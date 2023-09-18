<script>
    import { onMount, onDestroy } from "svelte";

    let countries = [];

    onMount(async () => {
        const url = 'https://gist.githubusercontent.com/anubhavshrimal/75f6183458db8c453306f93521e93d37/raw/f77e7598a8503f1f70528ae1cbf9f66755698a16/CountryCodes.json';
        const response = await fetch(url);

        if(response.status === 200){
            console.log("retrieval successful");

            const data = await response.json();

            // returned data list consists of dictionaries containing
            // keys name, dial_code, and code e.g. 'Afghanistan', '+93', 'AF'
            countries = [...data];
            console.table(countries);

        }else{
            console.log(`retrieval unsuccessful. Response status ${response.status} occured`)
        }
    });
</script>

<section id="contact-section">
    <div class="contact-content">
        <div class="header-container">
            <h1>Send me a message</h1>
        </div>
        <div class="form-container">
            <form class="form" action="/" method="post">
                <div class="fname-container">
                    <label for="first-name" class="fname-label">First name</label>
                    <input type="text" name="first-name" id="first-name" class="fname-field" placeholder="Larry Miguel" required />
                </div>
                <div class="lname-container">
                    <label for="last-name" class="lname-label">Last name</label>
                    <input type="text" name="last-name" id="last-name" class="lname-field" placeholder="Cueva" required />
                </div>
                <div class="email-container">
                    <label for="email-address" class="email-label">Email</label>
                    <input type="email" name="email-address" id="email-address" class="email-field" placeholder="MichaelAveuc571@gmail.com" required />
                </div>
                <div class="country-code-container">
                    <label for="country-code" class="country-code-label">Country Code</label>
                    <select name="country-code" id="country-code" class="country-code-field">
                        {#each countries as country}
                            <option value={country['dial_code']} label={`${country['name']} (${country['dial_code']})`} data-country-name={country['name']} data-country-code={country['code']} data-dial-code={country['dial_code']}></option>
                        {/each}
                    </select>
                </div>
                <div class="mobile-num-container">
                    <label for="mobile-number" class="mobile-num-label">Phone</label>
                    <input type="tel" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" name="mobile-number" id="mobile-number" class="mobile-num-field" placeholder="XXX-XXX-XXXX"/>
                </div>
                <div class="message-container">
                    <label for="message" class="message-label">Message</label>
                    <textarea id="message" rows="5" class="message-field" placeholder="Your message here"></textarea>
                </div>
                <button type="submit" class="submit-btn">Submit</button>
            </form>
        </div>
    </div>
</section>