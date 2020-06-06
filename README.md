<h3>Introduction:<h3> <br>
Doctor chatbot is a conversational system which can be used in predicting heart diseases. The system behaves like a Cardiologist which asks consulting questions related to heart problems and tries to provide relavent solutions. This helps in saving a lot of time of the doctor as it gets the consultation before hand. The system also helps the patient to book appointment with Cardiologists depending on the situation.
Prediction of Heart Diseases is achieved using ML based Support Vector Machine Algorithm with heart dataset implemented in python. To create a localhost on your PC, ngrok is used which uses port 5000 of your PC & generates a public link for your PC which is required to communicate with Dialogflow Chatbot. 

Project Demonstration Video (Youtube):
https://youtu.be/p3QAyCCfmLI

Technology Stack used:
Dialogflow (Api.ai)
python
ngrok
SVM Algorithm
Heart Disease Dataset

Python Libraries used:
flask
pandas
sklearn
smtplib
pygmail
json
os

pip install requirements.txt

How to use the Project:
Go to Dialogflow Console & create a new project named "Doctor_Chatbot". Click on the gear icon, and import the Doctor_Chatbot.rar file (repository) from the options available. 
Download ngrok. Open command prompt from that folder, and execute ngrok http 5000. Copy the https link. Go back to Dialogflow project, click on fulfillment and paste the link in the URL section followed by /webhook. Click save button below.
Go to Integrations, click Web Demo and replace the url link to the Chatbot.html file, down below inside the <iframe> where the url is present.
Next, run connection.py file (repository)
Open a browser, and enter localhost:5000 to execute the interface.
Watch the Project video to check its working.
