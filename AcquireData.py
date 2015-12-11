# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:16:15 2015

@author: SumanthSwaminathan
"""

import pandas as pd
#import quandl
import requests
import json
import numpy as np
import matplotlib as plt
from bokeh.plotting import figure, show, output_file, vplot

data=requests.get(url='https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=ekga5KU471MGZ5SnFsTM')
#data=requests.get('https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=ekga5KU471MGZ5SnFsTM')
pf=pd.read_json(data.text)
seriesdata=pd.Series(pf.dataset_data) #note that the closing value is at entry 4 of the data node

L = len(seriesdata['data']) #total number of data points to plot

Plot_Array = np.zeros(L)

for n in range(L):
    Plot_Array[n]=seriesdata['data'][n][4]
    
plt.pyplot.plot(Plot_Array)





#loop over all data entries and append

newdata=json.loads(data.text)
#frame=pd.read_json(newdata)
#pd.series(data)

#q=pd.read_csv(data)

#from urllib2 import Request, urlopen
#import json
#from pandas.io.json import json_normalize
#
##path1 = '42.974049,-81.205203|42.974298,-81.195755'
#request=Request('https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=ekga5KU471MGZ5SnFsTM')
#response = urlopen(request)
#elevations = response.read()
#data = json.loads(elevations)
#json_normalize(data['results'])
pd.DataFrame(df)