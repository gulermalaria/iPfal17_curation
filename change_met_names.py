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

met = args.met_name
with open(args.filename, 'r') as handle:
    file = list(csv.reader(handle))
    with open(args.filename + '_' + met, 'w+') as handle_write:
        file_write = list(csv.reader(handle_write))
        for i in range(1, len(file)):
            line = file[i][0]
            if re.search(r'([a-z]*%s[a-z]*)(\d+)_(\w)' % met, line) is not None:
                match = re.search(r'([a-z]*%s[a-z]*)(\d+)_(\w)' % met, line)
                new = match.groups()[1] + match.groups()[0] + '_' + match.groups()[2]
                new_line = line[0:match.span()[0]] + new + line[match.span()[1]:]
                handle_write.write(new_line + "\n")
            else:
                handle_write.write(line + "\n")



