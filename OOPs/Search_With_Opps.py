#!/usr/bin/env python3

import os

class Python(object):
    def get_python_home(self, server_):
        try:
            self.p_home = os.path.dirname(os.path.dirname(server_))
            self.conf_file = server_
        except Exception as e:
            print(e)

    @property
    def display_python_home(self):
        try:
            print('Python hom is:', self.p_home)
            print('Python conf file is: ', self.conf_file)

        except Exception as e:
            print(e)
        return None

def get_al_python():
    try:
        list_of_files = []
        for r, d, f in os.walk('/'):
            for each_file in f:
                if each_file == 'python3':
                    list_of_files.append(os.path.join(r, each_file))
        return list_of_files

    except Exception as e:
        print(e)
    return None

def main():
    try:
        print('Finding list of tomcats...')
        _list_of_python = get_al_python()
        _python_objects = []
        for each_file in _list_of_python:
            _python_object = Python()
            _python_object.get_python_home(each_file)
            _python_objects.append(_python_object)
        for each_ob in _python_objects:
            each_ob.display_python_home
    except Exception as e:
        print(e)
        return 0


if __name__ == '__main__':
    main()
