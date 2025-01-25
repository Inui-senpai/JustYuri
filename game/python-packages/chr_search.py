import glob
from re import search
from re import sub
#https://www.w3schools.com/python/python_regex.asp

def chr_search(chr_str):
    files_list = glob.glob("*.rpy")
    ###print(files_list)
    ###print("\n\n")
    total_num_instances = 0
    for file in files_list:
        #print(file)
        f = open(file, "r")
        line_list = f.readlines()
        i = 1
        num_instances = 0
        ###print(file)
        for line in line_list:
            #print(line)
            #print(chr_str)
            #print(line)
            #print(search("show_chr","persistent.dialogue_memory will house the main persistent info on dialogues"))
            if search(chr_str, line):
                ###print("File " + file + " - Line " + str(i) + ": " + line)
                num_instances +=1 
                total_num_instances += 1
                #newline = sub(r'.S.S"\)', r'ZZAD"\)', line)
                #if line != newline:
                #    print(newline)
            i = i + 1
        if num_instances !=0:
            pass
            ###print(num_instances)
        f.close()
    return total_num_instances

#chr_search(input("What chr string are you looking for?"))
#chr_search(r'show_chr\(".-.....-.[PQRS].."\)')
letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
for i in range(len(letter_list)):
    print("Total Number of Instances of Left Arm " + str(i) + ": " + str(chr_search(r'-.[' + letter_list[i] + r'].."\)')))
for i in range(len(letter_list)):
    print("Total Number of Instances of Right Arm " + str(i) + ": " + str(chr_search(r'-...[' + letter_list[i] + r']"\)')))
for i in range(len(letter_list)):
    print("Total Number of Instances of Left and Right Arm " + str(i) + ": " + str(chr_search(r'-.[' + letter_list[i] + r'].."\)') + chr_search(r'-...[' + letter_list[i] + r']"\)')))
#chr_search(r'show_chr\(".-.....-ZZAD"\)')
#chr_search(r'show_chr\(".-.....-ZZ.."\)')
#chr_search(r'.O.."\)')
