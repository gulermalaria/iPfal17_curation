# -*- coding: utf-8 -*-
import cobra
import csv
import time
import os
import argparse

if __name__ == "__main__":
    description = '''Plata model curation script'''
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", action="store", dest="model", required=True,
                        help="The path to SBML model file to be curated (in .xml format)")
    parser.add_argument("-d", action="store", dest="delete", required=True,
                        help="The paths(s) to the CSV file(s) with reactions to be deleted from the model.", nargs='*')
    parser.add_argument("-e", action="store", dest="edit", required=True,
                        help="The path(s) to the CSV file(s) with reactions to be edited in the model.", nargs='*')
    # Argument checking section
    args = parser.parse_args()
    try:
        cobra.io.read_sbml_model(args.model)
    except OSError:
        raise OSError("The SBML file you've provided is invalid or doesn't exist.")
    try:
        if len(args.delete) == 1:
            open(args.delete[0], 'r')
        else:
            for file in args.delete:
                open(file, 'r')
    except FileNotFoundError:
        raise FileNotFoundError("The file you've provided doesn't exist.")
    try:
        if len(args.edit) == 1:
            open(args.edit, 'r')
        else:
            for file in args.edit:
                open(file, 'r')
    except FileNotFoundError:
        raise FileNotFoundError("The file you've provided doesn't exist.")

dir_path = os.path.dirname(os.path.realpath(__file__))
print("Curation starting in %s" % (dir_path))
for file in args.delete:
    command = "sed -i 's/(e)/_LPAREN_e_RPAREN_/g' "+file
    # print(command)
    os.system(command)
command = "sed -i 's/_RSQBKT_//g' "+args.model
# print(command)
os.system(command)
command = "sed -i 's/_LSQBKT_/_/g' "+args.model
# print(command)
os.system(command)
for i in ['c', 'e', 'ap', 'mt', 'm', 'fv']:
    for file in args.edit:
        command = "sed  -i 's/\[" + i + "\]/\_" + i + "/g' " + file
        os.system(command)



timestr = time.strftime("%Y_%m_%d_%H:%M:%S")


def to_bool(s):
    return True if s == 1 else False


plata = cobra.io.read_sbml_model(args.model)
model = plata
no_of_rxns = len(model.reactions)
no_of_genes = len(model.genes)
print("Number of genes in original model: %d" % no_of_genes)
print("Number of reactions in original model: %d" % no_of_rxns)
a = model.optimize()
print("Original model model growth: %f" % a.f)
dict_elements = ['Confidence score', 'EC Number', 'Notes', 'References']
for filename in args.edit:
    with open(filename, 'r', encoding='iso-8859-1') as handle:
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
        dict_notes = {'Confidence score': [], 'EC Number': [], 'Notes': [], 'References': []}
        for j in range(0, 3):
            dict_notes[dict_elements[j]] = [file[i][11+j]]
        print(dict_notes)
        model.reactions.get_by_id(file[i][0]).notes = dict_notes
    del file, handle, filename

for filename in args.delete:
    with open(filename, 'r') as handle:
        file = list(csv.reader(handle))
    for i in range(1, len(file)):
        try:
            model.reactions.get_by_id(file[i][0])
        except KeyError:
            print('No reaction with ID: %s. Will not be removed' % (file[i][0]))
        else:
            model.remove_reactions([file[i][0]])
    del file, handle, filename

no_of_rxns = len(model.reactions)
no_of_genes = len(model.genes)
print("Number of genes: %d" % no_of_genes)
print("Number of reactions: %d" % no_of_rxns)
model.objective = "biomass"
a = model.optimize()
print("Modified model growth: %f" % a.f)
filename = dir_path + "/output/curated_model_" + timestr

cobra.io.save_json_model(model, filename + ".json")
cobra.io.save_matlab_model(model, filename + ".mat")
cobra.io.write_sbml_model(model, filename+".xml", use_fbc_package=True)

new_model = cobra.io.read_sbml_model(filename+".xml")


missing_metabolite_names = []
for met in new_model.metabolites:
    if met.name is None:
        missing_metabolite_names.append(met.id)

print("\nStarting metabolites attributes curation.\n%d metabolites do not have the name attribute prior to curaton\n" % len(missing_metabolite_names))

filename = "/home/mstolarczyk/PycharmProjects/uva/data/added_metabolites.csv"
with open(filename, 'r') as handle:
    file = list(csv.reader(handle))
    for i in range(1, len(file)):
        try:
            new_model.metabolites.get_by_id(file[i][0])
        except KeyError:
            print('No metabolite with ID: %s. Attributes will not be added' % (file[i][0]))
        else:
            new_model.metabolites.get_by_id(file[i][0]).formula = file[i][2]
            new_model.metabolites.get_by_id(file[i][0]).name = file[i][1]

comps = new_model.compartments
missing_metabolite_names = []
for met in new_model.metabolites:
    if met.name is None:
        missing_metabolite_names.append(met.id)
    metid = met.id
    compartment = metid.split("_")[-1]
    if compartment in comps.keys():
        met.compartment = compartment
    else:
        comps.update({compartment:compartment})
        met.compartment = compartment
        print("\nAdded new model compartment: %s" % compartment)
new_model.compartments = comps
# Fixing issues rendering the SBML to not pass the validation (specific to Michal's curation)
new_model.reactions.get_by_id("2.1.1.12").id = "MSMET"
new_model.reactions.get_by_id("2.4.1.141").id = "UDPGNT"
new_model.remove_reactions(new_model.metabolites.get_by_id("Asn_X_Ser/Thr_e").reactions)
new_model.metabolites.get_by_id("Asn_X_Ser/Thr_e").remove_from_model()
new_model.metabolites.get_by_id("Asn_X_Ser/Thr_c").remove_from_model()

print("\n%d metabolites do not have the name attribute after curation\n" % len(missing_metabolite_names))
print(missing_metabolite_names)
filename = dir_path + "/output/curated_model_" + timestr
cobra.io.write_sbml_model(new_model, filename+".xml", use_fbc_package=True)