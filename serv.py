
from flask import Flask, render_template, request
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
   twentyfourHourChange = CsvReader.LostTrail()[6]
   twentyfourHourChange1 = CsvReader.LostTrail()[7]
   return render_template('home.html', variable1 = keyword0, variable2 = depth0, variable3 = date0, variable4 = keyword1,
                          variable5 = depth1, variable6 = date1, variable7 = twentyfourHourChange,
                          variable8 = twentyfourHourChange1)

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
   twentyfourHourChange = CsvReader.CookeCity()[9]
   twentyfourHourChange1 = CsvReader.CookeCity()[10]
   twentyfourHourChange2 = CsvReader.CookeCity()[11]


   return render_template('cooke.html', variable1 = keyword0, variable2 = depth0, variable3 = date0, variable4 = keyword1,
                          variable5 = depth1, variable6 = date1, variable7 = keyword2, variable8 = depth2, variable9 = date2,
                          variable10 = twentyfourHourChange, variable11 = twentyfourHourChange1, variable12 = twentyfourHourChange2)

@app.route('/west')
def west():
   keyword0 = CsvReader.WestYellowstone()[0]
   depth0 =  CsvReader.WestYellowstone()[1]
   date0 = CsvReader.WestYellowstone()[2]
   keyword1 = CsvReader.WestYellowstone()[3]
   depth1 = CsvReader.WestYellowstone()[4]
   date1 = CsvReader.WestYellowstone()[5]
   keyword2 = CsvReader.WestYellowstone()[6]
   depth2 = CsvReader.WestYellowstone()[7]
   date2 = CsvReader.WestYellowstone()[8]
   twentyfourHourChange = CsvReader.WestYellowstone()[9]
   twentyfourHourChange1 = CsvReader.WestYellowstone()[10]
   twentyfourHourChange2 = CsvReader.WestYellowstone()[11]
   return render_template('west.html',  variable1 = keyword0, variable2 = depth0, variable3 = date0, variable4 = keyword1,
                          variable5 = depth1, variable6 = date1, variable7 = keyword2, variable8 = depth2, variable9 = date2,
                          variable10 = twentyfourHourChange, variable11 = twentyfourHourChange1, variable12 = twentyfourHourChange2)

@app.route('/SearchAnySite', methods=['GET', 'POST'])
def search():
   if request.method == "POST":
      byState = request.form.get("state")
      byCounty = request.form.get("county")
      deepState = request.form.get("deep")
      if byState != "":
         state = CsvReader.StationsByState(byState)
         return render_template('SearchAnySite.html', variable = state)
      elif byCounty != "":
         county = CsvReader.StationsByCounty(byCounty)
         return render_template('SearchAnySite.html', variable = county)
      elif deepState != "":
         deepest = CsvReader.DeepestInState(deepState)
         return render_template("SearchAnySite.html", variable1 = deepest)

   return render_template('SearchAnySite.html')


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=80, debug=True)

   # https://tinyurl.com/mtsnowinfo