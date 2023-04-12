# silvacomCraft by Kelsey Kirkland
Hosted on: AWS EC2

http://ec2-18-222-255-189.us-east-2.compute.amazonaws.com/

http://18.222.255.189/

NOTE: on the hosted app, it is only the frontend the backend does not work
it has the error "Failed to load resource: net::ERR_CONNECTION_REFUSED"
I believe it is an error in the nginx config file and is not routing properly to the 'http://127.0.0.1:5000/api' where the backend is.
So for now it is only the frontend. To see the backend working clone it from git and run it on local

To run in local:
add weatherAPIKey to config.py

In terminal backend directory run:
    export FLASK_APP=main.py
    flask run
    
In a seperate terminal in SilvacomCraft directory run:
    npm start   or   ng serve
    
Go to http://localhost:4200/


