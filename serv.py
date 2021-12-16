
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
   keyword0 = CsvReader.CookeCity()[0]
   depth0 =  CsvReader.CookeCity()[1]
   date0 = CsvReader.CookeCity()[2]
   keyword1 = CsvReader.CookeCity()[3]
   depth1 = CsvReader.CookeCity()[4]
   date1 = CsvReader.CookeCity()[5]
   keyword2 = CsvReader.CookeCity()[6]
   depth2 = CsvReader.CookeCity()[7]
   date2 = CsvReader.CookeCity()[8]
   return render_template('cooke.html', variable1 = keyword0, variable2 = depth0, variable3 = date0, variable4 = keyword1,
                          variable5 = depth1, variable6 = date1, variable7 = keyword2, variable8 = depth2, variable9 = date2)

@app.route('/west')
def west():
   keyword0 = CsvReader.CookeCity()[0]
   depth0 =  CsvReader.CookeCity()[1]
   date0 = CsvReader.CookeCity()[2]
   keyword1 = CsvReader.CookeCity()[3]
   depth1 = CsvReader.CookeCity()[4]
   date1 = CsvReader.CookeCity()[5]
   keyword2 = CsvReader.CookeCity()[6]
   depth2 = CsvReader.CookeCity()[7]
   date2 = CsvReader.CookeCity()[8]
   return render_template('west.html',  variable1 = keyword0, variable2 = depth0, variable3 = date0, variable4 = keyword1,
                          variable5 = depth1, variable6 = date1, variable7 = keyword2, variable8 = depth2, variable9 = date2)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80, debug=True)

   # https://tinyurl.com/mtsnowinfo