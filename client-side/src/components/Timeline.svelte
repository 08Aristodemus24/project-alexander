<script>
    import { afterUpdate } from "svelte";

    const exp_descriptions = [
        {year: '2022', title: 'X++ Developer', organization: 'Creative Dynamix Solutions, Inc.', accolades: ["Primarily developed reports using the X++ programming language", "Queried data from company database to create reports"]},
        {year: '2023', title: 'AI/ML Subject Matter Expert', organization: 'GDSC PUP (Manila Chapter)', accolades: ["Mentored and guided AI/ML department of org in developing roadmap used by junior AI/ML cadets"]},
        {title: 'Machine Learning Engineer', organization: 'Turing', accolades: ["Built recommendation models that helped increase customer satisfaction by 75%"]},
        {year: '2024', title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
        {year: '2024', title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
        {title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
        {year: '2025', title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
    ];

    // initially define width and height offsets as null for this
    // will be changed as size of the timeline-item header changes
    let header_size_offsets = exp_descriptions.map(() => ({offset_width: null, offset_height: null}));
    let accolades_size_offsets = exp_descriptions.map(() => ({offset_width: null, offset_height: null}));
    
    let header_max_width = null;
    let header_max_height = null;
    let accolades_max_width = null;
    // let accolades_max_height = null;

    afterUpdate(() => {
        /* 
        because upon mounting binded properties to state variables are triggered 
        in the carousel items and therefore triggeres a state update we also
        calculate right then adn there the maximum of the offset heights and widths
        in the newly updated size_offsets array
        again after changing state of dynamic max content and fit content values
        of height and width by resizing window calculate the max height and width
        and change the previous max height and width states 
        */
        header_max_height = Math.max(...header_size_offsets.map((timeline_item_header_offset) => timeline_item_header_offset['offset_height']));
        header_max_width = Math.max(...header_size_offsets.map((timeline_item_header_offset) => timeline_item_header_offset['offset_width']));
        // accolades_max_height = Math.max(...accolades_size_offsets.map((timeline_item_accolades_offset) => timeline_item_accolades_offset['offset_height']));
        accolades_max_width = Math.max(...accolades_size_offsets.map((timeline_item_accolades_offset) => timeline_item_accolades_offset['offset_width']));
    });
</script>
<div class="timeline-container">
    <!-- {#each exp_descriptions as exp_desc, index}
        <div class="timeline-item" class:up={index % 2 === 0} class:down={index % 2 !== 0}>
            <div class="header" style:min-height={`${header_max_height}px`} style:width={`${header_max_width}px`} bind:offsetWidth={header_size_offsets[index].offset_width} bind:offsetHeight={header_size_offsets[index].offset_height}>
                <h3 class="title">{exp_desc['title']}</h3>
                <h5 class="organization">{exp_desc['organization']}</h5>
                {#if exp_desc['year'] !== undefined}
                    <h3 class="year">{exp_desc['year']}</h3>
                {/if}                        
            </div>

            <div class="bar"></div>

            <ul class="accolades" style:width={`${accolades_max_width}px`} bind:offsetWidth={accolades_size_offsets[index].offset_width} bind:offsetHeight={accolades_size_offsets[index].offset_height}>
                {#each exp_desc['accolades'] as accolade}
                    <li class="accolade">{accolade}</li>
                {/each}
            </ul>
        </div>
    {/each} -->
    
    {#each exp_descriptions as exp_desc, index}
        <div 
            class="header" class:up={index % 2 === 0} class:down={index % 2 !== 0}
            style:min-height={`${header_max_height}px`}
            style:width={`${header_max_width}px`}
            style:grid-row={index % 2 === 0 ? `${1} / ${2}` : `${3} / ${4}`}
            style:grid-column={`${index + 1} / ${index + 2}`}
            style:align-self={index % 2 === 0 ? `end` : `start`}
            
            bind:offsetWidth={header_size_offsets[index].offset_width} 
            bind:offsetHeight={header_size_offsets[index].offset_height}
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
        ></div>
        <ul
            class="accolades" class:up={index % 2 === 0} class:down={index % 2 !== 0}
            style:width={`${accolades_max_width}px`} 
            style:grid-row={index % 2 === 0 ? `${3} / ${4}` : `${1} / ${2}`}
            style:grid-column={`${index + 1} / ${index + 2}`}
            style:align-self={index % 2 === 0 ? `start` : `end`}
            bind:offsetWidth={accolades_size_offsets[index].offset_width} 
            bind:offsetHeight={accolades_size_offsets[index].offset_height}
        >
            {#each exp_desc['accolades'] as accolade}
                <li class="accolade">{accolade}</li>
            {/each}
        </ul>
    {/each}
</div>
