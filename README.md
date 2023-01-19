# gender predicator

# algorithm
1 Import the pandas library and read a CSV file containing names and corresponding genders, creating a dataframe from the data.

2 Define a function gender_checker(name) that takes a name as an input.

3 Within the function, initialize a variable "gender" as "unknown".

4 Check the dataframe for the input name, if the name is found, assign the corresponding gender to the variable "gender" and return it.

5 If the name is not found in the dataframe, use a simple rule of thumb, check the last letter of the name, if it is 'a','e','i' or 'o', assign "female" to the variable "gender" and if it is anything else assign "male" to the variable "gender" and return it.

6 Define a function update_file(gender) that takes the gender as input.

7 Within the function, create a rule and a message for confirmation, and prompt the user to confirm if the gender is correct.

8 If the user confirms that the gender is correct, return "thank you".

9 If the user confirms that the gender is not correct, update the CSV file with the correct gender and return "file has been updated".

10 Prompt the user to enter their name and check if the input is valid, if it is not valid, prompt the user to enter a valid name.


11 Use a while loop to run the entire process again if the user wants to check another name.

12 Continue this process until the user chooses to exit the program.

# greet
Import the time and gender_checker modules
Take user input for the name
Define a function greet(name) that takes the name as input
Inside the function, call the gender_checker() function and assign the result to a variable gender
Assign the current time to a variable current_time
Define a list of greetings
Using time.sleep() method to wait for 1 sec before printing ">>> 3 second left" then again wait for 1 sec and print ">>> 2 second left" and again wait for 1 sec and print ">>> 1 second left"
Use an if-elif-else statement to check the current time and the gender, print the corresponding greeting from the list and the name with "sir" or "mam"
Call the greet() function with the name as the input
