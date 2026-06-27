from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, Krishna!"
@app.route('/about')
def about():
    return "This is the about page."
@app.route('/contact')
def contact():
    return '''Krishna Karthik
    krishna.karthik@example.com
    This is the contact page.'''
@app.route('/square/<int:num>')
def square_it(num):
    return f"{num} squared is {num * num}"
@app.route('/luffy/<string:favsportname>')
def luffy(favsportname):
    return f"my favsport_name is: {favsportname}"
if __name__ == '__main__':
    app.run(debug=True)