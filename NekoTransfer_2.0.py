# ------------------- MASSIVE COINS  TRANSFER v2.0 -------------------

import getpass
from threading import Thread
import aminofix
import pyfiglet
import os
import time
from progress.bar import IncrementalBar

def colored(r : int = None, g : int = None, b : int = None, rb : int = None, gb : int = None, bb : int = None, text = None):

    if rb is None and gb is None and bb is None:
        return "\033[38;2;{};{};{}m{}\033[0m".format(r, g, b, text)
    elif r is None and g is None and b is None:
        return "\033[48;2;{};{};{}m{}\033[0m".format(rb, gb, bb, text)
    else:
        return "\033[38;2;{};{};{}m\033[48;2;{};{};{}m{}\033[0m".format(r, g, b, rb, gb, bb, text)

print("\n" + colored(r = 180, g=197, b=49, text=f"""{pyfiglet.figlet_format("NekoTransfer", font="standard")}"""))

print("   " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Release 2.0 ") + "         " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ Made by: Neko ❯ ") + "\n")

client = aminofix.Client()

email = input("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Insira seu e-mail: ") + " ")

password = getpass.getpass("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Digite sua senha: ") + " ")

link = input("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Insira o link do blog: ") + " ")

client.login(email, password)

parsed = client.get_from_code(link)
comId = parsed.comId
blog = parsed.objectId

subclient = aminofix.SubClient(comId = comId, profile = client.profile)

print("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ LOGADO ! ❯                                           "))

print("\n  " + colored(r=181, g=45, b=27, text=" Coin balance ") + colored(r=251, g=197, b=49, text="antes ") + colored(r=181, g=45, b=27, text="Seus coins ") + colored(r=251, g=197, b=49, text=f"{int(client.get_wallet_info().totalCoins)}"))

amount = int(input("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Insira o valor: ") + " "))

print("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ TRANSFERINDO COINS ... ❯                                ") + "\n\n")

divided = (amount // 500)

bar = IncrementalBar('   Transferindo', max=divided + 1)

for _ in range(divided):
    Thread(target=subclient.send_coins, args=(500, blog)).start()
    time.sleep(0.30)
    bar.next()

little_sum = amount % 500
if little_sum != 0:
    subclient.send_coins(little_sum, blog)
    bar.next()

bar.finish()

print("\n\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ TRANSFERÊNCIA FINALIZADA ! ❯                               "))

print("\n  " + colored(r=181, g=45, b=27, text=" Coin balance ") + colored(r=251, g=197, b=49, text="depois ") + colored(r=181, g=45, b=27, text="Seus coins ") + colored(r=251, g=197, b=49, text=f"{int(client.get_wallet_info().totalCoins)}") + "\n")

client.logout()
os._exit(0)
