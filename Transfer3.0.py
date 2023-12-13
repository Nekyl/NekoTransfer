import getpass
from threading import Thread
import time
import os
import requests
from samino.acm import Acm
import aminofix
import pyfiglet
from progress.bar import IncrementalBar
from samino import Local, Client
from tqdm import tqdm

def colored(r=None, g=None, b=None, rb=None, gb=None, bb=None, text=None):
    if rb is None and gb is None and bb is None:
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    elif r is None and g is None and b is None:
        return f"\033[48;2;{rb};{gb};{bb}m{text}\033[0m"
    else:
        return f"\033[38;2;{r};{g};{b}m\033[48;2;{rb};{gb};{bb}m{text}\033[0m"

# Imprime o nome e a descrição do programa
print("\n" + colored(r=180, g=197, b=49, text=f"{pyfiglet.figlet_format('NekoTransfer', font='standard')}"))
print("   " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Release 3.0 ") + "         " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ Made by: Neko ❯ ") + "\n")

print("\033[1;40;44m ✨ Este é um transferidor estiloso feito pelo Neko.\n Tem alguma dúvida ou quer jogar conversa fora? \n Vem falar comigo no meu pv•-•)☕ \033[0m\n")

# Importa o módulo pkg_resources
import pkg_resources

# Define uma lista de pacotes que são necessários para o programa
required_packages = ["samino", "amino.fix", "pyfiglet", "progress", "requests", "tqdm"]

# Verifica se os pacotes já estão instalados
installed_packages = [pkg.key for pkg in pkg_resources.working_set]
missing_packages = [pkg for pkg in required_packages if pkg not in installed_packages]

# Se houver pacotes faltando, instala-os usando o pip
if missing_packages:
    print("\n" + "   " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ Instalando os pacotes necessários... ❯ ") + "\n")
    os.system(f"python -m pip install {' '.join(missing_packages)}")
    print("\n" + "   " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ Pacotes instalados com sucesso. ❯ ") + "\n")
else:
    print("\n" + "   " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ Todos os pacotes já estão instalados! ❯ ") + "\n")

# Continua com o resto do código

client = aminofix.Client()

email = input("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Insira seu e-mail: ") + " ")

password = getpass.getpass("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Digite sua senha: ") + " ")

client.login(email, password)
print("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ LOGADO ! ❯                                           "))

print("\n  " + colored(r=181, g=45, b=27, text=" Coin balance ") + colored(r=251, g=197, b=49, text=" ANTES ") + colored(r=181, g=45, b=27, text="Seus coins ") + colored(r=251, g=197, b=49, text=f"\033[1;40;44m {int(client.get_wallet_info().totalCoins)} "))

colored_text1 = "         " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" [1] Transferir via blog")
colored_text2 = "         " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" [2] Transferir via Fã club" + "\n" + "                "+ colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text="❮") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text= "Somente líderes")) + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text="❯")

print("\n" + colored_text1 + "\n" + colored_text2 + "\n")

x = int(input("Selecione: "))
if x == 1:
    link = input("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Insira o link do blog: ") + " ")
    parsed = client.get_from_code(link)
    comId = parsed.comId
    blog = parsed.objectId
    subclient = aminofix.SubClient(comId=comId, profile=client.profile)
    print("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ TUDO PRONTO ! ❯                                           "))
    
    print("\033[1;40;44m Transfere até 5k por vez \033[0m")

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
    print("\n  " + colored(r=181, g=45, b=27, text=" Coin balance ") + colored(r=251, g=197, b=49, text=" DEPOIS ") + colored(r=181, g=45, b=27, text="Seus coins ") + colored(r=251, g=197, b=49, text=f"\033[1;40;44m {int(client.get_wallet_info().totalCoins) }") + "\n")

elif x == 2:
    link = input("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Insira o link do perfil: ") + " ")
    parsed = client.get_from_code(link)
    comId = parsed.comId
    userId = parsed.objectId
    
    print("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ TUDO PRONTO ! ❯                                           "))
    
    print("\033[1;40;44m Tipo fracionado de transferência \n Envia parcelas únicas de 500 \n ILIMITADO \033[0m")
    
    amount = int(input("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Insira o valor: ") + " "))
    print("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ TRANSFERINDO COINS ... ❯                                ") + "\n\n")

    count_holder = [0]  # Using a list to hold a mutable variable

    def subscribe(userId):
        try:
            subclient.subscribe(userId)
            count_holder[0] += 500
        except Exception as e:
            print(f"Error subscribing: {e}")
            subscribe(userId)

    client = Client()
    mult = client.get_from_link(link)
    comId = mult.comId
    userId = mult.objectId
    client.login(email, password)
    coins = client.get_wallet_info().totalCoins
    subclient = Local(comId)

    if x == 2:
        acm = Acm(comId)

    if x == 2:
        acm.add_influencer(userId, monthlyFee=500)

    count_holder = [0]
    print()

    for i in tqdm(range(amount // 500)):
        subscribe(userId)

    print(f"Falha ao enviar: {amount - count_holder[0]}")
    print("\n\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ TRANSFERÊNCIA FINALIZADA ! ❯                               "))
    print("\n  " + colored(r=181, g=45, b=27, text=" Coin balance ") + colored(r=251, g=197, b=49, text=" DEPOIS ") + colored(r=181, g=45, b=27, text="Seus coins ") + colored(r=251, g=197, b=49, text=f"\033[1;40;44m {int(client.get_wallet_info().totalCoins) }") + "\n")

    if x == 2:
        acm.remove_influencer(userId)
else:
    print("Erro: Opção inválida")