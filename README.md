# Stock Data Web Application

This web application retrieves stock data for selected companies using the Alpha Vantage API and displays the information in a user-friendly format. To set up and run the application, you need Python 3.6 or higher, Flask, and the Requests library. The README file provided contains step-by-step instructions for installing the required packages, setting environment variables, and running the Flask application. Once the application is running, you can access it at http://127.0.0.1:5000 in your web browser to view the stock data. The README also includes troubleshooting tips and license information.
These are the screenshots of web application
![Screenshot (97)](https://user-images.githubusercontent.com/123728670/235984561-12d6060a-c442-4e63-93e6-f93b1e1a1633.png)
![Screenshot (98)](https://user-images.githubusercontent.com/123728670/235984605-758c736a-7864-4476-b7b6-292288880f5b.png)
![Screenshot (99)](https://user-images.githubusercontent.com/123728670/235984624-4989ef1c-9fcc-468b-bea7-c46b72c6d94f.png)
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



