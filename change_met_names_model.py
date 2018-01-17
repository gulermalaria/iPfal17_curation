import argparse
import re
import cobra

if __name__ == "__main__":
    description = '''Script changing metabolite names from *numbers_* to numbers*_*'''
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-mdl", action="store", dest="model", required=True,
                        help="The path to the SBML model file")

    # Argument checking section
    args = parser.parse_args()

model = cobra.io.read_sbml_model(args.model)

val_before = model.optimize().f
print("Flux before: %f" % val_before)

for met in ['pa', 'pe', 'ps', 'pg', 'pgp', 'crm', 'dhcrm', 'sphmyln', 'xolest']:
    for metabolite in model.metabolites:
        if re.search(r'([a-z]*%s[a-z]*)(\d+)_(\w{1,2})' % met, metabolite.id):
            print("Original metabolite ID: " + metabolite.id)
            match = re.search(r'([a-z]*%s[a-z]*)(\d+)_(\w{1,2})' % met, metabolite.id)
            new = metabolite.id[0:match.start()] + match.groups()[1] + match.groups()[0] + '_' + match.groups()[2]
            print("New ID: " + new)
            try:
                model.metabolites.get_by_id(new)
            except KeyError:
                print('No met with this ID. Adding...')
            else:
                model.metabolites.get_by_id(new).remove_from_model()
            model.metabolites.get_by_id(metabolite.id).id = new

val_after = model.optimize().f
print("Flux after: %f" % val_after)

cobra.io.write_sbml_model(model, "model_changed_names.xml")
