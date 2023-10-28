<script>
    import { createEventDispatcher } from 'svelte';
    import {range} from './Range';

    // prop that will be assigned the curr_index
    // of the carousel
    export let curr_index;

    export let max_year;
    export let min_year;
    const years = range(min_year, max_year + 1, 1);

    let curr_year;

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
    {#each years as year, index}
        <button class={`button-${year}`} data-year={year} on:click={handle_click} style:--btn-contrib-animation-order={index}>{year}</button>
    {/each}
    <button class="button-all" data-year="all" on:click={handle_click} style:--btn-contrib-animation-order={years.length}>all</button>
</div>