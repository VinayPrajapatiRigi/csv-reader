import csv

t1 = open('./62b7c5a8248128210ccffd4d_2022-12-10T04_00_11.565Z_earning_report.csv', 'r')

t2 = open('./62cc3ac5a999b5212be6eeef_2022-12-09T16_00_07.213Z_earning_report.csv', 'r')

fileone = t1.readlines()

filetwo = t2.readlines()

t1.close()

t2.close()

outFile = open('update.csv', 'w')

x = 0

for i in fileone:

    if i != filetwo[x]:

        outFile.write(filetwo[x])

    x += 1

outFile.close()