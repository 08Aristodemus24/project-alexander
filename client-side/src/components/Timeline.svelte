<script>
    // binds the timeline container to this variable in order
    // access element and element attributes
    let timeline_container;

    // binds the offset height of the timeline container to this
    // variable to lift state and set dynamically the height of
    // exp carousel container
    export let exp_carousel_height;

    // prop that will be assigned the curr_index
    // of the carousel
    export let curr_index;

    const exp_descriptions = [
        {year: '2022', title: 'X++ Developer', organization: 'Creative Dynamix Solutions, Inc.', accolades: ["Primarily developed reports using the X++ programming language", "Queried data from company database to create reports"]},
        {year: '2023', title: 'Full Stack Web Developer', organization: 'LMC Engineering Front', accolades: ["Currently building client-side and server-side architecture of our engineering consultancy business firm"]},
        {title: 'AI/ML Subject Matter Expert', organization: 'GDSC PUP (Manila Chapter)', accolades: ["Currently mentoring and guiding GDSC-PUPs AI/ML department in developing roadmap to be used by junior AI/ML cadets"]},
        // {year: '2024', title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
        // {year: '2024', title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
        // {title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
        // {year: '2025', title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
        // {year: '2025', title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
    ];

    // determine the number of grid columns based 
    // on length of experience descriptions
    const num_columns = exp_descriptions.length + 1;
    const end_col_index = num_columns + 1;

    // this callback is triggered when timeline container is 
    // scrolled over and 
    const scroll_x = (event) => {
        // prevents typical vertical scrolling
        // when on the element
        timeline_container.scrollLeft += event.deltaY;

        if(event.deltaY >= -15 && event.deltaY <= 15){
            timeline_container.scrollLeft += (event.deltaY * 40);
        }
        
        else{
            timeline_container.scrollLeft += (event.deltaY * 5);
        }
    }
</script>

<div 
    class="timeline-container"
    class:active={curr_index === 0}
    style:--end-col-index={end_col_index}
    on:wheel|preventDefault={scroll_x} 
    bind:this={timeline_container} 
    bind:offsetHeight={exp_carousel_height}
>
    {#each exp_descriptions as exp_desc, index}
        <!-- all odd numbered experiences will have its header on the end of the vertical axis and start of the horizontal axis -->
        <div 
            class="header" class:up={index % 2 === 0} class:down={index % 2 !== 0}
            style:grid-row={index % 2 === 0 ? `${1} / ${2}` : `${3} / ${4}`}
            style:grid-column={`${index + 1} / ${index + 2}`}
            style:--time-animation-order={index}
        >
            <h3 class="title">{exp_descriptions[index]['title']}</h3>
            <h5 class="organization">{exp_descriptions[index]['organization']}</h5>
            {#if exp_descriptions[index]['year'] !== undefined}
                <h3 class="year">{exp_descriptions[index]['year']}</h3>
            {/if}                 
        </div>
        <div 
            class="bar"
            style:grid-row={`${2} / ${3}`}
            style:grid-column={`${index + 1} / ${index + 2}`}
            style:--time-animation-order={index}
        ></div>
        <ul
            class="accolades" class:up={index % 2 === 0} class:down={index % 2 !== 0}
            style:grid-row={index % 2 === 0 ? `${3} / ${4}` : `${1} / ${2}`}
            style:grid-column={`${index + 1} / ${index + 2}`}
            style:--time-animation-order={index}
        >
            {#each exp_desc['accolades'] as accolade}
                <li class="accolade">{accolade}</li>
            {/each}
        </ul>
    {/each}
</div>
