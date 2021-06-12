# UOCIS322 - Project 4 #
Brevet time calculator.

### Aurhor: Chengji Zheng			### E-mail: chengjiz@uoregon.edu

<br/><br/>
This project is the first one of the series that builds a brevets web APP. In this section, it builds a website that allows the user to choose a date time when the brevets begins (starts calculate the time). Then the backend calculates the starts time and close time between the controls (with distences given by the user) and then pass the calculated time back to the frontend.
<br/><br/>

#### The `acp_times.py` is a time calculator set on the backend to calculate the open time and close time that passed from the client side.
#### The `flask_brevets.py` get the specific data (here is brevet control distance, the total brevets distance and the start time) then passed them into the calculator `acp_times.py` to calculate each open time and close time and pass them back to the client side.


## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.