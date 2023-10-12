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
      console.log(`message submission unsucessful. Response status '${response.status}' occured`);
    }
  }
  
  // initial state of list before fetching repositories
  let repos = [];

  // list of repositories to include in projects section
  // if retrieval of repositories is unsuccessful just initialize empty repos
  let included = [
    {name: null, description: null, html_url: null, project_id: 'I', project_image: "https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/ant%20swarm%20for%20breast-cancer-classifier%20upscaled.jpg"},
    {name: null,   description: null, html_url: null, project_id: 'II', project_image: "https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/hate%20speech%20thumbnail%20final%202.png"},
    {name: null, description: null, html_url: null, project_id: 'III', project_image: "https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/Default_futuristic_houses_in_the_neighborhood_using_Artificial_0_ab4ded69-8d1b-45e1-ab07-be2eb27054cc_1.jpg"},
    {name: null, description: null, html_url: null, project_id: 'IV', project_image: "https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/Default_multiple_jurisprudence_documents_0_63f0c99d-d7ee-42d8-85d5-f178c77abc9a_1.jpg"},
    {name: null, description: null, html_url: null, project_id: 'V', project_image: "https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/Default_lady_justice_sunset_background_wormseye_view_perspecti_0_f49a15e9-180d-4205-9a2d-d3efe582958f_1.jpg"},
    {name: null, description: null, html_url: null, project_id: 'VI', project_image: "https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/Default_far_out_side_view_statue_of_Alexander_The_Great_conque_1_76c1007c-b966-40e0-a74f-9ad4dc8bcec8_1.jpg"}
  ];

  const fetch_repos = async () => {
    try{
      const url = 'http://127.0.0.1:5000/repos';
      const response = await fetch(url);
      
      if(response.status === 200){
        console.log("retrieval successful");

        // pass retrieved repositories to another component called
        // Project.svelte
        const data = await response.json();

        // everytime new repositories are added we overwrite the old
        // contents of the repos state
        repos = [...data];

        repos = repos.filter((repo) => {
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

        console.log(repos);

        // update the repositories to include if request is successful
        included = repos.map((repo, index) => {
          // change null values reserved only for unsuccessful get request
          // should request be finally successful
          included[index]['name'] = repo['name'];
          included[index]['description'] = repo['description'];
          included[index]['html_url'] = repo['html_url'];

          return included[index];
        })

      }else{
        console.log(`retrieval unsuccessful. Response status '${response.status}' occured`);
      }

    }catch(error){
      console.log(`request denied. Error '${error}' occured.`);
    }
  }
  
  // initially all but user can change this depending
  // on what he wants to view
  let curr_year = null;

  // on moount min year and max year states will only be set once
  let min_year = null;
  let max_year = null;
  let contribs = [];
  
  const fetch_contribs = async (event) => {
    // upon mounting since user has not chosen a year yet 
    // event will be undefined and then should user click
    // a year only then event is not undefined, .detail can
    // be accessed, and then only can we set its next state
    curr_year = event === undefined ? null : event.detail;

    try{
      const url = `http://127.0.0.1:5000/contribs${curr_year === null ? '' : `/${curr_year}`}`;
      const response = await fetch(url);

      if(response.status === 200){
        console.log("retrieval successful");

        // pass retrieved repositories to another component called
        // Experience.svelte
        const data = await response.json();

        // if and only if upon page load curr_year is null in order
        // to get min and max years but if user requests for a specific
        // year then data does not contain anymore min and max year keys
        // so we only have to confine setting min and max year upon mounting
        if(curr_year === null){
          min_year = data[0]['min_year'];
          max_year = data[0]['max_year'];
        }
        contribs = data[0]['contribs'];

      }else{
        console.log(`retrieval unsuccessful. Response status '${response.status}' occured`);
      }

    }catch(error){
      console.log(`request denied. Error '${error}' occured.`);
    }
  }

  // upon mounting of component send http request to flask
  // backend proxy server and retrieve repositories
  onMount(async () => {
    fetch_repos();
    fetch_contribs();
  });

  
  

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
    <Experience slot="exp-section" min_year={min_year} max_year={max_year} contribs={contribs} on:changeYear={fetch_contribs}/>
  </Work>
  <Contact slot="contact-section" on:sendMail={send_mail}/>
</Content>