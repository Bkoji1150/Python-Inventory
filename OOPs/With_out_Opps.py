import os


def get_all_tomcats():
    try:
        list_of_conf=[]
        list_of_python = []
        for r,d,f in os.walk("/"):
            for each_file in f:
                if each_file == 'server.xml':
                    if each_file=='python':
                        list_of_python.append(os.path.join(r,each_file))
                        print(list_of_python)
                    list_of_conf.append(os.path.join(r,each_file))
        else:
            print('Tomcat is  not installed')
        return list_of_conf, list_of_python
    except Exception as e:
        print(e)


def main():
    try:
        print('finding list of tomcats')
        list_of_tomcat = get_all_tomcats()

        print(list_of_tomcat,)
    except Exception as e:
        print(e)
    return None


if __name__ == '__main__':
    main()