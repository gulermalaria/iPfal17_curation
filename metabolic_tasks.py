import cobra
import sys
import os
import argparse

if __name__ == "__main__":
    description = '''Metabolic tasks performing script'''
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", action="store", dest="model", required=True,
                        help="The path to SBML model file to be tested (in .xml format)")
    # Argument checking section
    args = parser.parse_args()
    try:
        cobra.io.read_sbml_model(args.model)
    except OSError:
        raise OSError("The SBML file you've provided is invalid or doesn't exist.")


dir_path = os.path.dirname(os.path.realpath(__file__))
print("Metabolic tasks starting in %s" % (dir_path))

model = cobra.io.read_sbml_model(args.model)

opt = model.optimize()
lethal = 0
frac = opt.f*.9

# Do antimetabolites of riboflavin, nicotinamide, pyridoxine, and thiamine
# inhibit growth? (Nutritional requirements of Plasmodium falciparum
# in culture. II. Effects of antimetabolites in a semi-defined medium.
# Geary TG, Divo AA, Jensen JB

# ribo

deleted = model.remove_reactions(['RBFK','RIBFLVt2','ACP1'])
opt = deleted.optimize()
if opt.f > lethal:
    p


ribo = removeRxns(model,{'RBFK';'RIBFLVt2';'ACP1'});
opt = optimizeCbModel(ribo);
if (opt.f > frac)
    warning('FAILS 1a: Model grows with riboflavin antimetabolite')
end

% nico
% findRxnsFromMets(model,'ncam[c]')
nico = removeRxns(model,{'NNAM';'EX_nicotinamide2'});
opt = optimizeCbModel(nico);
if (opt.f > frac)
    warning('FAILS 1c: Model grows with nicotinamide antimetabolite')
end
% Fails, but there are many ways to make NAD+ and NADP+
% off target affects of ncam antimetabolite, because NAD is similiar in
% structure?

% pyro
% findRxnsFromMets(model,'pydxn[c]')
pyro = removeRxns(model,{'PYDXNK';'PDXPP';'PYDXNtr'});
opt = optimizeCbModel(pyro);
if (opt.f > frac)
    warning('FAILS 1d: Model grows with pyridoxine antimetabolite')
end
% Fails, maybe antimetabolite has off target effects?

% thi
% findRxnsFromMets(model,'thm[c]')
thi = removeRxns(model,{'TMDPK';'THMP';'THMDP';'THMt3'});
opt = optimizeCbModel(thi);
if (opt.f > frac)
    warning('FAILS 1b: Model grows with thiamine antimetabolite')
end
% FAILS
