<script>
    import { range } from "./Range";

    export let button_carousel_height;

    const num_rows = 3;
    const num_cols = 14;
</script>

<div class="timeline-buttons" bind:offsetHeight={button_carousel_height}>
    <button class="contribs-button">
        View Github contributions
        <table>
            {#each range(0, num_rows) as i}
                {#each range(0, num_cols) as j}
                    <td style:grid-column={`${j + 1} / ${j + 2}`} style:grid-row={`${i + 1} / ${i + 2}`} style:--btn-grid-animation-order={j + i}></td>
                {/each}
            {/each}
        </table>
    </button>
    <a class="cv-button" href="https://drive.google.com/uc?export=download&id=1s36RyoYfjZOtEAxKcF4hchcIuXBYdAzu" download="Larry Miguel R. Cueva Resume">
        <span class="cv-header">Download my cv</span>
        <span class="download-icon"></span>
    </a>
</div>

