from Ava import Ava
from Online import Online
from Manager import Manager


teste = '3'

if teste == '1':
    urlAVA = 'https://ava.ufms.br/login/index.php'
    usernameAVA = 'miguel.s'
    passwordAVA = 'miguelsantosMM26*'
    
    ava = Ava(urlAVA, usernameAVA, passwordAVA)
elif teste == '2':
    urlManager = 'http://nccgsrv07/manager/login'
    usernameManager = '08234775170'
    passwordManager = '1111'
    
    manager = Manager(urlManager, usernameManager, passwordManager)
elif teste == '3':
    urlOnline = 'http://nccgsrv07/online/Login/Login.aspx'
    usernameOnline = '08234775170'
    passwordOnline = '1111'
    
    online = Online(urlOnline, usernameOnline, passwordOnline)
