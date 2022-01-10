import csv
from pprint import pprint


def _create_file(**kwargs):
    # Reading files
    # Copying the file content to another file.
    dt_file = './demo.csv'
    __ne = './FINANCE101MEMBERS.csv'
    meeting_file = '/Users/kojibello/Downloads/FINANCE 101 MEMBERS-2.xlsx'
    try:
        meeting_list = [['Names','Customer_Number','Age'],['Rob', '12234','32'],['Koji','122344','27'],['Christy', '11234', '40']]
        fo = open(dt_file, 'w',newline="")
        mo = open(meeting_file, 'w')
        _nt = open(__ne,'w')
        csv_write = csv.writer(fo, delimiter=",")
        fi = csv.writer(mo, delimiter=',')
        print(dir(fi))
        data = mo.readlines()
        # print(data)
        # for i in data:
        #     mo.write(_nt)

        # csv_read = csv.
        # Writing role without iterating.
        ''' 
        csv_write.writerow(['Names','Customer_Number','Age'])
        csv_write.writerow(['Koji','122344','27'])
        csv_write.writerow(['Christy', '11234', '40'])
        csv_write.writerow(meeting_list)
        '''
        # writing in a list format
        csv_write.writerows(meeting_list)
        _nt.close()
        mo.close()
        fo.close()
    except Exception as e:
        print(e)
    return


def main():
    try:
        print('Your running _reading function----')
        _create_file(name='koji')
    except Exception as e:
        print('Error found while reading',e)
    return None


if __name__== '__main__':
    main()
