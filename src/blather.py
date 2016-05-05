import os
import csv
import random

dirname = os.path.dirname;
here = dirname(dirname(os.path.abspath(__file__)))

os.makedirs(os.path.join(here, "day3"), exist_ok=True)

"""
Let's create some terrible CSV data that needs to be parsed using a regular expression.

1. Names in a single field, need to be pulled apart into two or more
2. Lat/Long pairs in a horrible degrees/minutes format, to be converted into decimal
3. Date strings (forget that the date module exists)
4. Some kind of long text field containing a pattern, filterable (hashtags?)
5. Some kind of long text field to extract/transform (election positions)
6.
"""

def name():
  return "Thomas Wilburn"
  
def date():
  return "2010-01-12"
  
def latLong():
  return "47'12,-122'16"

def gibberish():
  return "This space intentionally left blank."
  
def seat():
  return "Seattle City Council District #5"

def currency():
  return "$12,000,000.00"

generator_lookup = {
  "name": name,
  "date": date,
  "latLong": latLong,
  "gibberish": gibberish,
  "seat": seat,
  "currency": currency
}

fields = list(generator_lookup.keys())

with open(os.path.join(here, "day3", "regexable.csv"), "w") as file:
  writer = csv.writer(file)
  writer.writerow(fields)
  for i in range(1, 1000):
    row = list(map(lambda field: generator_lookup[field](), fields))
    writer.writerow(row)