
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('testingwebcam.html')

@app.route('/cooke')
def west():
   return render_template('cooke.html')

app.route('/west')
def cooke():
   return render_template('west.html')

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80, debug=True)