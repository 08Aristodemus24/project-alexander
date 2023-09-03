<script>
    let is_opened = false;
    console.log(is_opened)
    
    // if div is closed then its class is .closed if opened then .opened
    const toggle_menu = () => {
        
        is_opened = !is_opened;
        console.log(is_opened);
    };
</script>

<div class="centerer">
    <div on:click={toggle_menu} class="button-container" class:opened={is_opened === true}>
      <a class="top-left-corner"></a>
      <a class="top-edge"></a>
      <a class="top-right-corner"></a>
      
      <a class="left-edge"></a>
      <a class="center"></a>
      <a class="right-edge"></a>
      
      <a class="bottom-left-corner"></a>
      <a class="bottom-edge"></a>
      <a class="bottom-right-corner"></a>
    </div>
</div>

<style>
    .centerer{
    /* display */
    display: flex;
    
    /* // position */
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    
    /* parent alignment */
    margin-top: auto;
    margin-right: auto;
    margin-bottom: auto;
    margin-left: auto;
    
    /* child alignment */
    justify-content: center;
    align-items: center;
    
    /* size */
    height: 50vh;
    width: 50vw;
    
    /* design */
    border: 1px solid blue;
    }

    .button-container{
    /* position */
    position: relative;
    
    /* size */
    height: 10rem;
    width: 10rem;
    
    /* design */
    background: transparent;
    }

    a{
    /* display */
    display: block;
    
    /* position */
    position: absolute;
    
    /* sizing */
    height: 1rem;
    width: 1rem;
    
    /* design */
    border-radius: 50%;
    background: black;
    }

    .top-left-corner{
    top: 1rem;
    left: 1rem;
    }

    .top-edge{
    top: 1rem;
    left: 0;
    right: 0;
    margin-left: auto;
    margin-right: auto;
    
    /* animation */
    transition-property: transform;
    transition-duration: .5s;
    transition-timing-function: ease-in-out;
    }

    .top-right-corner{
    top: 1rem;
    right: 1rem;
    }

    .left-edge{
    left: 1rem;
    top: 0;
    bottom: 0;
    margin-top: auto;
    margin-bottom: auto;
    
    /* animation */
    transition-property: transform;
    transition-duration: .5s;
    transition-timing-function: ease-in-out;
    }

    .center{
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    margin: auto auto auto auto;
    }

    .right-edge{
    right: 1rem;
    top: 0;
    bottom: 0;
    margin-top: auto;
    margin-bottom: auto;
    
    /* animation */
    transition-property: transform;
    transition-duration: .5s;
    transition-timing-function: ease-in-out;
    }

    .bottom-left-corner{
    left: 1rem;
    bottom: 1rem;
    }

    .bottom-edge{
    bottom: 1rem;
    left: 0;
    right: 0;
    margin-left: auto;
    margin-right: auto;
    
    /* animation */
    transition-property: transform;
    transition-duration: .5s;
    transition-timing-function: ease-in-out;
    }

    .bottom-right-corner{
    right: 1rem;
    bottom: 1rem;
    }

    /* on hover on button-container then translate top, left, bottom, right edges to */

    .button-container.opened .top-edge{
        transform: translate(-175%, 175%);
    }

    .button-container.opened .left-edge{
        transform: translate(175%, 175%);
    }

    .button-container.opened .bottom-edge{
        transform: translate(175%, -175%);
    }

    .button-container.opened .right-edge{
        transform: translate(-175%, -175%);
    }
</style>