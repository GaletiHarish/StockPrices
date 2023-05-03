import requests
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def fetch_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/')
def home():
    return stocks()

@app.route('/stocks')
def stocks():
    api_key = '9U8FB39TC68EWQ9L'  
    companies = ['AAPL', 'AMZN', 'FB', 'GOOGL', 'NFLX']
    stock_data = []

    for symbol in companies:
        data = fetch_stock_data(symbol, api_key)
        print(data) 

        
        if 'Global Quote' in data and data['Global Quote']:
            stock_info = {
                'symbol': symbol,
                'price': data['Global Quote']['05. price'],
                'change_percent': data['Global Quote']['10. change percent']
            }
            stock_data.append(stock_info)
        else:
            print(f"Error fetching data for {symbol}")

    return render_template('stocks.html', stock_data=stock_data)

