from pprint import pprint


class Emp:
    count = 0

    def __init__(self):
        try:
            Emp.count = Emp.count + 1
            # print('This is an init method')
        except Exception as e:
            print(e)
        return

    def display(self):
        try:
            print('This is a display method')
        except Exception as e:
            print(e)
        return None


def main():
    try:
        emp1 = Emp()
        emp2 = Emp()
        print(f'There are {Emp.count} object created by Emp class')
    except Exception as e:
        print(e)

    # pprint(dir(emp1))
    return None


if __name__ == '__main__':
    main()