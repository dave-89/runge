
# coding: utf-8

# In[1]:

import unicodedata
import os
import json
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import StringIO
from flask import Flask, make_response, request, render_template, current_app
from custom_integrator import Integrator


# In[2]:

app = Flask(__name__)

@app.route('/api.html',methods = ['GET'])
def api():
    return render_template('api.html')

@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/scripts.js',methods = ['GET'])
def scripts():
    return render_template('script.js')

@app.route('/plot', methods = ['POST'])
def plot():
    global a
    global b

    data = request.data

    dataDict = json.loads(data)

    x0 = (float)(str(dataDict['x0Val']))
    p0 = (float)(str(dataDict['p0Val']))
    t0 = (float)(str(dataDict['t0Val']))
    t1 = (float)(str(dataDict['t1Val']))
    dt = (float)(str(dataDict['dtVal']))
    function = str(dataDict['functionVal'])
    print function
    if (t1-t0)/dt > 5000.0:
        dt = (t1-t0)/5000.0
    integrator=Integrator(dt=dt,t0=t0,t1=t1,y0=[x0,p0],function=function)
    integrator.integrate()
    y=integrator.y
    t=integrator.t
    fig = Figure(facecolor='white')
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(t,y)
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue().encode("base64"))
    response.mimetype = 'image/png'
    return response


# In[3]:

if __name__ == '__main__':
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)


# In[ ]:



