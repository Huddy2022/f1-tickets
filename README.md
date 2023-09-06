## F1 Tickets

The Live link can be found here - 

The F1 Tickets website offers an online ticket booking platform for Formula 1 racing events. It provides users with a seamless navigation experience, including sections like home, calendar, teams, drivers, contact, and user authentication for sign in/log in (and when logged in, there's an option to sign out and access a personalized reservations page in the navigation). The site is designed to cater to racing enthusiasts and individuals interested in attending Formula 1 races. Visitors can explore upcoming races and learn about the sport. To book tickets, users are encouraged to become members, granting them access to exclusive features. Membership benefits include a reservations page where users can review and manage their bookings, including the option to cancel or modify existing reservations. This ensures a convenient and tailored experience for F1 fans.

![Responsive](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

### Tools

* Django
* Stripe API
* Cloudinary
* Django Allauth
* Django-The Message Framework
* Python
* Bootstrap
* HTML
* CSS
* JavaScript
* PostgreSQL (or the database of your choice)
* Django Crispy Forms (for form styling)
* Gunicorn (for deployment)
* Heroku (for hosting)
* Git and GitHub (for version control)
* Stripe for payment processing
* Pillow (for image handling)
* Cloudinary (for image and media management)
* Django Q object (for complex database queries)
* Django's timezone and datetime libraries

### Base

This is the hub for all my templates in the F1 Tickets website. In the head of the base.html has all the required documents for the meta tags, font awesome, bootstrap CSS, google fonts used and the link to my static folder. In the body is the navigation, and the footer which links on to some pages of the website apart from the admin area, basket and my orders.

* Navigation

The navigation menu is styled to be user-friendly and incorporates Bootstrap for a responsive and visually appealing design. It aims to facilitate easy navigation throughout the website.

The "Sign In" and "Sign Up" options provide users with their own access to their bookings, allowing them to view and manage their reservations. Additionally, these features enable the super user to identify and track customers' bookings.

The "Admin User" tab grants convenient access for the super user to log in and out of the website. This access helps in managing bookings, cancellations, tables, and customer-related tasks efficiently.
  
  * When you are not logged in, there are nine navigation tabs and the F1 Tickets header, which also acts as a link to the home index page.
  * Home
  * Calendar
  * Teams
  * Drivers
  * Contact
  * Sign Up
  * Sign In
  * Admin User
  * Basket (shows number of items in basket)
  
  * When logged in, there are ten navigation tabs.
  * Home
  * Calendar
  * Teams
  * Drivers
  * Contact
  * Welcome User (doesn't link to any page but references the user)
  * My Orders
  * Logout
  * Admin User
  * Basket (shows number of items in basket)

![Navigation](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

* Footer

  * The footer has three compartments to it, about, contact and follow us.
  * About - is another useful navigation tool for the user but only for the home page, calendar page, teams page & drivers page.
  * Contact - is for the user to contact the website if they have any queries (the contact tab on navigation links to this footer contact section).
Follow us - Allows the user to follow us on social media sites such as Facebook and Instagram.

![Footer](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

### Home

* The index.html serves as the home page for the F1 Tickets website, featuring two prominent sections: the home image and the about us section.

* Home Image

  * The main image of the website showcases an immersive view of an F1 race, capturing the excitement and energy of a Formula 1 event. This image effectively conveys the essence of the website, providing visitors with a visual introduction to the thrilling world of Formula 1 racing.

![Home](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

* About us

  * The "About Us" section provides a brief narrative about the origins and essence of F1 Tickets.
  * It includes upper and lower headings, "F1 Experience" and "Formula One World Championship," to encapsulate the essence of your mission.
  * This section aims to convey the passion and journey behind F1 Tickets.
  * It complements the narrative with an engaging image for a visually appealing experience.
  * The "About Us" section sets the stage for visitors to understand the thrilling world of Formula 1 and the excitement offered by F1 Tickets.

![About Us](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Calendar

* The "Calendar" page serves as a hub for all Formula 1 events and races.
* It provides an interactive and user-friendly calendar interface for easy navigation.
* Users can view upcoming races, their dates, and locations in a chronological order.
* Each race entry on the calendar is hover/clickable, allowing users to access detailed information about that specific event.
* The "Add Tickets" section provides users with the ability to purchase tickets for upcoming Formula 1 races directly from the calendar page.
* Users can select a race of interest from the calendar and click on it to access this section.
* Within this section, users can specify their ticket preferences, such as the type of ticket (e.g., Friday, Saturday, Sunday, or a multi-day pass) and the desired quantity.
* To complete the purchase, users can click a "Add Tickets" button, which redirects them to the basket.
* The "Add Tickets" section streamlines the ticket-buying experience, making it convenient for users to secure their spots at Formula 1 events directly from the calendar page.

![Calendar](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Teams

* The "Team" page provides comprehensive information about the various Formula 1 teams participating in the championship.
* Users can access this page from the main navigation menu.
* Each team is showcased with its name, and image.
* Clicking/hovering on a team's image additional details, including the teams notable achievements.
* Users can explore the different teams, gaining insights into their competitive records in Formula 1.
* The "Team" page serves as a valuable resource for Formula 1 enthusiasts who want to learn more about their favorite teams.

![Teams](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Drivers

* The "Drivers" page offers a detailed overview of the drivers competing in the Formula 1 championship.
* Users can easily navigate to this page from the main menu.
* Each driver is featured with a photo, name, and competitive records of their racing career.
* Clicking on a driver's profile provides career achievements, and current team affiliation.
* Users can explore the unique profiles of Formula 1 drivers, getting to know their backgrounds and accomplishments.
* The "Drivers" page serves as a comprehensive guide for fans who want to keep track of their favorite drivers throughout the season.

![Drivers](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Contact

* The contact navigation tab is linked to the contact details shown on the footer, so whenever a user selects this tab it will take them to the bottom of any page showing the contact details for the restaurant.

## Sign up / Login

* The sign up and login in tabs have been created using Django’s Allauth
* I have styled both the sign up, log in and sign out pages to link to the base.html and the style used with this F1 Tickets website.
* Authorisation is needed to add tickets - which helps the manager/super user to manage all orders & customers.
* When signed in any user will have a my orders tab in the navigation, so they can see what orders if any they have.
* I have put ACCOUNT_EMAIL_VERIFICATION = 'none' so that login and registration should work without errors regardless of whether you use an email address to sign in/up.

## My orders
