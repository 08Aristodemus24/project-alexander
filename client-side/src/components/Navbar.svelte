<script>
  let is_opened = false;
  const body = document.body;
  
  // if div is closed then its class is .closed if opened then .opened
  const toggle_menu = (event) => {
    if(is_opened === false){
      is_opened = !is_opened;
      body.style.overflow = "hidden";
    }else{
      is_opened = !is_opened;
      body.style.overflow = "auto";
    }
  };

  // I don't want links in desktop mode to have access to the modal
  // if navbar is opened then only then can it be closed
  // but what if user opens modal and sets the dims to desktop
  // then when a tag is clicked modal will be closed
  const close_and_go = (event) => {
    if(is_opened === true){
      is_opened = !is_opened;
      body.style.overflow = "auto";
    }
  }
</script>

<header class="navbar-container">
  <nav class="navbar" class:opened={is_opened === true}>
    <div class="nav-brand-container">
      <a class="navbar-brand" href="/" on:click|preventDefault={() => {
        document.body.scrollIntoView();
      }}>Michael</a>
      
      <div on:click|preventDefault={toggle_menu} class="button-container" class:opened={is_opened === true}>
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
        <a class="nav-item" href="#about-section" aria-current="page" on:click={close_and_go}>ABOUT</a>
        <a class="nav-item" href="#work-group-section" on:click={close_and_go}>WORK</a>
        <a class="nav-item" href="#contact-section" on:click={close_and_go}>CONTACT</a>
      </div>
    </div>
  </nav>
</header>
