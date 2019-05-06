import sys
import csv
import random

#Generates either achiral, chiral, or a random mix of seed sets
#Inputs: "a/c/m" (achiral/chiral/mix); n (a number denoting how many seeds to include in each seed set)
#Defaults to 1000 seed sets created

TYPE = sys.argv[1]
N_SEEDS = int(sys.argv[2])
N_SETS = 1000

#create lists of chiral/achiral compounds
#Return a list of chiral compounds (chiral) & a list of achiral comopunds (achiral)
def chirality():
    chiral = []
    achiral = []
    with open("kegg_chirality.csv") as kegg:
        csv_reader = csv.reader(kegg)
        next(csv_reader)
        for row in csv_reader:
            #If compound is chiral
            if (int(row[6]) > 0):
                c = row[0][:-4]
                chiral.append(c)
            #If compound is not chiral
            else:
                c = row[0][:-4]
                achiral.append(c)
    return chiral, achiral

#Takes N_SETS random samples of the list of compounds provided, and writes each sample to a provided file
def make_seed_sets(outfile, list):
    #repeat 1000 times
    for i in range(N_SETS):
        #randomly sample N compounds from the achiral list
        cpds = random.sample(list, N_SEEDS)
        for c in cpds:
            outfile.write(c + " ")
        outfile.write("\n")

def main():
    #make list of chiral/achiral compounds
    chiral, achiral = chirality()
    #make outfile (in seeds directory) based on input
    outfile = ""

    #Make achiral-only seed sets
    if TYPE == "a":
        outfile = "achiral_" + str(N_SEEDS) + ".dat"
        with open("seeds/" + outfile, "w") as f:
            make_seed_sets(f, achiral)
    #Make chiral-only seed sets
    elif TYPE == "c":
        outfile = "chiral_" + str(N_SEEDS) + ".dat"
        with open("seeds/" + outfile, "w") as f:
            make_seed_sets(f, chiral)
    #Make a mix of chiral and achiral seed sets
    elif TYPE == "m":
        outfile = "mix_" + str(N_SEEDS) + ".dat"
        with open("seeds/" + outfile, "w") as f:
            make_seed_sets(f, achiral+chiral)


if __name__ == '__main__':
    main()
