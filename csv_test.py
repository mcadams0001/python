import csv

with open('/home/adam/src/python/buzzers.csv') as data:
    print ("as arrays")
    for line in csv.reader(data):
        print(line)

with open('/home/adam/src/python/buzzers.csv') as data:
    print("as dictionary")
    for line in csv.DictReader(data):
        print(line)