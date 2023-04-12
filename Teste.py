from Ava import Ava
from Online import Online
from Manager import Manager
from Changesets import Changesets

teste = '4'

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
    
elif teste == '4':
    urlChangeset = 'http://nccgtfs01:8080/tfs/NotaControl/ISS%20ONLINE/_backlogs/TaskBoard/Online%20ISS%20Vers%C3%A3o%20-%20Abril%202023/Licita%C3%A7%C3%A3o%20Contagem%201.3?_a=requirements'
    
    changesets = Changesets(urlChangeset)
