
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
