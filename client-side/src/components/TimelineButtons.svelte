<script>
    import { onMount } from "svelte";
    import { range } from "./Range";

    // a prop representing the parent component state
    // that will be binded to the timeline-buttons offset height
    export let button_carousel_height;

    // prop assigned to the callback that 
    // will handle viewing github contributions
    export let switch_slide;

    // prop that will be assigned the curr_index
    // of the carousel
    export let curr_index;

    const num_rows = 3;
    const num_cols = 14;
</script>

<div class="timeline-buttons" class:active={curr_index === 0} bind:offsetHeight={button_carousel_height}>
    <button class="contribs-button" data-carousel-button="contribs" on:click={switch_slide}>
        View Github contributions
        <table>
            {#each range(0, num_rows) as i}
                {#each range(0, num_cols) as j}
                    <td style:grid-column={`${j + 1} / ${j + 2}`} style:grid-row={`${i + 1} / ${i + 2}`} style:--btn-grid-animation-order={j + i}></td>
                {/each}
            {/each}
        </table>
    </button>
    <a class="cv-button" href="https://raw.githubusercontent.com/08Aristodemus24/auto-job-app-sender/master/documents/simple/Larry_Miguel_R_Cueva_CV.pdf" download="Larry_Miguel_R_Cueva_CV.pdf">
        <span class="cv-header">Download CV</span>
        <span class="download-icon"></span>
    </a>
</div>

