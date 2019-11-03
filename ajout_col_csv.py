import os
import csv

entree = csv.reader(open("full.csv","r"),delimiter=';', quoting=csv.QUOTE_ALL,lineterminator='\n')
sortie = csv.writer(open("sortie.csv", "w"),delimiter=';',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

row = next(entree)
row.insert(0,'id')
i=1
for row in entree:
        row.insert(0,i)
        sortie.writerow(row)
        i+=1
