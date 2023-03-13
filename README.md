<h1 align="center">Greg Goodrem Milestone Project 4</h1>
<h2 align='center'>London Omnibus Traction Society Website</h2>
<br>
<p>
This project is the first step in creating a fully functional website with capabilities to have products both sold and to sign up to the annual memberships. This website is constructed with my knowledge level of HTML, CSS, Python, Javascript, Django, Webhooks and API. 
</p>
<p>
The overall goal of the website is to build an annual subscription membership. The other main feature is to sell the many other publications that are being sold by LOTS.
</p>
<p>
The original website hasn't been updated properly since 2002 so the third and fundamental purpose is to revamp and make it much more modern and functional.
</p><p>
Members currently have to download and print an order form for publications and then they send their order to the Society. The idea is to change this into a website with sales ability so that it helps both the Society to sell more publications and also the customer receiving their products far quicker due to a more streamline website experience.
</p>

[View the live project here.](https://lots-project.herokuapp.com/)

<h2 align="center"><img src="documentation/readme_images/all-devices-black.png"></h2>

## Contents

-   ### [User Experience](#ux)
-   ### [Research](#research)
-   ### [Design Process](#design)
-   ### [Wireframe Outlines](#wireframes)
-   ### [Responsive Design Features](#responsive)
-   ### [Future Features](#future)
-   ### [Technologies used](#tech)
-   ### [Frameworks, Libraries & Programs Used](#frameworks)
-   ### [Credits](#credit)
-   ### [Testing & links](#testing)
-   ### [Errors and Bugs](#errors)
-   ### [Personal Conclusion](#conclusion)

***
<a name='ux'/>

## User Experience (UX and UI) 
    
### User Profile

- The profile of the users of this website are generally as follows:
    -   People that grew up in a period of time transportation was more prevalent(so over 55).
    -   More commonly to be male.
    -   Have used the old website & still use cheques.
    -   Often well-informed and knowledgeable about the technical and historical aspects of buses and public transportation.
    -   More likely to be found in urban areas where public transportation is a significant part of daily life.

### User Profile Impact
    
-   The world is changing rapidly and the automation of lots of public & private services means they are more likely to start using the website over the old way of sending a cheque.
-   The option of the old way can be included into the new website however with the intention to phase the old way of working out. 


### Initial User Experience
- The user is initially looking for 1 of 3 things:
    -   News from the society.
    -   Annual membership for The Bus Magazine or London Bus Magazine
    -   Buying publications about Buses
-   I would expect the people using this website being semi regular visitors to the old website.
-   The current members will be encouraged to use the new site so the renewals of membership is far easier.
-   The current members will have a new means of purchasing their other publications. 

<br>
<a name='research'/>

##  Research  
<p>The original website has been established for over 20 years and the brand itself has been around for almost 60 years.</p>
<p>There are many magazines websites that deal with Buses and transportation these are some of them:<p>
    

I wanted to explore a solution to the very heavily paperwork based industry when it comes to physiotherapy and sports therapy. I personally have experienced as client and also very much understand the role of the therapist as I have done a Sports Massage course.
Reaching out to active therapists I found that a lot of therapists still use paper based systems to collect this information and also when relaying the aftercare information. Not all therapists give advice sheets with detailed examples of the exercises a person should do to help continue injury recovery after a treatment. 
I found their are few treatment apps that include the client as the focus for outputting information to. A lot of the applications available such as Vagaro, Pabau, Noterro among others focus on the therapist souly being the user. 

-   [Omnibus Magazine](https://www.omnibus-society.org/omnibus-magazine) - Subscriptions and back issues are available. I think the website looks clean and well informed however the route to getting a membership is very slow and could be less complicated.
-   [Buses Magazine](https://www.keybuses.com/subscribe-now) - I think the website looks good and looks professional however it does only sell its own publications and not other organisations. It also has different periods of purchase such as quarterly, bi annually, annually and also back issues. 
-   [Classic Bus](https://www.classicbusmag.co.uk/subscriptions) - This website offers sales of annual memberships, back issues and also digital versions. Website looks good and easy to navigate. It is a very basic site. 
-   [On The Buses](https://shop.kelsey.co.uk/on-the-buses-magazine) - Magazines sold through Kelsey media with back issues monthly, annual or digital subscriptions.
-   [Buses Worldwide](https://www.magzter.com/GB/CPUK-Print-Publishing-Ltd/Buses-Worldwide/Automotive/) - This magazine is sold through Magzter with back issues, annual and monthly subscriptions with a digital subscription optional.
-   [LOTS](http://www.lots.org.uk) - Established for 59 years the society has been producing over a thousand different magazines through the variety of publications they provide. The website as it stands is very old with very little interactivity. It is still being updated on the news page fairly regularly with various information applicable to their audiance.

-   ### Research Analysis
    It appears there are a lot of different Bus magazines out there for which they all cover various areas of interest to the Bus enthiuiastsf. It clearly is a very niche sector and from talking also to some of the people running LOTS it is clear that they are suffering from the society membership dwindling. The hope of getting more memberships from the website being setup is vital for future developments with the ever decreasing use of cheques which a lot of members are still using. The reoccuring direct debit will help them to not lose customers in the long run as the DD will continue until it is cancelled without the need to send out renewal letters and spending money on letters etc.
    
    <br>
    <a name='#design'></a>
## Design 
-   I opted to use Bootstrap for this website as it is a well known framework and you can create professional looking websites. The style I was able to come up with based on talks with the members of the society. I'll cover all aspects of design in the sections below however please have a look at the new pages compaired to the original website that was created back in 2002.

One of the main instructions from the London Omnibus Traction Society was that they wanted to keep the website quite simple and not to change too much. The main reasoning was that the members that would use the site don't like too much change.


|   |   |
|---|---|
|<h2>New Index Page</h2>|<h2>Old Index Page</h2>|
|<img src="documentation/website-screenshots/LOTS-new-index.png">|<img src="documentation/website-screenshots/LOTS-old-index.png">|
|<h2>New Membership Page</h2>|<h2>Old Membership Page</h2>|
|<img src="documentation/website-screenshots/LOTS-new-membership.png">|<img src="documentation/website-screenshots/LOTS-old-membership.png">|
|<h2>New News Page</h2>|<h2>Old News Page</h2>|
|<img src="documentation/website-screenshots/LOTS-new-news.png">|<img src="documentation/website-screenshots/LOTS-old-news.png">|
|<h2>New Publications Page</h2>|<h2>Old Publications Page</h2>|
|<img src="documentation/website-screenshots/LOTS-new-publications.png">|<img src="documentation/website-screenshots/LOTS-old-publications.png">|
|<h2>New Sales Page</h2>|<h2>Old Sales Page</h2>|
|<img src="documentation/website-screenshots/LOTS-new-sales.png">|<img src="documentation/website-screenshots/LOTS-old-sales.png">|
|<h2>New About Page</h2>|<h2>Old About Page</h2>|
|<img src="documentation/website-screenshots/LOTS-new-about.png">|<img src="documentation/website-screenshots/LOTS-old-about.png">|
|<h2>New Links Page</h2>|<h2>Old Links Page</h2>|
|<img src="documentation/website-screenshots/LOTS-new-links.png">|<img src="documentation/website-screenshots/LOTS-old-links.png">|
|<h2>New Contact Page</h2>|<h2>Old Info Page</h2>|
|<img src="documentation/website-screenshots/LOTS-new-contact.png">|<img src="documentation/website-screenshots/LOTS-old-info.png">|

### Brand Logo
-   The Brand logo was quite pixelated when I first started looking at the original website and decided it was worth tweaking it and creating a newer clearer logo. I used Canva to redesign it and give it a couple of different designs. I created a smaller logo for when the display is responsive and the width gets smaller to only show the basic smaller logo seen below.

|   |   |
|---|---|
|New Redesigned Logo|Old Logo|
|<img src="documentation/readme_images/lots-logo-new.webp">|<img src="documentation/readme_images/lots-logo-old.gif">|
|New Redesigned Alternative Red Logo|   |
|<img src="documentation/readme_images/logo-red.webp">|   |
|Smaller Redesigned Logo|   |
|<img src="documentation/readme_images/logo-sm.webp">|   |


### Colour Scheme
-   The main colours used all associated with the original website and the different logos that the society has used in the past. I tried to incorporate these into the menus and the drop down menus and throughout the site.

<img src="documentation/readme_images/lots-colours.png">

### Typography
-   To conform with the simplistic request from the society I have used the more common professional fonts such as Arial, Helvetica and sans-serif. These will help the older users of the website be able to clearly read the text and feel comfortable.

### Imagery
-   The pictures used on this website have all come from the London Omnibus Traction Society. The majority of the imagery is from the publications themselves however I have also used some pictures of single buses for the sliders.

### Database
-   Django officially supports Postgres, My SQL, Oracle and many more I used Postgres during this project. These schema tables below are a visual representation of the data is collected that will be in the database and during the project development it has evolved to the below.

If you look at the schema you will see the fundamental differences in the colour schemes used to identify the different parts that are being used in this project.
    -   Green - This identifies the authorised section of Django this also includes the News app for posting.
    -   Blue - This is the Django admin and installed admin interface theme manager which was installed.
    -   Orange - This is the main schema structure for products and checkouts with the use of the profiles as an entry point.

<img src="documentation/readme_images/lots-project-schema.png"> 

<br>
<a name='wireframes'/>

## Wireframes 

The Wireframes were created using Wondershare Mockitt App this was for the basic structure of the main site pages such as the ones detailed below. The only pages of exception were those that were created by some of the installed application such as the AllAuth pages for confirming emails and signing up etc. These pages were edited to conform with the general page aesthetics with button design and general look to match all the other pages of the website.   

**Index/Home page:** The home page gives the site it's initial entry point and clear purpose as to what the end user is to expect. There is clear navigation to the top of the page either fully across the top or on smaller displays in a drop down navigation bar.

**How To Join Page:** The how to join page is the membership page for the site. It was discussed whether it should be called the membership page as it clearly is the main purpose of this page. The Society preferred calling it 'How To Join' so I stuck with their intention. This page forms a gateway to any of the different forms that enables the user to sign up for a membership.

**News Page:** The News page will populate with all the posts that the society chooses to put out to it's members.

**Publications Page:** The publications page has been created to show some of the different publications that are produced by The London Omnibus Traction Society. 

**Sales Page:** This is the main products sales page. It shows all the products available and is going to be managed by the Society on the volume of stock for each product.


**About Us Page:** This page has a small amount of history of the society and brief amount of information about their publications.

**Links Page:** These are all relevant pages that the members of the society and users of the website might be interested in.

**Contact Us Page:** The contact us page is used for communication purposes from website users to the society. Included on this site is old Information Service page.


|Pages|Mobile View|Tablet View|Desktop View|
|---|---|---|---|
|Index|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Index-Mobile.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Index-Tablet.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Index-Desktop.png)|
|How To Join|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/How-To-Join-Mobile.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/How-To-Join-Tablet.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/How-To-Join-Desktop.png)|
|Publications|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Publications-Mobile.png)|  [View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Publications-Tablet.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Publications-Desktop.png)|
|Sales|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Sales-Mobile.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Sales-Tablet.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Sales-Desktop.png)|
|News|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/News-Mobile.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/News-Tablet.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/News-Desktop.png)|
|About Us|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/About-Us-Mobile.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/About-Us-Tablet.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/About-Us-Desktop.png)|
|Links|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Links-Mobile.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Links-Tablet.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Links-Desktop.png)|
|Contact|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Contact-Us-Mobile.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Contact-Us-Tablet.png)|[View](https://github.com/CodeGreg1/lots-project-ms4/blob/main/documentation/wireframes/Contact-Us-Desktop.png)|

### Wireframes side by side


<img src="documentation/wireframes/wire-home.png"> 
<img src="documentation/wireframes/wire-join.png"> 
<img src="documentation/wireframes/wire-pubs.png"> 
<img src="documentation/wireframes/wire-sales.png"> 
<img src="documentation/wireframes/wire-news.png"> 
<img src="documentation/wireframes/wire-about.png"> 
<img src="documentation/wireframes/wire-links.png"> 
<img src="documentation/wireframes/wire-contact.png">


<br>
<a name='responsive'/>

## Responsive Design Features 
-   The website has been made to be responsive on varying sized screens.
-   The website will resize from the screen of a mobile phone all the way to a full desktop display.
-   It is intended use is for potential members to come and view the site and options for annual membership and publication sales.
-   It is also for current members to visit and see the news updates.
-   Another usage is for the society to be able to administrate the posts and products as and when they please.

<br>        
<a name='future'/>

## Future Features 
<!-- -   I think adding more advice sheets with video links and instructionals would be a great feature. Currently I have used Knee, Back, Shoulder and a general one advice sheet so I would actually break this down further to more specific injuries as well. For example if someone comes in with a shoulder injury the recovery advice can vary from being very general to being very specific e.g. If someone has an anterior injury of the deltoid or a injury to the rotator cuff the advice would be very different but are both in the shoulder area.
-   Having a time limited access to content could really help injury recovery and help promote a client to come back if at the end of that period if they haven't seen any progress. After all the client could try and do the recovery advice at another time and potentially make it worse because its a different type of injury. It could also be a completely different type of medical issue.
-   The ability to see the time of the next appointment with the therapist in the app itself and also the ability to pay for services in the app. This would be good for client tracking.
-   I could also include a communications system within the app so the therapist can respond and help injury recovery more thoroughly going forward. -->
<br>
<a name='tech'/>

## Technologies used 
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/javascript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [Django](https://docs.djangoproject.com/en/4.1/)

<br>
<a name='frameworks'/>

## Frameworks, Libraries & Programs Used 

- [Google Fonts:](https://fonts.google.com/) Google fonts were used to import the 'Roboto' font into the style.css file which is used on all pages throughout the project.
- [Font Awesome:](https://fontawesome.com/) Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
- [Git:](https://git-scm.com/) Git was used for version control by utilizing the terminal to commit to Git and Push to GitHub.
- [GitHub:](https://github.com/): GitHub is used to store the projects code after being pushed from Git.
- [Wondershare Mockitt:]() Wondershare was used to create the wireframes during the design process.
- [EmailJS:](https://www.emailjs.com/) I used EmailJS to enable free emailing to the therapist on the home page.
- [GoCardless:](https://gocardless.com/) This is the preferred payment platform that LOTS wanted to use for their annual subscriptions. 
- [PostgreSQL:](https://www.postgresql.org/) This is the Relational database I used to store the information on forms collected throughout the site.
- [Bootstrap:](https://getbootstrap.com/docs/5.3/getting-started/introduction/) Bootstrap is the front end tool kit I decided to use.
- [Heroku:](https://www.heroku.com/) Heroku is the cloud platform I have chosen to deploy the website with.
- [Stripe:](https://stripe.com/en-gb) Stripe is the payment gateway I have used to handle the point of sale payments so card payments can be made. 
- [DbSchema:](https://dbschema.com/) DbSchema was used to outline the database layout. 
- [ElephantSQL:](https://www.elephantsql.com/) This was used for the integration of the postgresql database that Django used.
- [AmazonAWS:](https://aws.amazon.com/s3/) The S3 bucket was used to store all media and static files here.

    <br>
    <a name='credit'/>

## Credits

I got some assistance from the Code institute tutors when I was using PostgreSQL but was really helpful in helping me identify the why as to thing. Also my mentor was able to help me identify a few changes in regards to MongoDB which helped me create a cascade style delete function even though this is a non-relational database.

<br>
<a name='testing'/>

## Testing 

The website has been continually tested manually and also with defensive coding included in the routes.py as well as some safeguarding delete functions created to protect the data from accidental deletion.

I've also tested the site on several different devices with different types of screen sizes for responsiveness.     

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

- [W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmilestone3-greg-goodrem.herokuapp.com%2Fhome) - Results - No Errors or Warnings on any page.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmilestone3-greg-goodrem.herokuapp.com%2Fstatic%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - Results No Errors

    ### Lighthouse Reports 

Below you will see the Lighthouse reports for the different pages of the website. As you can see the average percentage is above 90%. Some of the main issues with the best practice section in all pages are related to Chrome Dev Tools however I  

| Pages  |  Report  |
|---|---|
| Home  |<img src="documentation/lighthouse-images/lighthouse-home.png">|
| How To Join |<img src="documentation/lighthouse-images/lighthouse-membership.png">|
| News  |<img src="documentation/lighthouse-images/lighthouse-news.png">|
| Publications |<img src="documentation/lighthouse-images/lighthouse-publications.png">|
| Sales  |<img src="documentation/lighthouse-images/lighthouse-sales.png">|
| About Us  |<img src="documentation/lighthouse-images/lighthouse-about.png">|
| Links  |<img src="documentation/lighthouse-images/lighthouse-links.png">|
| Contact Us  |<img src="documentation/lighthouse-images/lighthouse-contact-us.png">|
| Register  |<img src="documentation/lighthouse-images/lighthouse-register.png">|
| Login |<img src="documentation/lighthouse-images/lighthouse-login.png">|
| Logout |<img src="documentation/lighthouse-images/lighthouse-logout.png">|
| Profile |<img src="documentation/lighthouse-images/lighthouse-profile.png">|
| Add Product |<img src="documentation/lighthouse-images/lighthouse-add-product.png">|


-   [Wave Report](https://wave.webaim.org/report#/https://milestone3-greg-goodrem.herokuapp.com/home) - There are 4 alerts which relate to Table layout (which is the timetable of availability), 2 redundant links which I want to keep on the page and a 1st level heading alert. All of these alerts are absolutely fine for my requirements of the pages.
-   [ESLint](https://eslint.org/play/) - This is to check the linting of the Javascript code. Again no errors. 

-   [Unittest](https://docs.python.org/3/library/unittest.html) - I've implimented a number of automatic tests to check whether the page loads and what kind of content is found. I've created 3 tests for each of the following Home, Login and registration pages:
    -   First is a test to check if the page exists with a 200 Status code response.
    -   Second is a test to check the type of data that exists and in this case it should be HTML.
    -   Third is a test to check specific string data on the page exists e.g. Log In, Username etc.
    
    These tests are carried out and all pass how they should.

<br>
<a name='errors'/>

## Errors and Bugs 

-   The biggest problem I had initially was when I had both postgres and mongodb working at the same time I opted for the use of MongoDB as this was in many ways an easier database to use and also meant that I could have as much or little data entered as required. See the SOAP notes that will be written by the therapist allows for different parts to be filled out and others to be left blank. Also the ongoing future development of the application means that I would be able to keep adding to this database a lot easier than in postgreSQL.  

-   The following were bugs that I found and corrected:
    - Deleting Clients & their treatments - So on two fronts I couldn't find a suitable Python Message box that was able to be triggered if you selected to delete something. Ordinarilly the delete button would go straight ahead and delete without any security measures. So I failed to find a python message box I could easily code so I implemented a modal that triggered with the press of the delete button to open up to an option of cancel or delete which solved both problems.

    -   A second issue was the displaying the map correctly without triggering issues with HTML errors. I realised that I had to use the iframe and specifically state in the style inline on the html to get the result I required.

    -   Another issue I had was using the booking system having it input the names and emails automatically into the form to schedule an appointment to the Calendly site I had linked. I overcame this by using Jinja in the HTML document. 

    -   I had trouble at one point displaying the old searched field when the page refreshed. This was quite an easy fix which was made in the routes file.

    -   I played with having a full width banner picture on the home page however due to the base.html file made all the pages content sit within a container which gave the banner a smaller size. I was able to change the size of the banner so it fit 100% across visually but this then had a knock on effect of the page beng able to be scrolled horizontally. I could of edited the base and then included a container on each page however I'm happy with the result that I have.

    -   After initially starting with postgres I found that I had to go through and remove all the links and programming related to it which a few times made a few problems happen. Working through this was the best option because otherwise it would have been wasted code and could of led to other faults further down the line even though it wasn't directly being used.    
<br>
<a name='conclusion'/>

## Conclusion 

#### I think in reflection over this project there are several things I think went well.
#### The positives I believe I have done well is:
-   Create a basic functional SOAP notes application for a Sports Therapist.
-   I've made it look professional and clean.
-   It has several features for creating, updating and deleting client information.

Areas I could improve is having a physical signature of the client so verify them when they start using their therapist. I think even though this currently works it has a lot to be added to it to make it a really effective app.