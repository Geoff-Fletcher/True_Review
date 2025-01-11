# True Review

(Developer: Geoff Fletcher)

am i responsive placeholder

## Live website

Link to live website:
## Why True Review?

The trust people have in review aggregator websites such as Rotten Tomatoes and IGN is at an all time low often with huge disparity between critic and audience scores. There are a multitude of reasons this is the case but what I believe is important is that a huge audience exists for media reviews that put content and the genuine attempt to analyse content first. True Review is built to step into this void as a platform for users to firstly read great reviews but also to create their own and comment on others. There are of course still ratings for the user to glean at a glance a rough idea on someones opinion of a piece of media but our ethos via moderation is to focus on the critque of storytelling, direction, cinematography and the acting performances that have made people fall in love with film, tv-series and video-games for generations. This is a full stack website built using the Django web framwork, with the aim of drawing in readers to enjoy great content and to go on to produce their own reviews that can inspire others and continue growing this platform. The initial idea was to use one model with 3 seperate modules to produce the three review types each with some unique fields: movie reviews, tv reviews and game reviews, but due to time constraints it has been initially launched with movie reviews active and the intent to add the other 2 soon.


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
- [Features](#features)
   * [Logo and navigation bar](#logo-and-navigation-bar)
     * [Django alert messages](#django-alert-messages)
   * [Clear indication as to whether the user is logged in or out at all times](#clear-indication-as-to-whether-the-user-is-logged-in-or-out-at-all-times)
    * [A list of review posts](#a-list-of-blog-posts)
   * [See an individual review post in detail](#see-an-individual-blog-post-in-detail)
   * [Pagination](#pagination)
   * [About page](#about-page)
    * [Sign in form](#sign-in-form)
   * [Register form (Sign up)](#register-form-sign-up)
   * [Sign out page](#sign-out-page)
     * [Form with CRUD functionality to create a review when logged in](#form-with-crud-functionality-to-make-a-review-when-logged-in)
      * [Edit the reviews I have made when I am logged in](#edit-the-reviews-i-have-made-when-i-am-logged-in)
   * [Delete the reviews I have made when I am logged in](#delete-the-reviews-i-have-made-when-i-am-logged-in)
   * [View comments on reviews](#view-comments-on-reviews)
   * [CRUD functionality on comments when logged in](#crud-functionality-on-comments-when-logged-in)
   * [Footer](#footer)   
    - [Future features](#future-features)
  - [Wireframes](#wireframes)
   * [Index page wireframes](#index-page-wireframes)
   * [About page wireframes](#about-page-wireframes)
   * [Create Review page wireframes](#create-review-page-wireframes)  
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





