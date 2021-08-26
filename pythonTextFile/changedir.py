import os
'''
req_path=input("Enter your required path to change directory: ")
print("Your current working directory is:", os.getcwd())
try:
    os.chdir(req_path)
    print("now you are working dir is: ",os.getcwd())
except FileNotFoundError:
    print("Given path is not a valid path, so can't change working dir")
except NotADirectoryError:
    print("The given file part is file path")
except PermissionError:
    print("Sorry you don't have access for the given path. so can't change working directory")
except Exception as e:
    print(e)
'''
def main():
    req_path=input("Enter your required path to change directory: ")
    print("Your current working directory is:", os.getcwd())
    try:
        os.chdir(req_path)
        print("now you are working dir is: ",os.getcwd())
    except FileNotFoundError:
        print("Given path is not a valid path, so can't change working dir")
    except NotADirectoryError:
        print("The given file part is file path")
    except PermissionError:
        print("Sorry you don't have access for the given path. so can't change working directory")
    except Exception as e:
        print(e)
    return None

if __name__=='__main__':
    main()
