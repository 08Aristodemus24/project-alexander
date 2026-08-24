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
        {year: '2022', title: 'X++ Developer', organization: 'Creative Dynamix Solutions, Inc.', accolades: [
            "Developed and queried data to enhance sales reporting using Power BI and X++, streamlining reporting turnaround for [ ]+ recurring sales reports",
            "Queried and transformed data from the company's ERP database to build production-ready X++ reports consumed by [ ]+ sales/ops stakeholders",
            "Utilized AnyDesk to tunnel into a remote virtual machine environment for day-to-day report development and deployment tasks"
        ]},
        {title: 'AI/ML Subject Matter Expert', organization: 'GDSC PUP (Manila Chapter)', accolades: ["Currently mentoring and guiding GDSC-PUP's AI/ML department in developing roadmap to be used by junior AI/ML cadets"]},
        {year: '2024', title: 'Data Engineer Intern', organization: 'Virtuals Protocol', accolades: [
            "Cleaned and processed more than 500k rows of data for various retrieval augmented generation (RAG) AI agents",
            "Developed and wrote scripts automating data ingestion processes for RAG AI agents, pulling raw datasets uploaded by users to offload the main workflow to data transformation"
        ]},
        {title: 'Customer Support', organization: 'Virtuals Protocol', accolades: 
            [
                "Addressed technical issues faced by clients in building RAG AI agents",
                "Debugged automatic HTTP requests from agents to the X/Twitter API endpoints",
                "Created guides for clients/builders on custom agent functionalities, e.g. automatic image generation via the OpenAI API, posting tweets via the X API",
                "Enabled agents to interact automatically with X users, contributing to increased market capital"
            ]},
        {year: '2025', title: 'Data & Analytics Engineer', organization: 'ACEN Corporation', accolades: [
            "Architected an ELT pipeline ingesting quarterly cost data across 3 fiscal years, 16+ workstreams, and 4 cost categories into Snowflake, replacing a fully manual Excel-driven process for FP&A",
            "Built a 3-layer dbt pipeline (staging → intermediate → marts) with SCD Type 2 dimensions, surfaced in a Power BI dashboard for FP&A and CFO-level stakeholders",
            "Spearheading a SharePoint Lists → MS Graph API → Snowflake redesign of the cost pipeline, delivering Snowflake Intelligence Agents as a self-service interface for FP&A",
            "Replaced a paid Fivetran connector with a custom REST API integration, eliminating recurring SaaS spend entirely ($0 ingestion cost)",
            "Automated ingestion of IT tickets, Microsoft user data, and dbt metadata into Snowflake, enabling real-time analytics across 5+ IT teams processing thousands of records daily",
            "Built an ML time-series model forecasting IT ticket volumes 1–6 months ahead to support proactive resource planning",
            "Contributed to Project Apollo's SAP ERP pipeline, standardizing 14 source table schemas and implementing MD5-hashed MERGE logic for idempotent incremental loads"
        ]},
        {title: 'AI-900: Microsoft Azure AI Fundamentals', organization: 'Microsoft Certification', accolades: ["Passed the AI-900: Microsoft Azure AI Fundamentals certification exam"]},
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
