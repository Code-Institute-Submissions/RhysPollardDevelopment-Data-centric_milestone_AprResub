[Back to main README.](https://github.com/RhysPollardDevelopment/Data-centric_milestone/blob/master/README.md)

## Testing
Testing was performed throughout this project when any new feature was implemented or changed. This was mostly done through the use of repeat exercises and changing each attempt by editing one variable. Equally chrome developer Tools was of key importance for any javascript or HTML issues which occured.

The use of branches was introduced for any major changes or possibly bug inducing changes. This can be seen in the range of branches made throughout this project which were then merged back into the master branch. Some have been deleted from github and local directories due to error or being very early on in the project life cycle.

My mentor Brian was also key in identifying possible future errors or issues which were missed in production or just beyond my current understanding of the topic.

### Defensive Programming
Following the course material and discussions with my mentor Brian, it was made clear that programming my website defensively was key to ensuring no accidental or malicious breaks occurred.

This can be seen in various examples such as the use of a confirmation modal when trying to delete a walk from your own user page. Equally the strict use of validation in front and back end of the project is to prevent users incorrectly inserting information which could lead to errors when accessing data from specific pages. If designed correctly no user should be able to

### User Story Testing from README.md
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
4. To help loading speeds, any images which were stored in the site itself and not imageUrls were reduced in size to sensible levels.

The use of lighthouse on chrome devtools found a few small issues with SEO, best practices and accessibility. 
#### SEO
SEO was mainly concerned with a lack of material in the manifest and page meta, reducing the search and descriptive capability for this website.
#### Accessibility:
Generally this scored well with few faults, however one consistent issue was headers not being sequential as walking route links each had a h5 so were considered out of order.
#### Best Practices:
Best practices errors were primarily down to trust issues with cross-origin destinations for my social media links and vulnerabilities with bootstrap and javscript libraries. I have made all reasonable changes but am unsure how to combat the issue with libraries without avoiding them currently. 
#### Performance:
Performance section had many more issues to discuss, however most regarded concepts such as lazy-loading of images, compression of images and texts beyond normal methods ad minification of javascript and CSS. Unfortunately this are things which fall beyond my understanding to perform and sadly will have to remain as errors, equally due to the possibility of user loaded images not being well optimized this score would always suffer.
I did alter the png header to a jpeg to improve speeds for first load and interactivity. While this does remove the possibility of changing background around the header and keeping transparency, for the scope of this project this seems appropriate.

### Responsive design
The use of responsive design is key to developing new websites. This website was build with a mobile first view and a large laptop view following second, once the back end frame work had been decided upon. Key details were then created for intermediate sizes from the smallest mobile to a large laptop. 

The responsiveness of this was finally testing using [Am i responsive](http://ami.responsivedesign.is/) and [Responsinator](http://www.responsinator.com/). Am I responsive showed no issues with the variable design, however responsinator did hightlight two issues:
* The contact page where the header was in vertical heights (vh) and would often be presented too small for its height on shorter screens or landscape orientation. This was corrected by choosing rem as a standard measurement. 
* It also highlighted that the walk-header of walkpage was incorrectly set to `col-sm-11` not `col-sm-12`, this was remedied to allow a complete width being filled.

The only flaw is that due to these services limitations, it was not possible to log in or access restricted material through them so I could not check the user pages or any add/edit forms.

All sizes of device screen were tested across all browsers with no observed errors for any page.
Family and friends have also tested the app on their mobile and tablet devices along with those available for emulation on browserstack and found no perceivable issues so far.
 
### Fixed bugs:
Below are a list of previously discovered by fixed bugs and errors made during development:
1. Directions were capable of stretching beyond the limits of the page and overflowing to the right. This was an unlikely situation for most input and was only found as extremely long strings were entered with no spaces to match the character limits required.
    Fix: The user of word-break: normal was found to be able to break up long text and words and prevent overflow, however whether other situations are possible is unknown.
2. The admin account could not edit others walks as the security checks in python would only allow the walks-user to matched against current session user.
    Fix: The easiest solution was to check that if the current user was not the owner AND also not the admin, then the walk would escape to the main page. Otherwise the walk edit form would be loaded. Equally it was required to update the walk user and userpage redirect to the username found in the loaded walk as the session user would not always be appropriate.
3. Deleting a walk would leave broken links lacking pictures in other userpages' favourites lists.
    Fix: By using the update command deleting a walk, any instance of the route_id to be deleted could be pulled from their respective arrays. If any user loaded their userpage, the walk Id could not be found and therefore would not have a space loaded for it.
4. Pagination would not apply the current filters to the subsequent pages during testing but would when searched on the first page.
    Fix: The error arouse when a new page was loaded using the buttons, the filters were reset on new page and the POST conditions were not met. This meant the filters did not remain during pagination. An elif statement was added which looked for the filters in the request arguments and applied them to the new pagination to maintain filters.

### known Bugs
* Older posts done before the WTForm update, could not be edited properly. This might be that they were failing validation before even being loaded so could not be stored. Unsure as most of these were unfit for purpose anyway and were deleted for new data which could not be entered with missing information.
* W3C validator for CSS does provide warning for webkit-scrollbar and scroll bar width. These are technically non-standard but do not have any problem with regression if not applicable on any website.
* The search page pagination is not truly responsive, after 5-6 pages it would become too large for very small screens. However, due to the limitations of this project in scope and the large number of images per page it was not felt to be a large issue currently as 108 walks would be required to create this event. This would be addressed for a larger set of data.
* Could not test some parts correctly in unit testing with Jasmine as it is impossible to test or spy on window.location. Doing so changes the actual window from testing and therefore negates any outcome.
* The favourites slide show has a small issue when when hovered over, the overlay has a delay in resizing compared to the image box and can be seen not quite overlapping for a moment. This is most likely due to how the overlay calculates its height and width only after the parent element has already met its new proportions.
* Going back after posting a new walk will reload the page and allow creation of a identical page. Have attempted Post/redirect/get to prevent this but was unsuccessful.
