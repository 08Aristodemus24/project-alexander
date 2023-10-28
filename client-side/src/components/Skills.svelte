<script>
    import InnerCarousel from "./InnerCarousel.svelte";
    import OuterCarousel from "./OuterCarousel.svelte";

    // initial index of the carousel
    let curr_index = 0;

    // binds the inner carousel to this variable
    // instead of using dom api
    let inner_carousel;

    // now shoudl new index be now set the active class 
    // will only be added to a slide with a specific index
    const switch_slide = (event) => {
        // access the data-<name> attributes value using
        // an elements .dataset property, because data attribute
        // is named carousel-button we access .carouselButton
        const offset = event.target.dataset.carouselButton === 'next' ? 1 : -1;
        console.log(`${offset === 1 ? 'next' : 'prev'} button has been clicked`);

        const carousel_items = [...inner_carousel.children];
        const active_slide = carousel_items[curr_index];
        console.log(carousel_items);

        // a + 1 offset means we go forwards in accessing the carousel_items
        // and a + -1 offset means we will go backwards in accessing the carousel_items
        curr_index = carousel_items.indexOf(active_slide) + offset;
        if(curr_index < 0){
            // should new index be of a negative value we go to the last slide
            curr_index = carousel_items.length - 1;

        }else if(curr_index >= carousel_items.length){
            curr_index = 0;
        }
    }
</script>

<section id="skills-section">
    <div class="skills-content">
        <div class="skills-header-container">
            <button class="button-container-prev" data-carousel-button="prev" on:click={switch_slide}></button>
            <OuterCarousel curr_index={curr_index}/>
            <button class="button-container-next" data-carousel-button="next" on:click={switch_slide}></button>
        </div>
        
        <div class="carousel-container">
            <InnerCarousel curr_index={curr_index} bind:inner_carousel/>
        </div>
    </div>
</section>