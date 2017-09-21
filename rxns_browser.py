import cobra
import argparse

if __name__ == "__main__":
    description = '''Reactions browser'''
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", action="store", dest="met", required=True,
                        help="The metabolite id to that you want to examine")
    parser.add_argument("-mdl", action="store", dest="model", required=True,
                        help="The path to the SBML model")
    # Argument checking section
    args = parser.parse_args()
    try:
        cobra.io.read_sbml_model(args.model)
    except OSError:
        raise OSError("The SBML file you've provided is invalid or doesn't exist.")

    model = cobra.io.read_sbml_model(args.model)

    try:
        model.metabolites.get_by_id(args.met)
    except KeyError:
        raise KeyError("The metabolite ID that you are looking for does not exist.")

    reactions = tuple(model.metabolites.get_by_id(args.met).reactions)
    if model.metabolites.get_by_id(args.met).name is None:
        print("\n" + args.met + " reactions:\n")
    else:
        print("\n" + args.met + " (" + model.metabolites.get_by_id(args.met).name + ") reactions:\n")
    for i in range(0, len(reactions)):
        print(reactions[i].id + " | " + reactions[i].reaction + "\n")