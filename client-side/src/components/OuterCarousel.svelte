<script>
    export let curr_index;
</script>
<div class="carousel-outer">
    
    <h1 class="main-title" class:active={curr_index === 0}>Skills</h1>
    <span class="ml-skills-title" class:active={curr_index === 1}>Machine Learning & Deep Learning</span>
    <span class="dva-skills-title" class:active={curr_index === 2}>Data Visualization & Analysis</span>
    <span class="csswd-skills-title" class:active={curr_index === 3}>Client & Server Side Web Development</span>
    <span class="misc-skills-title" class:active={curr_index === 4}>Miscellaenous</span>
</div>