# PROJECT NAME TBA
---
## Code Institute - Data Centric Development Milestone Project
---

The goal of this project is to build a full-stack website that allows users to manage a common dataset about a particular domain. The website must include front end technologies (HMTL, CSS) and backend technologies (JavaScript, Python+Flask and MongoDB).
---
## Table of Contents

* [Live Site](#live-site)
* [UX](#user-experience)
* [Features](#features)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

---
## Live Site
The live deployed demo is hosted by Heroku and can be found here.

---
## User Experience
WEBSITE NAME was designed as a website for people interested in outdoors walking to find and follow user input walking routes. Equally, users may input and store their own walking routes for others to read and follow. 
This site is tailored to walkers as many sites are, but was also meant to be focussed on more locally known walks and routes which may not be known to more commercial websites.

### User Stories
1.	As a user I want to be able to search for local walks in a desired area.
2.	As a user, I want to have the option to log in and add my own walks/routes
3.	As a user, I need a page to add my route and upload it to the website.
4.	As a registered user, i need to be able to edit or remove any routes I have added.
5.	As a registered user, it would be good to have an easy way of showing the route on a map.
6.	As a user, it would be useful to have extra information for each route available.
7.	As a registered user, I would like to be able to save routes for later.

### Database Collections
Categories:
```
    {
        "_id":<ObjectId>,
        "category_name":<string>
    }
```

Difficulty:
```
    {
        "_id":<ObjectId>,
        "challenge":<string>
    }
```

Routes:
``` 
    {
        "_id":<ObjectId>,
        "title":<string>,
        "description":<string>,
        "directions":<array>,
        "user":<string>,
        "category_name":<string>,
        "difficulty":<array>,
        "time":<string>,
        "distance":<string>,
        "startpoint":<string>,
        "dogs_allowed":<boolean>,
        "free_parking":<boolean>,
        "paid_parking":<boolean>,
        "saved":<boolean>
    }
```

Users:
```
    {
        "_id":<ObjectId>,
        "username":<string>,
        "password":<string>,
        "saved":<array of ObjectId>
    }
```

FAQs:
```
    {
        "_id":<ObjectId>,
        "FAQ":<string>,
        "Answer":<string>,
        *"report_problem":<string> - optional*
    }
```

### Wireframes
All wireframes were constructed using the Balsamiq Tool. As some webpages served very similar services, such as log in/register and add walk/edit walk, these were made using the same page template but with required information completed using the database.

### Surface Design

TBA

---
## Features

#### Front end features:
* Navigation: The user has easy access to any webpage using the navigation bar at the top of the page.
* An engaging landing page which is not overwhelmed with information.
* A footer for social media and some navigation purposes.
* Search Page: Walking routes can be browsed by categories of walks, key information such as dog-friendly, or by keywords in the title and description.
* Displays as cards with some details below and an image
* Profile Page: A page which selects and displays all walking routes uploaded by a user so that they can edit or delete them if they choose.
* Log in/Register Page: Two pages designed to allow easy options for creating or opening a profile on this website, allowing the creation and deletion of walking routes.
* Possibly a top rated walks section.
* Add/edit Route page: Forms for the creation and addition of personal walking routes  into the database which can be presented on the website. Also offers the change to edit content 
* Route page: This has not only a description and directions section, but key features and details of the walk along with images and maybe a map.

#### Back end features:
⦁	TBA

### Features to Implement:
⦁	Responsive Pagination: As there are not many walks currently uploaded to the website it was not required to make the pagination more expansive than it already is. However, if this
were to become a larger database of walking routes, pagination which is responsive to not stretch smaller screens would be required.

---
## Technologies

### Languages
* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
* [Javascript 6](https://developer.mozilla.org/en-US/docs/Web/JavaScript) Specifically ECMAScript 6/2015
* [Python 3.8.5](https://www.python.org/)

### Libraries, Frameworks and Tools
1. [Bootstrap v4.7.0](https://getbootstrap.com/): Front end framework for development of websites, offers pre-designed components and classes which can be further customised.
2. [jQuery](https://jquery.com/): Library of base JavaScript, allowing the use of interactivity and features on components and simplifying DOM.
3. Git: Version control system used to catalogue project development.
4. [Flask](https://flask.palletsprojects.com/en/1.1.x/): Version 1.2; a web framework with tools, libraries and technologies to develop this website.
5. [Jinja2](https://palletsprojects.com/p/jinja/) (2.11.2): Templating language enabling python to creat HTML and other markup formats for website.
6. [PyMongo](https://pypi.org/project/pymongo/): Version 2.3.0 Tool used to let Python interact with MongoDB.
7. [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools): Online resource in Chrome browser, used to make edit pages quickly to diagnose problems or test changes.
8. [Google Fonts](https://fonts.google.com/): Library used to embed and link expanded font choices into the project.
9. [Font-Awesome](https://fontawesome.com/): Library offering a wide icon set for use in projects.
10. [Favicon.io](): Favicon generator which converts images into favicons for use in the browser tab.
11. [Adobe Color](https://color.adobe.com/explore): Online tool used for identifying colour palettes and themes. Used to extrapolate colours from images and find suitable colour ranges.
12. [Balsamiq](https://balsamiq.com/): Wireframing tool for concept creation and design for website.
13. Clip Paint Studio: ?
14. [Autoprefixer CSS Online](https://autoprefixer.github.io/): parsed CSS and produced webkit vendor prefixes for CSS stylings to work correctly on other browsers.
15. [Visual Studio Code](https://code.visualstudio.com/): A programming environment for developing which allows for extensions and testing.
16. [Prettier](https://prettier.io/): A tool used in combination with VS Code to format and style code.
17. [Jasmine](https://jasmine.github.io/): A tool used in combination with VS code to perform unit testing.
18. [ESLint](https://eslint.org/): Linting tool installed in visual studio code.

### APIs

---
## Testing

### User Story Testing

### Validation

### Unit Testing

### Bugs
Older posts done before the WTForm update, could not be edited properly. This might be that they were failing validation before even being loaded so could not be stored. Unsure as most of these were unfit for purpose anyway and were deleted for new data which was not incomplete.

## Deployment
The source code for this website was deployed and stored in a GitHub repository while the website application is hosted by Heroku. The two are linked so any new commits or pushes to GitHub's master branch are also updated on the Heroku hosting service.
The database for this website is hosted in a cluster on MongoDB.

### Heroku Cloud
Heroku service allows for the deployment of our app as a live website, however two files are required for upload.
A requirements.txt file includes the majority applications and dependencies required for this app to be run correctly. This was created using the pip3 freeze --local > requirements.txt command in the terminal.

A Procfile is also required to to determine how the app is run. Please ensure the file has no extra lines below the text as this can cause problems with Heroku.

#### Create a new app linked to Github:
1. Assuming you are already logged into Heroku, from your dashboard click the _"New"_ button in the top right and select _"Create App"_.
2. Name your app and chose region (name must be unique and have no spaces)
3. On the new app's main page, go to the deployment method section and select _"Github: Connect to Github"_.
4. A new searchbar will appear below, check the user is correct and search for the relevant repository.
5. Once the correct repository has been found, scroll to the top of the page and select the "Settings" menu.
6. In Settings, locate the _"Reveal Config Vars"_ button and enter any private configuration variables required to run the app (I.E. Port, IP address, etc)
7. Assuming a Procfile and requirements file already exist, return to the _"Deploy"_ page in the top menu and select the _"Enable Automatic Deploys"_ button.
8. The bottom of the page should now build the app and present a message titled _"Your app was successfully deployed"_.
9. Your app should now be deployed and any Github pushes also pushed to the Heroku app.

#### How to clone the repository:
1. Navigate to the correct repository from the GitHub dashboard.
2. Above the list of files, click the green “Code” button.
3. From the dropdown, select the _“Clone with HTTPS”_ by selecting the clipboard icon.
4. Open Git Bash and change the working directory to the location you would like the clone to be.
5. Type git clone, and past the URL you have copied. (Should be in the format $ git clone https://github.com/username/repository.)
6. Press _"Enter"_ to create your local clone.

## Credits
### Content
TBA 

### Media
TBA            

### Acknowledgements
Special thanks to my mentor Brian Macharia for his help and advice in development this project.
Libraries for google fonts, bootstrap, jQuery and font-awesome were used throughout my project.

Inspiration and techniques for pagination found from three main sources:
* [Pretty Printed Tutorial](https://www.youtube.com/watch?v=Lnt6JqtzM7I&feature=emb_logo)
* [faithy80's milestone project](https://github.com/faithy80/dcd-project/blob/master/run.py)
* [The top comment by mangoed on this reddit post](https://www.reddit.com/r/flask/comments/fxtfzm/is_there_a_way_to_add_pagination_to_my_webapp/)
                            
### Disclaimer
This project has been made for purely academic purposes.