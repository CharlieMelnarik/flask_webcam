
from flask import Flask, render_template
import CsvReader
import scraper
app = Flask(__name__)

@app.route('/')
def testingwebcam():
   LostTrail = CsvReader.LostTrail()
   return render_template('home.html', variable = LostTrail)

@app.route('/cooke')
def cooke():
   CookeCity = CsvReader.CookeCity()
   return render_template('cooke.html', variable = CookeCity)

@app.route('/west')
def west():
   WestYellostone = CsvReader.WestYellowstone()
   return render_template('west.html', variable = WestYellostone)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80, debug=True)

   # https://tinyurl.com/mtsnowinfo