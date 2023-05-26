def writetofile(log, pas):
    with open('Bd.txt', 'a') as writ:
        try:
            writ.write(log + ' ' + pas + '\n')
            reg = 'Регистрация выполнена'
        except:
            reg = 'Регистрация не выполнена'
    return reg

def check(data, log):
    if data.get(log):
        return True
    else:
        return False

def checkau(data, log, pas):
    if check(data, log):
        if data[log][0] == pas:
            return 'Авторизация выполнена успешно'
        else:
            return 'Пароль введён неверно'
    else:
        return 'Логин отсутствует/введён неверно'