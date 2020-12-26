from factorial.factorial import fact
from logarithm.logarithm import *
from exp_root.root import *
from exp_root.exponentiation import *

choice = input('Write 1 to use the factorial module, 2 - to use the logarithm module and 3 to use exp_root module')
list = ['1', '2', '3']

while choice not in list:
    choice = input('Please check your data.')



if choice == '1':
    a = input('Enter an int. number please: ')
    while a.isdigit() != True:
        a = input('Please check your data.')
    print('The answer is ', fact(int(a)))



if choice == '2':
    choice_0 = input('Enter 1 to use log() function, 2 - to use ln() function and 3 for lg()')
    while choice_0 not in list:
        choice_0 = input('Please check your data.')

    if choice_0 == '1':
        choice_0_a = input('Enter the 1st numb')
        choice_0_b = input('Enter the 2nd numb')
        try:
            choice_0_a = float(choice_0_a)
            while float(choice_0_a) < 0:
                choice_0_a = input('Please check your data.')
        except ValueError:
            choice_0_a = input('Please check your data.')
        try:
            choice_0_b = float(choice_0_b)
            while float(choice_0_b) < 0 and float(choice_0_b) == 1:
                choice_0_b = input('Please check your data.')
        except ValueError:
            choice_0_b = input('Please check your data.')
        print('The answer is ', log(float(choice_0_a), float(choice_0_b)))

    if choice_0 == '2':
        choice_ln = input('Please enter the number: ')
        try:
            choice_ln = float(choice_ln)
            while float(choice_ln) <= 0:
                choice_ln = input('Please check your data.')
        except ValueError:
            print('Please check your data.')
        print('The answer is ', ln(float(choice_ln)))

    if choice_0 == '3':
        choice_lg = input('Please enter the number: ')
        try:
            choice_lg = float(choice_lg)
            while float(choice_lg) <= 0:
                choice_lg = input('Please check your data.')
        except ValueError:
            print('Please check your data.')
        print('The answer is ', lg(float(choice_lg)))



if choice == '3':
    choice_3_1 = input('Enter 1 to use exponentiation module and 2 to use the root module')
    while choice_3_1 not in list[0:2]:
        choice_3_1 = input('Please check your data.')

    if choice_3_1 == '1':
        choice_3_exp = input('Enter 1 to use the  exp2() module and 2 to use the  exp3() module: ')
        while choice_3_exp not in list[0:2]:
            choice_3_exp = input('Please check your data.')

        if choice_3_exp == '1':
            a = input('Enter the number:')
            try:
                a = float(a)
            except ValueError:
                print('Please check your data.')
            print('The answer is ', exp2(float(a)))

        if choice_3_exp == '2':
            a = input('Enter the number:')
            try:
                a = float(a)
            except ValueError:
                print('Please check your data.')
            print('The answer is ', exp3(float(a)))

    if choice_3_1 == '2':
        choice_3_root = input('Enter 1 to use the  root2() module and 2 to use the  root3() module: ')
        while choice_3_root not in list[0:2]:
            choice_3_root = input('Please check your data.')

        if choice_3_root == '1':
            a = input('Enter the number:')
            try:
                a = float(a)
                while float(a) < 0:
                    a = input('Please check your data.')
            except ValueError:
                print('Please check your data.')
            print('The answer is ', root2(float(a)))

        if choice_3_root == '2':
            a = input('Enter the number:')
            try:
                a = float(a)
                while float(a) < 0:
                    a = input('Please check your data.')
            except ValueError:
                print('Please check your data.')
            print('The answer is ', root3(float(a)))




