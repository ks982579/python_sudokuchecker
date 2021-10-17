# 2.5.1.11 Lab: Sudoku - Module 01

#Needs 9 numbers, between 1 and 9.
#Change to number, no further checks. 
def row_input():
    sudoku = []
    print("Rows are currently hardcoded")
    print("Enter an entire row, values separated by commas")
    for row_number in range(9):
        valid_row = False

        while valid_row == False:
            #clear values
            error = False
            sudo_row = []
            sudo_input_row = ""
            sudo_txt_elm = ""
            sudo_txt_row = []
            
            sudo_input_row = input("Row #"+str(row_number+1)+": ")

            #must force comma on end
            if sudo_input_row[-1] != ",":
                sudo_input_row += ","

            #for each element, append text between commas. 
            for elm in sudo_input_row:
                if elm != ",": # comma detection
                    if elm != " ": # to ignore spaces
                        sudo_txt_elm += elm
                else:
                    sudo_txt_row.append(sudo_txt_elm)
                    sudo_txt_elm = ""

            if len(sudo_txt_row) != 9:
                print("incorrect number of elements detected")
                print("please try again")
                continue

            if error == False: #more checks
                for val in range(9): # checking for integers
                    try:
                        sudo_number = int(sudo_txt_row[val])
                        sudo_row.append(sudo_number)
                    except:
                        print("non-integer value detected")
                        error = True
                        break #out of this for loop

            if error == False: #more checks
                for val in sudo_row:
                    if val < 1 or val >9:
                        error = True
                        print("Value detected no betwen 1 and 9 (inclusive)")
                        break
                    else:
                        continue
                #exit for loop

            if error == True:
                continue
            else:
                valid_row = True
                sudoku.append(sudo_row)
                continue
        #exit while loop
    return sudoku

def sudo_check(sudo_list): # Returns True if everything is found
    answer = True
    correct = [1,2,3,4,5,6,7,8,9]
    #if string 2 < string 1, return false
    length01 = len(correct)
    length02 = len(sudo_list)
    
    if length02 < length01:
        answer = False
    #end if
        
    else:
        for sudo01 in sudo_list:             #for01
            temp_answer = False
            #print(letter01)
            for val in range(len(correct)):  #for02
                correct02 = correct[val]
                #print(letter02)
                
                if sudo01 == correct02:
                    temp_answer = True
                    del correct[val]
                    #print(list02)
                    break                   #for02
                #end if
            #end for02

            #natural exit of for02 goes here
            if temp_answer != True:
                #we found letter not in string
                answer = temp_answer
                #print("I made it")
                break                       #for01
            #end if
        #end for
    #end else
        
    return answer
#end function

def row_check(sudoku):
    for row in sudoku:
        is_valid = sudo_check(row)

        if is_valid:
            ##print("continue")
            continue
        else:
            ##print("break")
            break
        #Exit if else
    #exit for loop
        
    return is_valid
#Exit function row_check()


def col_check(sudoku):
    is_valid = True
    new_sudo = []
    new_row = []

    #make columns?
    for elm in range(9): #gets (1-9) - makes a column
        
        for row in sudoku: #get elm, put in row
            new_row.append(row[elm])
        #end for - make row
        #print(new_row)

        new_sudo.append(new_row)
        new_row = []
    #end for - new sudo
    is_valid = row_check(new_sudo)
    return is_valid


def box_check(sudoku): #take in whole sudoku
    is_valid = True
    new_sudo = []
    new_row = []

    for row_shift in range(3): #making new rows to check
        row_shift*=3
        for col_shift in range(3):
            col_shift*=3
            for row_number in range(3):
                sudo_row = sudoku[(row_number+row_shift)]
                for col_number in range(3):
                    ##print("row:",row_number+row_shift,"; col:",col_number+col_shift)
                    sudo_elm = sudo_row[col_number+col_shift] # Get Element
                    new_row.append(sudo_elm) # append element to new row
                    continue
                continue
            # at this point we are shifting over to a new box
            # must save old box and clear contents
            new_sudo.append(new_row)
            new_row = []
            continue
        continue
    ##for rows in new_sudo:
      ##  print(rows)
    #Exit for loop recursion hell
    is_valid = row_check(new_sudo)
                    
    return is_valid

### testing ###

print("sudoku_mod.py uploaded")




