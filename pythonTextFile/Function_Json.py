import json
from pprint import pprint


def _json_file(**kwargs):

    dt_file = {'Name': {'First_Name': 'Bello','last_Name':'Koji', 'Middle_Name':''},'skills': ['Python','Devops','Terraform','yaml','AWS'], 'Age':26}
    new_file = './myinfo.json'
    try:
        fo = open(new_file,'w')
        json.dump(dt_file,fo,indent=4)

        # pprint(dir(json))
        print()
        # print(json.load(fo))
        # print(fo.read())
        # print(type(fo.read()))

        fo.close()
    except Exception as e:
        print(e)
    return


def main():
    try:
        print('Your running _reading function----')
        _json_file(name='koji')
    except Exception as e:
        print('Error found while reading',e)
    return None


if __name__== '__main__':
    main()
