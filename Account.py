from SQL_Connection import connecttomysql
from symmetrical import decrypt
from symmetrical import read_key



class account_class:
    db = 'password_manager'
    def __init__( self, data):
        self.id = data['id']
        self.url = data['url']
        self.username = data['username']
        self.password = data['password']
        self.other_info = data['other_info']
        self.account_name = data['account_name']
        self.email = data['email']

    @staticmethod
    def print_all(self):
        keys = read_key()
        # url = str(self.url)[5:-3]
        username = str(self['username'])[5:-3]
        password = str(self['password'])[5:-3]
        other_info = str(self['other_info'])[5:-3]
        email = str(self['email'])[5:-3]
        print(f'id: {self["id"]}')
        print(f'account name: {self["account_name"]}')
        # print(f'url: {decrypt(url, keys)}')
        print(f'username: {decrypt(username, keys)}')
        print(f'password: {decrypt(password, keys)}')
        print(f'other info: {decrypt(other_info, keys)}')
        print(f'email: {decrypt(email, keys)}')

    @staticmethod
    def save(data):
        query = 'INSERT INTO accounts (url, username, password, other_info, account_name, email) VALUES (%(url)s, %(username)s, %(password)s, %(other_info)s, %(account_name)s, %(email)s);'
        return connecttomysql(account_class.db).query_db(query, data)

    @staticmethod
    def select_one_account_name(data):

        query = "SELECT * FROM accounts WHERE account_name =%(account_name)s"


        return connecttomysql(account_class.db).query_db(query, data)

    @staticmethod
    def select_one_id(data):
        query = 'SELECT * FROM accounts WHERE id = %(id)s'
        return connecttomysql(account_class.db).query_db(query, data)

    @staticmethod
    def select_all():
        query = 'SELECT * FROM accounts'
        return connecttomysql(account_class.db).query_db(query)