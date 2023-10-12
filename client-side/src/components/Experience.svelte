<script>
    import { onMount } from "svelte";
    import Contributions from "./Contributions.svelte";

    // initially all but user can change this depending
    // on what he wants to view
    let curr_year = null;

    // on moount min year and max year states will only be set once
    let min_year = null;
    let max_year = null;
    let contribs = [];

    const fetch_contribs = async (event) => {
        // upon mounting since user has not chosen a year yet 
        // event will be undefined and then should user click
        // a year only then event is not undefined, .detail can
        // be accessed, and then only can we set its next state
        curr_year = event === undefined ? null : event.detail;

        try{
            const url = `http://127.0.0.1:5000/contribs${curr_year === null ? '' : `/${curr_year}`}`;
            const response = await fetch(url);

            if(response.status === 200){
                console.log("retrieval successful");

                // pass retrieved repositories to another component called
                // Experience.svelte
                const data = await response.json();

                // if and only if upon page load curr_year is null in order
                // to get min and max years but if user requests for a specific
                // year then data does not contain anymore min and max year keys
                // so we only have to confine setting min and max year upon mounting
                if(curr_year === null){
                    min_year = data[0]['min_year'];
                    max_year = data[0]['max_year'];
                }
                contribs = data[0]['contribs'];

            }else{
                console.log(`retrieval unsuccessful. Response status '${response.status}' occured`);
            }

        }catch(error){
            console.log(`request denied. Error '${error}' occured.`);
        }
    }

    // upon mounting of component send http request to flask
    // backend proxy server and retrieve contributions
    onMount(async () => {
        fetch_contribs();
    });
</script>

<section id="exp-section">
    <div class="exp-content">
        <div class="exp-header-container">
            <h1>Experience</h1>
        </div>
        <div class="exp-container">
            <div class="contribs-container">
                <Contributions min_year={min_year} max_year={max_year} contribs={contribs} on:changeYear={fetch_contribs}/>
            </div>
        </div>
    </div>
</section>