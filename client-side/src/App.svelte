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
  

  // initial state
  let repos = [];

  // upon mounting of component send http request to flask
  // backend proxy server and retrieve repositories
  onMount(async () => {
    const url = 'http://127.0.0.1:5000/';
    const response = await fetch(url);

    if(response.status === 200){
      console.log("retrieval successful");

      // pass retrieved repositories to another component called
      // Project.svelte
      const data = await response.json();

      // everytime new repositories are added we overwrite the old
      // contents of the repos state
      repos = [...data];
      console.log('repositories: ');
      console.table(repos);


    }else{
      console.log(`retrieval unsuccessful. Response status ${response.status} occured`)
    }
  });

  // this is a variable dependent upon the state of repos
  $: some_var = JSON.stringify(repos.slice(-1)) + "test";
  
  // pass the state to the experience section component

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
