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

### User Stories
1.	As a user I want to be able to search for local walks in a desired area.
2.	As a user, I want to have the option to log in and add my own walks/routes
3.	As a user, I need a page to add my route and upload it to the website.
4.	As a registered user, i need to be able to edit or remove any routes I have added.
5.	As a registered user, it would be good to have an easy way of showing the route on a map.
6.	As a user, it would be useful to have extra information for each route available.
7.	As a registered user, I would like to be able to save routes for later.

### Database Collections
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
10. [Favicon.io](): Favicon generator which converts images into favicons for use in the browser tab.
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
Testing was performed throughout this project when any new feature was implemented or changed. This was mostly done through the use of repeat exercises and changing each attempt by editing one variable. Equally chrome developer Tools was of key importance for any javascript or HTML issues which occured.

The use of branches was introduced for any major changes or possibly bug inducing changes. This can be seen in the range of branches made throughout this project which were then merged back into the master branch. Some have been deleted from github and local directories due to error or being very early on in the project life cycle.

My mentor Brian was also key in identifying possible future errors or issues which were missed in production or just beyond my current understanding of the topic.

### Defensive Programming
Following the course material and discussions with my mentor Brian, it was made clear that programming my website defensively was key to ensuring no accidental or malicious breaks occurred.

This can be seen in various examples such as the use of a confirmation modal when trying to delete a walk from your own user page. Equally the strict use of validation in front and back end of the project is to prevent users incorrectly inserting information which could lead to errors when accessing data from specific pages. If designed correctly no user should be able to

### User Story Testing
1.	As a user I want to be able to search for local walks in a desired area.
    * *To search for a walk the user must select the "Discover" option in the navbar, or on the landing page image.* This link shows interactivity suggesting action and works correctly at loading the new page.
    * *The user can type in a location or name of an area.* This works correctly, but is limited by user created names and naming conventions.
    * *The user checks a slider option such as free-parking.* The slider animates when selected signifying selection.
    * *The user chooses a difficulty from the drop down selection element.* This element reacts when selected with a drop down list as expected.
    * *The user presses the search button for their results.* The search button has a hover effect to show interactivity and upon retrieval, the page is scroll to the results.
2.	As a user, I want to have the option to log in and add my own walks/routes.
    * *To make an account in the user can either register or log-in on the respective pages.* Both register and log-in navigation links are interactive and correctly call routing for their pages.
    * *To register the user must enter details to the correct specifications and agree to terms.* The register form has comments suggesting the required information and coloured validation to inform user of errors/success.
3.	As a user, I need a page to add my route and upload it to the website.
    * *Once logged in the user should select "Add walk" on navbar and then enter the key details.* As with other navigation links, the link is interactive and has been shown to call correct routing. As with the search filter forms the buttons and sliders all show interactivity and the form has hints and coloured validation.
    * *Once completed the user can validate their form and/or submit by pressing "submit".* The submit button is interactive when hovered over or clicked to show its use and coloured validation and notes will emerge on incorrectly completed inputs.
4.	As a registered user, i need to be able to edit or remove any routes I have added.
    * *The registered user must go to the user dropdown on the navbar and select "Userpage".* The dropdown has a user/person icon which is well known as being linked to the person logged in and shows a drop down icon with interactive elements.
    * *The user must then select their walk from the list provided and either select edit or delete.* Userpage has a list and tally of user created walks and large accessible buttons for "edit" and "delete".
    * *If selecting delete, the user can confirm or cancel the action on the pop-up.* A modal correctly appears when delete is selected, offered the option or remove the walk entirely or not.
5.	As a registered user, it would be good to have an easy way of showing the route on a map.
    * This was not implemented and is currently been stored as a future feature the implement.
6.	As a user, it would be useful to have extra information for each route available.
    * *The viewer of each walk can select the desired route and inspect the key details.* Walking route links do react to user action and correctly call the desired routing to the specific walk page.
    * *On the walk, users may see a list of key details along side the directions for their walk.* By the user selected image there is a list of key details and features of the walking route before being able to scroll down and see a correctly loaded list of directions.
7.	As a registered user, I would like to be able to save routes for later.
    * *On a viewed walk, registered or logged in users can see a heart icon which when clicked changes colour.* The heard checkbox reacts when clicked and changes colour as feedback.
    * *Upon returning to their personal userpage, the favourited/saved walks are stored for viewing.* Userpage contains a scrolling view bar which can be moved by left or right scroll buttons on a computer of also swiping on the phone. The buttons are functional but also suggest interactivity or more information available. Saved walks are correctly stored for the independent user.

### Validation
#### W3C CSS Validator:
My CSS file are now parsed by the above validators with no errors and two warnings:
* Both warnings are the use of `wekbit-scroll` and `scroll-bar width` settings which are considered non-standard. Upon researching it is not considered non-standard to use `webkit-scroll` due to their usage in all modern and most previous browsers. Since both also regress gracefully there is no reason I feel to remove them.
* Other warnings which have been removed are obselete styles, an example is the use of `word-break: break-word` now being the same as `word-break: normal` and no longer used.

#### W3C HTML Validator:
All HTML is now parsed by the above validator with no errors or warnings:
* The only possible issue is if a user does not upload a valid image-url. If no Url is added this causes an error, but validation front and back end should prevent this case.

#### JSLint:
An online tool was used to parse all of my javascript files; no errors were found or warnings, although one or two "unused variables" were found, particularly in the spec files as jasmine code was not suitable for the linter.

#### PEP8 Online:
All python code is now parsed with the above validator and no warnings or errors are present.

### Unit Testing
Unit testing was performed using the Jasmine testing suite installed into VSCode.

Seperate testing specs were made for each javascript file to ensure they were directed at each correctly and did not interfere with other specs. For each spec the use of HTML was inserted and removed before each test with out key elements being targeted remaining. This was essential as most of the javascript functions were related to interactivity with HTML elements and performed very few external processes.

Two specs which had a limited testing application were `favtogglespec.js` and `userspec.js`. This occurred as the `bindFavourite` function and `confirm_delete` function both used AJAX requests and window.location to perform their actions. However, it was found to not be possible to spy on these elements easily or select their actions without processing the request and leaving the current window to a new href. To prevent accidentally aborting the testing suite it was decided that these could only be tested manually and at least check if the actions leading upto their calling was correct.

To view testing please click [here](https://data-centric-milestone-rhys.herokuapp.com/testing).

### Integration Testing
The live website was tested across all current browsers (chrome, firefox, safari, edge, opera) and some which were technically no longer in service (Internet explorer) to see whether any browser specific issues occurred. The site was also used on a range of phones and sites using browserstack and family and friends voluntarily testing the site.

The main issues found from integration were:
1. Opacity cannot be set to a percentage as found with the squars on index page, search page and userpage else they will appear black in safari, yandex and internet explorer. This was noticed to be easily fixed as hover still affected the opacity as it was set to `opacity:0.1` not `opacity:10%`. Changing all opacity to the same 0.4 etc style corrected this.
2. Internet explorer does not do multipy background or accept certain colour values with altered alpha levels. My headers were all edited in Clip Paint Studio to have a permanent darker overlay to prevent white text being lost without contrast.
3. Full text on some links to walks was not sitting correctly and overflowed. Found that editing the margins to a padding setting and removing top positioning solved this.

### Responsive design
The use of responsive design is key to developing new websites. This website was build with a mobile first view and a large laptop view following second, once the back end frame work had been decided upon. Key details were then created for intermediate sizes from the smallest mobile to a large laptop. 

The responsiveness of this was finally testing using [Am i responsive](http://ami.responsivedesign.is/) and [Responsinator](http://www.responsinator.com/). Am I responsive showed no issues with the variable design, however responsinator did hightlight an issue on the contact page where the header was in vertical heights (vh) and would often be presented too small for its height on shorter screens or landscape orientation. This was corrected by choosing rem as a standard measurement. 

It also highlighted that the walk-header of walkpage was incorrectly set to `col-sm-11` not `col-sm-12`.

The only flaw is that due to these services limitations, it was not possible to log in or access restricted material through them so I could not check the user pages or any add/edit forms.

### Bugs
* Older posts done before the WTForm update, could not be edited properly. This might be that they were failing validation before even being loaded so could not be stored. Unsure as most of these were unfit for purpose anyway and were deleted for new data which could not be entered with missing information.
* Very long words or long strings of characters lacking a space in directions could cause the page to over extend to the right. This has been investigated and corrected using word-break but could still be an error in rare cases where this does this apply correctly.
* W3C validator for CSS does provide warning for webkit-scrollbar and scroll bar width. These are technically non-standard but do not have any problem with regression if not applicable on any website.
* As mentioned above, could not test some parts correctly in unit testing with Jasmine as it is impossible to test or spy on window.location. Doing so changes the actual window from testing and therefore negates any outcome.
* The favourites slide show has a small issue when when hovered over, the overlay has a delay in resizing compared to the image box and can be seen not quite overlapping for a moment. This is most likely due to how the overlay calculates its height and width only after the parent element has already met its new proportions.

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
All walking content and routes created under the user account "Admin" has been selected from [falriver.co.uk](https://www.falriver.co.uk/) and 

### Media
All headers and website images have been taken or generated by myself and owned [RhysPollardDevelopment](https://github.com/RhysPollardDevelopment).

Any images used for walking routes made by the Admin account were chosen from [falriver.co.uk](https://www.falriver.co.uk/), while other images were used from various pictures found on google are not owned by me.

### Acknowledgements
Special thanks to my mentor Brian Macharia for his help and advice in development this project.
Extra thanks go to the testers composed of family and friends.
Pretty printed channel was very helpful for base concepts and tutorials throughout this project.
Libraries for google fonts, bootstrap, jQuery and font-awesome were used throughout my project.

Inspiration and techniques for pagination found from three main sources:
* [Pretty Printed Tutorial](https://www.youtube.com/watch?v=Lnt6JqtzM7I&feature=emb_logo)
* [faithy80's milestone project](https://github.com/faithy80/dcd-project/blob/master/run.py)
* [The top comment by mangoed on this reddit post](https://www.reddit.com/r/flask/comments/fxtfzm/is_there_a_way_to_add_pagination_to_my_webapp/)
                            
### Disclaimer
This project has been made for purely academic purposes.