<script>
  import { onMount, onDestroy } from "svelte";
  import Navbar from './components/Navbar.svelte';
  import Hero from "./components/Hero.svelte";
  import Content from "./components/Content.svelte";
  import About from "./components/About.svelte";
  import Work from "./components/Work.svelte";
  import Projects from "./components/Projects.svelte";
  import Skills from "./components/Skills.svelte";
  import Experience from "./components/Experience.svelte";
  import Contact from "./components/Contact.svelte";

  import './assets/stylesheets/content.css';
  import './assets/stylesheets/navbar-862-and-up.css';
  import './assets/stylesheets/navbar-862-down.css';
</script>

<Navbar/>
<Content>
  <Hero slot="landing-section"/>
  <About slot="about-section"/>
  <Work slot="work-group-section">
    <Projects slot="projects-section"/>
    <Skills slot="skills-section"/>
    <Experience slot="exp-section"/>
  </Work>
  <Contact slot="contact-section"/>
</Content>