// import dotenv to import access token
const response = require('dotenv').config({path: '../.env'});
// console.log(response);

const load_repos = async () => {
    // to pass multiple params encode it using encodeURIComponent
    // encodeURIComponent('www.foobar.com/?first=1&second=12&third=5');
    try{
        const url = 'https://api.github.com/users/08Aristodemus24/repos';
        const token = process.env['GITHUB_ACCESS_TOKEN'];
        
        // const auth_token = `Bearer ${process.env['GITHUB_ACCESS_TOKEN']}`;
        const response = await fetch(url, {
            headers: {
                "Accept": "application/vnd.github+json",
                "Authorization": `Bearer ${token}`,
            },
        });

        if(response.status === 200){
            console.log("retrieval successful");
            const repos = await response.json();

            const ul = document.createElement('ul');
            const proj_sect = document.querySelector('section#projects');


            for(let repo of repos){
                console.log(repo);

                // create li element for ul
                const li = document.createElement('li');
                
                // use repository html_url key for href attribute 
                // value of <a> tag point href to repository url
                const a = document.createElement('a');
                a.setAttribute('href', repo['html_url']);
                a.setAttribute('class', `${repo['name']} repo-${repo['id']}`);
                a.textContent = `${repo['name']}\nforks: ${repo['forks_count']}\nstars: ${repo['stargazers_count']}\nwatching: ${repo['watchers_count']}`;
                
                // append created elements to ul
                li.appendChild(a);
                ul.appendChild(li);
            }

            // append ul as child to selected element 
            // in dom which is section projects
            proj_sect.appendChild(ul);
        }else{
            console.log(`retrieval unsuccessful. response status ${response.status} occured`);
        }    
    }catch(error){
        console.log(`${error} HAS OCCURED`);
    }    
};

// upon loading of document set onload property 
// of window to the load_repos async callback
window.onload = load_repos;


const navigate = () => {
    const links = ['about-me', 'projects', 'contact']

    // grab the a element with arrow
    
    // change current state of the buttons
}