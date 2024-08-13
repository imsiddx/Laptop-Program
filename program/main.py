import pandas as pd
import time




#ADMIN_CODE
def admin_page():
    #Reading_CSV
    def read_csv():
        global df, excel_length

        df = pd.read_csv('data/laptopData.csv', encoding='unicode_escape')
        df['Inches'] = df['Inches'].astype('str')
        df['Price'] = df['Price'].astype('str')
        excel_length = len(df)


    read_csv()


    #Checking Admin And Password
    def login(admin, password):
        #reading_username
        file = open('data/admin_username.txt', 'r')
        r1 = file.read()
        file.close()

        #reading_password
        file = open('data/admin_password.txt', 'r')
        r2 = file.read()
        file.close()

        #checking
        if r1 == admin and r2 == password:
            return 1
        elif r1 == admin and r2 != password:
            return 2
        elif len(admin) == 0 and len(password) == 0:
            return 3
        else:
            return 0


    #changing_username
    def change_username(new_username):
        file = open('data/admin_username.txt', 'w')
        file.write(new_username)
        file.close()
        print('\n[] Username Changed Successfully. []')


    #changing_password
    def change_password(new_password):
        file = open('data/admin_password.txt', 'w')
        file.write(new_password)
        file.close()
        print('\n[] Password Changed Successfully. []')


    #finding a laptop by id
    def get_laptop(x):
        try:
            df.loc[x]
            #printing laptop_details_if_found
            print('\n[] Laptop Found. []')
            print(f'[] Laptop Id : - {x} []\n')

            for a in range(0, len(column_name)):
                space = 25 - len(column_name[a])
                print(column_name[a], end='')
                for b in range(space):
                    print(' ', end='')
                print(df.loc[x, column_name[a]])
            print()
            return True #returning true if laptop found's.
        except:
            print('\n[] Laptop Not Found ! []\n')
            return False  # returning false if laptop found's.





    # Filtering
    column_names = list(df.columns)
    def get_laptop2(x,y):
        global c_store, temp_df, id_list

        #making_a_temporary_data_according_to_the_brand
        if x == 0:
            c_store = [[], [], [], [], [], [], [], []]  # here, we are storing required common data according to input
            temp_df = pd.DataFrame()
            id_list = []
            for i in df.index:
                if df.loc[i, 'Company'] == y:
                    temp_df = temp_df._append(df.loc[i])
                    id_list.append(i)
                else:
                    pass

            unique = []
            for l in id_list:
                if temp_df.loc[l, column_names[x + 1]] not in unique:
                    unique.append(temp_df.loc[l, column_names[x + 1]])
                else:
                    pass
            c_store[x] = unique

        else:
            #matching_requests
            id_list = []
            for k in temp_df.index: #taken +1 because we have to match existing and giving data both
                flag = 0
                for j in range(0, x + 1):
                    if temp_df.loc[k,column_names[j]] == requests_store[j][0]:
                        flag+=1
                    else:
                        pass
                if flag == x+1:
                    id_list.append(k)

            #extracting_common_in_next_column_through_the_id_we_got
            if len(id_list) > 0:
                unique = []
                for l in id_list:
                    if temp_df.loc[l,column_names[x+1]] not in unique:
                        unique.append(temp_df.loc[l,column_names[x+1]])
                    else:
                        pass
                c_store[x]=unique
            else:
                pass


    # finding_brand
    def get_brand():
        global company_names
        company_names = []
        for i in df.index:
            if df.loc[i, 'Company'] not in company_names:
                company_names.append(df.loc[i, 'Company'])



    def invalid():
        print('\n[] Invalid Input, Try Again ! []\n')


    def empty_input():
        print('\n[] Empty Input ! []\n')


    def restart_again():
        print('\n[] Limit Exceed ! []')
        time.sleep(2)
        print()
        for restart in range(5, 0, -1):
            print(f'Restarting In {restart} Seconds.')
            time.sleep(1)



    def shutdown_read():
        global minute
        file = open('data/lockdown_time.txt','r')
        minute = file.read()
        file.close()
        return int(minute)


    def shutdown_write(time):
        file = open('data/lockdown_time.txt','w')
        file.write(str(time))
        file.close()


    def shutdown_timer():
        for timer in range(shutdown_read(),-1,-1):
            for minute2 in range(60,0,-1):
                for seconds in range(10000000*4):
                    pass

            file = open('data/lockdown_time.txt','w')
            file.write(str(timer))
            file.close()





    #SECURITY_CHECK
    if shutdown_read() > 0: #if not equal to zero then pass to further main_code
        time.sleep(0.5)
        print()
        time.sleep(1)
        print(f'\n!!! Sysyem Is Locked For {shutdown_read()} Minutes !!!')
        time.sleep(1)
        print('\n!!! Wait Here, Until It Completes !!!')
        time.sleep(1)
        print()
        time.sleep(0.5)
        print()
        shutdown_timer()
    else:
        pass







    #MAIN_CODE
    #using_everthing
    column_name = ['Company', 'TypeName', 'Inches', 'ScreenResolution', 'Cpu', 'Ram', 'Storage', 'Gpu', 'OpSys', 'Weight',
                   'Price']

    x = 0
    login_successfull = 0
    loop_limit = 50
    security_breach = 20
    time_for_lockdown = 5
    print('\n!!! For Administrator Use Only !!! ')
    while x == 0:
        if len(pd.read_csv('data/laptopData.csv', encoding='unicode_escape')) != excel_length:
            read_csv()
        else:
            pass


        if login_successfull == 0:  #once login successfull, login page will not occur.
            for sb in range(security_breach):
                #admin_info
                print('\nPress X Anywhere To Exit.')
                u = str(input('Enter Admin UserName :- '))
                if u == 'X':
                    break
                p = str(input('Enter Admin Password :- '))
                if p == 'X':
                    break

                flag = 0
                l = login(u, p)
                if l == 1:
                    flag += 1
                    login_successfull = 1
                    print('\n*-----------------*')
                    print('| Welcome Admin ! |')
                    print('*-----------------*')
                    break

                elif l == 3:
                    print('\n[]  Empty Username And Empty Password ! []\n')

                elif l == 2:
                    if p == '':
                        empty_input()
                    else:
                        print('\n[] Invalid Password, Try Again ! []\n')

                elif len(u.strip()) == 0 and len(p.strip()) == 0:
                    print('\n[]  Empty Username And Empty Password ! []\n')

                elif len(u.strip()) == 0:
                    print('\n[] Empty Username ! []\n')

                elif len(p.strip()) == 0:
                    print('\n[] Empty Password ! []\n')

                elif u == '' and p == '':
                    print('\n[]  Empty Username And Empty Password ! []\n')

                elif u == '':
                    print('\n[] Empty Username ! []\n')

                elif p == '':
                    print('\n[] Empty Password ! []\n')

                elif l == 0:
                    print('\n[] Invalid Username And Password, Try Again ! []\n')



                # preventing_unauthorised_access
                if sb == security_breach-1:
                    shutdown_write(time_for_lockdown)
                    time.sleep(0.5)
                    print()
                    time.sleep(1)
                    print('!!! Security Breached !!!')
                    time.sleep(1)
                    print()
                    time.sleep(0.5)
                    print(f'\n!!! System Is Locked For {shutdown_read()} Minutes !!!')
                    time.sleep(0.5)
                    x = 1
                    break


        #checking
        if u == 'X' or p == 'X':
            break
        else:
            pass


        #conditions
        if flag == 1:
            i_store = [[], [], [], [], [], [], [], [], [], [], []]
            print()
            n1 = str(input('Press 0 To Search Laptop.\nPress 1 To Insert Laptop Data\nPress 2 To Modify Laptop Data\nPress 3 To Delete Laptop Data\nPress 4 To Change Username And Password.\nPress X To Exit\n:- '))
            brand3=0


            #SEARCHING
            if n1 == '0':
                for ask in range(loop_limit):
                    print()
                    n4 = input('Press 0 To Find Laptop Via Id.\nPress 1 To Find Laptop Via Specification\nPress X To Exit\n:- ')  #input taken in string because we have to handle exceptions
                    if n4 == '0':
                        try:
                            n5 = input('\nEnter Laptop Id :- ')
                            if len(n5) == 0:
                                empty_input()
                                continue
                            if n5[0] == '0' and len(n5) > 1:
                                invalid()
                                continue
                            n5 = int(n5)
                            get_laptop(n5)
                        except:
                            if len(n5.strip()) == 0:
                                empty_input()
                            else:
                                invalid()

                    elif n4 == '1':
                        # STORING USER_REQUEST_AND_FINDING_THAT_LAPTOP
                        again = 0  # this variable, helps to continue from where input, it gets wrong.
                        flag1 = 0  # this help to, whether ask or not ask brand.
                        success = 0  # this helps to continue further code after user request complete's
                        requests_store = [[], [], [], [], [], [], [], [], []]  # in this, we are storing user request.
                        for loop in range(0, loop_limit):
                            # 1.From_User_Taking_Brand_Input
                            if flag1 == 0:
                                print()
                                get_brand()
                                for m in range(0, len(company_names)):
                                    print(f'Press {m} For {company_names[m]}')
                                print(f'Press {m + 1} For Exit')
                                c = str(input(f'\nSelect A {column_names[0]} :- '))
                                try:
                                    if c == str(m + 1):
                                        break
                                    if len(c) == 0:
                                        empty_input()
                                        continue
                                    if c[0] == '0' and len(c) > 1:
                                        invalid()
                                        continue
                                    if int(c) < 0:
                                        invalid()
                                        continue
                                    requests_store[0] = [company_names[int(c)]]
                                    flag1 = 1
                                except:
                                    if len(c.strip()) == 0:
                                        empty_input()
                                        continue
                                    elif len(c) > 0:
                                        invalid()
                                        continue
                            else:
                                if flag1 == -1:
                                    break
                                else:
                                    pass

                            # 2.Now,Taking_Other_Inputs
                            for n in range(again, len(requests_store)):
                                if n != 8:  # we don't have to fire operating system coz we do not need price of laptop.
                                    print()
                                    get_laptop2(n, requests_store[n][0])  # here, we get c_store from function.
                                    for o in range(0, len(c_store[n])):
                                        print(f'Press {o} For {c_store[n][o]}')
                                    print(f'Press {o + 1} For Previous Step.')
                                    print(f'Press {o + 2} For Exit.')
                                    r = str(input(f'\nSelect A {column_names[n + 1]} :- '))

                                    try:
                                        #error_handle1
                                        if len(r) == 0: #if input is empty, it breaks
                                            empty_input()
                                            again = n
                                            break
                                        # error_handle2
                                        if r[0] == '0' and len(r) > 1: #if input is like (001,01,01312) it breaks # length is taken more than 2 coz we don't wnt to ignore id (0).
                                            invalid()
                                            again = n
                                            break
                                        if n == 0 and r == str(o + 1):  # asking brand again
                                            flag1 = 0 # asking everthing again !
                                            requests_store[n] = []  # clearing not required request
                                            break
                                        if r == str(o + 1):  # going to previous step
                                            again = n - 1  # sending query to previous request
                                            requests_store[n] = []  # clearing not required request
                                            break
                                        if r == str(o + 2):  # stopping this loop
                                            flag1 = -1  # stoping loop when user wanna exit.
                                            break
                                        if int(r) < 0:
                                            invalid()
                                            again = n
                                            break

                                        # storing user request in requests_store
                                        requests_store[n + 1] = [c_store[n][int(r)]]

                                        if n == 7:
                                            flag1 = -1  # stoping loop when storing completes
                                            success = 1

                                    except:
                                        # error_handling
                                        if len(r.strip()) == 0:
                                            empty_input()
                                            again = n
                                            break
                                        elif len(r) > 0:
                                            invalid()
                                            again = n
                                            break
                        else:
                            restart_again()
                            continue

                        if success == 1:  # checking if found or not
                            gotcha = []  # here we are storing id of the laptop we selected.
                            for id_no in id_list:  # checking the laptop we got, in our dataframe.
                                flag4 = 0
                                for req in range(0, len(requests_store)):
                                    if temp_df.loc[id_no, column_names[req]] == requests_store[req][0]:
                                        flag4 += 1
                                if flag4 == 9:
                                    gotcha.append(id_no)  # appending to gotcha
                        else:
                            continue

                        # RESULT
                        if len(gotcha) == 1:
                            get_laptop(gotcha[0])
                        else:
                            print('Error 100')
                            continue


                    elif n4 == 'X':
                        break


                    else:
                        if len(n4) == 0 or len(n4.strip()) == 0:
                            empty_input()
                        else:
                            invalid()


            #INSERTING
            elif n1 == '1':
                print()
                time.sleep(0.5)
                print('!!! PROVIDED DATA MUST BE IN CORRECT FORMAT !!!')
                time.sleep(0.5)
                print()

                print('\nPress X Anywhere To Exit !')
                stop1 = 0
                again2 = 0
                done = 0
                for loop in range(loop_limit):
                    for i in range(again2, len(column_name)):
                        i_store[i] = input(f'\nEnter A {column_name[i]} :- ')
                        if i_store[i] == 'X':
                            stop1 = 1
                            break
                        if len(i_store[i].strip()) == 0 or len(i_store[i]) == 0:
                            empty_input()
                            again2 = i
                            break
                        if i == 2:
                            if i_store[i][0] == '0':
                                invalid()
                                again2 = i
                                break
                            try:
                                if int(i_store[i]) < 0:
                                    invalid()
                                    again2 = i
                                    break

                                float(i_store[i])
                            except:
                                print('\n[] Inches Should Be In Integer/Decimal Value ! []\n')
                                again2 = i
                                break

                        if i == 10:
                            if i_store[i][0] == '0':
                                invalid()
                                again2 = i
                                break
                            try:
                                if int(i_store[i]) < 0:
                                    invalid()
                                    again2 = i
                                    break
                                float(i_store[i])
                                done = 1
                            except:
                                print('\n[] Price Should Be In Integer/Decimal Value ! []\n')
                                again2 = i
                                break

                    if i == len(column_name)-1 and done == 1:  # breaking the loop after getting all data.
                        break

                    if stop1 == 1:
                        break    # stopping main when user wanna exit
                    else:
                        pass

                else:
                    restart_again()
                    continue

                if stop1 == 1:
                    continue    # continuing again
                else:
                    pass

                if stop1 != 1:
                    #temporary_taking_data
                    temp_data2 = {}
                    for j in range(0, len(column_name)):
                        temp_data2.update({f'{column_name[j]}': [f'{i_store[j]}']})

                    #temporary_making_dataframe_to_append_in_original_csv
                    temp_df3 = pd.DataFrame(temp_data2)


                    print('\n[] Record Inserted ! []')
                    print(f'[] Laptop Id :- {len(df)} []')

                    #appending_that_temp_df_in_original_csv
                    temp_df3.to_csv('data/laptopData.csv', mode='a', index=False, header=False)


            #MODIFYING
            elif n1 == '2':
                # taking laptop id which we want to modify
                modify_id = input('\nEnter Laptop Id You Want To Modify :- ')

                if len(modify_id) == 0 or len(modify_id.strip()) == 0:
                    empty_input()
                    continue
                elif modify_id[0] == '0' and len(modify_id) > 1: # length is taken more than 2 coz we don't want to ignore id (0).
                    invalid()
                    continue

                try:
                    modify_id2 = int(modify_id)
                    if get_laptop(modify_id2) == True: #laptop found's in our data
                        pass
                    else:
                        continue
                except:
                    if len(modify_id) > 0:
                        invalid()
                        continue

                # taking_input_to_modify
                m_store = [[], [], [], [], [], [], [], [], [], [], []]
                for m in range(loop_limit):
                    print()
                    for n in range(0, len(column_name)):
                        print(f'Press {n} To Modify {column_name[n]}')
                    print('Press X To Exit')
                    n2 = str(input(':- '))
                    print()

                    if n2 == 'X': #quitting and saving modified data
                        df.to_csv('data/laptopData.csv', mode='w', index=False, header=True)
                        break
                    elif len(n2) == 0 or len(n2.strip()) == 0:
                        empty_input()
                        continue
                    elif n2[0] == '0' and len(n2) > 1: # length is taken more than 2 coz we don't want to ignore (0).
                        invalid()
                        continue

                    try:
                        m_store[int(n2)] = [input(f'Modifying {column_name[int(n2)]} :- ')]

                        if len(m_store[int(n2)][0]) == 0 or len(m_store[int(n2)][0].strip()) == 0:
                            empty_input()
                            continue

                        # when input is about inches
                        if int(n2) == 2:
                            if m_store[int(n2)][0][0] == '0':
                                invalid()
                                continue

                            try:
                                if int(m_store[int(n2)][0]) < 0:
                                    invalid()
                                    continue

                                float(m_store[int(n2)][0])
                            except:
                                print('\n[] Inches Should Be In Integer/Decimal Value ! []\n')
                                continue

                        # when input is about price
                        if int(n2) == 10:
                            if m_store[int(n2)][0][0] == '0':
                                invalid()
                                continue

                            try:
                                if int(m_store[int(n2)][0]) < 0:
                                    invalid()
                                    continue
                                float(m_store[int(n2)][0])
                            except:
                                print('\n[] Price Should Be In Integer/Decimal Value ! []\n')
                                continue

                        # storing_modified_data
                        df.loc[modify_id2, column_name[int(n2)]] = m_store[int(n2)][0]
                        print('\n[] Data Modified []')

                    except:
                        invalid()

                else:
                    restart_again()
                    continue


            #Deleting
            elif n1 == '3':
                del_id = input('\nEnter Laptop Id You Want To Delete :- ')

                if len(del_id) == 0 or len(del_id.strip()) == 0:
                    empty_input()
                    continue
                elif del_id[0] == '0' and len(del_id) > 1: # length is taken more than 2 coz we don't want to ignore id (0).
                    invalid()
                    continue

                try:
                    del_id2 = int(del_id)
                    if get_laptop(del_id2) == True: #it will return True if laptop found or it will return False if laptop not found (it will also print if laptop founded or not)
                        # Deleting Founded Laptop.
                        print('\n[] Record Deleted. []\n')
                        df.drop(del_id2, inplace=True)
                        df.to_csv('data/laptopData.csv', mode='w', index=False, header=True)
                    else:
                        pass
                except:
                    invalid()





            #Changing_Admin_Login_And_Password
            elif n1 == '4':
                for c2 in range(security_breach):
                    #current_admin_login
                    print('\nPress X Anywhere To Exit.')
                    u = input('Enter Your Current Username :- ')
                    if u == 'X':
                        break
                    p = input('Enter Your Current Password :- ')
                    if p == 'X':
                        break
                    l = login(u, p)

                    #changing_admin_username_and_password
                    n3 = 0
                    flag2 = 0
                    if l == 1:
                        print('\n[] Login Details, OK. []')
                        for spin in range(20):
                            print()
                            n3 = str(input('Press 0 To Change Username.\nPress 1 To Change Password.\nPress X To Exit.\n:- '))
                            print()
                            if n3 == '0':
                                new_u = str(input('Enter Your New Username :- '))
                                try:
                                    int(new_u)
                                    print('\n[] Only Number Cannot Be Set As Username ! []')
                                    continue
                                except:
                                    pass

                                if len(new_u) == 0 or len(new_u.strip()) == 0:
                                    empty_input()
                                elif new_u[0] == '0':
                                    invalid()
                                elif len(new_u) > len(new_u.strip()) or ' ' in new_u:
                                    print('\n [] Space Are Not Allowed, Try Again ! []')
                                elif new_u == u:
                                    print('\n[] New Username Should Be Different From Current Username ! []')
                                elif new_u == 'X':
                                    print('\n[] Capital X Is Not Allowed To Be Set As A New Username ! []')
                                else:
                                    change_username(new_u)
                                    u = new_u
                                    flag2 += 1

                            elif n3 == '1':
                                new_p = str(input('Enter Your New Password :- '))

                                if len(new_p) == 0 or len(new_p.strip()) == 0:
                                    empty_input()
                                elif len(new_p) > len(new_p.strip()) or ' ' in new_p:
                                    print('\n [] Space Are Not Allowed, Try Again ! []')
                                elif new_p == p:
                                    print('\n[] New Password Should Be Different From Current Password ! []')
                                elif new_p == 'X':
                                    print('\n[] Capital X Is Not Allowed To Be Set As A New Password ! []')
                                else:
                                    change_password(new_p)
                                    p = new_p
                                    flag2 += 1

                            elif n3 == 'X':
                                if flag2>0:
                                    print('\n[] Now Please Login Again ! []\n')
                                    login_successfull = 0
                                    break
                                else:
                                    break

                            else:
                                if n3 == '':
                                    empty_input()
                                else:
                                    invalid()

                        #breaking_loop
                        if n3 == 'X':
                            break


                    # error_handling
                    elif l == 3:
                        print('\n[]  Empty Username And Empty Password ! []\n')

                    elif l == 2:
                        if p == '':
                            empty_input()
                        else:
                            print('\n[] Invalid Password, Try Again ! []\n')

                    elif len(u.strip()) == 0 and len(p.strip()) == 0:
                        print('\n[]  Empty Username And Empty Password ! []\n')

                    elif len(u.strip()) == 0:
                        print('\n[] Empty Username ! []\n')

                    elif len(p.strip()) == 0:
                        print('\n[] Empty Password ! []\n')

                    elif u == '' and p == '':
                        print('\n[]  Empty Username And Empty Password ! []\n')

                    elif u == '':
                        print('\n[] Empty Username ! []\n')

                    elif p == '':
                        print('\n[] Empty Password ! []\n')

                    elif l == 0:
                        print('\n[] Invalid Username And Password, Try Again ! []\n')


                    # security_measures_for_unauthorzed_user_or_for_bruteforce_attack
                    if c2 == security_breach-1:
                        shutdown_write(time_for_lockdown)
                        time.sleep(0.5)
                        print()
                        time.sleep(1)
                        print('!!! Security Breached !!!')
                        time.sleep(1)
                        print()
                        time.sleep(0.5)
                        n1 = 'X'
                        break

            else:
                if len(n1) == 0 or len(n1.strip()) == 0:
                    empty_input()
                elif n1 == 'X': # Exiting
                    print('\nLogging Out...!')
                    time.sleep(1.5)
                    x = 1
                else:
                    invalid()

            #Exiting
            if n1 == 'X' and x != 1:
                print('\nLogging Out...!')
                time.sleep(1.5)
                x = 1

















#USER_CODE
def user_page():
    #[] FUNCTIONS BELOW[]

    # Reading_CSV_data
    def read_csv():
        global df, excel_length
        df = pd.read_csv('data/laptopData.csv', encoding='unicode_escape')
        excel_length = len(df)
        df['Inches'] = df['Inches'].astype('str')
        df['Price'] = df['Price'].astype('str')
    read_csv() #calling


    # Filtering
    column_names = list(df.columns)
    def get_laptop(x,y):
        global c_store, temp_df, id_list

        #making_a_temporary_data_according_to_the_brand
        if x == 0:
            c_store = [[], [], [], [], [], [], [], []]  # here, we are storing required common data according to input
            temp_df = pd.DataFrame()
            id_list = []
            for i in df.index:
                if df.loc[i, 'Company'] == y:
                    temp_df = temp_df._append(df.loc[i])
                    id_list.append(i)
                else:
                    pass

            unique = []
            for l in id_list:
                if temp_df.loc[l, column_names[x + 1]] not in unique:
                    unique.append(temp_df.loc[l, column_names[x + 1]])
                else:
                    pass
            c_store[x] = unique

        else:
            #matching_requests
            id_list = []
            for k in temp_df.index: #taken +1 because we have to match existing and giving data both
                flag = 0
                for j in range(0, x + 1):
                    if temp_df.loc[k,column_names[j]] == requests_store[j][0]:
                        flag+=1
                    else:
                        pass
                if flag == x+1:
                    id_list.append(k)

            #extracting_common_in_next_column_through_the_id_we_got
            if len(id_list) > 0:
                unique = []
                for l in id_list:
                    if temp_df.loc[l,column_names[x+1]] not in unique:
                        unique.append(temp_df.loc[l,column_names[x+1]])
                    else:
                        pass
                c_store[x]=unique
            else:
                pass


    def show_extra():
        global gotcha2
        gotcha2 = []
        for i in range(0, len(df.index)):
            c = 0
            for j in range(1, len(requests_store)):
                if j > 3 and j < 8:
                    continue
                else:
                    if df.loc[df.index[i], column_names[j]] == requests_store[j][0]:
                        c += 1
            if c == 4:
                if i != gotcha[0]:
                    gotcha2.append(i)


    # finding_brand
    def get_brand():
        global company_names
        company_names = []
        for i in df.index:
            if df.loc[i, 'Company'] not in company_names:
                company_names.append(df.loc[i, 'Company'])


    def thanks():
        print('\n[] Thanks ! Visit Us Again ! []\n')


    def invalid():
        print('\n[] Invalid Input, Try Again ! []\n')


    def empty_input():
        print('\n[] Empty Input ! []\n')


    def restart_again():
        print('\n[] Limit Exceed ! []')
        time.sleep(2)
        print()
        for restart in range(5, 0, -1):
            print(f'Restarting In {restart} Seconds.')
            time.sleep(1)




    #MAIN_CODE
    x = 0
    loop_limit=10
    while x != 1:
        # checking if excel data is modified
        if len(pd.read_csv('data/laptopData.csv', encoding='unicode_escape')) != excel_length:
            read_csv()
        else:
            pass


        # checking_if_user_wanna_continue
        for loop1 in range(0, loop_limit):
            continuee = str(input('\nPress 0 To Search Laptop.\nPress X For Exit.\n:- '))

            if continuee == '0':
                break
            elif continuee == 'X':
                thanks()
                x = 1
                break
            else:
                if len(continuee) == 0 or len(continuee.strip()) == 0:
                    empty_input()
                else:
                    invalid()
        else:
            restart_again()
            x=1

        if x == 1: #breaking_main_loop_if_user_press_X
            break
        else:
            pass #passing user further to search laptop



        #STORING USER_REQUEST_AND_FINDING_THAT_LAPTOP
        again = 0  # this variable, helps to continue from where, it gets wrong_input.
        flag = 0 #this help to, whether ask or not ask brand.
        success = 0 #this helps to continue further code after user request
        requests_store = [[], [], [], [], [], [], [], [], []] #in this, we are storing user request.
        for loop in range(0, 100):
            #1.From_User_Taking_Brand_Input
            if flag == 0:
                print()
                get_brand()
                for m in range(0,len(company_names)):
                    print(f'Press {m} For {company_names[m]}')
                print(f'Press {m+1} For Exit')

                c = str(input(f'\nSelect A {column_names[0]} :- '))
                try:
                    if c == str(m+1):
                        break
                    if len(c) == 0 or len(c.strip()) == 0:
                        empty_input()
                        continue
                    if c[0] == '0' and len(c) > 1 or int(c) < 0:
                        invalid()
                        continue
                    requests_store[0] = [company_names[int(c)]]
                    flag = 1
                except:
                        invalid()
                        continue
            else:
                if flag == -1:
                    break
                else:
                    pass

            #2.Now,Taking_Other_Inputs
            error = 0
            for n in range(again, len(requests_store)):
                if n != 8: #we don't have to fire operating system coz we do not need price of laptop.
                    print()
                    get_laptop(n, requests_store[n][0]) #here, we get c_store from function.
                    for o in range(0,len(c_store[n])):
                        print(f'Press {o} For {c_store[n][o]}')
                    print(f'Press {o+1} For Previous Step.')
                    print(f'Press {o+2} For Exit.')
                    r = str(input(f'\nSelect A {column_names[n+1]} :- '))

                    try:
                        if n == 0 and r == str(o+1):  # asking brand again
                            flag = 0
                            requests_store[n] = []  # clearing not required request
                            break
                        if r == str(o+1):  # going to previous step
                            again = n-1
                            requests_store[n] = []  # clearing not required request
                            break
                        if len(r) == 0 or len(r.strip()) == 0:
                            empty_input()
                            again = n
                            break
                        if r[0] == '0' and len(r) > 1 or int(r) < 0:
                            invalid()
                            again = n
                            break
                        if r == str(o+2):  # stopping this loop
                            flag = -1  # stoping loop when user wanna exit.
                            break

                        #storing user request in requests_store
                        requests_store[n + 1] = [c_store[n][int(r)]]

                        if n == 7 and error == 0:
                            flag = -1  # stoping loop when storing completes
                            success = 1

                    except:
                        #error_handling
                        invalid()
                        again = n
                        break

        else:
            restart_again()
            continue



        if success == 1: #checking if found or not
            gotcha = [] #here we are storing id of the laptop we selected.
            for id_no in id_list: #checking the laptop we got, in our dataframe.
                flag4 = 0
                for req in range(0, len(requests_store)):
                    if temp_df.loc[id_no, column_names[req]] == requests_store[req][0]:
                        flag4 += 1
                if flag4 == 9:
                    gotcha.append(id_no) #appending to gotcha
        else:
            continue


        # RESULT
        if len(gotcha) == 1:
            print('\n\n\n/// Laptop Found According To Your Preferences. ///\n')
            for j in column_names:
                print(j, end='')
                space = 25 - len(j)
                for k in range(space):
                    print(' ', end='')
                print(temp_df.loc[gotcha[0], j])
            print()
            print()
        else:
            print('Error 100')
            continue


        # finding that laptop but different brand
        gotcha1 = []
        for p in df.index:
            flag3 = 0
            for q in range(1,len(requests_store)):
                if df.loc[p,column_names[q]] == requests_store[q][0]:
                    flag3+=1
            if flag3 == 8:
                if p != gotcha[0]:
                    gotcha1.append(p)


        if len(gotcha1) > 0:
            print('\n\n\n/// But We Have Other Laptops Brand\'s With Same Specification...! ///\n')
            for i in range(0, len(gotcha1)):
                print(f'#Suggestion_{i + 1}')
                for j in column_names:
                    print(j, end='')
                    space = 25 - len(j)
                    for k in range(space):
                        print(' ', end='')
                    print(df.loc[gotcha1[i], j])
                print()
                print()
        else:
            print('No Other Laptops Brand Found With Same Specification !')


        # Now, Let's Compare Gotcha And Gotcha1 Price
        if len(gotcha1) > 0:
            print('\n<<< Comparing Those >>>')
            compare = {} #main_dataframe

            #making dataframe of founded laptop
            temp = {}
            temp.update(
                {f'Column{1}':
                     {'Brand': f'{df.loc[gotcha[0], "Company"]}',
                      'Price': round(float(f'{df.loc[gotcha[0], "Price"]}'), 2),
                      },
                 },
            )
            compare.update(temp)

            og_price = f'{df.loc[gotcha[0], "Price"]}' #price of founded laptop

            #now,putting other founded laptop to temp
            for l in range(0, len(gotcha1)):
                temp = {}
                temp.update(
                    {f'Column{l + 2}':
                         {'Brand': f'{df.loc[gotcha1[l], "Company"]}',
                          'Price': round(float(f'{df.loc[gotcha1[l], "Price"]}'), 2),
                          'You Save': round(float(f'{float(og_price) - float(df.loc[gotcha1[l], "Price"])}'), 2),
                          },
                     },
                )

                compare.update(temp)

            compare2 = pd.DataFrame(compare)
            print(compare2.to_string())

        else:
            pass



        # Showing Laptops Of Same Specification Except Cpu, Ram, Storage And Gpu
        show_extra() #calling this function, to get gotcha2.
        if len(gotcha2) > 10:
            only = 10
        else:
            only = len(gotcha2)

        if len(gotcha2) > 0:
            for loop in range(0, loop_limit):
                se = str(input('\nPress 0 To See Laptop Recommendation For You.\nPress X If You Do Not Want To See.\n:- '))
                if se == '0':
                    # showing_extra's
                    print(f'\n\n/// Here Are {only} Laptop Recommendation For You ! ///\n')

                    for i in range(0, only):
                        print(f'#Extra_{i + 1}')
                        for j in column_names:
                            print(j, end='')
                            space = 25 - len(j)
                            for k in range(space):
                                print(' ', end='')
                            print(df.loc[gotcha2[i], j])
                        print()
                        print()
                    break

                elif se == 'X':
                    break

                else:
                    if len(se) == 0 or len(se.strip()) == 0:
                        empty_input()
                    else:
                        invalid()

            else:
                restart_again()

        else:
            pass












#starts_from here
while True:
    print('\n\n[] MAIN PAGE []')
    ask = input('Press 0 For Admin.\nPress 1 For User.\nPress 2 For Exit.\n:- ')
    if ask == '0':
        admin_page()
    elif ask == '1':
        user_page()
    else:
        if ask == '2':
            break
        elif len(ask) == 0 or len(ask.strip()) == 0:
            print('\n[] Empty Input, Try Again ! []')
        elif ask[0] == '0':
            print('\n[] Invalid Input, Try Again ! []')
        else:
            print('\n[] Invalid Input, Try Again ! []')




 # [] Coded By Mr.Yogesh ✌... []
