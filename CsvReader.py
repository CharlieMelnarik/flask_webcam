import csv
# import selenium
from datetime import date

today = date.today()
print(today)



def LostTrail():
    keyword = ["Saddle Mtn.", "Moose Creek"]
    with open("Snow Depth, December 5, 2021, end of day.csv", newline="") as csvfile:
        snowreader = csv.DictReader(csvfile)
        for row in snowreader:
            if row["Name"] == keyword[0]:
                snowDepth = (row["Value_inches"])
                date = (row["Date_of_Data"])
            if row["Name"] == keyword[1]:
                snowDepth1 = (row["Value_inches"])
                date1 = (row["Date_of_Data"])


    answer = ('%s depth: %s inches as of %s:\n%s depth: %s inches as of %s'  %
              (keyword[0],snowDepth,date,keyword[1],snowDepth1,date1))
    return answer

def WestYellowstone():
    keyword = ["West Yellowstone", "Madison Plateau"]
    with open("Snow Depth, December 5, 2021, end of day.csv", newline="") as csvfile:
        snowreader = csv.DictReader(csvfile)
        for row in snowreader:
            if row["Name"] == keyword[0]:
                snowDepth = (row["Value_inches"])
                date = (row["Date_of_Data"])
            if row["Name"] == keyword[1]:
                snowDepth1 = (row["Value_inches"])
                date1 = (row["Date_of_Data"])

    answer = ('%s depth: %s inches as of %s:\n%s depth: %s inches as of %s'  %
              (keyword[0],snowDepth,date,keyword[1],snowDepth1,date1))
    return answer

def CookeCity():
    keyword = ["Northeast Entrance", "White Mill"]
    with open("Snow Depth, December 5, 2021, end of day.csv", newline="") as csvfile:
        snowreader = csv.DictReader(csvfile)
        for row in snowreader:
            if row["Name"] == keyword[0]:
                snowDepth = (row["Value_inches"])
                date = (row["Date_of_Data"])
            if row["Name"] == keyword[1]:
                snowDepth1 = (row["Value_inches"])
                date1 = (row["Date_of_Data"])

    answer = ('%s depth: %s inches as of %s:\n%s depth: %s inches as of %s'  %
              (keyword[0],snowDepth,date,keyword[1],snowDepth1,date1))
    return answer

# use for debugging
# print(LostTrail())