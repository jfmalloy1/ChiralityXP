import pandas as pd
import json
import os
import numpy as np

import csv


#Folder path
fpath = "results/formatted/"

#Analysis to analyze
analysis = ["achiral_2", "achiral_3", "achiral_4", "achiral_5", "achiral_6", "achiral_7", "achiral_8", "achiral_9", "achiral_10", "chiral_2", "chiral_3", "chiral_4", "chiral_5", "chiral_6", "chiral_7", "chiral_8", "chiral_9", "chiral_10", "mix_2", "mix_3", "mix_4", "mix_5", "mix_6", "mix_7", "mix_8", "mix_9", "mix_10"]

#Store every file path within a list
master_fileList = []
individual_fileList = []

#create list of all json files
for a in analysis:
    for f in os.listdir(fpath):
        if f.startswith(a) and f.endswith(".json"):
            individual_fileList.append(fpath + f)
    master_fileList.append(individual_fileList)

#Summary statistics

#Total number of random seed sets (per classification)
total = 1000

#Sum of new compounds added
sum = 0

#Collection of all sums for each expansion (within a single classification)
master_sums = []
ind_sums = []
#Count to distinguish each classification
count = 0

for item in master_fileList[0]:
    count+=1
    print(item)
    with open(item) as f:
        #Taken directly from "netexp-plotting.ipynb" on jfmalloy1 Google Drive (originally coded by hbs)
        datajson = json.load(f)
        generations = pd.DataFrame(datajson["generations"])
        if generations.empty:
            sum = 0
        else:
            generations = generations.transpose()
            generations.index = generations.index.astype(int)
            generations = generations.sort_index()
            original_columns = generations.columns
            for col in original_columns:
                generations["n_"+col] = generations[col].str.len()

            sum = int((generations["n_compounds_cumulative"].iloc[-1]))
        ind_sums.append(sum)
        if (count % 1000 == 0):
            master_sums.append(ind_sums)
            ind_sums = []

#Summary statistics...summary ;)

#Average size of each expansion (number of new compounds added)
#print("Average sum of " + str(analysis) + " is: " + str(np.average(sums)))

#Write to a csv file
master_sums = np.asarray(master_sums)
master_sums = master_sums.transpose()
np.savetxt("expansions.csv", master_sums, fmt="%d", delimiter=",", header="achiral_2,achiral_3,achiral_4,achiral_5,achiral_6,achiral_7,achiral_8,achiral_9,achiral_10,chiral_2,chiral_3,chiral_4,chiral_5,chiral_6,chiral_7,chiral_8,chiral_9,chiral_10,mix_2,mix_3,mix_4,mix_5,mix_6,mix_7,mix_8,mix_9,mix_10")
