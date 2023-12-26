import os

def display_title_bar():
    print("\n\t*********************************")
    print("\t*******Count Lines of Code*********")
    print("\n\t*********************************")

choice = ''
while choice!='q':
    display_title_bar()
    
    print("\n[1] Count Lines for a Folder")
    print("\n[2] Count Lines for a Single File")
    print("\n[q] Quit")
    
    choice = str(input("\nWhat would like to do?\n"))
    
    if choice == '1':
        print('\nCount Lines for a Folder\n')
        file_path = input("\nPlease input folder path: \n")
        cmd = 'python3 LineCounter.py -p {} -c {}'.format(file_path, choice)
        os.system(cmd)
    elif choice == '2':
        print('\nCount Lines for a Folder')
        file_path = input("\nPlease input file path: \n")
        cmd = 'python3 LineCounter.py -p {} -c {}'.format(file_path, choice)
        os.system(cmd)
    elif choice == 'q':
        print('\nExiting....')
    else:
        print('\nDid not understand the input....')
        
        