from Ava import Ava
from Online import Online
from Manager import Manager
from Changesets import Changesets
from Youtube import Youtube

# 1 = AVA

# 2 = Manager

# 3 = Online
    # 3-1 = Solicitação de Cadastro
    
# 4 = Changesets

# 5 = Youtube

main = '5'

if main == '1':
    urlAVA = 'https://ava.ufms.br/login/index.php'
    usernameAVA = 'miguel.s'
    passwordAVA = 'miguelsantosMM26*'
    
    ava = Ava(urlAVA, usernameAVA, passwordAVA)
    
elif main == '2':
    urlManager = 'http://localhost:4200/login'
    usernameManager = '08234775170'
    passwordManager = '1111'
    
    manager = Manager(urlManager, usernameManager, passwordManager)
    
elif main[0] == '3':
    urlOnline = 'http://localhost:6988/Login/Login.aspx'
    usernameOnline = '08234775170'
    passwordOnline = '1111'
    
    if (main[2] == '1'):
        online = Online(urlOnline, usernameOnline, passwordOnline, 1)
    else:
        online = Online(urlOnline, usernameOnline, passwordOnline)
        
elif main == '4':
    urlChangeset = 'http://nccgtfs01:8080/tfs/NotaControl/_work'
    
    changesets = Changesets(urlChangeset)

elif main == '5':
    urlYoutube = 'https://www.youtube.com/feed/subscriptions'
    
    youtube = Youtube(urlYoutube)