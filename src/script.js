// import dotenv to import access token
// const response = require('dotenv').config({path: '../.env'});
// // console.log(response);



// const load_repos = async () => {
//     /*
//     fetches all my repositories using github api then renders
//     all public repositories uisng html dom api
//     */


//     // to pass multiple params encode it using encodeURIComponent
//     // encodeURIComponent('www.foobar.com/?first=1&second=12&third=5');
//     try{
//         const url = 'https://api.github.com/users/08Aristodemus24/repos';
//         const accept = 'application/vnd.github+json';
//         const auth_token =`Bearer ${process.env['GITHUB_ACCESS_TOKEN']}`;
        
//         const response = await fetch(url, {
//             headers: {
//                 "Accept": accept,
//                 "Authorization": auth_token,
//             },
//         });
        
//         if(response.status === 200){
//             console.log("retrieval successful");
//             const repos = await response.json();

//             const ul = document.createElement('ul');
//             const proj_sect = document.querySelector('section#projects');


//             for(let repo of repos){
//                 console.log(repo);

//                 // create li element for ul
//                 const li = document.createElement('li');
                
//                 // use repository html_url key for href attribute 
//                 // value of <a> tag point href to repository url
//                 const a = document.createElement('a');
//                 a.setAttribute('href', repo['html_url']);
//                 a.setAttribute('class', `${repo['name']} repo-${repo['id']}`);
//                 a.textContent = `${repo['name']}\nforks: ${repo['forks_count']}\nstars: ${repo['stargazers_count']}\nwatching: ${repo['watchers_count']}`;
                
//                 // append created elements to ul
//                 li.appendChild(a);
//                 ul.appendChild(li);
//             }

//             // append ul as child to selected element 
//             // in dom which is section projects
//             proj_sect.appendChild(ul);
//         }else{
//             console.log(`retrieval unsuccessful. response status ${response.status} occured`);
//         }    
//     }catch(error){
//         console.log(`${error} HAS OCCURED`);
//     }    
// };

// // upon loading of document set onload event property 
// // of window to the load_repos async callback
// window.onload = load_repos;

document.addEventListener('DOMContentLoaded', () => {
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
    console.log($navbarBurgers)
    // Add a click event on each of them
    $navbarBurgers.forEach(el => {
        el.addEventListener('click', () => {
    
            // Get the target from the "data-target" attribute
            const target = el.dataset.target;
            const $target = document.getElementById(target);
    
            // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
            el.classList.toggle('is-active');
            $target.classList.toggle('is-active');
        });
    });  
});