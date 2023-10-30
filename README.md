# Masterpiece

Code Institute Project nr 4.

Masterpiece is an online painting-sharing app designed to inspire artists from all over the world. The app is aimed at users who want to share their paintings and build a thriving artistic community together.

The site acts as a painting repository, allowing users to store their artworks, explore other users' paintings, and add them to their favorites.

The live link can be found here - [Masterpiece](https://masterpiece23-cbdad7ea4f9e.herokuapp.com/)

![Responsiveness of the website](#)

- [Masterpiece](#masterpiece)
  * [User Experience (UX)](#user-experience--ux-)
    + [User Stories](#user-stories)
      - [EPIC | Artist Profile](#epic--artist-profile)
      - [EPIC | Artist Navigation](#epic--artist-navigation)
      - [EPIC | Painting Management](#epic--painting-management)
      - [EPIC | Painting Interaction](#epic--painting-interaction)
      - [EPIC | Site Administration](#epic--site-administration)
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

### Design

#### Colour Scheme

![Colour Palette](https://res.cloudinary.com/masterpiece23/image/upload/v1698349807/wue7bjrtticmpldyzrjx.png)

During the development process, I took great care to refine the color scheme, aiming to highlight the essence of each painting. To maintain a clean and uncluttered focus, I deliberately embraced a neutral color palette.

Given that the core of my platform is centered on the world of painting, I opted for a pristine white background, accompanied by understated, light-colored details.

Databas
https://res.cloudinary.com/masterpiece23/image/upload/v1698686969/fgbjwuph9uew6vlcwhpc.png

#### Imagery

The webb app has no fixed images. All the imagery is uploaded paintings.

#### Fonts

The primary font used for the body and links on the website is the elegant Anek Bangla font. The logo, painting headings, and footer feature the artistic Mansalva font, adding a unique touch to the overall design.

For consistency and aesthetics, I've imported these fonts via Google Fonts. In the event that any issues arise with font import, I've configured Helvetica, Arial, sans-serif as a reliable backup font to ensure seamless readability.

#### Wireframes

<details>
<summary>Home Page</summary>

![Home Page](https://res.cloudinary.com/masterpiece23/image/upload/v1698691560/index_wireframe_vgv85x.png)
</details>

<details>
<summary>Home Page Mobile</summary>

![Home Page Mobile](https://res.cloudinary.com/masterpiece23/image/upload/v1698691560/mobile_wireframe_index_kke8xn.png)
</details>

<details>
<summary>Gallery</summary>

![Gallery](https://res.cloudinary.com/masterpiece23/image/upload/v1698691561/gallery_wireframe_aoicof.png)
</details>

<details>
<summary>Gallery Mobile</summary>

![Gallery](https://res.cloudinary.com/masterpiece23/image/upload/v1698691560/mobile_wireframe_gallery_abac9g.png)
</details>

<details>
<summary>My Paintings and My Likes</summary>

![My Paintings and My Likes](https://res.cloudinary.com/masterpiece23/image/upload/v1698691560/my_account_wireframe_deruxw.png)

There is a slight difference here: these two pages are separated in the final product.
</details>

<details>
<summary>My Paintings and My Likes Mobile</summary>

![My Paintings and My Likes Mobile](https://res.cloudinary.com/masterpiece23/image/upload/v1698691560/my_account_wireframe_deruxw.png)

There is a slight difference here: these two pages are separated in the final product.
</details>


## Agile Methodology

To handle the development process using an agile approach, we used GitHub Projects. You can check the project board [here](https://github.com/users/jindah/projects/4) for reference.

The five Epics we talked about earlier were added as milestones in the GitHub project. To efficiently manage each specific task, we made a corresponding GitHub Issue and connected it to the right milestone. Each task has clear criteria for completion, making it easy to understand what needs to be done. Additionally, we divided these criteria into smaller tasks to make it easier to work on each task.

## Data Model

Throughout the development of this project, I adhered to Object-Oriented Programming principles while making extensive use of Django's Class-Based Generic Views.

To ensure secure user authentication, I seamlessly integrated Django AllAuth, a powerful authentication system.

The website's core revolves around paintings. To create a painting, two fundamental elements are essential. Firstly, every painting must have an author, and it's the user who initiates the creation of a painting who takes on this role. Secondly, an image is a mandatory component for the upload process. Users are also granted the ability to choose the painting's category, although any modifications to categories are restricted to website administrators.

The Comment model is designed to allow users to provide feedback on individual paintings. Within the Comment model, the Painting and Profile models serve as foreign keys, ensuring a direct association between each comment and a specific painting, with attribution to a particular user. A similar structural approach is employed for the Likes model.

The diagram below provides a comprehensive visualization of the database schema.

![Database Schema](https://res.cloudinary.com/masterpiece23/image/upload/v1698686969/fgbjwuph9uew6vlcwhpc.png)

## Testing

### HTML Validation

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/).

<details>
<summary>Home Page</summary>

![Home Page](#)
</details>

<details>
<summary>About Us</summary>

![About Us](#)
</details>

<details>
<summary>Gallery</summary>

![Gallery](#)
</details>

<details>
<summary>My Paintings</summary>

![My Paintings](#)
</details>

<details>
<summary>Upload Painting</summary>

![Upload Painting](#)
</details>

<details>
<summary>My Favorites</summary>

![My Favorites](#)
</details>

<details>
<summary>Logout</summary>

![Logout](#)
</details>

<details>
<summary>Sign Up</summary>

![Sign Up](#)
</details>

<details>
<summary>Login</summary>

![Login](#)
</details>

<details>
<summary>Painting Details</summary>

![Painting Details](#)
</details>

<details>
<summary>Painting Update (Another test / deleted)</summary>

![Painting Update (Another test / deleted)](#)
</details>

<details>
<summary>Painting Delete (Another test / deleted)</summary>

![Painting Delete (Another test / deleted)](#)
</details>

<details>
<summary>Comment Update</summary>

![Comment Update](#)
</details>

<details>
<summary>Comment Delete</summary>

![Comment Delete](#)
</details>

### CSS Validation

No errors were found when passing my CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

<details>
<summary>Result</summary>

![CSS validation results](#)
</details>

### JavaScript Validation

No errors were found when passing the javascript snippet through [Jshint](https://jshint.com/).

<details>
<summary>Result</summary>

![JavaScript validation results](#)
</details>

### Python Linter Validation

All Python files I worked with were run through the [CI Python Linter](https://pep8ci.herokuapp.com/).

<details>
<summary>admin.py</summary>

![Result](#)
</details>

<details>
<summary>froms.py</summary>

![Result](#)
</details>

<details>
<summary>models.py</summary>

![Result](#)
</details>

<details>
<summary>blog/urls.py</summary>

![Result](#)
</details>

<details>
<summary>views.py</summary>

![Result](#)
</details>

<details>
<summary>settings.py</summary>

![CSS validation results](#)

The lines exceeding the maximal length have been solved by adding the # noqa tag.
</details>

<details>
<summary>masterpiece/urls.py</summary>

![CSS validation results](#)
</details>