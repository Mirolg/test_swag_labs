<h1>SWAG LABS - Test Cases</h1>

<h2>Checking the title of the page</h2>

<h3>TSLW-T1</h3>

<h3>Steps:</h3>

- Open Chrome browser. <br/>
- Go to the website https://www.saucedemo.com/<br />
- Check title of the website.<br />

<h3>Expected Behavior:</h3>
The page title is Swag Labs


<h2>Correct login to the account.</h2>

<h3>TSLW-T2</h3>

<h3>Test Data:</h3>
-Username: standard_user <br/>
-Password: secret_sauce<br />

<h3>Steps:</h3>
- Open Chrome browser.<br />
- Go to the website https://www.saucedemo.com/ <br/>
- Input a valid username.<br />
- Input a valid password.<br />
- Press the log in button.<br />
- Close Chrome browser.<br />

<h3>Expected Behavior:</h3>
User account is accessed.


<h2>Entering an correct username and incorrect password.</h2>

<h3>TSLW-T3</h3>

<h3>Test Data:</h3>
-Username: John <br />
-Password: John123 <br />

<h3>Steps:</h3>
- Open Chrome browser. <br />
- Go to the website https://www.saucedemo.com/ <br/>
- Input a invalid username. <br />
- Input a invalid password. <br />
- Press the log in button. <br />
- Close Chrome browser. <br />

<h3>Expected Behavior:</h3>
The appearance of information about an incorrect login or password.


<h2>Entering an correct username and incorrect password..</h2>

<h3>TSLW-T4</h3>

<h3>Test Data:</h3>
-Username: standard_user <br />
-Password: test123 <br />

<h3>Steps:</h3>
- Open Chrome browser. <br />
- Go to the website https://www.saucedemo.com/ <br />
- Input a invalid username. <br />
- Input a invalid password. <br />
- Press the log in button. <br />
- Close Chrome browser. <br />

<h3>Expected Behavior:</h3>
The appearance of information about an incorrect login or password.

<h2>Case sensitive when logging in.</h2>

<h3>TSLW-T5</h3>

<h3>Test Data:</h3>
-Username: Standard_user <br />
-Password: secret_sauce<br />

<h3>Steps:</h3>
- Open Chrome browser. <br />
- Go to the website https://www.saucedemo.com/ <br />
- Input a invalid username. <br />
- Input a valid password. <br />
- Press the log in button. <br />
- Close Chrome browser. <br />

<h3>Expected Behavior:</h3>
The appearance of information about an incorrect login or password.

<h2>Adding and removing items from the basket.</h2>

<h3>TSLW-T6</h3>

<h3>Test Data:</h3>
-Username: standard_user <br />
-Password: secret_sauce<br />

<h3>Steps:</h3>
- Open Chrome browser. <br />
- Go to the website https://www.saucedemo.com/ <br />
- Input a valid username. <br />
- Input a valid password. <br />
- Press the log in button. <br />
- Go to basket. <br />
- Checking if the basket is empty. <br />
- Pressing the continue shopping button. <br />
- Adding one item to the cart. <br />
- Go to basket. <br />
- Checking the number of items in the basket <br />
- Remove item from the basket. <br />
- Close Chrome browser. <br />

<h3>Expected Behavior:</h3>
After checking if the basket is empty and adding one item, the basket status should increase by one product, then after removing the product, the basket should be empty.

<h2>Sort data by lowest price.</h2>

<h3>TSLW-T7</h3>

<h3>Test Data:</h3>
-Username: Standard_user <br />
-Password: secret_sauce <br />

<h3>Steps:</h3>
- Open Chrome browser. <br />
- Go to the website https://www.saucedemo.com/ <br />
- Input a invalid username. <br />
- Input a valid password. <br />
- Press the log in button. <br />
- Choose a sort option "Price (low to high)"  <br />
- Close Chrome browser. <br />

<h3>Expected Behavior:</h3>
Sort items from cheapest to most expensive.

<h2>Sort data by highest price.</h2>

<h3>TSLW-T8</h3>

<h3>Test Data:</h3>
-Username: Standard_user <br />
-Password: secret_sauce <br />

<h3>Steps:</h3>
- Open Chrome browser. <br />
- Go to the website https://www.saucedemo.com/ <br />
- Input a invalid username. <br />
- Input a valid password. <br />
- Press the log in button. <br />
- Choose a sort option "Price (high to low)"  <br />
- Close Chrome browser. <br />

<h3>Expected Behavior:</h3>
Sort items from most expensive to cheapest

<h2>Sort items from the end of the alphabet.</h2>

<h3>TSLW-T8</h3>

<h3>Test Data:</h3>
-Username: Standard_user <br />
-Password: secret_sauce <br />

<h3>Steps:</h3>
- Open Chrome browser. <br />
- Go to the website https://www.saucedemo.com/ <br />
- Input a invalid username. <br />
- Input a valid password. <br />
- Press the log in button. <br />
- Choose a sort option "Name (Z to A)"  <br />
- Close Chrome browser. <br />

<h3>Expected Behavior:</h3>
Items should be sorted by names from the end of the alphabet

