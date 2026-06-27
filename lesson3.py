from flask import Flask, request

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'stranger')
    return f"Hello, {name}!"

@app.route('/sum', methods=['POST'])
def sum():
    data=request.get_json()
    a= data['a']
    b=data['b']
    return f'sum is {a+b}'
app.run(debug=True)