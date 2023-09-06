<script>
  let is_opened = false;
  console.log(is_opened)
  
  // if div is closed then its class is .closed if opened then .opened
  const toggle_menu = () => {
      
      is_opened = !is_opened;
      console.log(is_opened);
  };
</script>

<header class="navbar-container">
  <nav class="navbar">
    <div class="nav-brand-container">
      <a class="navbar-brand" href="/">Michael</a>
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
    
    <div class="nav-menu-container">
      <div class="nav-menu">
        <a class="nav-item" href="about-section" aria-current="page">ABOUT</a>
        <a class="nav-item" href="proj-section">WORK</a>
        <a class="nav-item" href="contact-section">CONTACT</a>
      </div>
    </div>
  </nav>
</header>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Nunito+Sans:opsz,wght@6..12,200;6..12,300;6..12,400;6..12,500;6..12,600;6..12,700;6..12,800&display=swap');

  /* html{
    border: 1px solid purple;  
  } */

  /* body{
    background: white;
    border: 1px solid red;
  } */

  /* .navbar-container{
  } */

  .navbar{
    /* size */
    height: 6.5rem;
    width: 100vw;
    
    /* display */
    display: flex;
    
    /*alignment */
    justify-content: center;
    align-items: center;
    
    /* position */
    position: relative;
    
    /* design */
    /* border: 1px solid green; */
    background: black;
  }

  .nav-brand-container{
    /* size */
    height: min-content;
    width: min-content;
    
    /* position */
    position: absolute;
    left: 8rem;
    top: 0;
    bottom: 0;
    margin-top: auto;
    margin-bottom: auto;
    
    /* design */
  /*   border: 2px solid red; */
  }

  .nav-brand-container .navbar-brand{
    /* design */
    color: white;
    font-size: 2rem;
    font-weight: 700;
    font-family: 'Cormorant Garamond', serif;
    text-decoration: none;
  }

  .nav-brand-container .button-container{
    display: none;
  }

  /* .nav-menu-container{
    border: 1px solid red;
  } */

  .nav-menu{
    display: flex;
  /*     border: 1px solid blue; */
  }

  .nav-item{
    /* display */
    display: block;
    
    /* spacing */
    margin-left: 1rem;
    margin-right: 1rem;
    padding-top: .5rem;
    padding-bottom: .5rem;
    
    /* size */
    width: 10rem;
    
    /* design */
    text-align: center;
    color: white;
    font-size: 13px;
    font-family: 'Nunito Sans', sans-serif;
    font-weight: 300;
    text-decoration: none;
    border: 1px solid transparent;
    
    /* animation */
    transition-property: border;
    transition-duration: 250ms;
    transition-timing-function: ease-in-out;
  }

  .nav-item:hover{
    border-top: solid 1px white;
    border-bottom: solid 1px white;
  }


  @media (max-width: 768px){
    .nav-menu-container{
      display: none;
    }
    
    /* override min-height and min-width height and width values of .nav-brand-container 
    but keep it absolute still */
    .nav-brand-container{
      /* display */
      display: flex;
      justify-content: space-between;
      align-items: center;
      
      /* size */
      width: 85%;
      
      /* alignment */
      left: 0;
      right: 0;
      margin-right: auto;
      margin-left: auto;
      
      /* design */
      border: 1px solid red;
    }
    
    .nav-brand-container .navbar-brand{
      display: block;
      border: 1px solid yellow;
    }
    
    /* for the navbar button and its animations */
    .nav-brand-container .button-container{
      /* display */
      display: block;
      
      /* design */
      color: white;
      border: 1px solid red;
      
      /* position*/
      position: relative;

      /* size */
      height: 2.25rem;
      width: 2.25rem;

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
      transform: translate(-107%, 107%);
    }

    .button-container.opened .left-edge{
      transform: translate(107%, 107%);
    }

    .button-container.opened .bottom-edge{
      transform: translate(107%, -107%);
    }

    .button-container.opened .right-edge{
      transform: translate(-107%, -107%);
    }
  }
</style>
