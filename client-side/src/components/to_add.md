
#landing-section::after{
    width: 100%;
    height: 100%;

    /* position */
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    /* to not affect contents color place pseudo element behind content */
    z-index: -1;

    /* alignment */ 
    /*   margin-left: auto;
    margin-right: auto;
    margin-top: auto;
    margin-bottom: auto; */

    /* design */
    content: '';
    background-image: url('https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/assets/mediafiles/Default_Far_out_image_of_a_human_at_the_forefront_of_human_exp_1_cd59dbf1-a928-4dbb-ae5d-6b76b432da37_1%20upscaled.jpg');
    background-attachment: fixed;
    background-position: center;
    filter: grayscale(100%) brightness(50%);
}



.timeline-container{
    /* design */
    /* background-color: rgb(255, 255, 255); */
    border: 2px solid rgb(8, 74, 255);

    /* display */
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    column-gap: 10rem;

    /* position */
    position: relative;

    /* spacing */
    padding: 1rem;
    margin-inline: 1rem;

    /* containment */
    overflow-x: scroll;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    scroll-padding-inline: 1rem;

    /* size */
    height: 75vh;
    width: 100%;
}

.timeline-container::-webkit-scrollbar{
    height: .25rem;
}

.timeline-container::-webkit-scrollbar-thumb{
    background-color: black;
}

.timeline-item{
    /* position */
    position: relative;

    /* display */
    display: flex;
    justify-content: center;

    /* spacing */
    row-gap: 5rem;

    /* design */
    outline: 1px solid rgb(202, 202, 202);

    /* scroll type */
    scroll-snap-align: center;

    /* transition */
    transition: 
        background-color 0.25s ease-in-out,
}

.timeline-item.up{
    /* alignment */
    align-items: flex-start;
    flex-direction: column;
}

.timeline-item.down{
    /* alignment */
    align-items: flex-end;
    flex-direction: column-reverse;
}

.timeline-item .bar{
    /* alignment */
    align-self: center;

    /* position */
    position: relative;

    /* size */
    width: 1rem;
    height: 3px;

    /* design */
    background-color: black;
}

.timeline-item .bar::after{
    /* display */
    display: block;

    /* position */
    position: absolute;
    inset-block: 0;
    margin-block: auto;

    /* size */
    width: 25rem;
    height: 1px;

    /* design */
    content: '';
    background-color: black;
}

.timeline-item .header{
    /* design */
    outline: 1px solid black;

    /* position */
    position: relative;

    /* display */
    display: flex;
    flex-direction: column;
    justify-content: center;

    /* size */
    padding: 0.5rem;
    min-height: min-content;
    width: fit-content;
}

.header .title{
    font-family: 'Nunito Sans', sans-serif;
    letter-spacing: 0.0625em;
    text-align: left;
    font-size: clamp(12px, 1vw, 1rem);
    font-weight: bold;
    color: rgb(0, 0, 0);
}

.header .organization{
    font-family: 'Nunito Sans', sans-serif;
    text-align: left;
    font-size: clamp(12px, 1vw, 1rem);
    font-weight: 300;
    color: rgb(0, 0, 0);
}

.timeline-item .year{
    /* design */
    background-color: white;
    font-family: 'Oswald', sans-serif;
    letter-spacing: 0.25em;
    text-align: center;
    font-size: clamp(12px, 1vw, 1rem);
    font-weight: 300;
    color: rgb(0, 0, 0);
    outline: 1px solid rgb(0, 0, 0);

    /* size */
    padding-inline: 1em;
    padding-block: 0.5em;

    /* position */
    position: absolute;
    z-index: -1;

    /* transition */
    transition: color 0.25s ease-in-out;
}

.timeline-item.up .year{
    /* position */
    bottom: 90%;
    left: 90%;
    
}

.timeline-item.down .year{
    /* position */
    top: 90%;
    right: 90%;
}

.timeline-item .accolades{
    /* design */
    list-style: none;
    outline: 1px solid black;

    /* size */
    min-height: min-content;
    width: fit-content;
    padding: 0.5rem;

    /* display */
    display: flex;
    flex-direction: column;
    justify-content: flex-start;

    /* spacing */
    row-gap: 1rem;

}

.accolades .accolade{
    /* size */
    width: 20em;

    /* design */
    background-color: transparent;
    font-family: 'Nunito Sans', sans-serif;
    font-size: clamp(12px, 1vw, 1rem);
    font-weight: 300;
    text-align: justify;
}