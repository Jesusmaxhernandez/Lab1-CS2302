#Jesus Maximino Hernandez 88756947
#Data Structures - Diego Aguirre
#Lab 1 - Option A
#Program classifys and sorts mages of animals

import os
import random


def get_dirs_and_files(path):
    
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list
#determines if image is a dog or cat
def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2

#count variable to count how many times process_dir() method iterates
count = 0
#Method to sort images into cat or dog list
def process_dir(path, cat_list, dog_list):
    global count 
        
    dir_list, file_list = get_dirs_and_files(path)
    
    #Goes through directories and files
    for f in file_list:
        #Condition to ignore unwanted files
        if f[0] is not '.' and f[0] is not 'M' :
            #method to classify whether image is dog or cat image and put it into its proper list
            if classify_pic(f) < .5:
                    cat_list.append(os.path.join(path, f))    
            else:
                    dog_list.append(os.path.join(path, f))
               
    #Recursive call to uterate through all the directories and files            
    for directory in dir_list:
        process_dir(os.path.join(path, directory), cat_list, dog_list)
    
    #print elements in cat_list and dog_list
#    if count == 5:
#        print ("Every full path of every dog image:" )
#        for x in range(len(dog_list)): 
#            print (dog_list[x][1:])
#        print()
#        print ("Every full path of every cat image:" )
#        for x in range(len(cat_list)): 
#            print (cat_list[x][1:])
    count = count + 1
    return cat_list, dog_list
    

def main():
    start_path = os.getcwd()# current directory

    process_dir(start_path, [], []),
    

main()

#TEST CASES:
#Initated differnet tests by : deleting directories and images ('DCIM' and all files in 'All', moving program to a differnt location 
#(Ex: Inside 'Pictures' and adding a word documebt in 'Pictures' folder)
