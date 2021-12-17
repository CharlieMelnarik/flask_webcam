import csv
from datetime import date

# today = date.today()
# print(today)



def LostTrail():
    keyword = ["Saddle Mtn.", "Moose Creek"]
    with open("/home/Chuckdafaq/flask_webcam/Snow Depth.csv", newline="") as csvfile:
    # with open("Snow Depth.csv", newline="") as csvfile:

        snowreader = csv.DictReader(csvfile)
        for row in snowreader:
            if row["Name"] == keyword[0]:
                snowDepth = (row["Value_inches"])
                date = (row["Date_of_Data"])
            if row["Name"] == keyword[1]:
                snowDepth1 = (row["Value_inches"])
                date1 = (row["Date_of_Data"])
                date1 = date1[:16]


    return [keyword[0], snowDepth, date, keyword[1], snowDepth1, date1]

def WestYellowstone():
    keyword = ["West Yellowstone", "Madison Plateau", "Black Bear"]
    with open("/home/Chuckdafaq/flask_webcam/Snow Depth.csv", newline="") as csvfile:
    # with open("Snow Depth.csv", newline="") as csvfile:

        snowreader = csv.DictReader(csvfile)
        for row in snowreader:
            if row["Name"] == keyword[0]:
                snowDepth = (row["Value_inches"])
                date = (row["Date_of_Data"])
            if row["Name"] == keyword[1]:
                snowDepth1 = (row["Value_inches"])
                date1 = (row["Date_of_Data"])
            if row["Name"] == keyword[2]:
                snowDepth2 = (row["Value_inches"])
                date2 = (row["Date_of_Data"])

    return [keyword[0], snowDepth, date, keyword[1], snowDepth1, date1, keyword[2], snowDepth2, date2]

def CookeCity():
    keyword = ["Northeast Entrance", "Fisher Creek", "White Mill"]
    with open("/home/Chuckdafaq/flask_webcam/Snow Depth.csv", newline="") as csvfile:
    # with open("Snow Depth.csv", newline="") as csvfile:
        snowreader = csv.DictReader(csvfile)
        for row in snowreader:
            if row["Name"] == keyword[0]:
                snowDepth = (row["Value_inches"])
                date = (row["Date_of_Data"])
            if row["Name"] == keyword[1]:
                snowDepth1 = (row["Value_inches"])
                date1 = (row["Date_of_Data"])
            if row["Name"] == keyword[2]:
                snowDepth2 = (row["Value_inches"])
                date2 = (row["Date_of_Data"])

    return [keyword[0], snowDepth, date, keyword[1], snowDepth1, date1, keyword[2], snowDepth2, date2]


def tallestMountain():
    with  open("Snow Depth.csv", newline = '') as csvfile:
        heightreader = csv.DictReader(csvfile)
        tallest = 0
        number = 0
        for row in heightreader:
            tallestnew = int(row["Elevation_ft"])
            if tallestnew > tallest:
                tallest = tallestnew
                number = row
        print("The highest weather station is", number["Name"], "at", tallest, "ft in", number["State"])

def deepestSnow():
    # with open("Snow Depth.csv", newline = '') as csvfile:
    with open("/home/Chuckdafaq/flask_webcam/Snow Depth.csv", newline="") as csvfile:

        depthreader = csv.DictReader(csvfile)
        deepest = 0
        number = 0
        for row in depthreader:
            try:
                deepestnew = int(row["Value_inches"])
                if deepestnew > deepest:
                    if row["Name"] == "Powder Mountain":
                        pass
                    else:
                        deepest = deepestnew
                        number = row
            except:
                pass
        print("The deepest snow of any station currently is", deepest, "inches at", number["Name"], "in", number["State"],
              "at", number["Elevation_ft"],"ft")

def StationsByCounty(county):
    list = []
    # with open("Snow Depth.csv", newline='') as csvfile:
    with open("/home/Chuckdafaq/flask_webcam/Snow Depth.csv", newline="") as csvfile:

        sitereader = csv.DictReader(csvfile)
        for row in sitereader:
            if row["County"] == county:
                try:
                    if int(row["Value_inches"]) == None:
                        pass
                except:
                    pass
                else:
                    list.append((row["Name"], "depth:",row["Value_inches"],"inches, Elevation:", row["Elevation_ft"]))
    return list

def StationsByState(state):
    list = []
    # with open("Snow Depth.csv", newline='') as csvfile:
    with open("/home/Chuckdafaq/flask_webcam/Snow Depth.csv", newline="") as csvfile:

        sitereader = csv.DictReader(csvfile)
        for row in sitereader:
            if row["State"] == state:
                try:
                    if int(row["Value_inches"]) == None:
                        pass
                except:
                    pass
                else:
                    list.append((row["Name"], "depth:",row["Value_inches"],"inches, Elevation:", row["Elevation_ft"]))
        return list

def DeepestInState(state):
    # with open("Snow Depth.csv", newline='') as csvfile:
    with open("/home/Chuckdafaq/flask_webcam/Snow Depth.csv", newline="") as csvfile:

        sitereader = csv.DictReader(csvfile)
        deepest = 0
        number = 0
        for row in sitereader:
            if row["State"] == state:
                try:
                    if int(row["Value_inches"]) == None:
                        pass
                except:
                    pass
                else:
                    newDeepest = int(row["Value_inches"])
                    if newDeepest > deepest:
                        deepest = newDeepest
                        number = row
        deep = ("The deepest snow in %s is %i inches at %s" % (state, deepest, number["Name"]))
        return deep


# use for debugging and just messing around
# print(LostTrail())
# print(CookeCity())
# print(WestYellowstone())
# tallestMountain()
# deepestSnow()
# StationsByCounty("Gallatin")
# StationsByState("Montana")
# print(DeepestInState("Montana"))
