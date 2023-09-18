from password_generator import Generate_medium
from password_generator import Generate_complex
from password_generator import Generate_simple
from symmetrical import read_key
from symmetrical import encrypt
from symmetrical import decrypt
from Account import account_class
import time
import pprint



# Info to store
# Website / Site (Location)
# Info to get the Site / Website
# Username:
# Password
# Email
# Other Info
# Should also have auto password generator




def enter_password_manager(times_tried):
    with open("password/pw.txt") as f:
        lines = f.readlines()[0]
    print('Hello Alex (hopefully) welcome to the password vault.')
    vault_password = input('Enter password: ')
    if vault_password == lines:
#        Password is successful
        return True
    else:

        if times_tried > 0:
            print(f'Incorrect password You have {times_tried} tries left')
            recursion = times_tried - 1
            enter_password_manager(recursion)
        else:
            # This is when you cannot remember the password
            # Do something
            #
            raise Exception('Oops Out of tries motherfucker')



def create_new_site():
    # print('Type "exit" if you wish to exit')
    account_name = input('Enter Account Name: ')
    check_for_exit(account_name)
    url = input('Enter Site url: ')
    check_for_exit(url)
    username = input('Enter Username: ')
    check_for_exit(username)
    email = input('Enter Email: ')
    check_for_exit(email)
    password = input('Enter "gen" to generate new one: Enter Password: ')
    if password.lower() == 'gen':
        length = input('Enter "ez" for ez password, or Enter length: ')
        if length.lower() == 'ez':
            password = Generate_medium(15)
        else:
            level = input('Enter "ez" for ez password, Enter 1 for easy, 2 for medium, 3 for hard: ')
            if level == '1':
                password = Generate_simple(length)
            elif level == '2':
                password = Generate_medium(length)
            elif level == '3':
                password = Generate_complex(length)
        print(password)
    check_for_exit(password)


    other_info = input('Other Information: ')
    check_for_exit(other_info)

    keys = read_key()

    url = encrypt(url, keys)
    username = encrypt(username, keys)
    password = encrypt(password, keys)
    other_info = encrypt(other_info, keys)
    email = encrypt(email, keys)
    username = f"'{username}'"
    url = f"'{url}'"
    password = f"'{password}'"
    other_info = f"'{other_info}'"
    email = f"'{email}'"
    data = {'account_name': account_name, 'url': url, 'username': username, 'password': password, 'other_info': other_info, 'email': email}
    account_class.save(data)
    return True


def get_account_info(id):
    data = {'id': id}
    full_data = account_class.select_one_id(data)
    # print(full_data)
    enter_data={'id': full_data[0]['id'], 'url': full_data[0]['url'], 'username': full_data[0]['username'], 'password': full_data[0]['password'], 'other_info': full_data[0]['other_info'], 'email': full_data[0]['email'], 'account_name': full_data[0]['account_name']}
    account = account_class(enter_data)
    # print(account.url)
    account.print_all(account)


# get_account_info(55)


def check_for_exit(message):
    if message.lower() == 'exit':
        print('Exiting...')
        # SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP SLEEP
        # time.sleep(0.5)
        raise Exception('Exit')
    else:
        return False


def see():

    temp = input('Would you like to see (all) records or just (one)/(1)?: ')
    check_for_exit(temp)
    if temp.lower() == 'all' or temp.lower() == 'al':
        all = account_class.select_all()
        # pprint.pprint(all)
        for x in all:
            account_class.print_all(self=x)
        # for x in all:
    if temp.lower() == 'one' or temp.lower() == '1':
        name = input('Enter the name: ')
        key = read_key()
        encrypted = encrypt(name, key)
        # ERROR ERROR ERROR ERROR ERROR ERROR
        data = {'account_name': name}
        id = account_class.select_one_account_name(data)
        # print(id)
        # data = {'id': id['id']}
        # print(data)
        full_data = account_class.select_one_id(data)
        # print('Type: full data: ' + str(type(full_data)))
        full_data = id
        # print(id)
        enter_data = {'id': full_data[0]['id'], 'url': full_data[0]['url'], 'username': full_data[0]['username'],
                      'password': full_data[0]['password'], 'other_info': full_data[0]['other_info'],
                      'email': full_data[0]['email'], 'account_name': full_data[0]['account_name']}
        account = account_class(enter_data)
        account.print_all(account)

# see()

def run_passwords():
    first_branching = input('Would you like too (add) or (see)/(c): ')
    check_for_exit(first_branching)

    if first_branching.lower() == 'add' or first_branching.lower() == 'ad':
        check1 = create_new_site()
        if not check1:
            return False
        run_passwords()
    if first_branching == 'see' or first_branching == 'se' or first_branching == 's' or first_branching == 'c':
        see()


run_passwords()