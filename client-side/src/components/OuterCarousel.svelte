<script>
    export let curr_index;
</script>
<div class="carousel-outer">
    
    <h1 class="main-title" class:active={curr_index === 0}>Skills</h1>
    <span class="de-skills-title" class:active={curr_index === 1}>Data Engineering</span>
    <span class="dva-skills-title" class:active={curr_index === 2}>Data Analytics</span>
    <span class="ml-skills-title" class:active={curr_index === 3}>Machine Learning & Deep Learning</span>
    <span class="dva-skills-title" class:active={curr_index === 4}>Cloud & DevOps</span>
    <span class="csswd-skills-title" class:active={curr_index === 5}>Client & Server Side Web Development</span>
    <span class="misc-skills-title" class:active={curr_index === 6}>Miscellaneous</span>
</div>