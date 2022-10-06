from flask import Flask
app=Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f"{word * num}"

@app.route('/<path:path>')
def catch(path):
    return 'Sorry no response. Try Again!'


if __name__== "__main__":  # lines 10 and 11 are required on all server.py files and will not run without them.
    app.run(debug=True)

# For macs, remember to add port = 5001 << something like this check the platform