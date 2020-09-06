# **Zero Contact Shopping**
### Shop easily and safely, without the requirement of a cashier  
  
Link to [Presentation](https://docs.google.com/presentation/d/1FtLTmS5Rl8KSzhiQJZQFLYIg77T_SDIqFU6Do7vkLDE/edit?usp=sharing).  
  
Our project is a simple, yet intuitive system which deploys ML models to recognise faces of people.
What makes it stand out is, it requires only **ONE** image to train the model.  
  
Our project is in response to the global pandemic, recognising that social distancing is one of the most effective ways to combat the virus.
Here, we try to make shopping, one of the most common activities, more safe and easy.  
  
Usually, a person goes to a store, buys the stuff he/she wants, pays for it at the counter, and exits the store. 
The difference in our project is, with our model, a person can just walk into a store, and walk out, **without having to come in contact with a cashier**.  
  
  
### Assumptions/Requirements:  
-> The person has an E-Commerce account (eg. Amazon, GPay, etc.)  
-> The store has RFID readers that can scan item as they pass through them  
-> The store has **at least** one camera  
  
### How our model works (simplified):
Here, we simulate a very natural way of shopping  

-> A person walks into the store  
-> One of the cameras reocgnise the face, using ML models in the backend  
-> Once the person is recognised, any relevant information stored about the shopper (his account ballance, in our case), is retrieved  
-> When the person leaves the store, RFID scanners pick up information on all the products that have been purchased and generate a bill  
-> Once we process the amount, we automatically subtract it from the person's associated account, or flag a warning in case there is ome discrepancy  
-> As a bonus, we generate a CSV file that gives us all the info we have on whoever the model has recognised  
  
  
  
## Files and Info  

**_NOTE_ :** Requirements.txt has to be opened and installed manually. IT IS NOT AN AUTORUN FILE!!  
**_NOTE_ :** All the images of people you want to train on **MUST** be placed in _Training Folder_  
  
  
->  **Base.py** is the main executable. _You have to run this file only._ [_Base Tester.ipynb is the same, but for debugging, and easy UI applications]  
->  **PrebuiltDB.py** and **PrebuiltBill.py** are pre-built databases you can use to quickly simulate how the model will work.  
-> **DataStore.py** and **BillMaker.py** are helper files that let you make your own users, and generate their bills.  
-> **PeoplesList.csv** is a generated file that records the info of whoever the model has recognised, thereby simulating multitudes of scopes for this project.  
  
  
## Usage
You can opt for either pre-built or custom Users, and pre-built or custom bills. This gives you a total of 4 operational modes.  
There are plenty of on screen instructions (CONSOLE OUTPUTS) that will guide you along the way.  
A CSV file is generated at the end.  
  
  
# Contact Us
**Jaspreet Singh**  
jaspreet099@gmail.com  
https://github.com/J-Singh99/  
  
  
**Ashish Adhikari**  
ashish.adhikari727@gmail.com  
https://github.com/ashish807
