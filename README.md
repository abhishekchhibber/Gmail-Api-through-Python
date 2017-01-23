# Using Gmail API and Python to read mail messages 

I personally find Gmail API to be a bit confusing for beginners. The API’s wizard comes handy to create the project, get credentials, and authenticate them. However, the process that should be followed after that is not mentioned clearly.

Therefore, I have created a sample Python script that does the following:
* Go to Gmal inbox
* Find and read all the unread messages
* Extract details (Date, Sender, Subject, Snippet, Body) and export them to a .csv file / DB
* Mark the messages as Read - so that they are not read again 


[Link to the script](https://github.com/abhishekchhibber/Gmail-Api-through-Python/blob/master/gmail_read.py)


Before running this script, the user should get the authentication by following 
the [Gmail API link](https://developers.google.com/gmail/api/quickstart/python)
Also, client_secret.json should be saved in the same directory as this file


The script outputs a dictionary in the following format:

```
{	'Sender': '"email.com" <name@email.com>', 
	'Subject': 'Lorem ipsum dolor sit ametLorem ipsum dolor sit amet', 
	'Date': 'yyyy-mm-dd', 
	'Snippet': 'Lorem ipsum dolor sit amet'
	'Message_body': 'Lorem ipsum dolor sit amet'
  }
  ```



The dictionary can be exported as a .csv or into a databse

