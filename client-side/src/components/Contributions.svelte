<script>
    // props that will be assigned the contributions fetched by the parent
    export let contribs;

    // prop that will be assigned the curr_index
    // of the carousel
    export let curr_index;

    let curr_year;

    // binds the contribs container to this variable
    let contribs_container;

    // this callback is triggered when timeline container is 
    // scrolled over and 
    const scroll_x = (event) => {
        // prevents typical vertical scrolling
        // when on the element
        event.preventDefault();
        contribs_container.scrollLeft += event.deltaY;

        if(event.deltaY >= -15 && event.deltaY <= 15){
            contribs_container.scrollLeft += (event.deltaY * 40);
        }
        
        else{
            contribs_container.scrollLeft += (event.deltaY * 5);
        }
    };
</script>

<div 
    class="contribs-container" 
    class:active={curr_index === 1} 
    bind:this={contribs_container} 
    on:wheel={scroll_x}
>
    <table class="contribs-table">
        <tbody class="contribs-body">
            {#if contribs.length === 0}
                <td class="empty-contribs">empty</td>
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
        </tbody>
    </table>
</div>
