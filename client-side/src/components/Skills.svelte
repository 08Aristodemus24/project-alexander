<script>
    // now shoudl new index be now set the active class 
    // will only be added to a slide with a specific index

    import InnerCarousel from "./InnerCarousel.svelte";
    import OuterCarousel from "./OuterCarousel.svelte";

    // because of the conditional class
    let new_index = 0;

    const switch_slide = (event) => {
        // access the data-<name> attributes value using
        // an elements .dataset property, because data attribute
        // is named carousel-button we access .carouselButton
        const offset = event.target.dataset.carouselButton === 'next' ? 1 : -1;
        console.log(`${offset === 1 ? 'next' : 'prev'} button has been clicked`);

        const carousel = document.querySelector('.carousel-inner');
        const active_slide = document.querySelector('.carousel-item.active');

        const carousel_items = [...carousel.children];
        console.log(carousel_items);

        // A + 1 offset means we go forwards in accessing the carousel_items
        // and a + -1 offset means we will go backwards in accessing the carousel_items
        new_index = carousel_items.indexOf(active_slide) + offset;
        if(new_index < 0){
            // should new index be of a negative value we go to the last slide
            new_index = carousel_items.length - 1;

        }else if(new_index >= carousel_items.length){
            new_index = 0;
        }
    }
</script>

<section id="skills-section">
    <div class="skills-content">
        <div class="skills-header-container">
            <button class="button-container-prev" data-carousel-button="prev" on:click={switch_slide}></button>
            <OuterCarousel new_index={new_index}/>
            <button class="button-container-next" data-carousel-button="next" on:click={switch_slide}></button>
        </div>
        
        <div class="carousel-container">
            <InnerCarousel new_index={new_index}/>
        </div>
    </div>
</section>