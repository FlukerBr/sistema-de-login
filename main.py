import PySimpleGUI as sg
sg.theme('Material1')
def getusers():
    try:
        with open('users.txt', 'r', encoding='utf-8') as gu:
            users = gu.readlines()
    except FileNotFoundError:
        with open('users.txt', 'w') as ur:
            ur.write('')
        return users
    return users
def login(name, password):
    if len(name) == 0 or len(password) == 0:
        return 'Erro ao Logar!'
    for user in getusers():
        if not name == user.split()[0]:
            return 'Usuário não se encontra registrado!'
    for user in getusers():
        if name == user.split()[0] and password == user.split()[1]:
            return 'Logado com sucesso!'
        else:
            return 'Senha incorreta!'
def register(name, password):
    if len(name) == 0 or len(password) == 0:
        return 'Erro ao Registrar!'
    if ' ' in name or ' ' in password:
        return 'Não coloque espaços no nome ou senha!'
    if len(getusers()) == 0:
        with open('users.txt', 'a', encoding='utf-8') as us:
            us.write(f'{name} {password}')
        return 'Registrado com sucesso!'
    else:
        for user in getusers():
            if name in user.split()[0]:
                return 'Usuário já se encontra registrado!'
            else:
                with open('users.txt', 'a', encoding='utf-8') as us:
                    us.write(f'{name} {password}')
                return 'Registrado com sucesso!'   
layout = [
    [sg.Text('Nome : ', size=(7, 1)), sg.Input(key='name', size=(20, 1))],
    [sg.Text('Senha : ', size=(7, 1)), sg.Input(key='password', size=(20, 1), password_char='*')],
    [sg.Button('Logar', key='login'), sg.Button('Registrar', key='register')],
    [sg.Text('', key='output')]
]
janela = sg.Window('Sistema de Login', layout, size=(280, 120))
while True:
    event, value = janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'login':
        janela['output'].update(login(value['name'], value['password']))
    if event == 'register':
        janela['output'].update(register(value['name'], value['password']))