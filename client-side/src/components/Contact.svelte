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
                <div class="name-group-container">
                    <div class="first-name-container">
                        <label for="first-name" class="first-name-label">First name</label>
                        <input type="text" name="first-name" id="first-name" class="fname-field" placeholder="Larry Miguel" required />
                    </div>
                    <div class="last-name-container">
                        <label for="last-name" class="last-name-label">Last name</label>
                        <input type="text" name="last-name" id="last-name" class="lname-field" placeholder="Cueva" required />
                    </div>
                </div>
                <div class="email-container">
                    <label for="email-address" class="email-label">Email</label>
                    <input type="email" name="email-address" id="email-address" class="email-field" placeholder="MichaelAveuc571@gmail.com" required />
                </div>
                <div class="caller-info-container">
                    <label for="country-code" class="country-code-label">Country Code</label>
                    <select name="country-code" id="country-code" class="country-code-field">
                        {#each countries as country}
                            <option value={country['dial_code']} label={`${country['code']} (${country['dial_code']})`} data-country-name={country['name']} data-country-code={country['code']} data-dial-code={country['dial_code']}></option>
                        {/each}
                    </select>
                    <label for="mobile-number" class="mobile-number-label">Phone</label>
                    <input type="tel" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" name="mobile-number" id="mobile-number" class="mobile-number-field" placeholder="970-745-1021"/>
                </div>
                <div class="message-container">
                    <label for="message" class="message-label">Message</label>
                    <textarea id="message" rows="5" class="message-field" placeholder="Leave a comment..."></textarea>
                </div>
                <button type="submit" class="submit-btn">Submit</button>
            </form>
        </div>
    </div>
</section>