from flask import Flask, render_template, request, redirect
import pandas as pd
import requests
#import json
import numpy as np
#import matplotlib as plt
from bokeh.plotting import figure, show, output_file, Plot
#import bokeh

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
    author = "Sumanth"
    Name = "Michael"
    return render_template('index.html')
    
@app.route('/StockData', methods = ['POST'])
def StockData():
    stock = request.form['Ticker Symbol']
    Ptype = int(request.form['Price'])
    
    #Create Dict for Price Type
#    Pdict={}
#    Pdict["Open"]=1
#    Pdict["High"]=2
#    Pdict["Low"]=3
#    Pdict["Close"]=4
    
    #Grab Data from Quandl API
    data=requests.get(url='https://www.quandl.com/api/v3/datasets/WIKI/' + stock + '/data.json?start_date=2012-11-01?api_key=ekga5KU471MGZ5SnFsTM')
    pf=pd.read_json(data.text)
    seriesdata=pd.Series(pf.dataset_data) #note that the closing value is at entry 4 of the data node
    
    #Initialize Arrays & Parameters
    L = len(seriesdata['data']) #total number of data points to plot
    Price = np.zeros(L)
    Pdate=[]
    
    for n in range(L):
        Price[n]=seriesdata['data'][L-n-1][Ptype]
        Pdate.append(seriesdata['data'][L-n-1][0])
#    
#    print(L)
#    print(Ptype)
#    print(Price)
    
    # Create plot of stock price
    Pdate=np.linspace(0,L-1,L)
    output_file("stocks.html", title="Stock Price Example")
    p2 = figure(x_axis_type="datetime")
    
    #p2.circle(Pdate, Price, size=4, color='darkgrey', alpha=0.2, legend='close')
    p2.line(Pdate, Price, color='navy', legend='avg')
    
    p2.title = "Stock Price History"
    p2.grid.grid_line_alpha=0
    p2.xaxis.axis_label = 'Day'
    p2.yaxis.axis_label = 'Price'
    p2.ygrid.band_fill_color="olive"
    p2.ygrid.band_fill_alpha = 0.1
    
    show(p2)  # open a browser
    
    return redirect('/')

if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run(port=33507)
    

