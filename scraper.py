# from selenium import webdriver
# import time
# import os.path
#
# # check if snow depth csv is there and removes it getting ready for the new one about to be scraped
# file_exists = os.path.exists("/Users/charliemelnarik/Desktop/testcams/testserv/Snow Depth.csv")
#
# if file_exists:
#     os.remove("/Users/charliemelnarik/Desktop/testcams/testserv/Snow Depth.csv")
#
#
# # Scrapes for the new csv to be used
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# # directory will need to be changed for pythonanywhere
# prefs = {"download.default_directory": "/Users/charliemelnarik/Desktop/testcams/testserv/"}
# options.add_experimental_option("prefs",prefs)
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.nrcs.usda.gov/wps/portal/wcc/home/quicklinks/imap#version=155.2&elements=&networks=!&states=!&counties=!&hucs=&minElevation=&maxElevation=&elementSelectType=all&activeOnly=true&activeForecastPointsOnly=false&hucLabels=false&hucIdLabels=false&hucParameterLabels=false&stationLabels=&overlays=&hucOverlays=&basinOpacity=100&basinNoDataOpacity=100&basemapOpacity=100&maskOpacity=0&mode=data&openSections=dataElement,parameter,date,basin,elements,location,networks&controlsOpen=true&popup=982:WY:SNTL&popupMulti=&popupBasin=&base=esriNgwm&displayType=station&basinType=6&dataElement=SNWD&depth=-8&parameter=OBS&frequency=DAILY&duration=I&customDuration=&dayPart=E&monthPart=E&forecastPubDay=1&forecastExceedance=50&seqColor=1&divColor=3&scaleType=D&scaleMin=&scaleMax=&referencePeriodType=POR&referenceBegin=1981&referenceEnd=2010&minimumYears=20&hucAssociations=true&relativeDate=-1&lat=44.708&lon=-103.624&zoom=7.5")
# time.sleep(5)
#
# datalink = driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div[2]/div/div/section/div[2]/div[5]/div[1]/div[6]/div/div[1]/div/div[1]/div[4]/h3/a/div')
# datalink.click()
# time.sleep(5)
# csvlink = driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/div/div[2]/div/div/section/div[2]/div[5]/div[1]/div[6]/div/div[1]/div/div[1]/div[4]/div/a[5]")
# csvlink.click()
# time.sleep(5)
# driver.quit()
#
# #renames csv to common name
# for file in os.listdir("/Users/charliemelnarik/Desktop/testcams/testserv/"):
#     if file.startswith("Snow"):
#         fresh_file_name = file
#         directory = "/Users/charliemelnarik/Desktop/testcams/testserv/" + fresh_file_name
#         print(directory)
#         os.rename(directory, "/Users/charliemelnarik/Desktop/testcams/testserv/Snow Depth.csv")