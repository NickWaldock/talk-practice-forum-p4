[<< Back to main README](/README.md)

# Manual Application Testing

Below is the account of all manual testing that has taken place on the project.
<br>
<br>
<table>
  <tr>
    <th>What is being tested</th>
    <th>How</th>
    <th>Expected Response</th>
    <th>Outcome</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td>Site Responsiveness - Desktop Browsers</td>
    <td>Checked responsiveness of site by navigating using Dev Tools on Chrome, Safari, Firefox, & Edge</td>
    <td>The contact form checkbox renders differently in design between the browsers. In Safari, the check box renders on the left of the screen and not the center as it should. Otherwise, all elements appear as they should</td>
    <td>PASS</td>
    <td>Minor Bug noted</td>
  </tr>
  <tr>
    <td>Site Responsiveness - Tablet (iPad 7th Gen)</td>
    <td>Checked responsiveness of site by navigating the site on an iPad using Safari, Chrome, Firefox, & Edge apps</td>
    <td>In the Safari, Firefox, Chrome, and Edge apps, the check box renders on the left of the screen and not the center as it should. Otherwise the site renders as expected on all apps</td>
    <td>PASS</td>
    <td>Minor Bug noted</td>
  </tr>
  <tr>
    <td>Site Responsiveness - Mobile</td>
    <td>Checked responsiveness of site by navigating with iPhone 11 and Google Pixel</td>
    <td>Site renders as expected</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Site Responsiveness - Sibebar/Footer</td>
    <td>Checking the position of the Sidebar/Footer on smaller screens</td>
    <td>On >Medium size screens the Sibebar is visiable on the right-hand side of the screen. On smaller devices it moves to the bottom</td>
    <td>PASS</td>
    <td>Future development: A fixed footer or post pagination solution will be needed for mobiles as the number of posts grows, in order to stop it being only visible with excess scrolling</td>
  </tr>
  <tr>
    <td>Internal Links: Landing Page -> Login Button</td>
    <td>Navigate to the login page</td>
    <td>On click with login button the login page is rendered</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Landing Page -> Register Button</td>
    <td>Navigate to the register page</td>
    <td>On click with login button the register page is rendered</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Login Page -> Login Button</td>
    <td>Login with existing username and password</td>
    <td>With valid credentials inputted -> On click with login button user is validated and is taken to the list of forum posts page and has general access to pages.  User's name is displayed on the right-hand side of the nav bar on >medium screens.If login credentials are not valid, page is reset and an "incorrect username/password" message is displayed to the user</td>
    <td>PASS</td>
    <td>A message appears for 2s to confirm successful login</td>
  </tr>
  <tr>
    <td>Internal Links: Login -> Register Link</td>
    <td>Clicking in-text link</td>
    <td>On click the user is taken to the register page</td>
    <td>PASS</td>
    <td></td>
  </tr>
    <tr>
      <td>Internal Links: Register -> Login Link</td>
      <td>Clicking in-text link</td>
      <td>On click the user is taken to the login page</td>
      <td>PASS</td>
      <td></td>
    </tr>
  <tr>
    <td>Internal Links: Sidebar/Footer Contact Link</td>
    <td>Clicking in-text link</td>
    <td>On click the user is taken to the contact form page</td>
    <td>PASS</td>
    <td>Links are available on all pages, except the landing page</td>
  </tr>
  <tr>
    <td>Internal Links: List View -> Edit Post</td>
    <td>Button click</td>
    <td> Clicking the button navigates to the Update Post page</td>
    <td>PASS</td>
    <td>Edit Post button is only be visible on posts that the logged-in user has authored</td>
  </tr>
  <tr>
    <td>Internal Links: Navbar -> Categories Dropdown</td>
    <td>Click nav link</td>
    <td>On the Home List, Category List pages the dropdown displays links to all available post categories</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Navbar -> Categories</td>
    <td>Click nav link</td>
    <td>On all pages execpt the Home List and Article Detail, the dropdown is replaced by a standard link to navigate to the Category List page</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Navbar -> Add Category</td>
    <td>Click nav link</td>
    <td> The link navigates to the Add Category page</td>
    <td>PASS</td>
    <td>Nav link is only available if the logged in user is assigned as staff/admin, otherwise link is not displayed</td>
  </tr>
  <tr>
    <td>Internal Links: Navbar -> Add Post</td>
    <td>Click nav link</td>
    <td>The link navigates to the Add Post page</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Navbar -> Logout</td>
    <td>Click nav link</td>
    <td>The link navigates to the Logout page</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Navbar -> Contact Us</td>
    <td>Click nav link</td>
    <td>The link navigates to the Contact Us Form page</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: List View -> Post Title Click</td>
    <td>Post card click</td>
    <td>Clicking on a post card title navigates to the detail view of that article</td>
    <td>PASS</td>
    <td>Only clicking the title navigates through to the post, not the card background (future development)</td>
  </tr>
  <tr>
    <td>Internal Links: List View -> Post Category Click</td>
    <td>Post category click</td>
    <td>Clicking on the post card's category navigates to the Category Post List page related to that category</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Article Detail View -> Category</td>
    <td>Click category name in text link</td>
    <td>Clicking the category name sends users to the Category Post List page related to that category</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Article Detail View -> Like Button</td>
    <td>Click Like button</td>
    <td>The link refreshes the page with the new like displayed at the top of the article. The like button turns red and displays "unlike". Clicking again refreshes the page, removes the 'like' and returns the button to the standard 'Like' format</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Article Detail View -> Edit Button</td>
    <td>Click Edit button</td>
    <td>The edit button is only visible if the user is the post author. Clicking the button navigates to the Update Post page</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Article Detail View -> Return Button</td>
    <td>Click Return button</td>
    <td>Clicking the return button navigates the user to the main Post List View page</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Article Detail View -> Comment Button</td>
    <td>Click Add Comment button</td>
    <td>Clciking the add comment button submits the above inputted text comment and renders it above the form input in the comments section. If comment text field is empty, notice is displayed that content is required</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Categories List Page -> Category</td>
    <td>Click Category</td>
    <td>Clicking on a category card navigates to the Category Post List View related to that category</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Categories Post List Page -> Post Title</td>
    <td>Click Post</td>
    <td>Clicking on a post card's title navigates to the detail view of that article</td>
    <td>PASS</td>
    <td>Only clicking the title navigates through to the post, not the card background (future development)</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Categories Post List Page -> Edit Button</td>
    <td>Click Edit button</td>
    <td>Clicking on a post card's Edit button navigates to the update page for that article</td>
    <td>PASS</td>
    <td>Only available if the user is the author of the post</td>
  </tr>
  <tr>
    <td>Internal Links: Update Post -> Update Button</td>
    <td>Click Update Button</td>
    <td>Clicking button submits the updated form and returns the user to the Home Post List View</td>
    <td>PASS</td>
    <td>Page only available if user is author</td>
  </tr>
  <tr>
    <td>Internal Links: Update Post -> Delete Button</td>
    <td>Click Delete Button</td>
    <td>Clicking button directs user to the Delete Post page</td>
    <td>PASS</td>
    <td>Page only available if user is author</td>
  </tr>
  <tr>
    <td>Internal Links: Delete Page -> Delete Button</td>
    <td>Click Delete Button</td>
    <td>Clicking button deletes the relevant post and returns the user to the Home Post List View</td>
    <td>PASS</td>
    <td>Page only available if user is author. Message is displayed to confirm deletion</td>
  </tr>
  <tr>
    <td>Internal Links: Delete Page -> Return Button</td>
    <td>Click Return Button</td>
    <td>Clicking button returns the user to the Home Post List View</td>
    <td>PASS</td>
    <td>Page only available if user is author</td>
  </tr>
  <tr>
    <td>Internal Links: Logout Page -> Logout Button</td>
    <td>Click button</td>
    <td>Clicking the button redirects the user to the Landing Page</td>
    <td>PASS</td>
    <td>A message is displayed for 2secs to confirm the user has logged out</td>
  </tr>
  <tr>
    <td>Internal Links: Logout Page -> Read More Button</td>
    <td>Click button</td>
    <td>Clicking the button returns the user to the Home Post List View page</td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>Internal Links: Register Page -> Create Account Button</td>
    <td>Click button</td>
    <td>Clicking the button generates the new user account and redirects the user to the Home Post List View page</td>
    <td>PASS</td>
    <td>A message is displayed for 2 secs to confirm the user has logged in</td>
  </tr>
  <tr>
    <td>Internal Links: Add Post Page -> Publish Button</td>
    <td>Click button</td>
    <td>Clicking the button submits the form and redirects the user to the Home Post List View</td>
    <td>PASS</td>
    <td>Form must be valid</td>
  </tr>


  <tr>
    <td>CRUD - Add Post</td>
    <td>Using the frontend Add Post page to submit a new post</td>
    <td>Adding content to the form and submitting creates a new post instance in the database. The post is visible on all relvant pages</td>
    <td>PASS</td>
    <td>Form must be valid. A "Post Created!" message is displayed for 2sec to confirm the post has been created</td>
  </tr>
  <tr>
    <td>CRUD - Update Post</td>
    <td>Using the frontend Update Post page to update an existing post</td>
    <td>The page automatically renders the post content. Clicking the update button updates the post instance in the database</td>
    <td>PASS</td>
    <td>Form must be valid. A "Post Updated!" message is displayed for 2sec to confirm the post has been updated</td>
  </tr>
  <tr>
    <td>CRUD - Delete Post</td>
    <td>Using the frontend Update Post page delete and existing post</td>
    <td>The page automatically renders the post content. Clicking the delete button directs the user to a delete confirmation page. Clicking delete permantly removes the instance of the post in the databse</td>
    <td>PASS</td>
    <td>A "Post Deleted!" message is displayed for 2sec to confirm the post has been deleted</td>
  </tr>
  <tr>
    <td>CRUD - View Posts</td>
    <td>Navigating the various Post List and Category List Views</td>
    <td>The Home Post List View, Categories View, and Categories Post List View all display the post instances currently held in the databases. Any new instances, updates, or deletions are reflected immediatly in the list views  </td>
    <td>PASS</td>
    <td></td>
  </tr>
  <tr>
    <td>CRUD - Add Category</td>
    <td>Submitting a new category on the add category page</td>
    <td>On submission of a valid text-input the new cateogry is available in the navbar dropdown Categories menu, also renders in the Category List View as an active link to display any related posts</td>
    <td>PASS</td>
    <td>Only available to admin/staff users. A "Category Created!" message is displayed for 2sec to the user</td>
  </tr>








  <tr>
    <td>External Links: Sidebar/Footer Socials</td>
    <td>Clickable icons to navigate to relevant social page</td>
    <td>Icons navigate to the relevant social media page. Pages open in a new tab</td>
    <td>PASS</td>
    <td>Icon links are available on every page except the landing page</td>
  </tr>
  <tr>
    <td>External Links: Sidebar/Footer Creator Link</td>
    <td>Site creator name links to professional website</td>
    <td>Text link navigates to relevnat site. Opens in a new tab</td>
    <td>PASS</td>
    <td>Link is available on every page except the landing page</td>
  </tr>








  <tr>
    <td>Django Messages</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Create Post</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  
  
</table>

[<< Back to README](/README.md)