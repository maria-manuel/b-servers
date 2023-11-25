# REMINDER: Use print to debug, and save and test after every change!

print('api review now')

# Challenges 1-4 have to do with data information about newspapers in Oakland,
# courtesy of Library of Congress' Chronicling America API.  To make the
# activity easier to get started, the data has been downloaded for you already,
# so you don't have to make a request to get the data.
#
# If you are curious, this is the URL that was used:
# chroniclingamerica.loc.gov/search/titles/results/?terms=oakland&format=json

import json
data = json.load(open('oakland_newspapers.json'))


print('Challenge 1 -------------')
# Challenge 1:
# The top-most newspaper is the Oakland Tribune, from Oakland, California. Here
# is how we access the publisher field of this data. Can you write the code to
# print out the start and end year of the Oakland Tribune?

# Hint: To figure out the shape of the data, either open up the JSON file in
# your editor and inspect it directly, or use
#      print(data['items'][0])
# to see just the item at index 0

### MM ###
print(data['items'][0]['publisher'])
print(data['items'][0]['start_year'])
print(data['items'][0]['end_year'])

### MB ###
print(data['items'][0]['start_year'], data['items'][0]['end_year'])

print('Challenge 2 -------------')
# Challenge 2:
# - Data coming back from APIs can sometimes be complicated or even seemingly
# too complex.
# - Examine (without changing) the following if-statements. How come only the
# last two if-statements work as intended?

tribune = data['items'][0]
if tribune['county'] == 'Alameda':
    print('Oakland Tribune is in Alameda County (1)')

if tribune['county'] == ['Alameda']:
    print('Oakland Tribune is in Alameda County (2)')

if tribune['county'][0] == 'Alameda':
    print('Oakland Tribune is in Alameda County (3)')


print('Challenge 3 -------------')
# Challenge 3:
# - Inspect the JSON more closely. The purpose of this activity is to only deal
# with newspapers in Oakland, California. There's a problem: Not all the
# newspapers here are actually from this Oakland, instead some are from other
# cities and places in the United States called Oakland!
# - Can you write code that for-loops through the data, getting only the
# Oakland, California newspapers and puts them into a new list?
# Hint: One way is to check for the "County" field and get only the ones in
# Alameda County, which is the county that contains Oakland, CA.
# Hint: Maybe write in pseudocode first.

### psuedocode ###
# find oakland newspapers from Alameda County

oakland_ca_newspapers = []
newspapers = data['items']

for newspaper in newspapers:
    if newspaper['county'][0] == 'Alameda':
        print(newspaper['publisher'])
        print(newspaper['county'])
        oakland_ca_newspapers.append(newspaper)


print('Challenge 4 -------------')
# Challenge 4:
# Some of the Oakland newspapers have garbage data, with the end year listed as
# 9999. Can you write another for loop that filters out these newspapers?
valid_ca_newspapers = []



print('Challenge 5 -------------')
# Challenge 5:
# Only including the valid Oakland California newspapers, can you write code
# that determines the average (mean) length of time in years that the
# publications lasted?
# Hint: Maybe write in pseudocode first.






print('-------------')
# Bonus Challenge 1:
# To get more practice with list comprehension:
# - Rewrite Challenge 3-5 to use "list comprehension" and/or "generator
# expressions" instead of "normal" for-loops (if you didn't do this first)
# - If you aren't sure where to start, see previous activity solutions for
# examples of this alternative for-loop syntax, or look up examples online.
# - Rewritten, you can fit everything in a clean 5-10 lines of code

# Bonus Challenge 2:
# - This is a tricky one: Can you get the most popular year to start a
# newspaper in a few lines of code? Hint: use max(...., key=.....)

# Bonus Challenge 3:
# - Rewrite the above challenges using the built-in statistics module, e.g. get
#  mean (average), and median (middle-most). (Note: Mode might not work... Why?)
# - Refactor your code to be a function that can be called on any list
# - Add to this function a few more statistical methods, e.g. Standard Deviation





# ----------------------


# Advanced Bonus Challenge #1:

# Can you get OpenWeatherMapAPI working in Python?
# You can use (not abuse!) this shared API Key:
# 0de82b6b4ba5d843dac44bbee4d02543
# - Can you print out information such as the temperature of a city?
# - Can you print out the sunrise and sunset times in human-readable formats?
# (Hint: Use the built-in datetime)


# Advanced Bonus Challenge #2:
# If you have more time, take a look at:
#   https://github.com/public-apis/public-apis
# Which of those public APIs could you get working using requests?
# If you found any really cool ones, show off your results in Chat!

