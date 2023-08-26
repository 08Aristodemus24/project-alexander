# **STILL IN PRODUCTION**

# My portfolio website for my AI/ML projects built with Vanilla.js, Bootstrap, and Flask

# Frontend
## Designing website template:
**Prerequisites to do:**
1. 
**To do:**
1. create designs for each section on paper for mobile and desktop
a. <s>about</s>
b. <s>skills or technologies used</s>
b. <s>projects</s>
c. <s>experience</s>
d. <s>contact me</s>
2. create background image in landing page
a. could use AI generated images from leonardo
b. could use photoshop to collage images from mediafiles
3. figure out colors to be used
4. figure out shape, border, texture, etc. of components like buttons, container, socials, navbar items, etc.
5. <s>uninstall bulma and switch to bootstrap for more components and community support</s>
6. <s>uninstall dotenv since dotenv will just be handled by backend server proxy</s>
7. include only relevant repositories by maybe including a rules lookup/dictionary or iterable that contains only the repositories to be displayed or not displayed

**Tech used:**
* Vanilla.js
* Boostrap
* Three.js (TBD)

**References:**
* https://wikiki.github.io/components/carousel/
* https://bulma-carousel.onrender.com/
* https://codepen.io/aeryla/pen/PoKaBYM
* https://codepen.io/jshwrnr/pen/BaRwBZM
* https://codepen.io/DivyaPatel/pen/dxjgVL

**Side notes:**
1. Mixins in sass:
main {
    @include flexCenter(row);
    width: 80%;
    margin: 0 auto;
    
    #{&}__paragraph {
        font-weight: weight(bold);

        &:hover { 
            color: pink;
        }
    }
}

@mixin <function name>($<parameter name>){
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

# Backend
## Setting up backend proxy server for accessing .env file
**Prerequisities to do:**
1. 

**To do:**
1. <s>install flask</s>
2. <s>set route's url pattern to https://<localhost>:5000 in order to receive http requests from client requesting this url</s>

**Problems and solutions:**
1. http://127.0.0.1:5000 blocked by CORS policy when requesting to api endpoint http://127.0.0.1:5500/ - solution: https://medium.com/@mterrano1/cors-in-a-flask-api-38051388f8cc
2. 

**Tech used:**
1. flask
2. flask-cors

**References:**
1. a

**Side notes:**