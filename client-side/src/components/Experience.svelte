<script>
    import { afterUpdate, onMount } from "svelte";
    import Contributions from "./Contributions.svelte";
    import Timeline from "./Timeline.svelte";
    import TimelineButtons from './TimelineButtons.svelte';
    import ContributionsButtons from "./ContributionsButtons.svelte";

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
            curr_index = 0;
        }

        // run for precisely 0.5s after is_opened is set to true
        setTimeout(() => {
            console.log("executing display none");
            exp_header_button.style.display = "none";
        }, 500);
    };

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
            // // for development
            // const url = `http://127.0.0.1:5000/contribs${curr_year === null ? '' : `/${curr_year}`}`;
            // for production
            const url = `const url = 'https://project-alexander.vercel.app/contribs${curr_year === null ? '' : `/${curr_year}`}`;
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

    // for setting height of exp-carousel-contaienr with carousel
    // item and  button-carousel-container that has largest height
    // which are the timeline container and contribs container and
    // the timeline buttons and contribs buttons. These parent states
    // will be passed as props and then binded to the child component's
    // offset height
    let exp_carousel_height = null;
    let button_carousel_height = null;

    // initial state of the current index
    let curr_index = -1;

    // binds the inner carousel to this variable
    // instead of using dom api
    let exp_carousel_container;

    // now shoudl new index be now set the active class 
    // will only be added to a slide with a specific index
    const switch_slide = (event) => {
        // access the data-<name> attributes value using
        // an elements .dataset property, because data attribute
        // is named carousel-button we access .carouselButton
        const offset = event.target.dataset.carouselButton === 'contribs' ? 1 : -1;
        console.log(`${offset === 1 ? 'contribs' : 'timeline'} button has been clicked`);

        const carousel_items = [...exp_carousel_container.children];
        const active_slide = carousel_items[curr_index];
        console.log(carousel_items);

        // a + 1 offset means we go forwards in accessing the carousel_items
        // and a + -1 offset means we will go backwards in accessing the carousel_items
        curr_index = carousel_items.indexOf(active_slide) + offset;
        if(curr_index < 0){
            // should new index be of a negative value we go to the last slide
            curr_index = carousel_items.length - 1;

        }else if(curr_index >= carousel_items.length){
            curr_index = 0;
        }
    }

    // on mount initially set state of null for the exp content
    // and exp header container centers will now have calculated
    // values of each of their respective center coordinates
    onMount(async () => {
        fetch_contribs();
        exp_content_values = get_elem_vals(exp_content);
    });

    afterUpdate(async () => {
        console.log("component updated");
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
        <div class="exp-carousel-container" style:height={`${exp_carousel_height}px`} bind:this={exp_carousel_container}>
            <Timeline bind:exp_carousel_height curr_index={curr_index}/>
            <Contributions contribs={contribs} curr_index={curr_index}/>
        </div>
        <div class="button-carousel-container" style:height={`${button_carousel_height}px`}>
            <TimelineButtons bind:button_carousel_height switch_slide={switch_slide} curr_index={curr_index}/>
            <ContributionsButtons min_year={min_year} max_year={max_year} on:changeYear={fetch_contribs} switch_slide={switch_slide} curr_index={curr_index}/>
        </div>
    </div>
</section>