# Masterpiece

Masterpiece is an online painting-sharing app designed to inspire artists from all over the world. The app is aimed at users who want to share their paintings and build a thriving artistic community together.

The site acts as a painting repository, allowing users to store their artworks, explore other users' paintings, and add them to their favorites.

The live link can be found here - [Masterpiece](https://masterpiece23-cbdad7ea4f9e.herokuapp.com/)

![Responsiveness of the website](#)

- [Masterpiece](#masterpiece)
  * [User Experience (UX)](#user-experience--ux-)
    + [User Stories](#user-stories)
      - [EPIC | Artist Profile](#epic---artist-profile)
      - [EPIC | Artist Navigation](#epic---artist-navigation)
      - [EPIC | Painting Management](#epic---painting-management)
      - [EPIC | Painting Interaction](#epic---painting-interaction)
      - [EPIC | Site Administration](#epic---site-administration)
    + [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  * [Agile Methodology](#agile-methodology)
  * [Data Model](#data-model)
  * [Testing](#testing)
    + [HTML Validation](#html-validation)
    + [CSS Validation](#css-validation)
    + [JavaScript Validation](#javascript-validation)
    + [Python Linter Validation](#python-linter-validation)
    + [Lighthouse](#lighthouse)
  * [Security Features and Defensive Design](#security-features-and-defensive-design)
    + [User Authentication](#user-authentication)
    + [Form Validation](#form-validation)
    + [Database Security](#database-security)
    + [Custom error pages](#custom-error-pages)
  * [Features](#features)
    + [Header](#header)
    + [Footer](#footer)
    + [Home Page](#home-page)
    + [Artist Account Pages](#artist-account-pages)
    + [Browse Paintings](#browse-paintings)
    + [Painting Detail Page](#painting-detail-page)
    + [Add Painting Form](#add-painting-form)
    + [Update Painting Form](#update-painting-form)
    + [Delete Painting](#delete-painting)
    + [My Paintings Page](#my-paintings-page)
    + [My Likes Page](#my-likes-page)
    + [Error Pages](#error-pages)
  * [Deployment - Heroku](#deployment---heroku)
    + [Create the Heroku App](#create-the-heroku-app)
    + [Attach the Postgres database](#attach-the-postgres-database)
    + [Prepare the environment and settings.py file](#prepare-the-environment-and-settingspy-file)
    + [Create files/directories](#create-files-directories)
    + [Update Heroku Config Vars](#update-heroku-config-vars)
    + [Deploy](#deploy)
  * [Forking this repository](#forking-this-repository)
  * [Cloning this repository](#cloning-this-repository)
  * [Languages](#languages)
  * [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  * [Credits](#credits)
    + [Code](#code)
    + [Media](#media)
    + [Content](#content)
  * [Special Thanks](#special-thanks)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## User Experience (UX)

A Site-Visitor to Masterpiece would be someone who takes pleasure in creating and exploring beautiful paintings. They are eager to expand and enrich their collection of artworks or simply share them with others.

### User Stories

#### EPIC | Artist Profile

- As a Site User, I can register myself to this website, so that I can create/update/delete my own paintings and comments.
- As a Site User, I can see my current login status, so that I know if I am logged in or logged out.
- As a Site User, I can log in and out of my account, so that I can post, comment, and like paintings.

#### EPIC | Artist Navigation

- As a Site User, I can navigate myself throughout the website in an intuitive way, so that I can go back and forth between pages without an issue.
- As a Site User, I can open a painting with a click, so that I can see the full details, materials required, comments, and like the painting.
- As a Site User, I can scroll through a paginated list of paintings, so that I can get a quick overview of many artworks.

#### EPIC | Painting Management

- As a Site User, I can upload my own paintings through an easy form, so that I can share them with other users.
- As a Site User, I can view my own paintings, so that I can review and manage the artworks I have created.
- As a Site User, I can view all paintings I liked on one page, so that I can sort out my favorite paintings from the big list of all artworks.
- As a Site User, I can edit and delete my own paintings, so that I can keep my artworks up to date or remove them.

#### EPIC | Painting Interaction

- As a Site User, I can comment on paintings, so that I can give my own feedback or start a conversation.
- As a Site User, I can edit and delete my comments, so that I can adjust my comments if I made a mistake.
- As a Site User, I can "Like" a painting, so that I can sort out paintings I like from others.

#### EPIC | Site Administration

- As a Site Administrator, I can create, read, update, and delete categories, paintings, and comments, so that I can manage the website.