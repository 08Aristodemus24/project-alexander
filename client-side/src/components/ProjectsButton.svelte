<script>
    import { range } from "./Range";

    export let close_header;

    const num_bars = 6;
</script>

<button on:click={close_header} class="projects-button">
    See my projects
    <table>
        {#each range(0, num_bars) as i}
            <td style:grid-column={`${i + 1} / ${i + 2}`} style:--btn-bar-animation-order={i}></td>
        {/each}
    </table>
</button>