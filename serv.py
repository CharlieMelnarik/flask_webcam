
from flask import Flask, render_template
import CsvReader
app = Flask(__name__)

@app.route('/')
def testingwebcam():
   keyword0 = CsvReader.LostTrail()[0]
   depth0 =  CsvReader.LostTrail()[1]
   date0 = CsvReader.LostTrail()[2]
   keyword1 = CsvReader.LostTrail()[3]
   depth1 = CsvReader.LostTrail()[4]
   date1 = CsvReader.LostTrail()[5]
   return render_template('home.html', variable1 = keyword0, variable2 = depth0, variable3 = date0, variable4 = keyword1,
                          variable5 = depth1, variable6 = date1)

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