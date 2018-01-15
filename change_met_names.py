import csv
import argparse
import re


if __name__ == "__main__":
    description = '''Script changing metabolite names from *numbers_* to numbers*_*'''
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", action="store", dest="filename", required=True,
                        help="The path to csv file with third column with metabolite names to be changed")
    parser.add_argument("-m", action="store", dest="met_name", required=True,
                        help="Generic name of the metabolite to be changed")

    # Argument checking section
    args = parser.parse_args()

with open(args.filename, 'r') as handle:
    file = list(csv.reader(handle))
for i in range(1, len(file)):
    print(file[i][2])
    if re.search(r'(args.met_name)(\d+)_(\w)', file[i][2]) is not None:
        print("TAK")

