def auth(db_type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            username = input("Enter your name: ").strip()
            password = input("Enter your password: ").strip()

            if db_type == 'file':
                print('from file')
                if username == 'admin' and password == 'admin':
                    result = function(*args, **kwargs)
                    return result
                else:
                    print('wrong')
            elif db_type == 'mysql':
                print('from mysql')
                if username == 'admin' and password == 'admin':
                    result = function(*args, **kwargs)
                    return result
                else:
                    print('wrong')
            elif db_type == 'ldap':
                print('from ldap')
                if username == 'admin' and password == 'admin':
                    result = function(*args, **kwargs)
                    return result
                else:
                    print('wrong')
            else:
                print('wrong')

        return wrapper

    return decorator


@auth('mysql')  # login = auth(db_type = 'mysql')
def login(username, password):
    print(username, password)


login('admin', 'admin')