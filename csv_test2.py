import pprint
from datetime import datetime

flights = {}    

def covert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('/home/adam/src/python/buzzers.csv') as data:
    ignore = data.readline()
    for line in data:
        k,v = line.strip().split(',')
        flights[k] = v
pprint.pprint(flights)
print()

flights2 = {}
for k, v in flights.items(): 
    flights2[covert2ampm(k)]=v.title()
pprint.pprint(flights2)
print()


more_flights = {}
more_flights = {covert2ampm(k): v.title() for k, v in flights.items()}
pprint.pprint(more_flights)
print()

just_freeport2 = {covert2ampm(k): v.title() for k, v in flights.items() if v == 'Freeport'}
pprint.pprint(just_freeport2)
print()

when = {}
for dest in set(flights.values()):
    when[dest] = [k for k, v in flights.items() if v == dest]

pprint.pprint(when)
print()

when2 = {dest: [k for k,v in flights.items() if v == dest] for dest in set(flights.values())}

pprint.pprint(when2)
print()
