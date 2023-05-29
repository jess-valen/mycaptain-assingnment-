# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:46:00 2023

@author: Jessika Valencia
"""

# School admission program

import csv

def write_into_csv(info_list):
    with open('student_info.csv' , 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow( [ "NAME", "AGE", "PLACE", "CONTACT_NO.", "EMAIL_ID"])
            
        writer.writerow(info_list)
if __name__ == "__main__":
    
        condition = True

while(condition):
    student_info = input(" Enter student information in the following foramt ( Name Age PLace Contact_no. Email_ID ):")
    print(" Entered information: " + student_info)
    
    #split
    
    student_info_list = student_info.split(" ")
    print("cEntered split up information is:" + str(student_info_list))
    
    print("\nThe entered information is -\nName: {}\nAge: {}\nPlace: {}\nContact_no.: {}\nEmail_ID: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3], student_info_list[4]))
    
    choice_check = input(" Is the entered information correct? (yes/no): ")
    if choice_check == "yes":
       write_into_csv(student_info_list)
    
    condition_check = input(" Enter (yes/no) if you want to enter information about another student: ")
    if condition_check == "yes":
        conditon = True
    elif condition_check == "no":
        condtion = False
    elif choice_check == "no":
        print(" \nPlease re-enter the values! ")
        

        
        
       