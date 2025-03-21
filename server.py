# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class and name
app = Flask("Application Development using Microservices and Serverless")

# Define a route for the root URL ('/')
@app.route("/")
def here():
    # Return a string as the response
    return "Here!"

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server with debugging enabled
    app.run(debug=True)
    # When no port is specified, the server starts at the default port 5000