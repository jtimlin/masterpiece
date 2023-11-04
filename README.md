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

The diagram below provides a visualization of the database schema.

![Database Schema](https://res.cloudinary.com/masterpiece23/image/upload/v1698686969/fgbjwuph9uew6vlcwhpc.png)

## Testing

### HTML Validation

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/).

<details>
<summary>Home Page</summary>

![Home Page](https://res.cloudinary.com/masterpiece23/image/upload/v1699104717/HTML%20checker/home_page_tex7g3.png)
</details>

<details>
<summary>About Us</summary>

![About Us](https://res.cloudinary.com/masterpiece23/image/upload/v1699104717/HTML%20checker/aboutus_skr3zd.png)
</details>

<details>
<summary>Gallery</summary>

![Gallery](https://res.cloudinary.com/masterpiece23/image/upload/v1699104718/HTML%20checker/gallery_ki11n1.png)
</details>

<details>
<summary>My Paintings</summary>

![My Paintings](https://res.cloudinary.com/masterpiece23/image/upload/v1699104718/HTML%20checker/my_paintings_os7zrk.png)
</details>

<details>
<summary>Upload Painting</summary>

![Upload Painting](https://res.cloudinary.com/masterpiece23/image/upload/v1699104719/HTML%20checker/upload_painting_aezosm.png)
</details>

<details>
<summary>My Favorites</summary>

![My Favorites](https://res.cloudinary.com/masterpiece23/image/upload/v1699104718/HTML%20checker/my_favorites_ljzla7.png)
</details>

<details>
<summary>Logout</summary>

![Logout](https://res.cloudinary.com/masterpiece23/image/upload/v1699104717/HTML%20checker/logout_jje55e.png)
</details>

<details>
<summary>Sign Up</summary>

![Sign Up](https://res.cloudinary.com/masterpiece23/image/upload/v1699104718/HTML%20checker/signup_lh3jwo.png)
</details>

<details>
<summary>Login</summary>

![Login](https://res.cloudinary.com/masterpiece23/image/upload/v1699104718/HTML%20checker/login_czv0ia.png)
</details>

<details>
<summary>Painting Details</summary>

![Painting Details](https://res.cloudinary.com/masterpiece23/image/upload/v1699104718/HTML%20checker/painting_detail_n7dfct.png)
</details>

<details>
<summary>Painting Update</summary>

![Painting Update](https://res.cloudinary.com/masterpiece23/image/upload/v1699104718/HTML%20checker/update_painting_i2jy5j.png)
</details>

<details>
<summary>Painting Delete</summary>

![Painting Delete](https://res.cloudinary.com/masterpiece23/image/upload/v1699104717/HTML%20checker/delete_painting_hfctms.png)
</details>

<details>
<summary>Comment Update</summary>

![Comment Update](https://res.cloudinary.com/masterpiece23/image/upload/v1699104717/HTML%20checker/comment_update_cqcn24.png)
</details>

<details>
<summary>Comment Delete</summary>

![Comment Delete](https://res.cloudinary.com/masterpiece23/image/upload/v1699104717/HTML%20checker/comment_delete_hps8fy.png)
</details>

### CSS Validation

No errors were found when passing my CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

<details>
<summary>Result</summary>

![CSS validation results](https://res.cloudinary.com/masterpiece23/image/upload/v1699105157/CSS_validator_tpt27j.png)
</details>

### JavaScript Validation

No errors were found when passing the javascript snippet through [Jshint](https://jshint.com/).

<details>
<summary>Result</summary>

![JavaScript validation results](https://res.cloudinary.com/masterpiece23/image/upload/v1699105157/JSHINT_validator_dxwivw.png)
</details>

### Python Linter Validation

All Python files I worked with were run through the [CI Python Linter](https://pep8ci.herokuapp.com/).

<details>
<summary>admin.py</summary>

![Result](https://res.cloudinary.com/masterpiece23/image/upload/v1699105150/Pyhton%20Linter/admin.py_tlmi8p.png)
</details>

<details>
<summary>froms.py</summary>

![Result](https://res.cloudinary.com/masterpiece23/image/upload/v1699105151/Pyhton%20Linter/forms.py_pyi77h.png)
</details>

<details>
<summary>models.py</summary>

![Result](https://res.cloudinary.com/masterpiece23/image/upload/v1699105152/Pyhton%20Linter/models.py_nl5q1r.png)
</details>

<details>
<summary>blog/urls.py</summary>

![Result](https://res.cloudinary.com/masterpiece23/image/upload/v1699105155/Pyhton%20Linter/urls.py_egrmnr.png)
</details>

<details>
<summary>views.py</summary>

![Result](https://res.cloudinary.com/masterpiece23/image/upload/v1699105154/Pyhton%20Linter/views.py_vgig7l.png)
</details>

<details>
<summary>settings.py</summary>

![CSS validation results](https://res.cloudinary.com/masterpiece23/image/upload/v1699105153/Pyhton%20Linter/settings.py_gju4pf.png)

The lines exceeding the maximal length have been solved by adding the # noqa tag.
</details>

<details>
<summary>masterpiece/urls.py</summary>

![CSS validation results](https://res.cloudinary.com/masterpiece23/image/upload/v1699105151/Pyhton%20Linter/masterpiece.urls.py_yfkgld.png)
</details>


### Lighthouse

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was run on all pages to check Performance, Accessibility, Best Practices, and SEO scores.

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

The drop in the performance is explained by the images and styles loading from an external source, [Cloudinary](https://cloudinary.com/).
</details>

<details>
<summary>Add Painting</summary>

![Add Painting](#)
</details>

<details>
<summary>My Paintings</summary>

![My Paintings](#)
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

The drop in the performance is explained by the images and styles loading from an external source, [Cloudinary](https://cloudinary.com/).
</details>

<details>
<summary>Painting Update</summary>

![Painting Update](#)

The drop of the [accessibility](<https://cdn.discordapp.com/attachments/1049024982694498367/1136306366114439329/image.png>) is explained by missing titles. The [titles](https://cdn.discordapp.com/attachments/1049024982694498367/1136306366361911477/image.png) are not actually missing. The problem is caused by the use of the Summernote extension.
</details>

<details>
<summary>Painting Delete</summary>

![Painting Delete](#)
</details>

<details>
<summary>Comment Update</summary>

![Comment Update](#)
</details>

<details>
<summary>Comment Delete</summary>

![Comment Delete](#)
</details>

## Browser Testing
- The website was tested on Google Chrome and Microsoft Edge browsers with no issues noted.
    
## Device Testing
- The website was viewed on a variety of devices such as Desktop, Laptop, Ipad and Iphone 12 mini to ensure responsiveness on various screen sizes in both portrait and landscape mode. The website performed as intended. The responsive design was also checked using Chrome developer tools across multiple devices with structural integrity holding for the various sizes.

## Manual Testing

## Site Navigation
| Element               | Action     | Expected Result                    | Pass/Fail |
|-----------------------|------------|------------------------------------|-----------|
| **NavBar**            |            |                                    |           |
| Site Name (logo area) | Click      | Redirect to home                   |     Pass      |
| Home Link             | Click      | Redirect to home                   |      Pass     |
| About Us Link        | Click      | Open About Us page                |     Pass      |
| Gallery Link          | Click      | Open Gallery Page                 |     Pass      |
| Login Link          | Click      | Open Login Page                 |      Pass     |
| Join Us! Link          | Click      | Open Sign Up Page                 |     Pass      |

## Home Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Hero 'Details' Button | Click   | Open Painting Details page               |     Pass      |
| Paintings | Display | Showing three latest added paintings |     Pass      |

## About Us Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Join Us link | Click   | Open Sign Up page               |      Pass     |
| Info text | Display | Showing information about Masterpiece |     Pass      |

## Gallery Page
| Element     | Action                  | Expected Result                                                                         | Pass/Fail |
|-------------|-------------------------|-----------------------------------------------------------------------------------------|-----------|
| Painting Card | Display correct content | Display correct image, painting title and artist                                |     Pass      |
| Painting Card | Click                   | Clicking anywhere inside the painting card takes you to the correct painting's detail page. |     Pass      |
| Painting Card | Pagination              | Site will paginate 8 painting cards to a page                                       |     Pass      |
| Painting Card | Order                   | Paintings are sorted by newest to oldest                                           |      Pass     |

## Painting Detail Page
| Element                        | Action              | Expected Result                                                                                                         | Pass/Fail |
|--------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------|-----------|
| Painting Content               | Display             | Display correct painting image, title, author, description, and comments                                                |     Pass      |
| Like button (Outline)          | Click               | Clicking the outlined heart changes it to a solid heart                                                                 |     Pass      |
| Like button (Outline)          | Click               | Painting is added to the user's My Favorites page                                                                          |     Pass      |
| Like button (Outline)          | Click               | Success message appears informing the user that the painting has been added to their liked paintings                  |      Pass     |
| Like button (Outline)          | Click               | Success message fades after 3 seconds                                                                                   |     Pass      |
| Like button (Solid)            | Click               | Clicking the solid heart changes it back to an outlined heart                                                           |      Pass     |
| Like button (Solid)            | Click               | Painting is removed from the user's My Favorites page                                                                       |     Pass      |
| Like button (Solid)            | Click               | Success message appears informing the user that the painting has been removed from their liked paintings              |      Pass     |
| Like button (Solid)            | Click               | Success message fades after 3 seconds                                                                                   |     Pass      |
| Like button                    | Display             | Button only clickable if user in session                                                                                  |    Pass       |
| Update painting button         | Click               | Opens Update Painting Form                                                                                                |     Pass      |
| Update painting button         | Display             | Button only visible if user is the author                                                                               |     Pass      |
| Delete painting button         | Click               | Opens Delete Painting confirmation page                                                                                   |     Pass      |
| Delete painting button         | Display             | Button only visible if user is the author                                                                               |     Pass      |
| User Comments                  | Display             | Displays correct name, date, time, and comment body                                                                    |     Pass      |
| User Comments                  | Display             | Comments are ordered oldest to newest                                                                                   |     Pass      |
| Update comment button          | Display             | Button only visible if user is the comment author                                                                       |     Pass      |
| Update comment button          | Click               | Opens Update Comment Form                                                                                               |    Pass       |
| Update comment form            | Leave empty         | On submit: form won't submit                                                                                            |     Pass      |
| Update comment form            | Leave empty         | Error message displays                                                                                                  |      Pass     |
| Update comment submit button   | Click               | Form submit - page updates and comment displays in comments section with correct content                                |     Pass      |
| Update comment submit button   | Click               | Success message appears informing the user that the comment has been updated                                            |     Pass      |
| Update comment submit button   | Click               | Success message fades after 3 seconds                                                                                   |     Pass      |
| Update comment form            | Access              | If a user tries to edit another user's comment (by changing the URL), they receive a 403 error.                        |     Pass      |
| Update comment form            | Access              | If a user tries to edit a comment (by changing the URL) without being signed in, they are redirected to the login page |     Pass      |
| Cancel update comment button   | Click               | Redirects the user back to the painting detail page                                                                   |      Pass     |
| Delete comment button          | Display             | Button only visible if the user is the comment author                                                                   |     Pass      |
| Delete comment button          | Click               | Opens delete comment confirmation page                                                                                  |     Pass      |
| Confirm delete button          | Click               | Comment is removed from the comment section                                                                             |     Pass      |
| Confirm delete button          | Click               | Success message appears informing the user that the comment has been deleted                                            |     Pass      |
| Confirm delete button          | Click               | Success message fades after 3 seconds                                                                                   |     Pass      |
| Confirm delete button          | Click               | Redirects the user back to the painting detail page                                                                   |     Pass      |
| Cancel delete button           | Click               | Redirects the user back to the painting detail page                                                                   |      Pass     |
| Delete comment                 | Access              | If a user tries to delete another user's comment (by changing the URL), they receive a custom 403 error.               |     Pass      |
| Delete comment                 | Access              | If a user tries to delete a comment (by changing the URL) without being signed in, they are redirected to the login page |     Pass      |
| Add comment Form               | Display             | Form only visible if user in session                                                                                    |     Pass      |
| Add comment Form submit button | Leave empty         | On submit: form won't submit                                                                                            |     Pass      |
| Add comment Form submit button | Leave empty         | Error message displays                                                                                                  |     Pass      |
| Add comment Form submit button | Filled in           | Form submit - page updates and comment displays in the comments section with correct content                            |     Pass      |
| Add comment Form submit button | Click               | Success message appears informing the user that the comment has been added                                              |     Pass      |
| Add comment Form submit button | Click               | Success message fades after 3 seconds                                                                                   |     Pass      |

## Add Painting Page
| Element                       | Action                | Expected Result                                                                                                     | Pass/Fail |
|-------------------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------|-----------|
| Add Painting                   | Access                | If a user tries to add a painting (by changing the URL) without being signed in, they are redirected to the login page |     Pass      |
| Form Text Input (if required) | Leave blank           | On Submit: Warning appears, form won't submit                                                                       |     Pass      |
| Painting Title                  | Duplicate Entry       | On Submit: Warning appears, form won't submit                                                                       |      Pass     |
| Form image select button      | Click                 | Opens device storage                                                                                                 |     Pass      |
| Form image select button      | Display               | Chosen image name displayed once selected                                                                           |     Pass      |
| Form image select button      | Display               | Form wont submit if no image selected. Shows warning message.                                                                      |      Pass     |
| Cancel button                 | Click                 | Redirects to the Gallery page                                                                                     |      Pass     |
| Add Painting button(form valid) | Click                 | Form submit                                                                                                         |    Pass       |
| Add Painting button(form valid) | Click                 | Redirects to the painting detail page for the new painting with all information displaying correctly                 |      Pass     |
| Add Painting button(form valid) | Click                 | Success message appears informing the user that the painting has been created                                         |       Pass    |
| Add Painting button(form valid) | Click                 | Success message fades after 3 seconds                                                                               |     Pass      |

## Update Painting Page
| Element            | Action  | Expected Result                                                                                                         | Pass/Fail |
|--------------------|---------|-------------------------------------------------------------------------------------------------------------------------|-----------|
| Update Painting      | Access  | If a user tries to edit another user's painting (by changing the URL), they receive a custom 403 error. (forbidden access) |     Pass      |
| Update Painting      | Access  | If a user tries to edit a painting (by changing the URL) without being signed in, they are redirected to the login page    |     Pass      |
| Update Painting Form | Display | Form has all the fields filled out with the original content                                                            |     Pass      |
| Update Button      | Click   | Updated painting is saved                                                                                                 |     Pass      |
| Update Button      | Click   | Success message appears telling the user that the painting has been successfully updated                                  |     Pass      |
| Update Button      | Click   | Success message fades after 3 seconds                                                                                   |      Pass     |
| Update Button      | Click   | User is redirected back to the current painting page                                                                      |     Pass      |
| Cancel Button      | Click   | User is redirected back to the current painting page                                                                      |      Pass     |

## Confirm Delete Painting Page
| Element       | Action | Expected Result                                                                                                        | Pass/Fail |
|---------------|--------|------------------------------------------------------------------------------------------------------------------------|-----------|
| Delete Painting | Access | If a user tries to delete another user's painting (by changing the URL), they receive a custom 403 error.                 |      Pass     |
| Delete Painting | Access | If a user tries to delete a painting (by changing the URL) without being signed in, they are redirected to the login page |     Pass      |
| Delete Button | Click  | Painting is deleted and removed from user paintings page                                                                   |      Pass     |
| Delete Button | Click  | Success message appears telling the user that the painting has been successfully deleted                                 |     Pass      |
| Delete Button | Click  | User is redirected back to the Gallery page                                                                         |      Pass     |
| Cancel Button | Click  | Redirects to the current painting page    

## My Paintings Page

| Element       | Action | Expected Result                                                                                                        | Pass/Fail |
|---------------|--------|------------------------------------------------------------------------------------------------------------------------|-----------|
| My Paintings Page | Access               | If a user tries to access this page (by changing the URL) without being signed in, they are redirected to the Login page |     Pass      |
| My Paintings Page | Display              | Only displays the paintings that the user is the author of |     Pass      |
| Painting Card   | Card Content Display | Display the correct image, painting title, and artist |      Pass     |
| Painting Card   | Click                | Clicking anywhere inside the painting card takes you to the correct painting's detail page |     Pass     |
| Painting Card   | Pagination           | The site will paginate 8 painting cards to a page   |     Pass      |
| Painting Card   | Order                | Paintings are sorted by the newest to the oldest    |      Pass     |

## My Favorites Page

| Element       | Action | Expected Result                                                                                                        | Pass/Fail |
|---------------|--------|------------------------------------------------------------------------------------------------------------------------|-----------|
| My Favorites Page   | Access               | If a user tries to access this page (by changing the URL) without being signed in, they are redirected to the Login page |     Pass      |
| My Favorites Page   | Display              | Only the paintings that the user has bookmarked are shown |     Pass      |
| Painting Card   | Card Content Display | Display the correct image, painting title, and artist |     Pass      |
| Painting Card   | Click                | Clicking anywhere inside the painting card takes you to the correct painting's detail page |     Pass      |
| Painting Card   | Pagination           | The site will paginate 8 painting cards to a page   |     Pass      |
| Painting Card   | Order                | Paintings are sorted by the newest to the oldest    |      Pass     |

## Django All Auth Pages

| Element       | Action | Expected Result                                                                                                        | Pass/Fail |
|---------------|--------|------------------------------------------------------------------------------------------------------------------------|-----------|
| **Sign Up**        |                     |                                                                |           |
| Log in link        | Click               | Redirect to the login page                                     |     Pass      |
| Username field     | Leave empty         | On submit: form won't submit                                   |      Pass     |
| Username field     | Insert correct format | On submit: form submit                                         |     Pass      |
| Username field     | Insert duplicate username | On submit: form won't submit                              |      Pass     |
| Email field        | Insert incorrect format | On submit: form won't submit                               |      Pass     |
| Email field        | Insert correct format | On submit: form submit                                         |     Pass      |
| Email field        | Leave empty         | On submit: form submit                                         |     Pass      |
| Email field        | Insert duplicate email | On submit: form won't submit                                   |     Pass      |
| Password field     | Insert incorrect format | On submit: form won't submit                                   |    Pass       |
| Password field     | Passwords don't match | On submit: form won't submit                                   |     Pass      |
| Password field     | Insert correct format and passwords match | On submit: form submit |     Pass      |
| Sign Up button(form valid) | Click        | Form submit                                                    |      Pass     |
| Sign Up button(form valid) | Click        | Redirect to the home page                                      |     Pass      |
| Sign Up button(form valid) | Click        | Success message confirming login appears                      |     Pass      |
| Sign Up button(form valid) | Click        | Success message fades after 3 seconds                          |      Pass     |
| **Log in**         |                     |                                                                |           |
| Sign up link       | Click               | Redirect to the sign-up page                                   |     Pass      |
| Username field     | Leave empty         | On submit: form won't submit                                   |      Pass     |
| Username field     | Insert wrong username | On submit: form won't submit                                   |     Pass      |
| Password field     | Leave empty         | On submit: form won't submit                                   |     Pass      |
| Password field     | Insert wrong password | On submit: form won't submit                                   |    Pass       |
| Login button(form valid) | Click         | Form submit                                                    |      Pass     |
| Login button(form valid) | Click         | Redirect to the page where user logged in from                                     |     Pass      |
| Login button(form valid) | Click         | Success message confirming login appears                      |      Pass     |
| Login button(form valid) | Click         | Success message fades after 3 seconds                          |      Pass     |
| **Log Out**        |                     |                                                                |           |
| Logout button      | Click               | Redirect to the homepage                                       |     Pass      |
| Logout button      | Click               | Success message confirming log out appears                     |      Pass     |
| Logout button      | Click               | Success message fades after 3 seconds                         |     Pass      |

### Bugs 

#### Fixed Bugs

## CSRF Verification Failed with Allauth
- **Problem**: Allauth was not allowing login or signup and displayed a "CSRF verification failed. Request aborted." message.
- **Solution**: The issue was related to a newer version of Allauth. The solution involved adding CSRF trusted origins to the settings.py file. [More details](https://stackoverflow.com/questions/70285834/forbidden-403-csrf-verification-failed-request-aborted-reason-given-for-fail)

## Page Titles Not Displayed
- **Problem**: Page titles were not being displayed correctly.
- **Solution**: Adding a `{% block title %}` tag to the base.html file resolved the issue.

## Error When Uploading a New Painting
- **Problem**: When attempting to upload a new painting, an error message appeared: "django.urls.exceptions.NoReverseMatch: Reverse for 'painting_detail' with arguments '('',)' not found."
- **Issue**: The Add Painting form did not automatically generate a slug for the painting, causing a failure to load the home page.
- **Solution**: The issue was addressed by overriding the save model method and adding the slugify field. [More details](https://stackoverflow.com/questions/70601191/how-to-auto-populate-slug-field-in-django-forms)

## Update Painting Form Doesn't Show Image
- **Problem**: The Update Painting form did not display the actual painting image.
- **Issue**: A function that checked if an uploaded file was an image inadvertently cleared the current image when updating an existing image.
- **Solution**: To make it work, file validation was temporarily removed. The issue was further addressed by implementing Cloudinary's file validation to display error messages properly.

## Large Image Sizes
- **Problem**: Image sizes were too large.
- **Issue**: Attempting to automate image optimization with Cloudinary resulted in image sizes that were still too big.
- **Solution**: It was found that Cloudinary's automated optimization requires a paid service. The issue was addressed by exploring image optimization alternatives, such as using Django's Pillow library.

## Error on Upload Image Page
- **Problem**: The Upload Image page displayed an error message stating, "Invalid image file. Please upload a valid image file," even for valid image formats like jpg or png.
- **Issue**: This issue arose from a previous attempt to use Cloudinary's image optimization in the models and not properly migrating after changes.
- **Solution**: The issue was resolved by performing the necessary migrations.

#### Unfixed bugs:

- #### Not there yet
     - **Bug**: Here will be something.


## Security Features and Defensive Design

### User Authentication

- Django's LoginRequiredMixin is employed to ensure that any attempts to access secure pages by non-authenticated users are redirected to the login page.
- Django's UserPassesTestMixin is utilized to restrict access based on specific permissions, such as allowing users to edit or delete only their own paintings and comments. If the user does not pass the test, they will be presented with an HTTP 403 Forbidden error.

### Form Validation

When incorrect or empty data is entered into a form, submitting the form will not be possible, and a warning message will be displayed to the user, indicating which field raised the error. This ensures that users are informed about the issues in their input and prompts them to correct the errors before submitting the form.

### Database Security

The database URL and secret key are stored in the env.py file to prevent any unauthorized connections to the database. This setup was implemented prior to the initial push to GitHub, ensuring sensitive information remains secure.

Furthermore, Cross-Site Request Forgery (CSRF) tokens have been incorporated into all forms across the site. This additional security measure helps protect against CSRF attacks, enhancing the overall security of the application.

### Custom error pages

Custom Error Pages have been implemented to offer users more information about the encountered errors and to guide them back to the site with the help of navigational buttons.

400 Bad Request: Masterpiece is unable to process this request.

403 Forbidden: It appears that you are attempting to access restricted content. Please log out and sign in with the appropriate account.

404 Not Found: The page you are searching for does not exist.

500 Internal Server Error: Masterpiece is presently unable to handle this request.

## Features

### Header

![header logged out](#)

**Logo**

- A personalized logo was crafted with inspiration from [this](https://codepen.io/maheshambure21/pen/MWWgyyG) webpage.
- This logo is situated in the top left corner of the navigation bar, providing a distinct brand identity for the site. Moreover, the logo is linked to the home page, enabling seamless navigation for the users back to the main page with just a click.,

**Navigation Bar**

- The website features a consistent navigation bar at the top of every page, containing links to various other pages.
- The "My Account" link appears as a drop-down menu for logged-in users. "Join Us" and "Login." is visible for non-logged-in users.
- Once a user successfully logs in, the "My Account" drop-down menu dynamically changes to show the user's name along with logout button.

### Footer



### Home Page

**Hero Section**