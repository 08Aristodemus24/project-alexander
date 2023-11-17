<script>
    import { afterUpdate, onMount } from "svelte";
    import Accordion from "./Accordion.svelte";
    import ProjectsButton from "./ProjectsButton.svelte";

    // initial state of list before fetching repositories
    let repos = [];

    // list of repositories to include in projects section
    // if retrieval of repositories is unsuccessful just initialize empty repos
    let included = [
        {name: null, description: null, html_url: null, project_id: 'I', project_image: 'https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/compressed%20images/breast-cancer-classifier.jpg'},
        {name: null, description: null, html_url: null, project_id: 'II', project_image: 'https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/compressed%20images/hate-speech-classifier.png'},
        {name: null, description: null, html_url: null, project_id: 'III', project_image: 'https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/compressed%20images/housing-prices-predictor.jpg'},
        {name: null, description: null, html_url: null, project_id: 'IV', project_image: 'https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/compressed%20images/larj-corpus.jpg'},
        {name: null,   description: null, html_url: null, project_id: 'V', project_image: 'https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/compressed%20images/phil-jurisprudence-recsys.jpg'},
        {name: null, description: null, html_url: null, project_id: 'VI', project_image: 'https://raw.githubusercontent.com/08Aristodemus24/project-alexander/master/client-side/src/boards/compressed%20images/project-alexander.jpg'},
    ];

    const fetch_repos = async () => {
        try{
            // // for development
            // const url = 'http://127.0.0.1:5000/repos/100';
            // for production
            const url = 'https://project-alexander.vercel.app/repos/100';
            const response = await fetch(url);
            
            if(response.status === 200){
                console.log("retrieval successful");

                // pass retrieved repositories to another component called
                // Project.svelte
                const data = await response.json();

                // everytime new repositories are added we overwrite the old
                // contents of the repos state
                repos = [...data];
                console.log(data);

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
                    included[index]['stargazers_count'] = repo['stargazers_count'];
                    included[index]['forks_count'] = repo['forks_count'];

                    return included[index];
                });

            }else{
                console.log(`retrieval unsuccessful. Response status '${response.status}' occured`);
            }

        }catch(error){
            console.log(`request denied. Error '${error}' occured.`);
        }
    }


    let is_opened = false;
    let proj_header_container;
    const close_header = (event) => {
        // close header only once
        if(is_opened === false){
            is_opened = true;
        }

        // run for precisely 1 second after state update
        setTimeout(() => {
            // remove projects-header-container from dom precisely 1
            // second after visibility and opacity transition is ran
            proj_header_container.style.display = "none";
        }, 1000);
    };

    // upon mounting of component send http request to flask
    // backend proxy server and retrieve repositories
    onMount(async () => {
        fetch_repos();
    });

    afterUpdate(async () => {
        console.log("component updated");
    })
</script>

<section id="projects-section">
    <div class="projects-content">
        <div class="projects-header-container" class:closed={is_opened === true} bind:this={proj_header_container}>
            <h1>Projects</h1>
            <ProjectsButton close_header={close_header}/>
        </div>
        <div class="projects-accordion-container" class:opened={is_opened === true}>
            <Accordion repos={included}/>
        </div>
    </div>
</section>