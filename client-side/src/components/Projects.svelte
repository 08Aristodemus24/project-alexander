<script>

    let is_opened = false;

    const close_header = (event) => {
        
        // close header only once
        if(is_opened === false){
            is_opened = true;
        }
    }
</script>

<section id="projects-section">
    <div class="projects-content">
        <div class="projects-header-container" class:closed={is_opened === true}>
            <h1>Projects</h1>
            <button on:click={close_header}>See my projects</button>
        </div>
        <div class="projects-accordion-container">
            <slot name="accordion-group"/>    
        </div>
    </div>
</section>