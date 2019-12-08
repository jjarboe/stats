from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import sys
import io
from base64 import b64encode

from stats import *


'''
Description: Handles web requests
Params: request
Output: Values for p,n,b,t,s
'''
def index(request):
    #initialize values
    try: p = request.GET['p']
    except: p = 0.5

    try: n = request.GET['n']
    except: n = 1000

    try: b = request.GET['b']
    except: b = 5

    try: t = request.GET['t']
    except: t = 50

    try: np.random.seed(int(request.GET['s']))
    except: pass

    values = [float(p),int(n),int(b),int(t)]

    #Take sample
    avg = sample(values[0],values[1],values[3])

    #Create graphs
    hist, dot = qualgraph(avg, values[2])
    
    #Create statistics
   
    #Output graphs
    fhist = io.BytesIO()
    hist.figure.savefig(fhist)

    hist = (b'data:image/png;base64,'+b64encode(fhist.getvalue())).decode('utf-8')

    fdot = io.BytesIO()
    dot.savefig(fdot)

    dot = (b'data:image/png;base64,'+b64encode(fdot.getvalue())).decode('utf-8')
    
    if request.GET.get('json'):
        resp = {
            'p': p,
            'n': n,
            'b': b,
            't': t,
            'values': values,
            'averages': avg,
            'hist_dataurl': hist,
            'dot_dataurl': dot
        }
        return JsonResponse(resp)
    else:
        return HttpResponse('''
<p>p={}</p>
<p>n={}</p>
<p>b={}</p>
<p>t={}</p>
<p>values={}</p>
<p>averages={}</p>
<p><img src="{}"></img></p>
<p>dot=<img src="{}"></img></p>
'''.format(p, n, b, t, values, avg, hist, dot))
