<script>
    let curr_year;
    export let contribs;
</script>

<div class="contribs-container">
    <table class="contribs-table">
        {#if contribs.length === 0}
            <div class="empty-contribs">empty</div>
        {:else}    
            {#key curr_year}
                {#each contribs as row, i}
                    <tr class="contribs-row">
                        {#each row as data, j}
                            <td class="contribs-cell" data-level={data['level']} style:--exp-animation-order={j + i}></td>
                        {/each}
                    </tr>
                {/each}
            {/key}
        {/if}
    </table>
</div>
