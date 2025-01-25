# Sonny Luong
# JY Project
# Objective: Find files with matching names in 2 folders, and output
# the matches in a list

import os
#result_list = make_list()
folder_name_1 = raw_input('Which folder to check?: ') # Added eval
folder_name_2 = raw_input('Which folder to compare with?: ')
#folder1= open(folder_name_1)
#folder2= open(folder_name_2)

def matching_files(folder_name_1, folder_name_2):
    folder1 = os.listdir(folder_name_1)
    folder2 = os.listdir(folder_name_2)
    result_list = []
    for i in range(len(folder1)):
        for j in range(len(folder2)):
            if folder1[i] == folder2[j]:
                result_list.append(folder1[i])

    print(result_list)
    if len(result_list) > 0:
        print('True')
        return True
    else:
        print('False')
        return False
