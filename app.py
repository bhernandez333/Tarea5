from flask import Flask, escape, request
app = Flask(__name__)

@app.route('/')
def Sumatoria():
    N1 = request.args.get("Numero1", 0, type=int)
    N2 = request.args.get("Numero2", 0, type=int )
#    return f'Hello,{escape(name)}!'
    return 'Resultado de la suma de ambos valores ==> {}'.format(N1 + N2)
