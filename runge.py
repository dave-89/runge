'''
Simple Runge-Kutta Integrator with a simple REST API for hosting the webpage

'''


import unicodedata
import os
import json
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import StringIO
from flask import Flask, make_response, request, render_template, current_app


def J(X,t):
    x1 = X[1]
    p1 = - a*X[1]+X[0]**2-b
    return np.array([x1,p1])



def runge4(X,t,dt):
    k1 = J(X,t)
    k2 = J(X+dt*k1/2.,t+dt/2.)
    k3 = J(X+dt*k2/2.,t+dt/2.)
    k4 = J(X+dt*k3,t+dt)
    return X+(k1+2.*k2+2.*k3+k4)*dt/6.




app = Flask(__name__)

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

    a = (float)(str(dataDict['aVal']))
    b = (float)(str(dataDict['bVal']))
    x0 = (float)(str(dataDict['x0Val']))
    p0 = (float)(str(dataDict['p0Val']))
    t0 = (float)(str(dataDict['t0Val']))
    t1 = (float)(str(dataDict['t1Val']))
    dt = (float)(str(dataDict['dtVal']))
    if (t1-t0)/dt > 5000.0: 
	dt = (t1-t0)/5000.0


    X0 = np.array([x0,p0])
    T = np.arange(t0,t1,dt)
    X = np.vstack([X0])
    for t in T[1:]:
        X = np.vstack([X,runge4(X[-1],t,dt)])


    x = np.array(map(lambda xi: xi[0], X))


    fig = Figure(facecolor='white')
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(T,x)
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue().encode("base64"))
    response.mimetype = 'image/png'
    return response




if __name__ == '__main__':
     app.debug = True
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)

