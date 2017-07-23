import csv
import json

neighborhoods = {}

#Read CSV
with open('./data/ATL_2016.csv') as inputcsv:
    readCSV = csv.reader(inputcsv, delimiter=',')
    next(readCSV, None)
    for row in readCSV:
        crime = {}
        if row[3].split('/', 2)[2] == '2016':
            crime['occur_date'] = row[3]
            crime['street_address'] = row[10]
            #Calculate day_part
            crime['occur_time'] = row[4].split(':', 1)[0]
            #morning = ['02', '03', '04', '05', '06', '07', '08', '09']
            #day = ['10', '11', '12', '13', '14', '15', '16', '17']
            #evening = ['18', '19', '20', '21', '22', '23', '00', '01']
            #if occur_time in morning:
            #    crime['day_part'] = "Morning"
            #elif occur_time in day:
            #    crime['day_part'] = "Day"
            #elif occur_time in evening:
            #    crime['day_part'] = "Evening"
            crime['day'] = row[16]
            crime['type'] = row[18]
            crime['neighborhood'] = row[19]
            crime['longitude'] = row[21]
            crime['latitude'] = row[22]
            if row[19].lower() in neighborhoods:
                neighborhoods[row[19].lower()].append(crime)
            else:
                neighborhoods[row[19].lower()] = [crime]

#Write JSON
for neighborhood, neighborhoodData in neighborhoods.items():
    if '/' in neighborhood:
        neighborhoodName = neighborhood.lower().split('/')[0] + '_' + neighborhood.lower().split('/')[1]
    else:
        neighborhoodName = neighborhood.lower()
    with open('./data/' + neighborhoodName + '_data_2016.json', 'w') as outputjson:
        json.dump(neighborhoodData, outputjson)