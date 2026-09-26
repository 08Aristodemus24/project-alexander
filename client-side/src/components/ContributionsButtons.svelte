<script>
    import { createEventDispatcher } from 'svelte';
    import {range} from './Range';

    // prop that will be assigned the curr_index
    // of the carousel
    export let curr_index;

    // props are states of the parent experience component
    export let max_year;
    export let min_year;

    // years depends on the state of the parents max_year 
    // and min_year so specify dollar sign
    $:years = range(min_year, max_year + 1, 1);

    let curr_year;

    export let switch_slide;

    let dispatch = createEventDispatcher();

    // when user clicks on one of the years this will dispatch an event which will change the
    // state of the year and call the fetch_data function handler again
    const handle_click = (event) => {
        curr_year = event.target.getAttribute('data-year') === "all" ? null : event.target.getAttribute('data-year');
        console.log(curr_year);
        dispatch('changeYear', curr_year);
    };
</script>
<div class="contribs-buttons" class:active={curr_index === 1}>
    <button class="button-back" on:click={switch_slide} data-carousel-button="timeline" style:--btn-contrib-animation-order={0}>back</button>
    {#each years as year, index}
        <button class={`button-${year}`} data-year={year} on:click={handle_click} style:--btn-contrib-animation-order={index + 1}>{year}</button>
    {/each}
    <button class="button-all" data-year="all" on:click={handle_click} style:--btn-contrib-animation-order={years.length + 1}>all</button>
</div>