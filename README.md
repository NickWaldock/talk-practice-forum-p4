# Talk Practice Forum
<img src="readme-imgs/titles.png" width="50%">
<br/>

[View the live site here](https://talk-practice-forum-p4.herokuapp.com/)
<br/>
<br/>

# Table of Contents
1. [Introduction](#introduction)
    1. [Aims](#aims)
    2. [User Stories](#user-stories)
2. [Main Features](#main-features)
    1. [Wireframes](#wireframes)
    2. [DataBase](#database)
    3. [](#)
    4. [](#)
    5. [](#)
    6. [](#)
    7. [](#)
    8. [](#)
    9. [](#)
3. [Future Development](#future-developments)
4. [Technologies](#technologies)
    1. [](#)
5. [Testing](#testing)
    1. [Pep8](#pep8)
    2. [Manual Testing](#manual-testing)
    3. [Tools](#tools)
    4. [Bugs](#bugs)
6. [Deployment](#deployment)
    1. [Heroku](#heroku)
    2. [Forking](#forking)
    3. [Cloning](#cloning)
7. [References & Acknowledgements](#references--acknowledgements)
   1. [References](#references)
   2. [General Reference](#general-reference)
   3. [Code Reference](#code-reference)
   4. [Code Syntax Validators](#code-syntax-validators)
   5. [Acknoledgements](#acknoledgements)
<br />
<br />

# Introduction

<br>
<br>

## Aims
- 
- The project should utilise a full-stack framework with relevant technologies and be deployed via [Heroku](https://signup.heroku.com/)
- 
- 
- 
- 
- 
- 
<br />
<br />

## Agile Methodology

## User Stories
### Milestones
As a new user, I want to:
- 
- 
As a new registered user, I want to:
- 
- 
As admin, I want to:
- 
-
<br />
<br />

# Main Features
## Wireframes


<img src="" width="45%">
<br />
<br />

## UX Desgin
### Typography
<br />

### Colour
<br />

### Bootstrap
<br />
<br />

## Database
<img src="" width="100%">
<br />
This flowcart was created using [Lucid Chart](https://www.lucidchart.com/). The database is hosted by 
[ElephantSQL](https://www.elephantsql.com/) using a [PostgresSQL](https://www.postgresql.org/) relational database structure for storing the django models data
<br />
<br />

## CRUD
<img src="" width="50%">
<br />
info

<br />
<br />

<img src="" width="50%">
<br />
info

<br />
<br />

## 1. Create
<img src="" width="50%">
<br />

Add post


<br />
<br />

<img src="" width="50%">
<br />
add category
Dynamic nav bar menu
<br />
<br />


<img src="" width="50%">
<br />
Contact form

<br />
<br />

## 2. Read / View
<img src="" width="50%">
<br />
view Posts list

<br />
<br />
<img src="" width="50%">
view full article

<br />
<br />


## 3. Update Post
<img src="" width="50%">
<br />
Update Post
<br />
<br />



## 4. Delete Post
<img src="" width="50%">
<img src="" width="50%">
<br />
Delete post
<br />
<br />

## 4. Dynamic Category Menu
<img src="" width="50%">
<br />
dynamic category menu
<br />
<br />

<img src="" width="50%">
<br />
dynamic category list page
<br />
<br />


<img src="" width="50%">
<br />
Articles by category list page
<br />
<br />

## 5. Contact Page
<img src="" width="50%">
<br />
Contact page
<br />
<br />

## 6. Messages
<img src="" width="50%">
<br />
Form validation and login messages
<br />
<br />

# Future Developments
This project has a great deal of developmental potential in features that could eventually add increased functionality and a deeper user experiece. 

The following are a few examples:
- Page loading by 10 posts when there are multiple posts- pagination
- Save post as draft
- Sidebar becomes footer in md and small screens
- Reset password / forgotten password links
- Search function
- Tags
- Rich text editor on front end, formatting the display of posts
- In the contact form, remove the checkbox asking if user is a member and code to check for this automatically on submission
- Having the post card clickable to navigate to the post rather than just the title, but still able to click the author or category to navigate
- Allow personal profiles page, to add, update user's public information
- Post author's user profile's linked to relevant posts for public viewing

<br />
<br />

# Technologies
Technologies used in this site are:
- [Django]() for the rendering of the database models and templates
- [Javascript]() at this point in the project JS is soley used for making django validation messages auto-dissapear, and to automatically set the current user as the 'author' in the form field for the database when adding a new post
- [HTML]() for creating the web templates and navigating between them
- [CSS]() for custom styling
- [Bootstrap]() for general layout and styling


Additional technologies include: 
- [GitHub](https://github.com/)
  - Site repository
- [Gitpod](https://gitpod.io/)
  - Online IDE for all coding work and site file management, terminal was used to add, commit, and push to Github
<br />
<br />

## Requirements
Additional requirements used in this python project include:
<br />

<img src="" width="30%">
<br />

- 

<br />
<br />
-

<br />
<br />

# Testing
## Pep8

<br />
<br />

## Manual Testing 
Each function and validation has been manually tested. All testing logs can her viewed here:
[>> Testing](/readme-files/manual-testing.md)
<br />
<br />

## Tools
Tools used in the development of this project include:
- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)
- [Heroku](https://heroku.com/)
- [Lucid Chart](https://www.lucidchart.com/)
<br />
<br />

## Bugs

- On desktop - Safari: The checkbox button for the contact form renders on the left of the page and not the center as it should, and as it does in Chrome, Firefox, and Edge - *SOLVED*
- On Tablets - Safari, Firefox, Chrome, Edge: The checkbox button for the contact form renders on the left of the page and not the center as it should. - *SOLVED*

### 1. Messages 
<img src="" width="70%">

- 

<br />
<br />

### 2. Heroku
<img src="readme-imgs/herouku-bug.png" width="70%">

- On deployment to [Heroku](https://signup.heroku.com/) a irritating bug occurs within the console. The program uses specific and commonly used 'clear screen' command (from the [OS Module](https://docs.python.org/3/library/os.html)) which within the IDE GitPod functions as intended. However, within Heroku although the clear screen command seems functional, if the user scrolls up the console previous printed data can be viewed is glitched. On researching this issue I found little help, and at the time of deployment I was unable to solve this issue.
<br />
<br />



# Deployment
The live site can be accessed [here](https://talk-practice-forum-p4.herokuapp.com/)
<br />
<br />

## Heroku
This project was deloyed to [Heroku](https://heroku.com/) with the following steps:
1. Log in to Heroku (create an account if necessary)
2. Navigate to your dashboard, click "New" and select "Create new app"
3. Input an appropriate name for your project and choose a region
4. Click the "Settings" tab
5. Click "Reveal Config Vars"
6. Input PORT and 8000 as one config var and click add
7. Input CREDS and the information from your Google Sheet API creds file as another config var and click add
8. Click "Add buildpack"
9. Add "nodejs" and "python" from the list or search if required, click save.
10. Ensure python is the first build pack. YOu can drag to change the order
11. Select "Deploy" from the heading tabs
12. Select "GitHub - Connect to GitHub" next to the Deployment Methods
13. Click "Connect to GitHub"
14. Search for the repository ("practice-log") and click to connect
15. Click either 'Enable Automatic Deploys' or 'Deploy Branch' to deploy manually. If you select Deploy Branch please note you will need to manually deploy each time you update the repository.
16. Finally, click 'View' to visit the deployed site. It may take a moment to become visible
<br />
<br />

## Forking
To fork this repository on [Github](https://github.com/NickWaldock/practice-log) proceed with the following steps:
1. Log it to GitHub (create an account if necessary)
2. Locate the [GitHub Respository](https://github.com/NickWaldock/practice-log)
3. On the repository page, find the 'Fork' menu in the top right, click on the small down arrow
4. Select '+ Create a new fork'
5. Remane repository as required
6. Click 'Create Fork'
7. You now have your forked version of this repository
<br />
<br />

## Cloning
To clone the repository procees with the following steps:
1. Log in to GitHub (create an account if necessary)
2. Locate the [GitHub Respository](https://github.com/NickWaldock/practice-log)
3. On the repository page, find and click on the 'Code' menu in the mid-top right of the page
4. Choose to either download or open in GitHub Desktop,
  - or;
    5. Choose the HTTPS option and copy the URL to your clipboard
    6. - To clone the repository using HTTPS, under "HTTPS", copy the url
       - To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then copy the url
       - To clone a repository using GitHub CLI, click GitHub CLI, then copy url
    7. Open Terminal and change the current directory to where you want the cloned directory
    8. Type git clone, and paste the url, press Enter to create your local clone
<br />
<br />

# References & Acknoledgements
- Gitpod repository template provided by [Code Institute](https://codeinstitute.net)
<br />
<br />

## General Reference
- [Python](https://www.python.org/)
General Reference

<br />
<br />

## Code Reference - Walkthroughs

<br />
<br />

### Walkthrough Reference 1
-[]()

<br />
<br />

### Walkthrough Reference 2
- []()

<br />
<br />

## Code Syntax Validators
The following sites were used for syntax and logic checking:
<br />
<br />

## Acknoledgements
I am incredibly grateful to my Code Institute Mentor Chris Quinn for his support and guidance, as well as the course providers and tutors at Code Institute for the expertise and support.

Connect with me on [LinkedIn](https://www.linkedin.com/in/nicholas-waldock-05237071/)


------------------------------------------------------------------------------------------


Improvments



References
Summernote
https://summernote.org/

Python
https://realpython.com/

Elephant SQL Database
Cloudinary media and static files hosting

For logo design
https://looka.com/

CSS
For navbar gradient
https://mdbootstrap.com/docs/standard/tools/design/gradients/

Card Hover
https://ordinarycoders.com/blog/article/codepen-bootstrap-card-hovers



Django
https://ccbv.co.uk/projects/Django/4.1/django.views.generic.edit/CreateView/
https://docs.djangoproject.com/

Slugs
https://forum.djangoproject.com/t/django-how-to-add-slug-as-arguments-in-url-tag-using-django/12636
https://forum.djangoproject.com/t/passing-slug-to-createview/4287

All Auth
https://django-allauth.readthedocs.io/en/latest/

Messages
https://docs.djangoproject.com/en/3.2/ref/contrib/messages/#using-messages-in-views-and-templates
https://stackoverflow.com/questions/24914637/show-a-successful-message-with-class-based-views
https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown






Random Text Generator - for post content
https://randomtextgenerator.com/