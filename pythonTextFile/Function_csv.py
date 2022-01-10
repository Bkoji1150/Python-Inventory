import csv
from pprint import pprint as p


def _reading_csv_file(**kwargs):
    #
    dt_file = './first_csv.csv'
    try:
        fo = open(dt_file, 'r')
        _emp_list = []
        content = fo.readlines()
        data = csv.reader(content, delimiter=',')
        #print(list(data)[0]) # Fist cursor
        print()
        hearder = next(data)
        print('The header is',hearder)
        print(len(hearder)-1)
        # Data is now an object that can be itirable
        # Readding Header in scv
        for each in data:
            print(each)

        fo.close()
        # Convert to csv
        for each in content:
            pass
            # print(each.strip('\n').split(","))
    except Exception as e:
        print(e)
    return None


def main():
    try:
        _reading_csv_file(Name='koji')
    except Exception as e:
        print('Error found while reading',e)
    return None


if __name__== '__main__':
    main()
