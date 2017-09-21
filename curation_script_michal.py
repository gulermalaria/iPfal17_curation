import cobra
import csv
import re
import time
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
print("Curation starting in %s" % (dir_path))
command = "sed -i 's/(e)/_LPAREN_e_RPAREN_/g' "+dir_path+"/data/reaction_delete_edits_final.csv"
print(command)
os.system(command)
command = "sed -i 's/_RSQBKT_//g' "+dir_path+"/data/plata_sbml_up_model.xml"
print(command)
os.system(command)
command = "sed -i 's/_LSQBKT_/_/g' "+dir_path+"/data/plata_sbml_up_model.xml"
print(command)
os.system(command)
for i in ['c', 'e', 'ap', 'mt', 'm']:
    for j in [dir_path+"/data/biomass_edits_final.csv", dir_path+"/data/edits_additions_or_modifications_final.csv"]:
        command = "sed  -i 's/\["+i+"\]/\_"+i+"/g' "+j
        os.system(command)

timestr = time.strftime("%Y_%m_%d_%H:%M:%S")

def to_bool(s):
    return True if s == 1 else False

plata = cobra.io.read_sbml_model(dir_path+"/data/plata_sbml_up_model.xml")
model = plata
no_of_rxns = len(model.reactions)
no_of_genes = len(model.genes)
print("Number of genes in original model: %d" % (no_of_genes))
print("Number of reactions in original model: %d" % (no_of_rxns))
a = model.optimize()
print("Original model model growth: %f" % (a.f))

with open(dir_path+"/data/reaction_delete_edits_final.csv", 'r') as handle:
    file = list(csv.reader(handle))
for i in range(1, len(file)):
    try:
        model.reactions.get_by_id(file[i][0])
    except KeyError:
        print('No reaction with ID: %s. Will not be removed' % (file[i][0]))
    else:
        model.remove_reactions([file[i][0]])
del file, handle

for filename in [dir_path+"/data/edits_additions_or_modifications_final.csv", dir_path+"/data/biomass_edits_final.csv"]:
    with open(filename, 'r') as handle:
        file = list(csv.reader(handle))
    for i in range(1, len(file)):
        try:
            model.reactions.get_by_id(file[i][0])
        except KeyError:
            print('No reaction with ID: %s. Creating...' % (file[i][0]))
        else:
            model.remove_reactions([file[i][0]])
        new_reaction = cobra.Reaction(file[i][0])
        model.add_reactions([new_reaction])
        model.reactions.get_by_id(file[i][0]).build_reaction_from_string(reaction_str=file[i][2])
        model.reactions.get_by_id(file[i][0]).bounds = (float(file[i][8]), float(file[i][9]))
        model.reactions.get_by_id(file[i][0]).reversibility = to_bool(file[i][7])
        model.reactions.get_by_id(file[i][0]).subsystem = file[i][6]
        model.reactions.get_by_id(file[i][0]).gene_reaction_rule = file[i][3]
        model.reactions.get_by_id(file[i][0]).annotation = file[i][14]
        model.reactions.get_by_id(file[i][0]).notes = file[i][13]
    del file, handle

no_of_rxns = len(model.reactions)
no_of_genes = len(model.genes)
print("Number of genes: %d" % (no_of_genes))
print("Number of reactions: %d" % (no_of_rxns))
model.objective = "biomass"
a = model.optimize()
print("Modified model growth: %f" % (a.f))
filename = dir_path + "/output/curated_model_" + timestr

cobra.io.save_json_model(model, filename+".json")
cobra.io.save_matlab_model(model, filename+".mat")
cobra.io.write_sbml_model(model, filename+".xml",use_fbc_package=True)
