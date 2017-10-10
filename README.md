This system serves as the portal for the Engineering department to dynamically manage a wide variety of information

===

Current instructions for starting from scratch:

git clone https://github.com/quantumleeps/engineering-tools.git
cd engineering-tools
virtualenv env
source env/bin/activate
pip install -r requirements.txt
cd engineering
python manage.py makemigrations projects
python manage.py migrate
python manage.py
python manage.py populate_history --auto
python manage.py runserver

To create a superuser to manage the sytem, run the following command: 
python manage.py createsuperuser

To run on a different port, you can run:
python manage.py runserver <serveraddress>:<port>

For example:
python manage.py runserver '127.0.0.1:8000'
will run the server on localhost on port 8000. To open the server up to outside computers on the network and host from the local machine's IP address, type the following command: 

python manage.py

====

to do:
get the things to sort the way you want them to
1. systems and tags should sort by some methodology
2. you should be able to click links on the list page to get sorting to work
3. make a detail page
4. read about ajax POSTing
5. would be really nice to be able to add photos on the spot in the plant. as the thing keeps screwing up, it can be documented by anyone looking at it with pictures getting descriptions later (via email even)
6. setup a basic RFQ for pumps after getting schema sorted out