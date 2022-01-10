import shutil


def copy_files(name):
    src = "/Users/kojibello/Downloads/src/Python-Inventory/Functions/Folder1/ec2file.py"
    dest = "/Users/kojibello/Downloads/src/Python-Inventory/Functions/Folder2/backupfile2"
    try:
        print("Good morning ",name)
        #shutil.copyfile(src,dest)
        shutil.copy2(src,dest)
    except Exception as e:
        print(e)
    return None


def main():
    copy_files('koji')
    copy_files('Kelder')
    return None


if __name__=='__main__':
    main()