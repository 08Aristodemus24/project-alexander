<script>
    const exp_descriptions = [
        {year: '2022', title: 'X++ Developer', organization: 'Creative Dynamix Solutions, Inc.', accolades: ["Primarily developed reports using the X++ programming language", "Queried data from company database to create reports"]},
        {year: '2023', title: 'AI/ML Subject Matter Expert', organization: 'GDSC PUP (Manila Chapter)', accolades: ["Mentored and guided AI/ML department of org in developing roadmap used by junior AI/ML cadets"]},
        {title: 'Front End Web Developer', organization: 'LMC Engineering Front', accolades: ["Impemented and deployed client-side architecture of our engineering consultancy business firm"]},
        {year: '2024', title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
        {year: '2024', title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
        {title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
        {year: '2025', title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
        {year: '2025', title: 'AI Researcher', organization: 'Deep Mind', accolades: ["Lead a team of ML researchers in conducting an experiment of testing novel language model architectures"]},
    ];

    // determine the number of grid columns based 
    // on length of experience descriptions
    const num_columns = exp_descriptions.length;
    const end_col_index = num_columns + 1;
</script>

<div class="timeline-container" style:--end-col-index={end_col_index}>
    {#each exp_descriptions as exp_desc, index}
        <!-- all odd numbered experiences will have its header on the end of the vertical axis and start of the horizontal axis -->
        <div 
            class="header" class:up={index % 2 === 0} class:down={index % 2 !== 0}
            style:grid-row={index % 2 === 0 ? `${1} / ${2}` : `${3} / ${4}`}
            style:grid-column={`${index + 1} / ${index + 2}`}
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
            style:grid-row={index % 2 === 0 ? `${3} / ${4}` : `${1} / ${2}`}
            style:grid-column={`${index + 1} / ${index + 2}`}
        >
            {#each exp_desc['accolades'] as accolade}
                <li class="accolade">{accolade}</li>
            {/each}
        </ul>
    {/each}
</div>
