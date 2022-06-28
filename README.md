## UPDATE: Check out the WORKING DEMO of Doctor Chatbot Project: https://doctor-chatbot-project.herokuapp.com/. Please note that this version (v2) is re-built using React, Flask & deployed on Heroku!

About Doctor Chatbot
===
Doctor chatbot is a conversational system which can be used in predicting heart diseases. The system behaves like a Cardiologist which asks consulting questions related to heart problems and tries to provide relavent solutions. This helps in saving a lot of time of the doctor as it gets the consultation before hand. The system also helps the patient to book appointment with Cardiologists depending on the situation.
Prediction of Heart Diseases is achieved using ML based Support Vector Machine Algorithm with heart dataset implemented in python. To create a localhost on your PC, ngrok is used which uses port 5000 of your PC & generates a public link for your PC which is required to communicate with Dialogflow Chatbot. 
Note: The Appointment Scheduler is just a dummy module for this project.




#### [Project Demonstration Video](https://youtu.be/p3QAyCCfmLI/) (Youtube):

Technology Stack used:
---
* [Dialogflow (Api.ai)](https://dialogflow.com/)
* python
* [ngrok](https://ngrok.com/)
* SVM Algorithm
* [Heart Disease Dataset](https://www.kaggle.com/ronitf/heart-disease-uci/)
* HTML, CSS, JS

Python Libraries used:
---
* flask
* pandas
* sklearn
* smtplib
* json

from Project folder, run this command to install the libraries:
```
$ pip install -r requirements.txt
```

How to use the Project:
---
* Before we start, go to Project folder and edit `pygmail.py` file, filling `gmailaddress` and `gmailpassword` variables with a email and password, which are admin credentials for this project. We recommend creating & using a dummy Gmail for test purpose. Login, and go to [Less Secure App Access](https://myaccount.google.com/lesssecureapps) and turn it ON to allow mail permissions.
* Now, Go to [Dialogflow Console](https://dialogflow.cloud.google.com/#/login/) & create a new project named `Doctor_Chatbot`. Click on the gear icon (next to project name), and import the `Doctor_Chatbot.rar` file (from repository) from the **IMPORT FROM ZIP** option available. 
* Download [ngrok](https://ngrok.com/download/). Open command prompt from that folder in which it's present, and execute `ngrok http 5000` command. Copy the **https** link. Go back to Dialogflow project, click on *Fulfillment* tab and paste the link in the URL section followed by `/webhook`. Click SAVE button below.
* Go to *Integration* tab, click **Web Demo** and copy the url link. Replace this link in the `Chatbot.html` file, down below inside the <iframe> where the src url is present.
* Next, run `connection.py` file from the Project folder (repository). Open a browser, and enter `localhost:5000` or `127.0.0.1:5000` to execute the interface.
* Watch the [Project video](https://youtu.be/p3QAyCCfmLI/) to check its working.

### Project Screenshot
![Screenshot 1](https://user-images.githubusercontent.com/66524582/83961537-b524ff80-a8b1-11ea-86d3-bf5a58401795.png)
