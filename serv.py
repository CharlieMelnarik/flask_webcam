
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('testingwebcam.html')

@app.route('/')
def west():
   return render_template('cooke.html')

app.route('/')
def cooke():
   return render_template('west.html')

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80, debug=True)