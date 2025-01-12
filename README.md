# True Review

(Developer: Geoff Fletcher)

![True Review am i responive](https://github.com/user-attachments/assets/d282bf00-17f1-4985-b918-d006d3069564)


## Live website

Link to live website:[True Review](https://true-review-86503744e159.herokuapp.com)

## Why True Review?

The trust people have in review aggregator websites such as Rotten Tomatoes and IGN is at an all time low often with huge disparity between critic and audience scores. There are a multitude of reasons this is the case but what I believe is important is that a huge audience exists for media reviews that put content and the genuine attempt to analyse content first. True Review is built to step into this void as a platform for users to firstly read great reviews but also to create their own and comment on others. There are of course still ratings for the user to glean at a glance a rough idea on someones opinion of a piece of media but our ethos via moderation is to focus on the critque of storytelling, direction, cinematography and the acting performances that have made people fall in love with film, tv-series and video-games for generations. This is a full stack website built using the Django web framwork, with the aim of drawing in readers to enjoy great content and to go on to produce their own reviews that can inspire others and continue growing this platform. The initial idea was to use one model with three seperate "modules" to produce the three review types each with some unique fields: movie reviews, tv reviews and game reviews, but due to time constraints it has been initially launched with movie reviews active and the intent to add functionality for the other two soon.

## Index

- [User experience (UX)](#user-experience-ux)
   * [Key project goals](#key-project-goals)
   * [Target audience](#target-audience)
   * [User requirements and expectations](#user-requirements-and-expectations)
   * [Design inspiration](#design-inspiration)
   * [Colour Scheme](#colour-scheme)
- [Epics and user stories](#epics-and-user-stories)
   * [Epics](#epics)
   * [User stories](#user-stories)
   * [Agile Methodologies](#agile-methodologies)
   * [MoSCoW Prioritization](#MoSCoW-Prioritization)
 - [Wireframes](#wireframes)
   * [Index page wireframes](#index-page-wireframes)
   * [About page wireframes](#about-page-wireframes)
   * [Create Review page wireframes](#create-review-page-wireframes)
- [Features](#features)
   * [Logo and navigation bar](#logo-and-navigation-bar)
     * [Django alert messages](#django-alert-messages)
   * [Clear indication as to whether the user is logged in or out at all times](#clear-indication-as-to-whether-the-user-is-logged-in-or-out-at-all-times)
    * [A list of review posts](#a-list-of-review-posts)
   * [See an individual review post in detail](#see-an-individual-review-post-in-detail)
   * [Pagination](#pagination)
   * [About page](#about-page)
    * [Sign in form](#sign-in-form)
   * [Register form (Sign up)](#register-form-sign-up)
   * [Sign out page](#sign-out-page)
     * [Form with CRUD functionality to create a review when logged in](#form-with-crud-functionality-to-create-a-review-when-logged-in)
      * [Edit the reviews I have made when I am logged in](#edit-the-reviews-i-have-made-when-i-am-logged-in)
   * [Delete the reviews I have made when I am logged in](#delete-the-reviews-i-have-made-when-i-am-logged-in)
   * [View comments on reviews](#view-comments-on-reviews)
   * [CRUD functionality on comments when logged in](#crud-functionality-on-comments-when-logged-in)
   * [Footer](#footer)   
    - [Future features](#future-features)
    
- [Database schema](#database-schema)
   * [Entity relationship diagram](#entity-relationship-diagram)
   * [Entity relationship tables](#entity-relationship-tables)
- [Technology used](#technology-used)
   * [Languages and framework](#languages-and-framework)
   * [Database](#database)
   * [Technologies and tools](#technologies-and-tools)
- [Testing](#testing)
   * [Fixed bugs](#fixed-bugs)
   * [Unfixed bugs](#unfixed-bugs)
   * [Supported screens and browsers](#supported-screens-and-browsers)
- [Deployment](#deployment)
   * [Pre deployment](#pre-deployment)
   * [Deploying with heroku](#deploying-with-heroku)
   * [Fork this repository:](#fork-this-repository)
   * [Clone this repository:](#clone-this-repository)
- [Credits](#credits)
   * [Code](#code)
   * [Media](#media)
   - [Acknowledgements](#acknowledgements)

## User experience (UX)

### Key project goals

- Offer an atractive and accessible platform to read great media reviews
- Encourage readers to contribute to content themselves first in the form of interesting/ constructive insights via comments then in the form of their own reviews
- Build a platform that has the potential to keep users coming back for content that inspires them and cascades this enthusiasm into more great content and the potential to create a community that could continually grow.

### Target audience

- Users that are interested in Films, Tv shows and Video games.
- Users that enjoy intellectually genuine criticque and are pationate about media.
- User that enjoy writing reviews and want a good looking easy to work with platform to deploy their work and increase its reach.

### User requirements and expectations

- An intuitively structured and visually appealing website that is easy to read on all screen sizes
- Navigation that is easy to use and understand whether using mobile, tablet or monitor
- Ability to quickly understand the purpose of the website
- An ability to register, login and logout
- An ability to interact with content by commenting
- An ability to read comments that have been made under reviews
- An ability to update and delete comments
- An ability to create a review and see it published
- An ability for the user to update and delete their reviews
- An accessible website for all users

### Design Inspiration

My design ideas came from the classic color and aesthetic of old glamorous Hollywood cinema with rich red and gold embellishing and contrasting a dark background that emulates a cinema screen on which the bright images from each film in the pagniated reviews feel like films playing on that screen. This simple but strong aesthetic evokes a classic era and the traditional values coming from the idea that great art is timeless and therefore by extent is its honest critique. I think many people out there just want honest yet nuanced and detailed opinions free from alterior pretentions (in any direction) and this platform aims to deliver.

### Colour Scheme

The contrast colour scheme is designed to make it easy for users to navigate and draw the eye round each page as well as be evocatove as mentioned above.

I used Coolors [https://coolors.co/000000-f39c12-cba17b-e81010-445261](https://coolors.co/000000-f39c12-cba17b-e81010-445261)) to generate the colour palette for this website.


![Coolors](https://github.com/user-attachments/assets/4ce22a1e-0326-4b6a-b171-ceee7d981a39)

### Agile Methodologies - Project Management
I used an agile approach to project management. The True Review development process was divided into user stories shown below which were added to the GitHub project board to be tracked and managed as issues.

### MoSCoW Prioritization

My user stories were given priority labels according to the moscow prioritisation system alongside labels indicating my percieved size of the task as I started the project. All my user stories with full labelling and acceptance criteria can be found on my project board [https://github.com/users/Geoff-Fletcher/projects/6](https://github.com/users/Geoff-Fletcher/projects/6)

- **Must-Haves:** View Paginated list of reviews, See full review on click, Crud functionality for the review   
   model, Draft posts, Register an account, Review views and template 
- **Should-Haves:** Comment Approval, Comment form threads, CRUD functionality for comments.
- **Could-Haves:** About page, update about
- **Won’t-Haves:** Review types for games and tv shows

## Epics and user stories

### Epics
1.  As a user I can view a paginated list of reviews so that I can easily parse and select what I want to read about
2.  As a user I can see read and click through reviews on movies ** so that ** I can checkout ones I am interested 
    in
3.  As a User I can create, read, update and delete reviews so that I can take part in the websites primary purpose

### User stories

1. As a user I can View a full review when I click on its preview so that ** I can easily access the content that 
   interests me**
2. As a site admin I can draft a review so that I can finish writing content later and am not obliged to complete 
   in one go.
3. As a user I can register an account so that ** I can leave comments on reviews**
4. As a user I can see a burger icon that expands into the navbar on smaller screens so that I can navigate the 
   site on all screen sizes
5. As a site admin I can approve or disapprove comments so that *I can filter out objectionable or inappropriate 
   comments
6. As a user I can understand the purpose and mission of the website easily so that I stay interested and become 
   inspired to contribute the kind of content that will build towards the websites mission
7. As a user I can leave comments on a review so that I can be part of an ongoing conversation
8. As a site admin I can update the about text so that the user can understand what the site is doing and where it 
   is headed

## Wireframes

### Index page wireframes

Monitor wire frame for main page shown with full header menu on display and 6 reviews paginated to fill one page

![Index page wireframe](https://github.com/user-attachments/assets/fe390697-6c9d-41dd-b81c-d76ad3c8272c)

Tablet view shown; as the page shrinks it will move from a 3x2 format of pagination to a 1x3 with the full header menu of pages being replaced with the collapsable burger icon that will expand to show these menu options as a dropdown when moused over. The header uses the same responsive styling on all pages of the project including the full review details, about and create pages.

![Index page ipad](https://github.com/user-attachments/assets/5aa0462d-7096-43bd-8973-d9fd6e8b7c88)

### About page wireframes

### Create Review page wireframes

## Features

Many of the features are already shown in the wireframes so for brevity where relevant I will refer to them there whilst providing a commentary on their function

### Logo and navigation bar

A responsive navigation bar is in place. Concentrating on 'mobile first' design, the navigation bar incorporates a clickable burger icon with a drop down menu on mobile. There is a burger icon at tablet size too, but when moving to monitor size the burger disappears and a navigation bar appears with options to navigate to pages; 'Home', 'About' or 'Create' and depending on the user login status also a 'Register' and 'Login' link or a 'Logout'. The nav bar also displays the user login status with the message 'You are not logged in' or 'You are logged in as XXXXX'. In the top left corner there is a clickable project logo that also acts as a 'Home' button. See wireframes and other screenshots to view these features or log in to the project.

### Django alert messages

Every time there is a change in data the user is alerted. For example when a review is created, or edited and the same for comments. Also there is a notification when the user logs in or out to confirm their action. These appear in the blank space in the middle of the navigation bar to be in the users eyeline when possible.

### Clear indication as to whether the user is logged in or out at all times

As mentioned above the nav bar displays user login status with the message 'You are not logged in' or 'You are logged in as XXXXX'

### A list of review posts

On mobile and small Tablet screens reviews are displayed on the home page in a column of 3 as displayed in wireframes above. On larger tablets and monitiors there are 3 review posts displayed in a row and 6 on a page, with the option to use a next and previous button. As monitor size grows the review cards on the home page simply enlarge.

### See an individual review post in detail

When the title of a review is clicked on the home page the review detail html is rendered creating a page that show the image for the review and title above a large text box containg the review itself. Underneath this is a thread of comments and a comment box to allow for submission of the users own comments

### Pagination

This feature forms the list of 1x3 or 3x2 review mentioned in a list of review posts and generates the next and previous buttons dependent on the users position in the content.

### About Page

The about page gives information about True Review's concept and goals moving forward.lt talks about what the website hopes to acheive and how users can contribute. It also lays down some expectations for the user about what will be moderated in the hope that content submission will feel easy and keep the site on the right track. The image I have used is a little abstract but actually used AI to incorporate my facial features as I didn't feel it was crucial to lose privacy by putting my own or anyone elses image in the project but I could of course change this in the future if I felt it was meaningful to take on a more public status. I also felt True Review is not all about me so keeping a more abstract persona made sense.

### Sign in form

For the security forms at the moment I have django generics but I plan to replace the with crispy forms the moment i get time.

### Register form (Sign up)

For the security forms at the moment I have django generics but I plan to replace the with crispy forms the moment i get time.

### Sign out page

For the security forms at the moment I have django generics but I plan to replace the with crispy forms the moment i get time.

### Form with CRUD functionality to create a review when logged in

The create a review is impossible to use without having a logged in user account it displays a simple form with the fields shown in the image below:

![Create form](https://github.com/user-attachments/assets/f503f464-27a5-46f0-8bfd-cdf8d0c1172f)

This allows the user to fill out all field needed to create a film review ready to appear on the front-end including choosing an image which will be hosted by Cloudinary. Once this is done the users review will be visible as a draft to the admin which they must decide to publish before it appears in the site index. When the author of a review enters the review detail of a review they have created it is there they will see the edit and delete buttons/functionality if they are logged in. The author of reviews appears on both the index page and in the review detail itself to make it easy to see what a given user has written.

### Edit the reviews I have made when I am logged in

As mentioned above the edit functionality shows in the reviews details page on any review the users has written as long as they are logged in clicking this then feeds them to the edit form which mirrors the create form but allows adjustment of any field before resubmitting, after clicking this the user is returned to the main page and will see a Django alert informing them that the edit was successful.

![Edit form](https://github.com/user-attachments/assets/fb7f6315-7a9c-41b1-b130-9d59d16b9447)

### Delete the reviews I have made when I am logged in

The user can use the delete functionality on any review they have made whilst they are logged in; it checks if they are certain then when they respond 'yes' or 'no' they are returned to the main page with a Django alert that indicates the result of their choice.

![Delete form](https://github.com/user-attachments/assets/856e7d55-7cb0-43a9-b15a-ef2ed2f71a28)

### View comments on reviews

The user can see all the comments on a review in the comment thread text box directly below the review on the review detail page. Comments can be seen regardless of user login status but can only be created, edited and deleted when they are logged in and only if they are that users own comments.

![Comment Crud](https://github.com/user-attachments/assets/d1d95778-138d-4c30-a047-245e32a4d269)

the screen-shot shows the bottom of a review on a phone screen leading to the comments count, comments thread with delete and edit buttons on the users published comments and underneath the Leave a comment (create) box which can be freely typed in before clicking submit to post.

### CRUD functionality on comments when logged in

Full front end CRUD functionality is available on comments if the user is logged in. Every time data is created, edited or deleted there is an appropriate notification from Django alerts to give the user feedback. All this is visible in the above screenshot.

### Footer

This includes social media icons and copyright. It could potentially include contact details for colloboration or dicsussion over moderation in the future.

### Future Features

- A search box to allow users to search for reviews based on specific titles they are interested in.
- A sort filter for reviews into media type, reviews by author and potentially by genre which will be present for movies, tv shows and games but will take different categories in each case.
- Email confirmation when a users draft review has been publised.
- Enabling all three review types since this early version of the project sadly did not have time to inlcude TV reviews and game reviews.
- A like feature on reviews and a like counter for them to track their popularity and those whom click it potentially like the one for posts on Facebook.
- A like feature on comments similar to the above.
- 






