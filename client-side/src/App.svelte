<script>
  import { onMount, onDestroy } from "svelte";
  import Navbar from './components/Navbar.svelte';
  import Hero from "./components/Hero.svelte";
  import Content from "./components/Content.svelte";
  import About from "./components/About.svelte";
  import Work from "./components/Work.svelte";
  import Projects from "./components/Projects.svelte";
  import Accordion from "./components/Accordion.svelte";
  import Skills from "./components/Skills.svelte";
  import Experience from "./components/Experience.svelte";
  import Contact from "./components/Contact.svelte";

  import './assets/stylesheets/content.css';
  import './assets/stylesheets/navbar-862-and-up.css';
  import './assets/stylesheets/navbar-862-down.css';
  

  // initial state of list before fetching repositories
  let repos = [];

  // list of repositories to include in projects section
  let included = [];

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
      // console.table(repos);

      included = repos.filter((repo) => {
        const repo_names = ['LaRJ-Corpus',
         'phil-jurisprudence-recsys',
         'hate-speech-classifier',
         'breast-cancer-classifier',
         'housing-prices-predictor',
         'project-alexander'];
        
        // callbacdk returns true if repo name is part of
        // exclusive repos list
        return repo_names.includes(repo['name']);
      });

      console.log(included);


    }else{
      console.log(`retrieval unsuccessful. Response status ${response.status} occured`)

      // if retrieval of repositories is unsuccessful just initialize empty repos
      included = [
        {name: null, description: null, html_url: null},
        {name: null, description: null, html_url: null},
        {name: null, description: null, html_url: null},
        {name: null, description: null, html_url: null},
        {name: null, description: null, html_url: null},
        {name: null, description: null, html_url: null}
      ];
    }
  });
  
  const send_mail = async (event) => {
    const raw_data = event.detail;

    // send here the data from the contact component to 
    // the backend proxy server
    const url = 'http://127.0.0.1:5000/send-mail';
    const response = await fetch(url, {
      'method': 'POST',
      'headers': {
        'Content-Type': 'application/json'
      },
      'body': JSON.stringify(raw_data)
    });

    if(response.status === 200){
      console.log('message sent');

    }else{
      console.log(`message submission unsucessful. Response status ${response.status} occured`);
    }
  }

  // this is a variable dependent upon the state of repos
  $: some_var = JSON.stringify(repos.slice(-1)) + "test";
</script>

<Navbar/>
<Content>
  <Hero slot="landing-section"/>
  <About slot="about-section"/>
  <Work slot="work-group-section">
    <Projects slot="projects-section">
      <Accordion slot="accordion-group" repos={included}/>      
    </Projects>
    <Skills slot="skills-section"/>
    <Experience slot="exp-section"/>
  </Work>
  <Contact slot="contact-section" on:sendMail={send_mail}/>
</Content>
