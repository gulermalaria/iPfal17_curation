import cobra
import argparse

if __name__ == "__main__":
    description = '''Reactions balance check'''
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-r", action="store", dest="reaction", required=True,
                        help="The reaction id to that you want to examine")
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
        model.reactions.get_by_id(args.reaction)
    except KeyError:
        raise KeyError("The reaction ID that you are looking for does not exist.")

    # reactions = tuple(model.metabolites.get_by_id(args.met).reactions)
    if model.reactions.get_by_id(args.reaction).name is None:
        print("\n" + args.reaction + " reaction:\n")
    else:
        print("\n" + args.reaction + " (" + model.reactions.get_by_id(args.reaction).name + ") reaction:\n")
    print(model.reactions.get_by_id(args.reaction).reaction)
    print("\nBalance:\n")
    print(model.reactions.get_by_id(args.reaction).check_mass_balance())
    print("\n")