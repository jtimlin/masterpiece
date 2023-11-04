# Masterpiece

Code Institute Project nr 4.

Masterpiece is an online painting-sharing app designed to inspire artists from all over the world. The app is aimed at users who want to share their paintings and build a thriving artistic community together.

The site acts as a painting repository, allowing users to store their artworks, explore other users' paintings, and add them to their favorites.

The live link can be found here - [Masterpiece](https://masterpiece23-cbdad7ea4f9e.herokuapp.com/)

![Responsiveness of the website](https://res.cloudinary.com/masterpiece23/image/upload/v1699107123/home_page_responsive_rgfx3j.png)

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
    + [Header](#features--header)
    + [Footer](#features--footer)
    + [Home Page](#features--home-page)
    + [Browse Gallery](#features--browse-gallery)
    + [Painting Detail Page](#features--painting-detail-page)
    + [Upload Painting Form](#features--upload-painting-form)
    + [Update Painting Form](#features--update-painting-form)
    + [Delete Painting](#features--delete-painting)
    + [My Paintings Page](#features--my-paintings-page)
    + [My Favorites Page](#features--my-favorites-page)
    + [Error Pages](#features--error-pages)
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

![header logged out](https://res.cloudinary.com/masterpiece23/image/upload/v1699107461/features/header_ddq3cc.png)

**Logo**

- A personalized logo was crafted with inspiration from [this](https://codepen.io/maheshambure21/pen/MWWgyyG) webpage.
- This logo is situated in the top left corner of the navigation bar, providing a distinct brand identity for the site. Moreover, the logo is linked to the home page, enabling seamless navigation for the users back to the main page with just a click.,
- All the social links are on the right side for easy access.

**Navigation Bar**

- Sticky bar for easy access.
- The website features a consistent navigation bar at the top of every page, containing links to various other pages.
- The "My Account" link appears as a drop-down menu for logged-in users. "Join Us" and "Login." is visible for non-logged-in users.
- Once a user successfully logs in, the "My Account" drop-down menu dynamically changes to show the user's name along with logout button.

![header logged in](https://res.cloudinary.com/masterpiece23/image/upload/v1699107636/features/header_logged_in_qb1r1g.png)

- Once a user has logged in, the options to "Sign Up" or "Log In" in the navigation bar will dynamically change to "Log Out" for easy account management.
- Upon successful login, additional options such as "Add Painting", "Upload Painting" and "My Favorites" become accessible, providing enhanced functionality and personalized features to the user.
- The navigation bar is fully responsive, collapsing into a hamburger menu for smaller screens to enhance user experience. Links receive a white shadow for visibility on dark backgrounds.
- Hovering over the links in the navigation bar triggers a visual effect where the font darkens and gets underlined, providing feedback to users as they interact with the links.

### Footer

- The footer section is a sticky bar that holds only a copyright message. "© 2023 Masterpiece By: J. Timlin"

### Home Page

**Hero Section**

![hero-section](https://res.cloudinary.com/masterpiece23/image/upload/v1699108450/features/home_page_w5mkqx.png)

- The homepage prominently features a call-to-action (CTA) section that invites users to engage with the site, ensuring they quickly grasp the site's purpose. When they click on painting details, they'll receive a message encouraging them to join the community with options to 'Join Us!' or 'Login!

### User Account Pages

**Sign Up, Log in and Log out**

![sign Up, log in and log out](https://res.cloudinary.com/masterpiece23/image/upload/v1699108729/features/signing_egqy9l.png)

- The implementation of Django AllAuth facilitated the establishment of essential user functionalities such as Sign Up, Log In, and Log Out.

**Messages**

![messages](https://res.cloudinary.com/masterpiece23/image/upload/v1699108822/features/message_mcajjq.png)

- To enhance user experience, success messages are incorporated to provide immediate feedback when users successfully log in or log out. These messages play a pivotal role in informing users about the status of their actions and contribute to seamless interaction with the website.
- The messages close themselves after a short delay of three seconds.

### Browse Gallery

![browse gallery page](https://res.cloudinary.com/masterpiece23/image/upload/v1699109592/features/gallery_qgthe8.png)

- This page showcases a collection of paintings, organized in descending order based on their creation date.
- To enhance the presentation, the painting cards are grouped into paginated sets, with a new set of cards appearing after every 8 paintings.
- Each individual painting card offers a thoughtful display of the painting's image, title, artist and likes.
- Moreover, users can effortlessly delve into the comprehensive details of any painting by simply clicking anywhere on the corresponding painting card.
- This user-friendly design ensures direct access to the dedicated detailed page, where users can explore the painting's details, techniques, and additional information.

### Painting Detail Page

![painting detail page](https://res.cloudinary.com/masterpiece23/image/upload/v1699109914/features/painting_details_zqv6ut.png)

- The first thing for users to see is, of course, a big image of the painting.
- Beneath the painting, you'll find all the relevant information, including the painting title, number of likes, artist, and, if available, a description provided by the author.
- When a user is logged in, they are able to share their thoughts about the painting. If not logged in, the page will display the message: "Want to share your thoughts? Join Us! or Login!"
- If a user is the author of the painting, they are able to see an editing button and a delete button.
- If a user is the author of a comment, they will see edit and delete comment buttons.

### Upload Painting Form

![upload painting page](https://res.cloudinary.com/masterpiece23/image/upload/v1699110484/features/upload_painting_yq1v2y.png)

- When a logged-in user can upload a painting image using the "Upload Painting" form.
- The form only accepts images and cannot be submitted without one.
- The user is also required to provide a title and select a category. Categories are predefined by administrators.
- The description is an optional field.
- For users attempting to add a painting without being logged in, they will be automatically redirected to the login page, preventing unauthorized access.
- Following the successful addition of a painting, users are promptly presented with a success message confirming the completion of the process.

### Update Painting Form

![painting update page](https://res.cloudinary.com/masterpiece23/image/upload/v1699111052/features/update_painting_bdtk3c.png)

- If the user is the author of a painting and logged in, they can edit it by clicking the edit button on the painting's detail page.
- When the user starts editing, all the fields are pre-filled with the original content to make the process smooth.
- If the user is not logged in and tries to update a painting, they will be redirected to the login page for secure access.
- If the user attempts to modify another user's painting by manipulating the URL, they will see a custom 403 error, ensuring content integrity.
- After successfully updating a painting, the user will receive a confirmation message.

### Delete Painting

![delete painting](https://res.cloudinary.com/masterpiece23/image/upload/v1699111528/features/delete_painting_x7taen.png)

- When a logged-in user is the author of a painting, the user has the option to delete the painting by clicking the dedicated delete button on the painting detail page.
- Clicking the delete button prompts the user with a confirmation dialog, giving them the choice to proceed with deleting the painting or to cancel the action.
- After successfully confirming the deletion, the user is informed of the success with a prompt message indicating that the painting has been successfully deleted. This feedback ensures the user is aware of the outcome of their action and maintains transparency in the process.

### My Paintings Page

![my paintings](https://res.cloudinary.com/masterpiece23/image/upload/v1699111713/features/my_paintings_qckjua.png)

- This page displays a comprehensive list of paintings exclusively authored by the logged-in user.
- To enhance presentation, the painting cards are grouped into pagination sets, with each set containing up to 8 paintings.
- Clicking anywhere within the painting card seamlessly directs the user to the dedicated detail page for that specific painting, ensuring quick access to comprehensive information.
- To maintain access integrity, the user attempting to reach this page without being logged in will be automatically redirected to the login page, ensuring the privacy of painting creators.

### My Favorites Page

![my favorite paintings](https://res.cloudinary.com/masterpiece23/image/upload/v1699111891/features/favorite_paintings_f33viv.png)

- This page displays a collection of paintings that the currently logged-in user has liked.
- The user can easily navigate to the detailed page of any desired painting by clicking anywhere within its respective painting card.
- To safeguard access integrity, the user attempting to reach this page without being logged in will be promptly redirected to the login page, ensuring the security of user data and preferences.

### Error Pages

Tailored error pages have been developed to offer users detailed insights into encountered errors and to provide guidance for returning to the main site.

These error pages are designed to enhance the user experience by delivering relevant information and navigation options in case unexpected issues arise during their interaction with the website.

![header](https://res.cloudinary.com/masterpiece23/image/upload/v1699112112/features/errors_erfbgg.png)

- 400 Bad Request - Masterpiece is unable to handle this request.
- 403 Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Not Found - The page you're looking for doesn't exist.
- 500 Internal Server Error - Masterpiece is currently unable to handle this request.

## Deployment - Heroku

The subsequent actions were carried out to facilitate the deployment of this page to Heroku from its corresponding GitHub repository:

### Create the Heroku App

- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labeled "New" in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next, select your region.
- Click on the Create App button.

### Attach the Postgres database

- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file

- In your workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py.
- Add the Cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url, and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR.
- Add Heroku to the ALLOWED_HOSTS list.

### Create files/directories

- Create requirements.txt file.
- Create three directories in the main directory; media, storage, and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi.

### Update Heroku Config Vars

Add the following Config Vars in Heroku:

- SECRET_KEY = yoursecretkey
- CLOUDINARY_URL = yourcloudinaryurl
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy

- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.

## Forking this repository

- Locate the repository at this link [Masterpiece](https://github.com/jindah/masterpiece).
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
- A copy of the repository is now created.

## Cloning this repository

To clone this repository follow the below steps:

1. Locate the repository at this link [Masterpiece](https://github.com/jindah/masterpiece).
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the preferred cloning option, and then copy the link provided.
3. Open **Terminal**.
4. In the Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier.
6. Type **'Enter'** to create the local clone.

## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks - Libraries - Programs Used

- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [PostgreSQL](https://www.postgresql.org/) was used as the database for this project.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud-based platform to deploy the site on.
- [AmIResponsive?](https://ui.dev/amiresponsive) - Used to verify the responsiveness of my website on different devices.
- [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and using lighthouse.
- [Font Awesome](https://fontawesome.com/) - Used for icons in the three-reasons section.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [CI Python Linter](https://pep8ci.herokuapp.com/) - used to validate all the Python code
- [Jshint](https://jshint.com/) - used to validate javascript
- [Colormind](http://colormind.io/) - Used to create color palette.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design
- [Summernote](https://summernote.org/): A WYSIWYG editor to allow users to edit their posts
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images
- [Bootstrap v5.3.2](https://getbootstrap.com/docs/5.3/getting-started/introduction/): CSS Framework for developing responsiveness and styling

## Credits

### Code

- I created my website partially with the help of [KaiLangen96 Disful Discoveries](https://github.com/KaiLangen96/dishful-discoveries/tree/main).

### Media and Content

- There are no static images on the website.
- The majority of the uploaded paintings are painted by my brother, Olli Timlin.
- A couple of them are from Pixabay.com, and the artists are credited

## Special Thanks

[Code Institude](https://codeinstitute.net/), for teaching me the languages needed to create this page.

[w3schools](https://www.w3schools.com/), for so many helpful pages and tools to support learning the languages.

[Django](https://docs.djangoproject.com/en/4.0/) and [Bootstrap v5.3.2](https://getbootstrap.com/docs/5.3/getting-started/introduction/) docs, for a lot of helpful information.

[Stack Overflow](https://stackoverflow.com/), for a lot of help, especially regarding bug fixes.

[Martina Terlevic](https://www.linkedin.com/in/martinaterlevic/), as my mentor.

[Kai Langen](https://www.linkedin.com/in/kai-langen/), my fellow student with the help on slack and standups.
