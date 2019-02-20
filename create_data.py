import csv

#open output file
output = open("seeds.dat", "w")

with open("kegg_chirality.csv") as kegg:
    csv_reader = csv.reader(kegg)
    next(csv_reader)
    #Add the compound to an input list
    for row in csv_reader:
        #If compound is chiral
        if (int(row[6]) > 0):
            c = row[0][:-4]
            output.write(c+ " "),

output.close()
