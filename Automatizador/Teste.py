from Ava import Ava
from Online import Online
from Manager import Manager


teste = input()

if teste == 'Ava':
    urlAVA = 'https://ava.ufms.br/login/index.php'
    usernameAVA = 'miguel.s'
    passwordAVA = 'miguelsantosMM26*'
    
    ava = Ava(urlAVA, usernameAVA, passwordAVA)
elif teste == 'Online':
    urlOnline = ''
    usernameOnline = ''
    passwordOnline = ''
    
    online = Online(urlOnline, usernameOnline, passwordOnline)
elif teste == 'Manager':
    urlManager = ''
    usernameManager = ''
    passwordManager = ''
    manager = Manager(urlManager, usernameManager, passwordManager)
