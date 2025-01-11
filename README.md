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
- [Epics and user stories](#epics-and-user-stories)
   * [Epics](#epics)
   * [User stories](#user-stories)
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
     * [MoSCoW](#moscow)
- [Future features](#future-features)
- [Design](#design)
   * [Color](#color)
- [Wireframes](#wireframes)
   * [Index page wireframes](#index-page-wireframes)
   * [About page wireframes](#about-page-wireframes)
   * [Create Review page wireframes](#create-review-page-wireframes)
   * [Review detail page](#review-detail-page)
   * [Register page](#register-page)
   * [Log in page](#log-in-page)
   * [Log out page](#log-out-page)
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

### Epics and user stories

### Epics

### User stories

