from flask import Flask ,render_template
app=Flask(__name__)
@app.route('/greet2/<name>')
def greet2(name):
    return render_template("greet.html", name=name, count=3)
if __name__ == '__main__':
    app.run(debug=True)