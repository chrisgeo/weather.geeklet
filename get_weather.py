#!/usr/bin/python
import yql
output = "Weather @ %s\n\nSunrise: %s\nSunset: %s\n"

y = yql.Public()

query = 'select * from weather.forecast where location=%s'
zipcode = 95060
results = y.execute(query%zipcode)

for row in results.rows:
    print output % (row['location']['city'], row['astronomy']['sunrise'], row['astronomy']['sunset'])
