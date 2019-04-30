from bio.KEGG import REST, Enzyme, Compound, Map
import pandas

#Purpose: download the molfiles of given compounds into a (pre-created) directory named "molfiles"
#Input: CSV file consisting of a list of comopunds
#Output: Mol files (if they exist) of compounds
def main():
    #list of compounds to be analyzed
    data=pandas.read_csv("updated_compounds.csv", header=0)
    compounds = list(data.Compound)
    print(compounds)

    for c in compounds:
        #access mol info through KEGG API
        try:
            print(c)
            mol_info = REST.kegg_get(c, option="mol")
            filename = c + ".mol"
            for item in mol_info:
                print(item, file=open(filename, "a"))
        except:
            pass

if __name__ == "__main__":
    main()
