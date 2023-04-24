from Ava import Ava
from Online import Online
from Manager import Manager
from Changesets import Changesets
from Youtube import Youtube

# 1 = AVA
# 2 = Manager
# 3 = Online
# 4 = Changesets
# 5 = Youtube

teste = '2'

if teste == '1':
    urlAVA = 'https://ava.ufms.br/login/index.php'
    usernameAVA = 'miguel.s'
    passwordAVA = 'miguelsantosMM26*'
    
    ava = Ava(urlAVA, usernameAVA, passwordAVA)
    
elif teste == '2':
    urlManager = 'http://localhost:4200/login'
    usernameManager = '08234775170'
    passwordManager = '1111'
    
    manager = Manager(urlManager, usernameManager, passwordManager)
    
elif teste == '3':
    urlOnline = 'http://localhost:6988/Login/Login.aspx'
    usernameOnline = '08234775170'
    passwordOnline = '1111'
    
    online = Online(urlOnline, usernameOnline, passwordOnline)
    
elif teste == '4':
    urlChangeset = 'http://nccgtfs01:8080/tfs/NotaControl/ISS%20ONLINE/_backlogs/TaskBoard/Online%20ISS%20Vers%C3%A3o%20-%20Abril%202023/Online%20ISS%20V4.4.2?_a=requirements'
    
    changesets = Changesets(urlChangeset)

elif teste == '5':
    urlYoutube = 'https://www.youtube.com/feed/subscriptions'
    
    youtube = Youtube(urlYoutube)