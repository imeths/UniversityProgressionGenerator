#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
#Any code taken from other sources is referenced within my code solution. 
#Student ID: w1986579 
#Date: 2023.04.18


#introducing the variables
pass_credit=0
defer_credit=0
fail_credit=0
progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0
outcome_count=0

#creating the lists
progress_list=[]
trailer_list=[]
retriever_list=[]
exclude_list=[]


#validating the user input
while True:

    marks=[]        #creating a list to append all the marks entered
    
    try:
        pass_credit=int(input("Please enter your credit at pass:"))
        marks.append(pass_credit)       #appending the credit entered to a list
        if pass_credit > 120 or pass_credit%20!=0 :
            print("Out of range")
            continue
        else:
            defer_credit=int(input("Please enter your credit at defer:"))
            marks.append(defer_credit)
        if defer_credit > 120 or defer_credit%20!=0 :
            print("Out of range")
            continue
        else:
            fail_credit=int(input("Please enter your credit at fail:"))
            marks.append(fail_credit)
        if fail_credit > 120 or fail_credit%20!=0 :
            print("Out of range")
            continue
        if pass_credit + defer_credit + fail_credit !=120 :
            print("Total incorrect")
            continue
    except ValueError:      #validating whether the input is an integer
        print("Integer required.")
        continue



#printing the output based on the information entered
    if pass_credit==120 :
        print("Progress")
        progress_count+=1       #getting the count of specific grade to print "*" 
        progress_list.append(marks)         #appending the total marks entered to the specific grade list

    if pass_credit==100 :
        if defer_credit==20 or fail_credit==20 :
            print("Progress (module trailer)")
            trailer_count+=1
            trailer_list.append(marks)
            
    elif pass_credit==80 and defer_credit+fail_credit==40 :
        print("Module retriever")
        retriever_count+=1
        retriever_list.append(marks)
        
    elif pass_credit==60 :
        print("Module retriever")
        retriever_count+=1
        retriever_list.append(marks)
        
    if pass_credit==40 :
        if fail_credit!=80 :
            print("Module retriever")
            retriever_count+=1
            retriever_list.append(marks)
        else :
            print("Exclude")
            exclude_count+=1
            exclude_list.append(marks)
            
    if pass_credit==20 :
        if fail_credit==80 or fail_credit==100 :
            print("Exclude")
            exclude_count+=1
            exclude_list.append(marks)
            
        else :
            print("Module retriever")
            retriever_count+=1
            retriever_list.append(marks)
            
    if pass_credit==0 :
        if fail_credit==80 or fail_credit==100 or fail_credit==120 :
            print("Exclude")
            exclude_count+=1
            exclude_list.append(marks)
            
        else :
            print("Module retriever")
            retriever_count+=1
            retriever_list.append(marks)
            
    outcome_count+=1        #getting the total number of correct inputs to get the number of outcomes
    print()



#getting the user input to continue the program or to quit the program and print the results
    check=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    if check.lower()== "y" :
        print()
        continue

    
    
#printing the marks of students according to their credits as a horizontal histogram
    if check.lower()== "q" :
        print()
        print("-"*60)
        print("Histogram")
        print("Progress",progress_count," :","*"*progress_count)
        print("Trailer",trailer_count,"  :","*"*trailer_count)
        print("Retriever",retriever_count,":","*"*retriever_count)
        print("Exclude",exclude_count,"  :","*"*exclude_count)
        print()

#printing the number of correct inputs inserted 
        print(outcome_count,"outcomes in total.")
        print("-"*60)



#printing the marks of students according to their credits as a list
        print()
        print("Part 2:")
        print("Progress -",*progress_list)
        print("Progress (module trailer) -",*trailer_list)
        print("Module retriever -",*retriever_list)
        print("Exclude -",*exclude_list)



#converting the lists created to text files and printing the text files created
        print()
        print("Part 03:")
        with open ("output.txt","w") as file:
            for item in progress_list:
                file.write("progress -"+str(item)+"\n")
        with open ("output.txt","a") as file:
            for item in trailer_list:
                file.write("Progress (module trailer) - "+str(item)+"\n")
        with open ("output.txt","a") as file:
            for item in retriever_list:
                file.write("Module retriever -"+str(item)+"\n")
        with open ("output.txt","a") as file:
            for item in exclude_list:
                file.write("Exclude - "+str(item)+"\n")
        with open ("output.txt","r") as  file:
            for outputs in file:
                print(outputs)
        break
