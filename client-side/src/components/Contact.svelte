<script>
    import Form from "./Form.svelte";

    const send_mail = async (event) => {
        const raw_data = event.detail;

        // send here the data from the contact component to 
        // the backend proxy server
        const url = 'http://127.0.0.1:5000/send-mail';
        const response = await fetch(url, {
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': JSON.stringify(raw_data)
        });

        if(response.status === 200){
            for(let key in response){
                console.log(key);
                console.log(response[key]);
            }
            alert(`message has been sent ${response.statusText}`);

        }else{
            console.log(`message submission unsucessful. Response status '${response.status}' occured`);
        }
    };
</script>

<section id="contact-section">
    <div class="contact-content">
        <div class="contact-header-container">
            <h1>Send me a message</h1>
        </div>
        <div class="form-container">
            <Form on:sendMail={send_mail}/>
        </div>
    </div>
</section>