# ChiralityXP

Purpose:
Use network expansion to analyze chiral evolution over biochemical reactions.

Instructions:
Create a space-seperate .dat file with all seed set compounds on a single line. (ex: C00001 C00002 C12532) 

Set SEEDJSON (line 227 in netexp.jl) to the .dat file

>> julia netexp.jl
>> julia netexp_postprocessing.jl

Output:
A .json file (found in results/formatted) with all compounds and reactions created from network expansion
