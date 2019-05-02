import pandas as pd

#Find the size of a network (number of unique compounds)
def main():
    #compound list
    cpds = []
    with open("links/reaction_edges.json") as input:
        data = pd.read_json(input)
        #search through both products and substrates
        #add unique compounds to growing list
        for rn in data.products:
            for c in rn:
                if c not in cpds:
                    cpds.append(c)
        for rn in data.substrates:
            for c in rn:
                if c not in cpds:
                    cpds.append(c)

    #output the number of unique compounds within the network
    print("Unique Compounds: ", len(cpds))

if __name__ == "__main__":
    main()
