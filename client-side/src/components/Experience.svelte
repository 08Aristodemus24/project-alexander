<script>
    import { createEventDispatcher } from 'svelte';
    import {range} from './Range';

    let curr_year;
    export let max_year;
    export let min_year;

    let dispatch = createEventDispatcher();

    // when user clicks on one of the years this will dispatch an event which will change the
    // state of the year and call the fetch_data function handler again
    const handle_click = (event) => {
        curr_year = event.target.getAttribute('data-year') === "all" ? null : event.target.getAttribute('data-year');
        console.log(curr_year);
        dispatch('changeYear', curr_year);
    }
</script>

<section id="exp-section">
    <div class="exp-content">
        <div class="exp-header-container">
            <h1>Experience</h1>
            {#each range(min_year, max_year + 1, 1) as year}
                <button data-year={year} on:click={handle_click}>{year}</button>
            {/each}
            <button data-year="all" on:click={handle_click}>all</button>    
        </div>
    </div>
</section>