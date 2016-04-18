import os
import math
from random import random
from faker import Faker
faker = Faker()

"""
Generates 'receipts' in the format of:

#123    Name Here   352-52-4213
14 Somewhere St.
Seattle, WA 98107

$1304.23    Acct: 4422151583784700

Receipts that we are interested in will come from a single mailing address, namely 221 Baker St.

To make things more interesting, the word VOID is randomly placed into the file, often overlapping with the address.

"""
dirname = os.path.dirname
here = dirname(dirname(os.path.abspath(__file__)))

os.makedirs(os.path.join(here, "day1"), exist_ok=True)

for i in range(1, 1000):
    name = faker.name()
    ssn = faker.ssn()
    if random() > .95:
        address = "221 Baker St."
    else:
        address = faker.street_address()
    zipcode = faker.zipcode()
    amount = "{:.2f}".format(random() * 1000)
    account = faker.credit_card_number()

    #output into a multiline string
    receipt = """
#{i}    {name}    {ssn}
{address}
Seattle, WA {zipcode}

${amount}    Acct: {account}
"""
    output = receipt.format(i=i, name=name, ssn=ssn, address=address, zipcode=zipcode, account=account, amount=amount)

    #insert VOID at random
    index = math.floor(random() * len(output))
    output = output[0:index] + "VOID" + output[index:]

    #create file
    filename = os.path.join(here, "day1/", str(i) + ".txt")
    with open(filename, "w") as f:
        f.write(output)
