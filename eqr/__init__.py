import flask
import sys, os
import pickle

import ResistorSolver
import makeForm
app = flask.Flask(__name__)
syspath = "/var/www/html/faithinnothing.me/eqr/eqr/"
@app.route('/', methods=['POST', 'GET'])# ,subdomain="resist")
def enter(name=None):
    if flask.request.method == 'GET':
        return flask.render_template("Entry.html")
    print("Dict: ",flask.request.form)
    #print(flask.request.form["Component Value"])
    try:
        qkeys=[]
        vkeys=[]
        for tup in flask.request.form.keys():
            #print("Key: ", tup)
            if "Quant" in tup:
                qkeys.append(tup)
            if "Comp" in tup:
                #print("Value: ",flask.request.form[tup])
                vkeys.append(tup)
        vkeys.sort()
        qkeys.sort()
        Quant = [int(float(flask.request.form[k])) for k in qkeys]
        Vals = [float(flask.request.form[i])     for i in vkeys]
        try:
            isCap = flask.request.form["isCap"]=="on"
        except:
            isCap = False
        #isCap=False
        #Quant = [int(float(flask.request.form[tup]))] + Quant
        #Vals=[float(flask.request.form[tup])] + Vals
        #print(isCap)
        #print("Quant: ", Quant)
        #print("Vals: ", Vals)
        tol = float(flask.request.form["Tolerance"])
        desRes = float(flask.request.form["Desired Equivalence"])
    except:
        return flask.render_template("Entry.html")
    with open(syspath+"dump.pkl", 'wb') as pk:
        pickle.dump({'Q':Quant, 'V':Vals, 'iC': isCap,
                    'T':tol, 'D':desRes},pk)
    return flask.redirect('/eqr/entered')
@app.route('/entered',methods=['GET'])# ,subdomain="resist")
def render(name=None):
    with open(syspath+"dump.pkl", "rb") as pk:
        pickleDict = pickle.load(pk)
        
    Quant   = pickleDict['Q']
    Vals    = pickleDict['V']
    isCap   = pickleDict['iC']
    desRes  = pickleDict['D']
    tol     = pickleDict['T']
    ans = ResistorSolver.resistorSolve(Vals, desRes, Quant, tol, isCap)
    #print("Ans = ", str(ans.decode('utf-8')))
    s = makeForm.makeForm(ans)
    #print(s)
    #return flask.render_template("form.html")
    pk = open(syspath+"dump.pkl",'wb')
    pk.close()
    return flask.render_template_string(s)
if __name__ == '__main__':
    
    app.run(host= '127.0.0.1', port=5000, debug=False)
