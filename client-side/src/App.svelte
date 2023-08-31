<script>
  import './app.css'
  import { onMount, onDestroy } from "svelte";

  // initial state
  let repos = [];

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

</script>

<main>
  <ul>
    {#each repos as repo}
      <li>{repo}</li>
    {/each}
    <!-- {some_var} -->
  </ul>
</main>