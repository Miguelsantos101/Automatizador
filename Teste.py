from Ava import Ava
from Online import Online
from Manager import Manager


teste = 'Manager'

if teste == 'Ava':
    urlAVA = 'https://ava.ufms.br/login/index.php'
    usernameAVA = 'miguel.s'
    passwordAVA = 'miguelsantosMM26*'
    
    ava = Ava(urlAVA, usernameAVA, passwordAVA)
elif teste == 'Manager':
    urlManager = 'http://nccgsrv07/manager/login'
    usernameManager = '08234775170'
    passwordManager = '1111'
    
    manager = Manager(urlManager, usernameManager, passwordManager)
elif teste == 'Online':
    urlOnline = ''
    usernameOnline = ''
    passwordOnline = ''
    
    online = Online(urlOnline, usernameOnline, passwordOnline)
