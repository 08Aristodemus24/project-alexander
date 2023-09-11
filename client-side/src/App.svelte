<script>
  import { onMount, onDestroy } from "svelte";
  import Navbar from './components/Navbar.svelte';
  import NavbarBurger from './components/NavbarBurger.svelte';

  import './assets/stylesheets/small-desktop.css';
  import './assets/stylesheets/small-phone.css';
  import Hero from "./components/Hero.svelte";
  // import Tailwind from "./components/Tailwind.svelte";
  

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
<Hero/>
<Hero/>
<Hero/>
<Hero/>
<Hero/>
<Hero/>
<Hero/>
<Hero/>
<Hero/>
<Hero/>