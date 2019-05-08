# ChiralityXP

Purpose:

Use network expansion to analyze chiral evolution over biochemical reactions.

Instructions:

Create a space-seperate .dat file with all seed set compounds on a single line. (ex: C00001 C00002 C12532) 

Set SEEDJSON (line 227 in netexp.jl) to the .dat file (if only using a single file - for multiple files, uncomment the "Multiple Files" section and include path to directory)

>> julia netexp.jl

>> julia netexp_postprocessing.jl

Output:

A .json file (found in results/formatted) with all compounds and reactions created from network expansion

**Script details**

*compress_data.py*
Compresses pre-downloaded sections of the KEGG database into a single JSON file. The files to be compressed are specified by the *kegg_types* list. Note: replace the date with the most recent download date to track database updates.

*create_data.py*
Reads from a csv file (kegg_chirality.csv) denoting the chirality of a compound. Output is a seed set file with all chiral compounds. To change to achiral compounds, replace ">" in line 12 with "==".

*generate_seeds.py*
Generates 1000 seed sets for specificied input (either achiral, chiral, or a random mix of both; and 2-10 compounds per seed set).

*get_KEGG.py*
Downloads KEGG database. The sections of KEGG to be downloaded are specified in lines 20 and 45.

*get_molfiles.py*
Downloads molecular files from KEGG for specified compounds (given by updated_compounds.csv)- necessary for determining chirality.

*network_size.py*
Outputs the number of compounds present in a network, represented within the "links/reaction_edges.json" file.
