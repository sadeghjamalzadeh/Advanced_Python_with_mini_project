def check_registration_rules(**kwargs):
    list = []
    for username, password in kwargs.items():
        if (len(password) >= 6) and (len(username) >= 4) and (
                str(username) != "codecup") and (str(username) != "quera") and (password.isnumeric() == False) :
           list.append(username)
    return list
