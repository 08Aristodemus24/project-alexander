// import dotenv to import access token
// const response = require('dotenv').config({path: '../.env'});
// // console.log(response);



const load_repos = async () => {
    /*
    fetches all my repositories using github api then renders
    all public repositories uisng html dom api
    */


    // to pass multiple params encode it using encodeURIComponent
    // encodeURIComponent('www.foobar.com/?first=1&second=12&third=5');
    try{
        const url = 'http://127.0.0.1:5000/';
        
        const response = await fetch(url);
        
        if(response.status === 200){
            console.log("retrieval successful");
            const repos = await response.json();
            // console.log(repos);

            for(let repo of repos){
                console.log(repo);
            }
        }else{
            console.log(`retrieval unsuccessful. response status ${response.status} occured`);
        }    
    }catch(error){
        console.log(`${error} HAS OCCURED`);
    }    
};

// upon loading of document set onload event property 
// of window to the load_repos async callback
window.onload = load_repos;