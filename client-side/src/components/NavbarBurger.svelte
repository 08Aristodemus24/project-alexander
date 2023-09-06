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
      <a href="#" class="top-left-corner"></a>
      <a href="#" class="top-edge"></a>
      <a href="#" class="top-right-corner"></a>
      
      <a href="#" class="left-edge"></a>
      <a href="#" class="center"></a>
      <a href="#" class="right-edge"></a>
      
      <a href="#" class="bottom-left-corner"></a>
      <a href="#" class="bottom-edge"></a>
      <a href="#" class="bottom-right-corner"></a>
    </div>
</div>

<style>
    @media (max-width: 768px){
        /* for the navbar button and its animations */
        div.button-container{
            /* display */
            display: block;
            
            /* design */
            color: white;
            border: 1px solid red;
            
            /* position*/
            position: relative;

            /* size */
            height: 2rem;
            width: 2rem;

            /* design */
            background: transparent;
            border: 1px solid lightgreen;
        }

        .button-container > a{
            /* display */
            display: block;

            /* position */
            position: absolute;

            /* sizing */
            height: 6px;
            width: 6px;

            /* design */
            border-radius: 50%;
            background: white;
        }

        .top-left-corner{
        top: 1px;
        left: 1px;
        }

        .top-edge{
        top: 1px;
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
        top: 1px;
        right: 1px;
        }

        .left-edge{
        left: 1px;
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
        right: 1px;
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
        left: 1px;
        bottom: 1px;
        }

        .bottom-edge{
        bottom: 1px;
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
        right: 1px;
        bottom: 1px;
        }

        /* on hover on button-container then translate top, left, bottom, right edges to */
        .button-container.opened .top-edge{
        transform: translate(-100%, 100%);
        }

        .button-container.opened .left-edge{
        transform: translate(100%, 100%);
        }

        .button-container.opened .bottom-edge{
        transform: translate(100%, -100%);
        }

        .button-container.opened .right-edge{
        transform: translate(-100%, -100%);
        }
    }
</style>