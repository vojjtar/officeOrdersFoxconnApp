
# officeOrdersFoxconnApp

## Python version used: 3.9.5

### Setting up the application
- Export an environment variable that tells Flask where to find the application \
    Bash: `$ export FLASK_APP=run.py` \
    CMD: `> set FLASK_APP=run.py`

- For testing the app turn the flask environment to development \
    Bash: `$ export FLASK_ENV=development` \
    CMD: `> set FLASK_ENV=development`

- To install requirements \
    Bash: `$ pip3 install -r requirements.txt` \
    CMD: `> pip install -r requirements.txt`

- Create .env file in the root directory following the .env.template file. Create your own secret key.

- Run the app with the following command \
    `flask run` or `python run.py`

- The main page is on `localhost:5000/orderPage` by default

- To get information about an order go to: `localhost:5000/getOrderInfo/{id_of_needed_order}`
- To set an order as processed go to: `localhost:5000/setOrderAsProcessed/{id_of_needed_order}`
    
