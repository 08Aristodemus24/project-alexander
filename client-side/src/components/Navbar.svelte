<script>

</script>

<header class="navbar-container">
  <nav class="navbar">
    <div class="nav-brand-container">
      <a class="navbar-brand" href="/">Michael</a>
      <slot/>
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
  /*   border: 1px solid blue; */
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
      
      /* size */
      width: 75vw;
      
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
    }
  }
</style>
