### Navigation Bar
#### Products page
- When clicked, the dropdown menu provides links to the cookie category and the brownie category. Result = Passed

#### All products page
- When clicking the all products link in the navigation bar, the dropdown menu proivides links to products sorted by price and category. Result = Passed

#### Favourites
- When clicked, the user is brought to the favourites page. Result = Passed

#### Bag page
- When clicked, the browser redirects to the bag page. Result = Passed 

#### Accounts - Logged in
- When clicked, a dropdown menu provides links to product management, profile and log out. Result = Passed 

#### Accounts - Logged out
- When clicked, a dropdown menu provides links to register and log in. Result = Passed  

#### Login/ Log out page	
- When clicked, the browser redirects to the login/ logout page. Result = Passed 

#### Profile page	
- When clicked, the browser redirects to the profile page. Result = Passed 

#### Product Management page	
- When clicked, the browser redirects to the product management page. Result = Passed 

#### Bag page	
- When clicking the bag icon, the browser redirects the user to the bag page. Result = Passed 

#### Search bar	
- When searching for a keyword, the results will show the products that contain the keyword in the product name. Result = Passed 
	
### Footer	
#### Newsletter	
- When the user enters their email in the newsletter form, it displays a success message when enetered. Result = Passed 
#### Facebook	
- When clicking the Facebook icon, it redirects to Facebook in a new tab. Result = Passed 
#### Twitter	
- When clicking the Twitter icon, it redirects to Twitter in a new tab. Result = Passed 
#### Instagram 	
- When clicking the Instagram icon, it redirects to Instagram in a new tab. Result = Passed 
	
### Product Detail Page	
#### Favourite Button	
- When clicked, the product has been added to the users favourites. A success message is also displayed. Result = Passed 

#### Edit Button	
- Only if the user is a superuser that the edit button is displayed. Result = Passed 

#### Delete Button	
- Only if the user is a superuser that the delete button is displayed. Result = Passed 

#### Add to Bag Button	
- When clicked, the add to bag button adds the product to the users bag. Result = Passed 

#### Back to Products Button	
- When clicked, the back to products button brings the user back to the products page. Result = Passed 
	
### Bag Page	
#### Remove from bag button	
- When clicked, the product is removed from the users bag. Result = Passed 

#### Quantity buttons	
- The plus and minus buttons add or lower the quantity of the item in the users bag. Result = Passed 
	
### Checkout Page	
#### Checkout form	
- Filling out the form with the correct validation processes the order. Filling out the form with incorrect validation shows error messages. Result = Passed 

#### Save Details 
- Checkout	Selecting the save delivery information checkbox, this saves/updates my profile details. Result = Passed 

#### Card Authentication	
- Used the Stripe test card details and purposely failed authentication to check for error messages. Result = Passed 
	
### Checkout Success	
#### Order History 	
- When clicking on an order number in the order history section, this takes the user to a past order confirmation summary page. Result = Passed 

#### Updating profile page	
- When updating the delivery information, it is auto filled on the checkout page. Result = Passed 
	
### Product Management Page	
#### Adding a product	
- When adding a new product, the product is added to the relevant category and is searchable via the search bar. Result = Passed 
	
### Favourites Page	
#### Removing an item from favourites	
- When the bin icon is clicked, the product is removed from the users favourites. Result = Passed 
	
### Contact Page	
#### Submitting the contact form	
- When the user submits the form, a success massage is displayed. Result = Passed 

#### Incorrect or missing fields	
- When the user inputs incorrect or missing fields in the form, the form doesn't submit. Result = Passed 

### Bugs
#### Fixed:
- I was getting an UnboundLocalError at /products/, to fix this I added categories = Noneto the all_products view.

- The bag quantity was only updating by €1 instead of the full amount of the product. After lloking into it I had a + instead of * in the contexts.

- Crispy forms not was working bootstrap 5/field.html. To fix this I installed cripsy-bootstrap 5, but have since changed to Bootstrap 4.

- Images were their original size and not matching. This was fixed using aspect ratio in css.

- The footer had two white blocks on either side in the order confirmation. To fix this all that was needed was en extra closing div.


#### Unfixed:
- The add to favourites button would not fill in when a user added the product to their favourites. To add a temporary fix this I added a toast to let the user know the product had been added to their favourites. I would like to go back and change it in the future to have the icon empty and then fill when added.

- Webhook resulting in a 500 internal error. During testing when the payment flow is interupted, the payment is going through but the order not being saved. I'm still not sure what the problem is as I've tried to log into Heroku through gitpod terminal but due to two step verification it won't allow me to log in to see what the exact error is, I've also deleted webhook secret codes, and rewrote the code all again and the problem is still persiting. The webhook returns status 200 when the payment flow is not interupted. 
