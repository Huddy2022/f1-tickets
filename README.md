## F1 Tickets

The Live link can be found here - https://f1-tickets-e355687b93ca.herokuapp.com/

The F1 Tickets website offers an online ticket booking platform for Formula 1 racing events. It provides users with a seamless navigation experience, including sections like home, calendar, teams, drivers, contact, and user authentication for sign in/log in (and when logged in, there's an option to sign out and access a personalized reservations page in the navigation). The site is designed to cater to racing enthusiasts and individuals interested in attending Formula 1 races. Visitors can explore upcoming races and learn about the sport. To book tickets, users are encouraged to become members, granting them access to exclusive features. Membership benefits include a reservations page where users can review and manage their bookings, including the option to cancel or modify existing reservations. This ensures a convenient and tailored experience for F1 fans.

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

![Calendar add basket](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

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

![Contact](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Sign up / Login

* The sign up and login in tabs have been created using Django’s Allauth
* I have styled both the sign up, log in and sign out pages to link to the base.html and the style used with this F1 Tickets website.
* Authorisation is needed to add tickets - which helps the manager/super user to manage all orders & customers.
* When signed in any user will have a my orders tab in the navigation, so they can see what orders if any they have.
* I have put ACCOUNT_EMAIL_VERIFICATION = 'none' so that login and registration should work without errors regardless of whether you use an email address to sign in/up.

![Sign up](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

![Login](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Basket

* Content: This page is designed to display the selected tickets in the user's basket and provides options for editing or removing them.

* Table Display:

The table displays the following ticket information:
Race
Day (Ticket Type)
Ticket Type (Ticket Category)
Quantity
Total Price
Action (Edit and Remove options)

* Edit and Remove Options:

For each ticket item in the basket, users can choose to edit or remove it using the provided buttons.
Edit: Allows users to modify the ticket's details but redirecting to the edit tickets page.
Remove: Permanently removes the ticket from the basket & my orders.

* Add More Tickets Button:

Users can add more tickets to their basket by clicking the "Add More Tickets" button. It redirects them to the Calendar page to make additional selections.

* Purchase Button:

A "Buy Tickets" button is displayed at the bottom of the page, allowing users to proceed with the purchase.

* Checkout Process:

When users click the "Buy Tickets" button, the system creates a checkout session using Stripe for processing payments.
The user is redirected to the Stripe checkout page to complete the payment process.

* Data Handling:

Hidden input fields are used to store the ticket details in the form for submission.
The basket data is serialized and stored as a hidden JSON script for processing.

* CSRF Token:

A CSRF token is used to protect against cross-site request forgery.

* JavaScript Functionality:

JavaScript is used to interact with the Stripe API, create a checkout session, and handle the redirection to the Stripe checkout page.
This page allows users to review and manage the tickets they have selected for purchase before proceeding with the payment process.

![Basket](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Edit Basket

* Content: This page allows users to edit the details of a ticket item in their basket before finalizing the purchase.

* Original Ticket Information:

Displays the original details of the ticket item selected for editing, including:
Race
Ticket Type
Ticket Category
Quantity
Total Price

* Edit Order Section:

Users can modify the ticket item's details in this section.

* The following options are available for modification:
Race (Select from available races)
Ticket Type (Select from available days)
Ticket Category (Select from available ticket types)
Quantity (Select the desired quantity)

* Total Price:

The page dynamically calculates and displays the total price based on the selected options, quantity, and pricing table.
Confirm Edited Order:

Users can confirm their edited order by clicking the "Confirm Edited Order" button. This updates the ticket item's details in the basket & my orders page.

* Cancel:

Users can cancel the editing process and return to the Basket page by clicking the "Cancel" button.

* JavaScript Functionality:

JavaScript is used to dynamically update the total price based on the selected options and quantity.
Event listeners are added to each option (race, ticket type, ticket category, quantity) to trigger price updates.
This page provides a user-friendly interface for modifying ticket details, ensuring users have the flexibility to adjust their selections before proceeding with the purchase.

![Edit Basket](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## My orders

* Content: This page provides users with a summary of their past orders, displaying details about each order they have made.

* Order Table:

Displays a table with the following columns for each order:
Race Name: The name of the Formula 1 race.
Date: The date of the race.
Location: The location of the race.
Ticket Type: The type of ticket purchased (e.g., Friday, Saturday).
Ticket Category: The category of the ticket (e.g., General Admission, Grandstand Seat).
Quantity: The number of tickets purchased.
Total Price: The total cost of the order.
Payment Status: Indicates whether the order has been paid or is unpaid. (linked with stripe checkout)

* Order Details:

For each order in the table, it displays:
Race details, including name, date, and location.
Ticket details, including ticket type, ticket category, quantity, and total price.
Payment status, showing if the order has been paid or is still unpaid.

* No Orders Message:

If the user has no previous orders, a message is displayed indicating, "You have no orders yet."

* Dynamic Styling:

The payment status column dynamically changes text color to green for "Paid" and red for "Unpaid" orders.
This page serves as a record of the user's past orders, allowing them to review the details of each order, including payment status, for their reference.

![My Orders](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Admin User

* As I have created a super user to basically be the manager of this website/orders, I thought it would be easier to have an accessibility to the administration by having a admin user link in the navigation. It only allows staff members to log in on this particular area.

Race Model:

* Represents a Formula 1 race event.
* Attributes:
  * name: A character field with a maximum length of 100 characters to store the race name.
  * date: A DateField to store the date of the race.
  * location: A character field with a maximum length of 100 characters to store the location of the race.
  * The Race model is used to manage race information.

Order Model:

* Represents an order for Formula 1 tickets.
* Attributes:
  * user: A foreign key to the built-in Django User model, representing the user who placed the order.
  * race: A foreign key to the Race model, representing the race for which the tickets are ordered.
  * ticket_type: A character field with choices, allowing users to select the ticket type (e.g., Friday, Saturday).
  * ticket_category: A character field with choices, allowing users to select the ticket category (e.g., General Admission, Grandstand Seat).
  * quantity: An integer field to specify the quantity of tickets ordered.
  * order_date: A DateTimeField that automatically records the date and time when the order was created.
  * total_price: An integer field (in cents) to store the total price of the order.
  * paid: A boolean field to track the payment status of the order, with a default value of False.
  * The Order model is used to manage user orders for Formula 1 tickets.

These models help you manage race information and user orders efficiently in your application, allowing users to place orders for tickets with various options and track their payment status.

## Testing

| Test Case ID | Description                                | Test Steps                                              | Expected Results                                | Status  |
|--------------|--------------------------------------------|---------------------------------------------------------|--------------------------------------------------|---------|
| **Responsive Design Testing** |
| TC01         | Test website responsiveness on mobile      | Open the website on various mobile devices           | Website should adapt to different screen sizes  | Passed  |
| TC02         | Test website responsiveness on tablets     | Open the website on various tablet devices           | Website should adapt to different screen sizes  | Passed  |
| TC03         | Test website responsiveness on desktop     | Open the website on different desktop screen sizes   | Website should adapt to different screen sizes  | Passed  |
| **Functionality Testing** |
| TC04         | Test user registration functionality        | Register a new user account                           | User should be able to register successfully    | Passed  |
| TC05         | Test user login functionality              | Log in using a registered user account                | User should be able to log in successfully      | Passed  |
| TC06         | Test ticket booking functionality          | Select a race, day, ticket type, and quantity, then book  | User should see booking in basket     | Passed  |
| TC07         | Test ticket editing functionality           | Edit the quantity of tickets in the basket          | A order can be edited fully, and price recalculated  | Passed  |
| TC08         | Test ticket removal functionality           | Remove a ticket from the basket                      | Ticket should be removed, and price updated     | Passed  |
| TC09         | Test payment processing functionality      | Proceed to checkout and make a payment               | Payment should be processed successfully through stripe        | Passed  |
| TC10         | Test order history functionality            | View the user's order history                        | User should see a list of their previous orders  | Passed  |
| **Security Testing** |
| TC11         | Test user authentication security           | Attempt to access secure pages without logging in    | Unauthorized access should be denied             | Passed  |
| TC12         | Test input validation                      | Enter invalid data during registration/login        | System should display appropriate error messages | Passed  |
| **Usability Testing** |
| TC13         | Test navigation menu                       | Check if navigation menu items are clickable        | Menu items should lead to the corresponding pages | Passed  |
| TC14         | Test website load time                    | Measure the website's load time on different devices | Website should load within an acceptable time   | Passed  |
| **Cross-browser Testing** |
| TC15         | Test website on different browsers         | Open the website on various browsers (Chrome, Firefox, Safari, Edge) | Website should function correctly on all browsers | Passed  |
| **Accessibility Testing** |
| TC16         | Test website accessibility                 | Use accessibility tools (e.g., screen readers) to navigate the website | Website content should be accessible to all users | Passed  |
| **Performance Testing** |
| TC17         | Test website performance                   | Analyze the website's performance under load        | Website should handle expected user traffic      | Passed  |

## Validator Testing

* HTML
  
  * I can confirm no errors were returned when passing through the official w3c validator.

* CSS
  
  * I can confirm no errors were returned when passing through the official w3c validator.

* Python
  
  * I used the CI Python Linter to check my code and I can confirm all clear and no errors were found.

* Accessibility

  * I confirmed the colours and fonts are easy to read and I tested the colours I have chosen through the web aim contrast checker.
  * I used the lighthouse in dev tools to test my web page on a desktop and mobile devices.

## Bugs

* Issue with styling and responsiveness on certain pages. - Resolution: Reviewed and adjusted CSS styles and Bootstrap classes to ensure consistent styling and responsiveness across all pages.
* Validation issues with user inputs in forms. - Resolution: Added form validation logic in Django views and forms to ensure data integrity and security.
* Stripe payment integration not functioning correctly. - Resolution: Reviewed Stripe integration code, ensured correct API keys, and handled payment processing errors to make payments work seamlessly.
* User authentication issues, including login and registration problems. - Resolution: Implemented Django Allauth for user authentication, resolved configuration issues, and added custom templates to enhance the user registration and login process.
* Session-related problems with the shopping basket. - Resolution: Implemented session management in Django to correctly handle shopping basket data, including adding, removing, and updating items.
* Data inconsistency in the database leading to incorrect display of race details. - Resolution: Conducted a database audit, cleaned up inconsistent data, and improved database queries to ensure accurate race information display.
* JavaScript errors impacting the functionality of interactive features. - Resolution: Debugged JavaScript code, resolved syntax errors, and optimized scripts for smooth interaction.
* Deployment issues on the production server. - Resolution: Reviewed server configurations, updated environment variables, and resolved deployment-related errors to ensure the website runs smoothly in the production environment.
* Inconsistent behavior of the "My Orders" page. - Resolution: Refactored Django views and templates for the "My Orders" page to ensure consistent and accurate order display.
* Image upload and display problems. - Resolution: Corrected image paths, optimized image uploads, and resolved issues related to Cloudinary integration for proper image handling.

## Commented code left in

* I know you need to take out commented code you’re not using but there are two I left in as per the reasons below.
* I left in the code for the database SQLite as I needed this when I did my testing on the test_models.py and the test_views.py. I thought this might be needed later on.
* I also left in the password validation commented out code, as in the think I therefore blog it was also left in.

## Deployment

* created a Heroku app - F1-Tickets.
* created a new instance from elephantSQL.
* I created an env.py file to hide to the secret key, database URL and the Cloudinary URL, stripe secrect and public keys.
* Linked the env.py file to my settings.py.
* In the settings of the Heroku app I added the database_url, cloudinary_url, secret_key, stripe secrect key, stripe public key and PORT 8000.
* For deployment I set debug to False.
* Removed the DISABLE_COLLECTSTATIC 1
* Deployed branch to main in Heroku

The live link can be found here - <https://f1-tickets-e355687b93ca.herokuapp.com/>

## Credits

* The think before I blog project helped me with my initial models but mainly with the Allauth authentication.
* The hello Django project helped me with my test_views and my test_models.
* This youtube video helped me intergrate stripe with this django project <https://www.youtube.com/watch?v=722A27IoQnk>
* I got my driver and team stats from this website <https://www.4mula1stats.com/driver>
* The icons used were taken from font awesome <https://fontawesome.com>.
* I got my pictures from Pexels website.
