# Write a CSV-to-JSON translator 
# that expects a path to a CSV file as argument,
# and for each line,
#  prints out a JSON object encapsulating that record 

# import modules
import sys
import os
import _pickle as pickle
import json


def convert_dict_to_json(file_path):  # function to handle CSV, use json.dumps method
    with open(file_path, 'rb') as fpkl, open('%s.json' % file_path, 'w') as fjson:
        data = pickle.load(fpkl)
        json.dump(data, fjson, ensure_ascii=False, sort_keys=True, indent=4)



def main():
    if sys.argv[1] and os.path.isfile(sys.argv[1]):
        file_path = sys.argv[1]
        print("Processing %s ..." % file_path)
        convert_dict_to_json(file_path)
    else:
        print("Usage: %s abs_file_path" % (__file__))


if __name__ == '__main__':
    main()
