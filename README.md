# Cornish Walks
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
The live deployed demo is hosted by Heroku and can be found [here](http://data-centric-milestone-rhys.herokuapp.com/home).

---
## User Experience
Cornish Walks was designed as a website for people interested in outdoors walking to find and follow user input walking routes. Equally, users may input and store their own walking routes for others to read and follow. 
This site is tailored to walkers as many sites are, but was also meant to be focussed on more locally known walks and routes which may not be known to more commercial websites.

### Business Goals:
Cornish walks as a company website is based on the collection of users and sharing of information:
* Registering users for a returning viewer baser.
* User's adding walks to grow content and encourage site traffic.
* Eventually add in some form of monetization or revenue such as advertisements, endorsements or subscriptions.
* Encourage a healthy activity for users in a safe environment.

### User Goals:
Users are the primary goal and content of this website so their goals must align with the core concepts of designing and implementing any service offered on this project:
* Find walks in their local area.
* Find trips or walks for a holiday.
* Undertake walks they like the look of.
* Bookmark and retry walks they have enjoyed.
* Add personal experiences and walks to share with others.

### User Stories
1.	As a user I want to be able to search for local walks in a desired area.
2.	As a user, I want to have the option to log in and add my own walks/routes
3.	As a user, I need a page to add my route and upload it to the website.
4.	As a registered user, i need to be able to edit or remove any routes I have added.
5.	As a registered user, it would be good to have an easy way of showing the route on a map.
6.	As a user, it would be useful to have extra information for each route available.
7.	As a registered user, I would like to be able to save routes for later.

### Structure/Database Collections
##### Categories:
```
    {
        "_id":<ObjectId>,
        "category_name":<string>
    }
```

##### Difficulty:
```
    {
        "_id":<ObjectId>,
        "challenge":<string>
    }
```
Both categories and difficulty are used to complete select element options dynamically. This way if the difficulties were changed or updated, they only need to be corrected at the source. This also allows for them to be more easily validated if changed.

##### Routes:
``` 
    {
        "_id":<ObjectId>,
        "title":<string>,
        "description":<string>,
        "directions":<array>,
        "imageUrl":<string>,
        "category_name":<string>,
        "difficulty":<string>,
        "time":<string>,
        "distance":<string>,
        "startpoint":<string>,
        "dogs_allowed":<boolean>,
        "free_parking":<boolean>,
        "paid_parking":<boolean>,
        "user":<string>
    }
```
All the data required to fill a walking route page.

##### Users:
```
    {
        "_id":<ObjectId>,
        "username":<string>,
        "password":<string>,
        "favourites":<array of ObjectId>
    }
```
All users must have an empty favourite array upon creation at minimum to prevent errors entering pages which look for a `favourites` field.

##### FAQs:
```
    {
        "_id":<ObjectId>,
        "FAQ":<string>,
        "Answer":<string>,
        *"report_problem":<string> - optional*
    }
```

##### Messages:
```
    {
        "_id":<ObjectId>,
        "Issue":<string>,
        "Message":<string>,
    }
```

The message collection was used as an alternative to a email system as most messages do not currently required direct feed back. Also the email features were not considered essential to the current website construction so have been considered future goals to implement.

### Wireframes
All wireframes were constructed using the Balsamiq Tool. As some webpages served very similar services, such as log in/register and add walk/edit walk, these were made using the same page template but with required information completed using the database.

Initial designs were designed to have large images and easily selectable objects without too much distracting or confusing information. This was decided as most people after a walking route will only take a few moments to see and decide on a walk and will not be interested if the information is hard to find. Also, walking is a common activity for older users who may not be as technical as younger users might be.

* [Home page -mobile/laptop](https://github.com/RhysPollardDevelopment/Data-centric_milestone/tree/master/wireframes/indexpage.pdf)
* [Search page -mobile/laptop](https://github.com/RhysPollardDevelopment/Data-centric_milestone/tree/master/wireframes/searchpage.pdf)
* [Contact page -mobile](https://github.com/RhysPollardDevelopment/Data-centric_milestone/tree/master/wireframes/contactpagemobile.pdf)
* [Contact page -laptop](https://github.com/RhysPollardDevelopment/Data-centric_milestone/tree/master/wireframes/contactpagelaptop.pdf)
* [Login/register -mobile/laptop](https://github.com/RhysPollardDevelopment/Data-centric_milestone/tree/master/wireframes/loginregisterpage.pdf)
* [User page -mobile/laptop](https://github.com/RhysPollardDevelopment/Data-centric_milestone/tree/master/wireframes/userpage.pdf)
* [Walk page -mobile/laptop](https://github.com/RhysPollardDevelopment/Data-centric_milestone/tree/master/wireframes/walkpage.pdf)
* [Add/Edit walk page -mobile/laptop](https://github.com/RhysPollardDevelopment/Data-centric_milestone/tree/master/wireframes/walkformpage.pdf)

### Surface Design
* #### Colour Scheme:
    For the main colours of this project I have chosen to go with a teal colour and soft gray for the header and footer navigations, along with some localised elements for continuity. Originally the main background was a soft yellow in colour so that the teal and cream would inspire beaches, while the gray would inspire granite while also being very smart and sleek.
    The cream background elements were removed as it was made pages with heavy focus on forms, pages lacking images such as add-walk and contact us, seem to stand out unpleasantly and was deemed not necessary to the overall colour palette. Teal has remained a key focus for buttons, featured elements and general user interface, unless requiring clearer context such as warning or delete buttons.

* #### Typography:
    Oswald and Raleway were chosen for headings and main text respectively from [Google Fonts](https://fonts.google.com/). Oswald has a very strong, smart style which draws the eye to key points and creates a good contrast between any background colour or image. On the other hand Raleway is softer and curved, making it easy and approachable to read on majority of screen sizes compared to thinner, more stylized fonts. Ensuring that fonts are readable over images was also a key point, specifically on the walking pages headers where user selected images may not always perfect for the colour text chosen. This is why an overlay of black was used to always provide better contrast to the off-white text.

* #### Images:
    There are many images to this project but most are to be provided by users through image urls. This means I had to present them clearly using square or rectangluar boxes which would ideally not lose a lot of detail. Locally sourced images of Cornwall are used primarily for headers, large landing page images or smaller backgrounds to text.

* #### Form Design:
    Forms were designed to stick to the colour themes were possible, however they could not be mis-interpreted for validation such as the green/red validation offered by bootstrap. Similarly buttons are all based on a core rounded shape and are either clear for ones based above images or teal coloured. Some do seperate this by being red or other colours well known by users to represent warnings, errors or success.

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
* Featured walk section on landing page.
* Contact form and FAQ section in contact us page.
* Add/edit Route page: Forms for the creation and addition of personal walking routes  into the database which can be presented on the website. Also offers the change to edit content 
* Route page: This has not only a description and directions section, but key features and details of the walk along with images and maybe a map.
* Favourite walk scroll window.
* Changing icon for mobile navbar/burger icon.

#### Back end features:
* Create and add new walking routes to the MongoDB data base collections.
* Updated and edit information on walking routes already stored in MongoDB.
* Read information from the database when requested.
* Delete walks from databse using user's own userpage as required.
* Walks selected in MongoDB can be filtered.
* WTForms/FlaskForms offers validation and routing for forms which may hold sensitive information or to prevent dangerous activity.
* Password validation through Javascript which in turns can present a front end response informing the user.
* Addition and removal of favourite walks from a user profile to allow storage later.
* Pagination calculations and routing for search page number.
* Login capabilities and restrictions on content depending on user.

### Features to Implement:
* Responsive Pagination: As there are not many walks currently uploaded to the website it was not required to make the pagination more expansive than it already is. However, if this
were to become a larger database of walking routes, pagination which is responsive to not stretch smaller screens would be required.
* Automated emails and the ability to change email address: Email was requested on registration for these two features from the contact page report form and userpage respectively. Currently email is only used when a user needs to ask for a temporary log in as shown in the FAQ section. The goal would be to have the form check for a signed in user and send an automated reply upon submission of report but this was not made due to time constraints.
* EmailJS was originally planned as a feature, however due to the round-tripping nature of the contact form posting this was not possible to implement and was the main factor in deciding that a new email system would be too long to architecture.
* Automated forgotten password page: System to enter username and/or email and be sent a temporary password. As no email system was included this was not possible to implement.
* Map Waypoint system: Use of google maps and their SVG map creation tool to allow users to add a visual map route to each walk. The complexity of this made it not feasible as an option to add to this project.
* Word limit counter: A base word limit counter below certain text inputs. This was not chosen yet as the bootstrap validation offers some visual cue already when text has reached its desired length.

---
## Technologies

### Languages
* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
* [Javascript 6](https://developer.mozilla.org/en-US/docs/Web/JavaScript) Specifically ECMAScript 6/2015
* [Python 3.8.5](https://www.python.org/)
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/): Templating language used extensively for HTML in this project.

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
10. [favicon-generator](https://www.favicon-generator.org/): Favicon generator which converts images into favicons for use in the browser tab.
11. [Adobe Color](https://color.adobe.com/explore): Online tool used for identifying colour palettes and themes. Used to extrapolate colours from images and find suitable colour ranges.
12. [Balsamiq](https://balsamiq.com/): Wireframing tool for concept creation and design for website.
13. [MongoDB](https://mongodb.com): NoSQL database used to store and read information for this project.
14. [Autoprefixer CSS Online](https://autoprefixer.github.io/): parsed CSS and produced webkit vendor prefixes for CSS stylings to work correctly on other browsers.
15. [Visual Studio Code](https://code.visualstudio.com/): A programming environment for developing which allows for extensions and testing.
16. [Prettier](https://prettier.io/): A tool used in combination with VS Code to format and style code.
17. [Jasmine](https://jasmine.github.io/): A tool used in combination with VS code to perform unit testing.
18. [ESLint](https://eslint.org/): Linting tool installed in visual studio code.
19. [Pep8 Online](http://pep8online.com/): Linting tool online used to correct python code and ensure was pep8 compliant.
20. [WTForms/FlaskForms](https://wtforms.readthedocs.io/en/2.3.x/): Flask library used to create forms using flask and add backend validation.
21. [Am i responsive](http://ami.responsivedesign.is/): Tool used to see if a webpage is responsive across multiple screens.
22. [Responsinator](http://www.responsinator.com/): Website which mocks multiple phones and devices of different sizes and orientations.
23. [Clip Paint Studio](https://www.clipstudio.net/en/): Used to adjust some images and create landing page header.

---
## Testing

Testing can be found [here](https://github.com/RhysPollardDevelopment/Data-centric_milestone/blob/master/Testing.md)

## Deployment
The source code for this website was deployed and stored in a GitHub repository while the website application is hosted by Heroku. The two are linked so any new commits or pushes to GitHub's master branch are also updated on the Heroku hosting service.
The database for this website is hosted in a cluster on MongoDB.

### Heroku Cloud
Heroku service allows for the deployment of our app as a live website, below are the steps required to host a project:

#### Create a new app linked to Github:
1. Travel to the heroku website and create a user account as required.
2. Once registered, click  _"New"_ in the top right and _"Create App"_ from the dropdown.
3. Choose a name and region best suited for you before pressing the create app button.
4. Once on your new app page, select the _"Settings"_ header and scroll to Config Var. Here you can click _"reveal Config Vars"_ to add new configuration details.
5. Initially you want to ass a variable of 'IP' with a value of '0.0.0.0', once done add another named 'PORT' with a value of '5000'. You should also add any URI, DBNAME, SECRET_KEYS or other variables you have used in your environment which you do not want to be public.
6. Before connecting your github account to your Heroku app, return to your gitpod/VSCode and create a file named Procfile. Open this new file and enter 'web: python app.py', this will help Heroku define what sort of app you are creating.
7. Once your Procfile has been created, in the command line type 'pip3 freeze --local > requirements.txt'. This will automatically generate a file with any flask or python tools which are used in creating/using your project.
8. Return to Heroku and choose the _"Deploy"_ tab. In the section named _"Deployment method"_, choose the _"Github: Connect to Github"_ service.
9. When you created your account, you had the option to link a Git account to this heroku account. If so, then type in the repository which you want to host and search. If valid an option to connect will appear below which you can click.
10. Once connected you will be given an option to _"Choose branch to deploy"_ which should ideally be master. Once chosen, click the _"Enable Automatic Deploys"_ button below to create an updated site anytime you push to the master branch.
11. At the bottom of the page, make sure you are still using the master branch and click _"Deploy branch"_.
12. The website will now build your app and install any requirements found in 'requirements.txt'. Once built successfully.
13. The bottom of the page should now build the app and present a message titled _"Your app was successfully deployed"_.
14. Your app should now be deployed and any Github pushes also pushed to the Heroku app.


#### How to clone the repository:
1. Navigate to the correct repository from the GitHub dashboard.
2. Above the list of files, click the green “Code” button.
3. From the dropdown, select the _“Clone with HTTPS”_ by selecting the clipboard icon.
4. Open Git Bash and change the working directory to the location you would like the clone to be.
5. Type git clone, and past the URL you have copied. (Should be in the format $ git clone https://github.com/username/repository.)
6. Press _"Enter"_ to create your local clone.

#### Running the application locally:
1. Clone the repository as defined above.
2. Install the necessary libraries specified in the requirements.txt.
3. Create a new file names env.py and add your environment variables to it, such as IP, PORT SECRET_KEYS.
4. Create a gitignore file in your root directly and ensure env.py is in the list so it does get pushed to your master branch.
5. At the top of your app.py file which runs the project, 'Import' your env.py file.
6. Finally you can run the application from command line using 'python3 app.py'.

## Credits
### Content:
* All walking content and routes created under the user account "Admin" has been selected from [falriver.co.uk](https://www.falriver.co.uk/). This includes images used for the links.
* Images used for walks created by myself as "heather crawford" and "r pollard" have come from the following sources:
    1. [https://www.cornwalls.co.uk/sites/default/files/attractions/kennall-vale-2_2.jpeg](https://www.cornwalls.co.uk/sites/default/files/attractions/kennall-vale-2_2.jpeg)
    2. [https://media-cdn.tripadvisor.com/media/photo-s/18/5e/3e/f7/the-pandora-inn-viewed.jpg](https://media-cdn.tripadvisor.com/media/photo-s/18/5e/3e/f7/the-pandora-inn-viewed.jpg)
    3. [https://www.visitcornwall.com/sites/default/files/styles/product_image_breakpoints_theme_visitcornwall2_mobile_2x/public/maenporth-beach.jpg?itok=j3wxDY-e&timestamp=1314804350](https://www.visitcornwall.com/sites/default/files/styles/product_image_breakpoints_theme_visitcornwall2_mobile_2x/public/maenporth-beach.jpg?itok=j3wxDY-e&timestamp=1314804350)
    4. [https://www.eatoutcornwall.com/wp/wp-content/uploads/Carn-Brea.jpg](https://www.eatoutcornwall.com/wp/wp-content/uploads/Carn-Brea.jpg)
    5.  [http://127.0.0.1:5000/edit_walk/60253aea30607e9616f4ed48](http://127.0.0.1:5000/edit_walk/60253aea30607e9616f4ed48)
* All other users are created by friends and families acting as testers.

### Code:
During construction of this project, many tutorials on the uses of functions or even the names of functions have been found and applied to this project. These have been noted in the code when they are beyond my previous understanding or required more application in concept than just assessing the function's usability but no specific code was copied.

#### Bibliography:
Any code which was copied entirely or, as with most cases, used as a strong reference and emulated by example are referenced here:
1. w3schools animated navbar icon, copied majority as changes from burger to X from [tutorial].(https://www.w3schools.com/howto/howto_css_menu_icon.asp)
2. Stack Overflow: Answered issue where error messages did not appear from this [post].(https://stackoverflow.com/questions/6463035/wtforms-getting-the-errors)
3. The image viewer for add and edit walk forms was inspired by a stack overflow answer from [this link]. Though none of the code was directly used, the idea of assigning src to input value was found here.(https://stackoverflow.com/questions/31398473/load-image-in-div-from-url-obtained-from-a-text-box)
4. w3schools tutorial on custom sliders for checkboxes was [copied] to achieve the same effect.(https://www.w3schools.com/bootstrap4/bootstrap_forms_custom.asp)
5. This code by [diegoleme] was used to make my register page password validator.(https://codepen.io/diegoleme/pen/surIK)
6. The format for using an ajax post to send data was found [here]. This information is technically standard and no specific code was copied but similar enough to be worth identifying.(https://stackoverflow.com/questions/37631388/how-to-get-data-in-flask-from-ajax-post)
7. Inspiration for how to use scrollLeft in the userpage. While made clearer in mozilla developer documentation, [this post] was what gave the idea originally.(https://stackoverflow.com/questions/56392199/make-a-button-to-scroll-horizontally-in-div)
8. Bootstrap validation was achieved using their [bootstrap validator] entirely.(https://getbootstrap.com/docs/4.0/components/forms/#validation)
9. Idea that page title can be changed for each page loaded was found from another students work: [faithy80](https://github.com/faithy80/dcd-project/blob/master/run.py)
10. My mentor discussed the confirmation/delete code through a skype message and my work was taken from this advice.

### Media
All headers and website images have been taken or generated by myself and owned [RhysPollardDevelopment](https://github.com/RhysPollardDevelopment).

Any images used for walking routes made by the Admin account were chosen from [falriver.co.uk](https://www.falriver.co.uk/), while other images were used from various pictures found on google are not owned by me.

### Acknowledgements
Special thanks to my mentor Brian Macharia for his help and advice in development this project.
Extra thanks go to the testers composed of family and friends.
Pretty printed channel was very helpful for base concepts and tutorials throughout this project, no code was copied but much of their tutorial proved useful for grasping new concepts.
Libraries for google fonts, bootstrap, jQuery and font-awesome were used throughout my project.

Inspiration and techniques for pagination found from three main sources:
* [Pretty Printed Tutorial](https://www.youtube.com/watch?v=Lnt6JqtzM7I&feature=emb_logo)
* [faithy80's milestone project](https://github.com/faithy80/dcd-project)
* [The top comment by mangoed on this reddit post](https://www.reddit.com/r/flask/comments/fxtfzm/is_there_a_way_to_add_pagination_to_my_webapp/)
                            
### Disclaimer
This project has been made for purely academic purposes.