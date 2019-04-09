import os

def main():
    #directories to analyze
    kegg_types = ["pathway","enzyme","reaction","compound", "reaction_detailed"]

    for k in kegg_types:
        #directory and outpath
        dirpath = "kegg/2019-04-04/" + k + "/"
        outpath = "kegg/2019-04-04/" + k + "_all.json"

        f = open(outpath, "w")
        f.write("[\n")
        f.close()
        with open (outpath, "a") as outfile:
            for file in os.listdir(dirpath):
                f = open(dirpath + file)
                data = f.readlines()
                f.close()
                data = data[1:-1]
                outfile.writelines(d for d in data)


        f = open(outpath, "a")
        f.write("]")
        f.close()


if __name__ == "__main__":
    main()
