# 2.5.1.11 LAB: Sudoku

#import sudoku module
import sudoku_mod as sudo

sudo_list = sudo.row_input()

for row in sudo_list:
    print(row)

#Check if valid
is_valid = True

#if still valid, check rows
if is_valid:
    print("checking row values")
    is_valid = sudo.row_check(sudo_list)
    print("Are rows valid:",is_valid)
    #end if

#if still valid, check Columns
if is_valid:
    print("checking column values")
    is_valid = sudo.col_check(sudo_list)
    print("Are columns valid:",is_valid)

#if still valid, check Boxes
if is_valid:
    print("checking box values")
    is_valid = sudo.box_check(sudo_list)
    print("Are boxes valid:",is_valid)

#print Answer!
print("Is sudoko valid:",is_valid)
