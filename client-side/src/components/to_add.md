# DESKTOP NAVBAR
.nav-menu-container{
      /* display: none; */
      position: fixed;
      /* transform: scale(0%); */
      visibility: hidden;
      opacity: 0%;

      transition-property: visibility, opacity;
      transition-duration: 250ms;
      transition-timing-function: ease-in-out;
    }

/* TO TEST AND REFACTOR FOR BUGS */
    /* when .navbar has .opened class apply block display
    to the none displayed .nav-menu-container */
    .navbar.opened .nav-menu-container{
      /* display */
      /* since .navbar is in flex this will be a flex item still */
      /* .navbar still has height to 6.5rem that's why when showing 
      this .nav-menu-container it still stays in the .navbar and not in the middle */
      opacity: 100%;
      visibility: visible;
      /* display: flex; */

      /* size */
      width: 100vw;
      /* transform: scale(100%); */

      /* position */
      position: fixed;

      /* alignment */
      top: 6.5rem;
      bottom: 0;
      margin-top: auto;
      margin-bottom: auto;
      justify-content: center;

      /* design */
      background-color: black;

    }

    .navbar.opened .nav-menu-container .nav-menu{
      flex-direction: column;
      justify-content: center;
      row-gap: 5rem;
    }


# FOR DESKTOP NAVBAR AND SECTION
<header class="navbar-container">
  <nav class="navbar closed">
    <div class="nav-brand-container">
      <a class="navbar-brand" href="/">Michael</a>
      <div class="button-container closed">
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
        <a class="nav-item" href="#about-section" aria-current="page">ABOUT</a>
        <a class="nav-item" href="#work-section">WORK</a>
        <a class="nav-item" href="#contact-section">CONTACT</a>
      </div>
    </div>
  </nav>
</header>
<main class="main-content">
  <section id="landing-section">
    <div class="landing-content">
      <div class="greetings-container">
        <h1>Warm greetings to you my friend, my name is Michael.</h1>
        <p>Тепло приветствую тебя, мой друг, меня зовут, Михайл.</p>
      </div>
      <div class="socials-container">
        <svg 
              viewBox="-2.5 0 19 19" 
              xmlns="http://www.w3.org/2000/svg" 
              class="github-icon"
          >
              <path d="M9.464 17.178a4.506 4.506 0 01-2.013.317 4.29 4.29 0 01-2.007-.317.746.746 0 01-.277-.587c0-.22-.008-.798-.012-1.567-2.564.557-3.105-1.236-3.105-1.236a2.44 2.44 0 00-1.024-1.348c-.836-.572.063-.56.063-.56a1.937 1.937 0 011.412.95 1.962 1.962 0 002.682.765 1.971 1.971 0 01.586-1.233c-2.046-.232-4.198-1.023-4.198-4.554a3.566 3.566 0 01.948-2.474 3.313 3.313 0 01.091-2.438s.773-.248 2.534.945a8.727 8.727 0 014.615 0c1.76-1.193 2.532-.945 2.532-.945a3.31 3.31 0 01.092 2.438 3.562 3.562 0 01.947 2.474c0 3.54-2.155 4.32-4.208 4.548a2.195 2.195 0 01.625 1.706c0 1.232-.011 2.227-.011 2.529a.694.694 0 01-.272.587z"/>
          </svg>
        <svg 
              viewBox="0 0 32 32" 
              xmlns="http://www.w3.org/2000/svg"
              class="kaggle-icon"
          >
              <path d="M25.099 31.812c-.025.12-.156.188-.375.188h-4.183c-.249 0-.468-.109-.656-.328l-6.907-8.787-1.932 1.828v6.817c0 .313-.151.469-.463.469H7.338c-.312 0-.469-.156-.469-.469V.469c0-.308.157-.469.469-.469h3.245c.312 0 .463.161.463.469v19.124l8.271-8.359c.224-.224.443-.328.661-.328h4.319c.192 0 .317.077.38.239.063.199.047.339-.047.417l-8.74 8.459 9.115 11.343c.125.141.156.276.093.48z"/>
          </svg>
          <svg 
              version="1.0" 
              xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 1008 1008"
              class="stackoverflow-icon"
          >
              <path d="M631.9 26.6c-19.5 14.6-35.5 26.9-35.7 27.4-.3.8 261.8 354.1 265.9 358.4 1.7 1.9 2.6 1.3 37.4-24.8 19.6-14.7 35.5-27.1 35.3-27.6-.2-.8-97-131-244.6-329.2L667.3 0l-35.4 26.6zM472.6 178.2c-21.7 26.2-28.2 34.6-27.3 35.4.7.7 78.3 65.6 172.6 144.4C758 475 789.5 500.9 790.5 499.8c4.4-4.7 55.5-67.1 55.5-67.7 0-.8-342.4-287.3-344-287.9-.5-.2-13.7 15.1-29.4 34zM350 371.4c-10.1 22.2-18.4 40.7-18.3 41.1.3 1.2 406.7 190.4 407.4 189.7 1.4-1.5 36.9-79.6 36.7-80.4C775.5 521 370.4 331 369 331c-.3 0-8.8 18.2-19 40.4zM291.6 536.1c-1.6 4.5-18.3 86.5-17.7 87 .6.6 431.1 91 436.9 91.7 1.7.2 3.2 0 3.2-.4 0-.5 4.1-20 9-43.3 5-23.4 8.7-42.8 8.3-43.1-.5-.4-98.5-21.3-217.9-46.4-119.4-25.2-218.1-46-219.3-46.3-1.3-.3-2.3 0-2.5.8z"/>
              <path d="M84 828v180h809V648h-90v270H174V648H84v180z"/>
              <path d="M263.2 782.7l.3 44.8 224.8.3 224.7.2v-90H263l.2 44.7z"/>
          </svg>
          <svg 
              version="1.0" 
              xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 1440 1008"
              class="facebook-icon"
          >
              <path d="M813.5.7c-107.1 9.3-184.2 75.9-207 178.8-6.4 28.5-6.7 34.4-7.2 111.7l-.5 70.8H447v207h152v439h213l.2-219.2.3-219.3 87.3-.3 87.2-.2-.2-103.3-.3-103.2-87.3-.3-87.3-.2.4-59.3c.3-51.7.6-60.1 2.1-66.7 5.8-25 20.1-36.2 50.6-40 4.9-.6 32.9-1 67.6-1h59.1l.6-10.7c.4-5.8.7-49.7.7-97.5V0l-87.7.2c-48.3.1-89.6.3-91.8.5z"/>
          </svg>
          <svg 
              version="1.0" 
              xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 1440 1008"
              class="linkedin-icon"
          >
              <path d="M326.5 3.1c-43.9 5.5-82.9 38.1-96.4 80.4-4.1 13-5.5 22.2-5.5 37 .1 14.5 1.8 24.8 6.6 38.5 14 39.9 49 69.2 91.2 76.5 12.1 2.1 46 2.1 57.7.1 23.3-4.1 45.2-15.7 62.4-33.1 40.5-40.8 45.8-104.2 12.7-151-18.1-25.7-46.8-43.2-78.7-48-10.9-1.6-38.2-1.8-50-.4zM994.5 313.6c-72.1 4.8-135.9 41.4-174.7 100.2l-6.8 10.4V330H587.5l-.1 339-.2 339H812V812.7c0-120.8.4-198.8 1-204.7 3.6-35 15.3-59.7 38.6-82 23.5-22.6 52.3-34 85.5-34 43.3 0 75.3 18.9 93.7 55.6 8.1 16.1 13.3 34.4 16.9 59 1.5 10.8 1.7 29.3 2 206.6l.4 194.8h225l-.4-215.8c-.4-233.8-.1-220.1-5.7-253.6-11.1-65.9-35.7-118.2-73.5-156.2-37.7-37.9-86.8-60.5-145-66.8-13.8-1.5-46.2-2.6-56-2zM236 669v339h226V330H236v339z"/>
          </svg>
      </div>
    </div>
  </section>
  
  <section id="about-section">
    <div class="about-content">
      <div class="">
        <h1>I am a currently a student specializing in machine learning engineering and an aspiring computational immunologist</h1>
        <p></p>
      </div>
    </div>
  </section>
  <section id="work-section">
    <div class="work-content">
      <div class="">
        <h1>Work</h1>
        <p></p>
      </div>
    </div>
  </section>
  <section id="contact-section">
    <div class="contact-content">
      <div class="">
        <h1>Send me a message</h1>
        <p></p>
      </div>
    </div>
  </section>
</main>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Nunito+Sans:opsz,wght@6..12,200;6..12,300;6..12,400;6..12,500;6..12,600;6..12,700;6..12,800&display=swap');

*,
::before,
::after{
    box-sizing: border-box;
}

html{
    /* design */
    line-height: 1.5;
    /* border: 1px solid purple; */

    /* behavior */
    scroll-behavior: smooth;
}

body{
    /* design */
    /* inherit line height of parent which is html */
    line-height: inherit;
    /* border: 1px solid red; */

    /* spacing */
    margin: 0;   
}

.navbar-container{
  width: 100vw;
}

.navbar{
    /* size */
    height: 6.5rem;
    width: 100%;

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
    /* border: 2px solid red; */
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

.nav-menu-container{
    /* border: 1px solid red; */
}

.nav-menu{
    display: flex;
    /* border: 1px solid blue; */
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
    /* border: 1px solid red; */

    /* animation */
    transition-property: border;
    transition-duration: 250ms;
    transition-timing-function: ease-in-out;
}

.nav-item:hover{
    border-top: solid 1px white;
    border-bottom: solid 1px white;
}

.main-content{
  width: 100vw;
}

#landing-section{
  /* size for each section*/
  height: 100vh;

  /* design */
  outline: 2px solid green;
}

.landing-content{
  /* size. takes % of landing-section as min-height */
  min-height: 100%;

  /* alignment */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  /* position */
  position: relative;

  /* spacing */ 
  row-gap: 2rem;

  /* outline: 3px solid purple; */
}

.landing-content::after{
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

.greetings-container{
  outline: 2px solid red;
}

.greetings-container h1{
  /* spacing */
  margin-left: 10px;
  margin-right: 10px;

  /* design */
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(1.5rem, 3.75vw, 3.75rem);
  text-align: center;
  color: white;
  outline: 1px solid lightgreen;
}

.greetings-container p{
  /* spacing */
  margin-left: 10px;
  margin-right: 10px;

  /* design */
  text-align: center;
  font-family: 'Nunito Sans', sans-serif;
  font-size: clamp(14px, 2.1875vw, 22.4px);
  color: white;
  outline: 1px solid lightgreen;
}

.socials-container{
  /* size */
  width: 20rem;

  /* design */
  /*     outline: 2px solid blue; */

  /* display */
  display: flex;

  /* alignment */
  align-items: center;
  justify-content: center;

  /* spacing */
  column-gap: 2rem;
}

.github-icon, .kaggle-icon, .stackoverflow-icon{
  /* design */
  fill: white;
  outline: 1px solid lightgreen;

  /* size */
  width: 30px;
  height: 30px;
}

.facebook-icon, .linkedin-icon{
  /* design */
  fill: white;
  outline: 1px solid lightgreen;

  /* size */
  width: 36px;
  height: 25px;
}



#about-section, #work-section, #contact-section{
  outline: 1px solid black;
  min-height: 100vh;
}

.about-content h1{
  font-size: 14px
}

@media (width < 768px){
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Nunito+Sans:opsz,wght@6..12,200;6..12,300;6..12,400;6..12,500;6..12,600;6..12,700;6..12,800&display=swap');

    *,
    ::before,
    ::after{
      box-sizing: border-box;
    }

    html{
      /* design */
      line-height: 1.5;
      /* border: 1px solid purple; */

      /* behavior */
      scroll-behavior: smooth;
    }

    body{
      /* design */
      /* inherit line height of parent which is html */
      line-height: inherit;
/*       border: 1px solid red; */

      /* spacing */
      margin: 0;
    }

    .navbar-container{
      width: 100vw;
    }

    .navbar{
      /* size */
      height: 5rem;
      width: 100%;

      /* display */
      display: flex;

      /*alignment */
      justify-content: center;
      align-items: center;

      /* position */
      position: relative;

      /* design */
/*       outline: 1px solid white; */
      background-color: black;
    }

    /* override min-height and min-width height and width values of .nav-brand-container 
    but keep it absolute still */
    .nav-brand-container{
      /* display */
      display: flex;
      justify-content: space-between;
      align-items: center;

      /* size */
      height: min-content;
      width: 85%;

      /* position */
      position: absolute;
      z-index: 3;
      left: 0;
      top: 0;
      right: 0;
      bottom: 0;
      margin-top: auto;
      margin-bottom: auto;
      margin-right: auto;
      margin-left: auto;

      /* design */
/*       outline: 2px solid red; */
      background-color: black;
    }

    .nav-brand-container .navbar-brand{
      /* display */
      display: block;

      /* design */
      color: white;
      font-size: 24px;
      font-weight: 700;
      font-family: 'Cormorant Garamond', serif;
      text-decoration: none;
/*       outline: 1px solid yellow; */

      /* animation */
      transition-property: opacity;
      transition-duration: 125ms;
      transition-timing-function: ease-in-out;
    }

    /* for the navbar button and its animations */
    .nav-brand-container .button-container{
      /* display */
      display: block;      

      /* position*/
      position: relative;

      /* size */
      height: 1.75rem;
      width: 1.75rem;

      /* design */
      color: white;
      background: transparent;
/*       outline: 1px solid lightgreen; */
    }

    .nav-menu-container{
      /* display */
      display: flex;
      visibility: hidden;
      opacity: 0%;

      /* position */
      position: fixed;
      z-index: 2;

      /* design */
      background-color: black;
/*       outline: 1px solid yellow; */

      /* alignment */
      top: 0;
      bottom: 0;
      margin-top: auto;
      margin-bottom: auto;
      justify-content: center;

      /* size */
      width: 100vw;

      /* animation */
      transition-property: opacity, visibility;
      transition-duration: 250ms;
      transition-timing-function: ease-in-out;
    }

    .nav-menu{
      display: flex;
      /* border: 1px solid blue; */
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
      /* outline: 1px solid red; */

      /* animation */
      transition-property: border;
      transition-duration: 250ms;
      transition-timing-function: ease-in-out;
    }

    .nav-item:hover{
      border-top: solid 1px white;
      border-bottom: solid 1px white;
    }

    /* MOBILE */
    .button-container > a{
      /* display */
      display: block;

      /* position */
      position: absolute;

      /* sizing */
      height: 5px;
      width: 5px;

      /* design */
      border-radius: 50%;
      background: white;
      /* outline: 1px solid red; */
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
      transition-duration: 125ms;
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
      transition-duration: 125ms;
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
      transition-duration: 125ms;
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
      transition-duration: 125ms;
      transition-timing-function: ease-in-out;
    }

    .bottom-right-corner{
      right: 1px;
      bottom: 1px;
    }

    /* on hover on button-container then translate top, left, bottom, right edges to */
    .button-container.opened .top-edge{
      transform: translate(-105%, 105%);
    }

    .button-container.opened .left-edge{
      transform: translate(105%, 105%);
    }

    .button-container.opened .bottom-edge{
      transform: translate(105%, -105%);
    }

    .button-container.opened .right-edge{
      transform: translate(-105%, -105%);
    }

    .navbar.opened .nav-brand-container .navbar-brand{
      opacity: 0%;
    }

    .navbar.opened .nav-menu-container{
      visibility: visible;
      opacity: 100%;
    }

    .navbar .nav-menu-container .nav-menu{
      /* display */
      flex-direction: column;
      
      /* alignment */
      justify-content: center;
      
      /* spacing*/
      row-gap: 5rem;
    }
}