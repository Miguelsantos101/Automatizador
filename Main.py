from src.Ava import Ava
from src.Online import Online
from src.Manager import Manager
from src.Changesets import Changesets
from src.Youtube import Youtube

# 1 = AVA

# 2 = Manager

# 3 = Online
# 3-1 = Solicitação de Cadastro

# 4 = Changesets

# 5 = Youtube

main = "3-1"

if main == "1":
    urlAVA = "https://ava.ufms.br/login/index.php"
    usernameAVA = "miguel.s"
    passwordAVA = "miguelsantosMM26*"

    ava = Ava(urlAVA, usernameAVA, passwordAVA)

elif main == "2":
    urlManager = "http://localhost:4200/login"
    usernameManager = "08234775170"
    passwordManager = "1111"

    manager = Manager(urlManager, usernameManager, passwordManager)

elif main[0] == "3":
    urlOnline = "http://localhost:6988/Login/Login.aspx"
    usernameOnline = "08234775170"
    passwordOnline = "1111"

    if main[2] == "1":
        online = Online(urlOnline, usernameOnline, passwordOnline, 1)
    else:
        online = Online(urlOnline, usernameOnline, passwordOnline)

elif main == "4":
    urlChangeset = "http://nccgtfs01:8080/tfs/NotaControl/ISS%20ONLINE/_backlogs/TaskBoard/Online%20ISS%20Vers%C3%A3o%20-%20Junho%202023/Online%20ISS%20V4.6.3?_a=requirements"

    changesets = Changesets(urlChangeset)

elif main == "5":
    urlYoutube = "https://www.youtube.com/feed/subscriptions"

    youtube = Youtube(urlYoutube)
