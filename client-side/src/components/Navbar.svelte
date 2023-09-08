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
  <nav class="navbar" class:opened={is_opened === true}>
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
        <a class="nav-item" href="work-section">WORK</a>
        <a class="nav-item" href="contact-section">CONTACT</a>
      </div>
    </div>
  </nav>
</header>
