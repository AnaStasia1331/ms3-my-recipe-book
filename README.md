## Contents
- [My Recipe Book site](#my-recipe-book-site)
- [UX](#ux)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

# My Recipe Book site 
My Recipe Book was built to demostrate my ability to design, develop and implement a back-end for a full-stack web application as well as to be able to manipulate data in non-relational database. The programming languages that were used are HTML, CSS, JavaScript and Python.

![screen shots on various devices](static/img/readme/am-i-responsive.PNG)

# UX

## Who is this website for?
For users who want to record and store their recipes in an online cookbook.

## What it is that they want to achieve?
They need a simple way to write down new cooking recipes in an online recipe book, be able to find them, edit or delete.

## How does the project fulfil the users’ needs?
It provides an intuitive user interface for creation of new recipes. A recipe category can be assigned to a recipe that helps to search for it later, as each category lists all related recipes on a separate page. All recipes overview is also available to website users. They are able to view already existing recepies, modify and remove them.  

## Wireframes
The [wireframes](https://github.com/AnaStasia1331/ms3-my-recipe-book/tree/master/static/img/readme/my-recipe-book-wireframes.pdf) were created using Balsamiq tool.

## User Stories 
As a website user, I want to:

1. be able to create a new recipe.
2. be able to find an existing recipe based on category/group it belongs to.
3. be able to access all recipes in a single place.
4. view the details of an existing recipe.
5. edit a recipe.
6. delete a recipe.
7. access the website from multiple devices of different sizes without major UI issues.

## Nice-to-have features 

1. Login functionality.
2. Image upload for a specific recipe.

# Technologies Used (to edit)

The below list includes all of the languages, frameworks, tools, learning platforms and stock image websites I have used to create this project. 
## Languages Used
- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
## Frameworks
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
    - used Bootstrap components to design the responsive website faster.
- [JQuery 3.6.0](https://jquery.com/)
    -  a JavaScript library that simplifies JavaScript programming.
- [Flask]()
## Exteral APIs
## Database
- [MongoDb]()
## IDE and VCS
- [Git](https://git-scm.com/)
    - used as a version control system.
- [GitHub](https://github.com/)
    - used as a web-based platform to store and share the project.
- [Gitpod](https://www.gitpod.io/)
    - used as a cloud-based integrated developer environment.
## Font, wireframes and media
- [Unsplash](https://unsplash.com/)
    - downloaded the images for header background and courses cards
- [DesignEvo Free Logo Maker](https://www.designevo.com/)
    - for creation of the standard image for recipe card.
- [Flaticon](https://www.flaticon.com) 
    - for logo creation.
- [Pinetools](https://pinetools.com/darken-image)
    - allowed to apply filters on images.
- [Google fonts](https://fonts.google.com/specimen/Quicksand)
    - used to import 'Quicksand' font.
- [Balsamiq](https://balsamiq.com/wireframes/)
    - used for creation of wireframes.
- [ColorPick Eyedropper](https://chrome.google.com/webstore/detail/colorpick-eyedropper/ohcpnigalekghcmgcdcenkpelffpdolg)
    - a Chrome plugin that was used to choose a desired color code.
## Debugging 
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools)
    - modify CSS on-the-fly, test responsiveness, simulate slow network for testing the page loader; 'Console' and 'Sources' tab were helpful in debugging JS code.
## Knowledge sources 
- [Code Institute learning platform](https://codeinstitute.net/)
    - used to revise the theory of JavaScript Essentials and Interective Frontend Development modules, find solutions for JS/JQuery issues.
- [W3schools](https://www.w3schools.com/)
    - used to revise the theory of CSS/JS/JQuery and find solutions for code issues.
- [Stack Overflow](https://stackoverflow.com/)
    - used to find answers to challenging coding questions.
## Code Validators
- [JavaScript validator](https://jshint.com/)
    -  a static code analysis tool used for checking if JavaScript source code complies with coding rules.
- [Jigsaw](https://jigsaw.w3.org/css-validator/validator)
    - tool for css validation.
- [W3C validator](https://validator.w3.org/)
    - tool for html validation.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
    - tool for perfomance, accessibility validation.

# Testing (to edit)
## Test environments
Google Chrome dev tool was used during development to make sure the website is responsiveness. The final testing of the deployed site was performed on the devices:
- Laptop HP ZBook 15 G3, 1920x1080-pixel screen resolution, Google Chrome browser.
- Iphone XR with 1792 x 828-pixel screen resolution, Safari browser.

## Testing User Stories from User Experience (UX) Section (in progress)

ToDo: link tests to US
1. Home page.  
    * Expected: user clicks the nav and social media links from the Home page and is redirected to the right pages/sections.
    * Testing:
        * click on the Home nav item -> the Home page is refreshed;
        * click on the logo -> the Home page is refreshed;
        * click on the Add A New Recipe nav item -> Add A New Recipe form is opened with 2 buttons: Cancel and Save;
        * click on the Courses nav item -> the Courses section is opened with multiple courses types;
        * click on the My Recipes nav item -> All Recipes page is opened either with recipe cards or 'No recipes have been added yet' text;
        * click on the Add A New Recipe pencil icon -> Add A New Recipe form is opened with 2 buttons: Cancel and Save;
        * click on each Course picture in the Course section -> page is loaded for the specific Course type, e.g. breakfast or dinner. The page displays recipes in the selected category or 'No recipes have been added yet' text;
        * click on the facebook/instagram/twitter icons -> facebook/instagram/twitter page is opened in a separate tab.
2. Add a New Recipe form.
    * Expected: when user forgets to add a title to a recipe, the new recipe can't be created.
    * Testing:
        * leave the Recipe Name field empty and try to save the recipe -> user is asked to fill in the field and the recipe wasn't saved.
    * Expected: user can save a recipe with a recipe name with no more than 50 characters.
    * Testing:
        * try to add recipe name containing more than 50 char  -> after 50th character typing is not possible.
    * Expected: user can select any course type from the Courses dropdown.
    * Testing:
        * click the dropdown -> all 6 course types are visible in the dropdown;
        * select a value from the dropdown -> the correct value is selected.
    * Expected: user can paste/type large amount of text in Ingredients and Steps textarea.
    * Testing:
        * paste a long text (more than 2000 characters) -> the long text is accepted.
    * Expected: user can set preparation time.
    * Testing:
        * select a half an hour or an hour as cooking time -> the correct time is set.
    * Expected: user can cancel the recipe creation.
    * Testing:
        * click the Cancel button -> from Add a New Recipe form the user is redirected back the page visited earlier.
    * Expected: user can save a new recipe successfully.
    * Testing:
        * fill in all required and optional fields in the form and click the Save button -> user is redirected to the All Recipes page, he can find his recipe on the page based on title.
3. All Recipes page.
    * Expected: the links on the page work. 
    * Testing:
        * test all nav item and footer links -> each link redirects to the desired page/section.
        * preconditon: at least 1 recipe must be created:
            * on the recipe card click the View icon -> View Recipe page is opened;
            * on the recipe card click the Edit icon -> Edit Recipe page is opened;
            * on the recipe card click the Delete icon -> the delete modal window for the selected recipe pops up.
    * Expected: when many recipes were created on the page, the cards layout displays without major issues.
    * Testing:
        * create more than 4 recipes (for desktop) -> the recipes are displayed in 4 columns. They have the same size: height and width regardless difference in title length. Long titles are shown with ellipsis;
        * create many recipes to check the list is scrollable -> user can scroll without issues.
4. Edit Recipe form.
    * Expected: 
    * Testing:
        * some text
            


## Major bugs discovered and fixed:
1. When triggering the delete recipe popup, for example, for the 3d recipe on the page, it showed the first recipe to remove. Fixed by passing {{ recipe._id }} into the delete popup.

## Known bugs:
1. 

## Further Testing (to edit):

- [W3C Markup Validator](https://validator.w3.org/) was used to validate every HTML page of the project on syntax error. No issues have been detected.
- [Jigsaw](https://jigsaw.w3.org/css-validator/) service was used to validate css files. No validation errors have been detected.
![css validator result]()
- Run the JS files through [Jshint](https://jshint.com/) linter, there are warnings but no major issues.
- Lighthouse tool was used to audit performance, accessibility, best practice and SEO.
    - the results for the Home page:
![Lighthouse validator homepage]()
    - the results for the Quiz Card page:
![Lighthouse validator quiz card page]()
    - the results for the Finish Quiz page:
![Lighthouse validator quiz card page]()
- misconfiguration, connection issues (?)
- testing of the README links was performed.

# Deployment

## Run the project locally

Steps:

1. Open the repository in GitHub https://github.com/AnaStasia1331/ms3-my-recipe-book.
2. Find the Code button, choose the HTTPS clone option, copy the command.
3. Open a local directory where you want to clone the project to.
4. Open the Git Bash terminal in that directory.
5. Type the command 'git clone' plus the copied https url. 
6. After executing the command, the repository will be created in the local directory.
7. ....

## Heroku 
I've published my website using Heroku. To deploy a project, one should follow these steps:

1. As a prerequisite, your project must contain _requirements.txt_. Heroku uses that file to know what application and dependencies are required to run the app. To create _requirements.txt_ in the project run the command: 
```
pip3 freeze --local > requirements.txt
```
2. Next, create the _Procfile_ that specifies the commands that are executed by the app on startup. Execute the command: 
```
echo web: python app.py > Procfile
```
3. On Heroku website https://dashboard.heroku.com/apps create a new app. The app must have a unique name.
4. In the _Deploy_ tab -> _App connected to GitHub_ section connect the Heroku app to your GitHub account.
5. In the _Settings_ tab -> _Config Vars_ click the _Reveal Config Vars_ button. Copy and save the key-value pairs that mentioned in the _env.py_ of your project.
6. In the _Deploy_ tab -> _Automatic deploys_ enable automatic deploys. 
7. To open the website from Heroku, click on the _Open app_ button.

My project is accessible via this link https://ms3-my-recipe-book.herokuapp.com/

# Credits

## Code
Major credits go to:
 - [Bootstrap free theme 'Agency'](https://startbootstrap.com/theme/agency) was imported into the project with predefined HTML, CSS and JS files. The theme was significantly modified for the needs of the project.
 - code examples of how to work with Flask framework provided during the 'Backend Development' course from Code Institute.

## Media
- To make the website look colorful and attractive, several images were used from [Unsplash](https://unsplash.com/). Dark filter was applied on the top of some images with the help of [Pinetools](https://pinetools.com/darken-image)
- Recipe card image (chef cap) was designed in the tool [DesignEvo Free Logo Maker](https://www.designevo.com/)
- [Flaticon](https://www.flaticon.com) allowed to create the logo.

## Acknowledgements 
- Code Institute for the provided study materials and the idea for MS3 project.