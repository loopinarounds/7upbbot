import requests
import pandas as pd
import random

df = pd.read_csv("Bible.csv",header=None,encoding= 'unicode_escape')

print(df.iloc[0][0])

# County
num = random.randint(0, 47)
county = df.iloc[num][7]

# Store
store_num = random.randint(0,6)
store_ = df.iloc[store_num][8]

data_val = {"firstName": "George",
"lastName": "Lopez",
"email": "bluegeorge64@gmail.com",
"emailConfirm": "bluegeorge64@gmail.com",
"telephoneNumber": "07421237823",
"county": F'{"ID":55,"text":"{county}"}',
"county_search": None,
"store": F"{store_}",
"above18": "Y",
"terms": "Y",
"marketing":None }

r = requests.post('https://7up.co.uk/moments',data=data_val)
print(r)