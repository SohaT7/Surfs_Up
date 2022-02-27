# Import Flask dependency
from flask import Flask

# Create a new Flask instance
app = Flask(__name__)

# Define the starting point, and add a function called hello_world()
# in the specific route:
@app.route('/')
def hello_world():
    return 'Hello world'

    
