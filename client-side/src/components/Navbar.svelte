<script>

</script>

<!-- <header class="">
  <nav class="" aria-label="Global">
    <div class="">
      <a class="" href="/">Michael</a>
      <div class="">
        <button type="button" class="" data-hs-collapse="#navbar-collapse-with-animation" aria-controls="navbar-collapse-with-animation" aria-label="Toggle navigation">
          navbar burger here
        </button>
      </div>
    </div>
    <div id="navbar-collapse-with-animation" class="">
      <div class="">
        <a class="" href="about-section" aria-current="page">About</a>
        <a class="" href="work-section">Work</a>
        <a class="" href="contact-section">Contact</a>
      </div>
    </div>
  </nav>
</header> -->

<!-- <header class="flex flex-wrap sm:justify-start sm:flex-nowrap z-50 w-full bg-white text-sm py-4 dark:bg-gray-800">
  <nav class="max-w-[85rem] w-full mx-auto px-4 sm:flex sm:items-center sm:justify-between" aria-label="Global">
    <div class="flex items-center justify-between">
      <a class="flex-none text-xl font-semibold dark:text-white" href="#">Brand</a>
      <div class="sm:hidden">
        <button type="button" class="hs-collapse-toggle p-2 inline-flex justify-center items-center gap-2 rounded-md border font-medium bg-white text-gray-700 shadow-sm align-middle hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-white focus:ring-blue-600 transition-all text-sm dark:bg-slate-900 dark:hover:bg-slate-800 dark:border-gray-700 dark:text-gray-400 dark:hover:text-white dark:focus:ring-offset-gray-800" data-hs-collapse="#navbar-collapse-with-animation" aria-controls="navbar-collapse-with-animation" aria-label="Toggle navigation">
          <svg class="hs-collapse-open:hidden w-4 h-4" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
          </svg>
          <svg class="hs-collapse-open:block hidden w-4 h-4" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
            <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
          </svg>
        </button>
      </div>
    </div>
    <div id="navbar-collapse-with-animation" class="hs-collapse hidden overflow-hidden transition-all duration-300 basis-full grow sm:block">
      <div class="flex flex-col gap-5 mt-5 sm:flex-row sm:items-center sm:justify-end sm:mt-0 sm:pl-5">
        <a class="font-medium text-blue-500" href="#" aria-current="page">Landing</a>
        <a class="font-medium text-gray-600 hover:text-gray-400 dark:text-gray-400 dark:hover:text-gray-500" href="#">Account</a>
        <a class="font-medium text-gray-600 hover:text-gray-400 dark:text-gray-400 dark:hover:text-gray-500" href="#">Work</a>
        <a class="font-medium text-gray-600 hover:text-gray-400 dark:text-gray-400 dark:hover:text-gray-500" href="#">Blog</a>
      </div>
    </div>
  </nav>
</header> -->

<header class="navbar-container">
  <nav class="navbar">
    <div class="nav-brand-container">
      <a class="navbar-brand" href="/">Michael</a>
      <div class="button-container">
        button here
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
    .nav-brand-container .button-container{
      /* display */
      display: block;
      
      /* design */
      color: white;
      border: 1px solid red;
    }
  }
</style>
