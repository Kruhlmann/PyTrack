# PyTrack
A startup script which tracks your IP address when you log in in case your computer is stolen

## Usage
There are a few things that needs to be set up before the script will track your IP address

### Obtaining a credentials file
To obtain a credentials file for the API go to the [Google API manager](https://console.developers.google.com/projectselector/apis/) and create a new project, add the Google Drive API to the application, generate a credentials file as the role *Project -> Editor*, and download the file as JSON. This file must be placed into the same folder as the source file.

### Setting up a google sheet
Create a google sheet and name it `PyTrack`. Once created share it with the email contained in the JSON file labeled as `client_email`.

### Placing the script in the startup folder
On MS Windows open a run window and type `shell:startup` to access your startup folder. In here place the [source file](PyTrack.py), the [batch file](PyTrack.bat) and your personal credentials file renamed to `client_credentials.json`.
