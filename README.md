# BigBasecampBoi
## Get basecamp project updates straight to your slack DMs!

NOTE: Under development, very basic functionality so far.

[Get DMs NOW](https://bigbasecampboi.herokuapp.com/)


## How to use
You will have to first set up a slack workflow, and provide a webhook to the app. To do this, follow these steps:
1. Click workflow builder as shown in the image below.
<img src="https://raw.githubusercontent.com/Hallicopter/BigBasecampBoi/master/Screenshot%202020-07-25%20at%209.53.26%20PM.png" width="50%">


2. Click on create flow from scratch.
<img src="https://raw.githubusercontent.com/Hallicopter/BigBasecampBoi/master/Screenshot%202020-07-25%20at%209.57.42%20PM.png" width="50%">

3. Select the webhook option.
<img src="https://raw.githubusercontent.com/Hallicopter/BigBasecampBoi/master/Screenshot%202020-07-25%20at%209.58.52%20PM.png" width="50%">

4. Give your flow a nice name.
<img src="https://raw.githubusercontent.com/Hallicopter/BigBasecampBoi/master/Screenshot%202020-07-25%20at%209.58.30%20PM.png" width="50%">

5. Create a variable with the name `kind` (This will tell what kind of action occured on our project.)
<img src="https://raw.githubusercontent.com/Hallicopter/BigBasecampBoi/master/Screenshot%202020-07-25%20at%209.59.57%20PM.png" width="50%">

6. Setup the workflow to send yourself a DM when the webhook URL is hit.
<img src="https://raw.githubusercontent.com/Hallicopter/BigBasecampBoi/master/Screenshot%202020-07-25%20at%2010.00.13%20PM.png" width="50%">

7. Copy the webhook url, and put it in my [app](https://bigbasecampboi.herokuapp.com/)
<img src="https://raw.githubusercontent.com/Hallicopter/BigBasecampBoi/master/Screenshot%202020-07-25%20at%2010.01.07%20PM.png" width="50%">

8. Fill details on the web app. 
Note, the format for any project is assumed to be 

`https://3.basecamp.com/<teamId>/projects/<projectId>`

If you get a success by the end of the process you should be good to go.
