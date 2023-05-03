# Stock Data Web Application

This web application fetches stock data for selected companies using the Alpha Vantage API and displays the information in a user-friendly format.

## Prerequisites

- Python 3.6 or higher
- Flask
- Requests

## Installation

1. Clone the repository or download the source code.

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
3.Activate the virtual environment:
On Windows:venv\Scripts\activate
On macOS and Linux:source venv/bin/activate
4. Install the required packages:
pip install -r requirements.txt



##  Running the Application
 1. Set the environment variables:
    On Windows: set FLASK_APP=app.py
    set FLASK_ENV=development
    On macOS and Linux: export FLASK_APP=app.p
    export FLASK_ENV=development
2. Run the Flask application:
   flask run
   The application will be accessible at http://127.0.0.1:5000.
   
   ####Usage
Open a web browser and navigate to http://127.0.0.1:5000.
The web application will display stock data for the selected companies, including the stock symbol, price, and change percentage.
Troubleshooting
If you encounter issues with the Alpha Vantage API, make sure you have a valid API key and that the API service is not down or experiencing issues.

If you run into other issues, check the Flask logs in your terminal or command prompt for detailed error messages and traceback information.

