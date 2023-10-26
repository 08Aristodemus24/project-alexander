<script>
    import { afterUpdate, onMount } from "svelte";
    import Contributions from "./Contributions.svelte";
    import Timeline from "./Timeline.svelte";
    import ContribsButton from "./ContribsButton.svelte";
    import CvButton from "./CVButton.svelte";

    // when component is mounted get experience content elements
    // bounding rectangle and client width and height to compute
    // distance from top
    let exp_content;
    let exp_content_values;
    let exp_header_button, header_height;
    
    // for header
    let is_opened = false;
    const close_header = (event) => {
        // close header only once
        if(is_opened === false){
            is_opened = true;
        }
    };


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

    const get_elem_vals = (el) => {
        let rect = {};
        const box = el.getBoundingClientRect();

        rect['center_x'] = (el.clientWidth) / 2;
        rect['center_y'] = (el.clientHeight) / 2;
        rect['client_width'] = el.clientWidth;
        rect['client_height'] = el.clientHeight;
        rect['offset_left'] = el.offsetLeft;
        rect['offset_top'] = el.offsetTop;
        rect['client_top'] = box.top;

        return rect;
    }

    // on mount initially set state of null for the exp content
    // and exp header container centers will now have calculated
    // values of each of their respective center coordinates
    onMount(async () => {
        fetch_contribs();
        exp_content_values = get_elem_vals(exp_content);
    });

    afterUpdate(async () => {
        if(is_opened === true){
            setTimeout(() => {
                // remove projects-header-container from dom precisely 
                // 0.5s after visibility and opacity transition is ran
                exp_header_button.style.display = "none";
            }, 500);
        }
    });
</script>

<svelte:window on:resize={() => {
    /*
    when window resizes we always calculate the state of the binded elements
    current center coordinates, since their top, left, bottom, and right,
    properties will always change 
    */
    exp_content_values = get_elem_vals(exp_content);
}}/>

<section id="exp-section">
    <div class="exp-content" bind:this={exp_content}>
        <div 
            class="exp-header-container"
            class:closed={is_opened === true} 
            style:height={`${header_height}px`}
        >
            <div class="wrapper" style:--top-value={`${exp_content_values?.center_y}px`}>
                <h1 class="exp-header" bind:offsetHeight={header_height}>Experience</h1>
                <button class="exp-header-button" on:click={close_header} bind:this={exp_header_button}>View time sequence</button>
            </div>
        </div>
        <Timeline/>
        <Contributions min_year={min_year} max_year={max_year} contribs={contribs} on:changeYear={fetch_contribs}/>
        <ContribsButton/>
        <CvButton/>
    </div>
</section>

<!-- <h3>View my github contributions</h3>
<Contributions min_year={min_year} max_year={max_year} contribs={contribs} on:changeYear={fetch_contribs}/> -->