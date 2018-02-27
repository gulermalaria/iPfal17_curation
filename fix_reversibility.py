import csv
import argparse
import re
import cobra

if __name__ == "__main__":
    description = '''Script fixing reactions reversibility based on the arrow type in reaction field'''
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", action="store", dest="filename", required=True, help="The path to the csv file")

    # Argument checking section
    args = parser.parse_args()

with open(args.filename, 'r') as handle:
    file = list(csv.reader(handle))
    with open(args.filename, 'w+') as handle_write:
        file_write = list(csv.reader(handle_write))
        for i in range(0, len(file)):
            line = file[i][2]
            if re.search(r'>', line) is not None:
                if re.search(r'<', line) is not None:
                    file[i][7] = str(1)
                    file[i][8] = str(-1000)
                else:
                    file[i][7] = str(0)
                    file[i][8] = str(0)
            handle_write.write(','.join(file[i]) + "\n")
