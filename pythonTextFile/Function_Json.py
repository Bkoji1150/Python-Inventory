import json
from pprint import pprint

dt_file = {'Name': {'First_Name': 'Bello', 'last_Name': 'Koji', 'Middle_Name': ''},
           'skills': ['Python', 'Devops', 'Terraform', 'yaml', 'AWS'], 'Age': 26}


def _json_file(**kwargs):
    new_file = './myinfo.json'
    try:
        # fo = open(new_file,'w')
        # json.dump(dt_file,fo,indent=4)
        data = kwargs
        open()
        print(type(data))
        for k,v in data.items():
            print(k,v)

        # for i in data:
        #     print()
        # pprint(dir(json))

        # print(json.load(fo))
        # print(fo.read())
        # print(type(fo.read()))

        # fo.close()
    except Exception as e:
        print(e)
    return


def main():
    try:
        print('Your running _reading function----')
        _json_file()
        _json_file(name='koji',age=28,status='married',job='iT',Area_Of_Expartise=['AWS','Devops','Cloudformation','Python','Boto3'])
    except Exception as e:
        print('Error found while reading',e)
    return None


if __name__ == '__main__':
    main()
