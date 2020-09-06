# **Zero Contact Shopping**
### Shop easily and safely, without the requirement of a cashier

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
