
import pandas as pd
from sqlalchemy import create_engine
poll_data = pd.read_csv('https://projects.fivethirtyeight.com/polls-page/president_primary_polls.csv')
poll_data['candidate_name'].unique()

import requests
response = requests.get("https://gbfs.citibikenyc.com/gbfs/en/station_information.json")

if response.status_code != 200:
    print("Error with website. If problem persists, contact your Facilitator!")
else:
    print("Data download successful")

datadict = response.json()

print(datadict['last_updated'])
import time
print(time.ctime(datadict['last_updated']))


import numpy as np
coordinates = np.array([[station['lon'], station['lat']] for station in datadict['data']['stations']])
coordinates.shape

plt.figure(figsize=(6,6))
plt.scatter(x=coordinates[:,0], y=coordinates[:,1], s=3)