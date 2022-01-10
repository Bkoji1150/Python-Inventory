def _reading_file(argv, **kwargs):
    # Reading files
    # Copying the file content to another file.
    dt_file = './file1.txt'
    try:
        fo = open('newdemo.txt', 'r')
        do = open(dt_file,'w')
        data = fo.readlines()
        for i in data:
            do.write(i)

        for each in range(3):
            print(data[each])
            print(data)
            print(i)

            print(data[each])
            print(data)
        do.close()
        fo.close()
    except Exception as e:
        print(e)
    return


def main():
    try:
        print('Your running _reading function----')
        _reading_file('')
    except Exception as e:
        print('Error found while reading',e)
    return None


if __name__== '__main__':
    main()
