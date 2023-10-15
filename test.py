from flask import Flask,Response , request , flash , url_for,jsonify
from flask import Flask

app = Flask(__name__)

@app.route('/xyz', methods = ['GET', 'POST'])
def test():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))

@app.route('/abc/sudh', methods=['POST'])
def test1():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))

@app.route('/abc/sudh/xyz', methods=['POST'])

def test2():
    if(request.method == 'POST'):
        a = request.json['num3']
        b = request.json['num4']
        result = a + b
        return jsonify(str(result))

@app.route('/abc/sudh/kumar', methods=['POST'])
def test3():
    if(request.method == 'POST'):
        a = request.json['num5']
        b = request.json['num6']
        result = a + b
        return jsonify(str(result))


if __name__ == '__main__' :
    app.debug = True
    app.run()
