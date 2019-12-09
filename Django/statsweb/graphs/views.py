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
    if request.GET.get("present"):
        vars = request.GET
        json = False
    else:
        vars = request.POST
        json = True
        
    #initialize values
    p = vars.get('p')
    try: p = float(p)
    except: p = 5.0

    n = vars.get('n')
    try: n = int(n)
    except: n = 1000

    b = vars.get('b')
    try: b = float(b)
    except: b = 0.5

    t = vars.get('t')
    try: t = int(t)
    except: t = 50

    try: np.random.seed(int(vars['s']))
    except: pass

    values = [float(p),int(n),float(b),int(t)]

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
    
    if json:
        resp = {
            'hist_dataurl': hist,
            'dot_dataurl': dot,
            'p': p,
            'n': n,
            'b': b,
            't': t,
            'values': values,
            'averages': avg
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
