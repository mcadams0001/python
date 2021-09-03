import pandas as pd

def read_population_data(filename):
    populations = {}
    fileobj = open(filename, 'r')
    for line in fileobj:
        sline = line.split() #split into words
        population = int(sline[-1]) # last entry in row
        country = ' '.join([w for w in sline[0:-1]]) # all previous
        populations[country] = population
    fileobj.close()
    return populations

populations = read_population_data('countries_population_2016.txt')
pops = pd.Series(populations)

def read_populations_data_better(filename):
    populations = {}
    with open(filename, 'r') as fileobj:
        for line in fileobj:
            sline = line.split()
            population = int(sline[-1])
            country = ' '.join([w for w in sline[0:-1]])
            populations[country] = population 
    return populations