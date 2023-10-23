<script>
    import { range } from "./Range";

    const num_rows = 3;
    const num_cols = 14;
</script>
<button class="contribs-header">
    View Github contributions
    <table>
        {#each range(0, num_rows) as i}
            {#each range(0, num_cols) as j}
                <td style:grid-column={`${j + 1} / ${j + 2}`} style:grid-row={`${i + 1} / ${i + 2}`} style:--btn-grid-animation-order={j + i}></td>
            {/each}
        {/each}
    </table>
</button>