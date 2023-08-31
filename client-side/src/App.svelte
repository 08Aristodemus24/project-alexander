<script>
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
      repos = await response.json();

    }else{
      console.log(`retrieval unsuccessful. Response status ${response.status} occured`)
    }
  })

</script>

<main>
  <ul>
    {#each repos as repo}
      <li>{repo}</li>
    {/each}
  </ul>
</main>