## Exercise Tracking app 
* Workout tracking app using Python and Google Sheets

### What does it do?
The Workout Tracking app will:
* Ask the user to provide the activity (workout) done for how long (e.g. Dancing for 2 hours)
* Send a POST request to the Nutritionix API along with user data (height, weight, age & gender)
* Receives the JSON data from Nutritionix containing data on calories burn
* Send a POST request to Sheety API to add the workout on the user's shared worksheet stored on their Google Drive

### How does it work?
On the command-line (or terminal), type the following:<br>
* python3 <b>exercise_tracker.py</b>

<b>NOTE:</b> It is assumed that the <b>Python 3 interpreter</b> had already been installed on your computer.
