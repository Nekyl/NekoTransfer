import getpass
import pyfiglet

def colored(r : int = None, g : int = None, b : int = None, rb : int = None, gb : int = None, bb : int = None, text = None):

    if rb is None and gb is None and bb is None:
        return "\033[38;2;{};{};{}m{}\033[0m".format(r, g, b, text)
    elif r is None and g is None and b is None:
        return "\033[48;2;{};{};{}m{}\033[0m".format(rb, gb, bb, text)
    else:
        return "\033[38;2;{};{};{}m\033[48;2;{};{};{}m{}\033[0m".format(r, g, b, rb, gb, bb, text)
print("\n" + colored(r = 180, g=197, b=49, text=f"""{pyfiglet.figlet_format("NekoTransfer", font="standard")}"""))

print("   " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Release 1.0 ") + "         " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❮ Made by: Neko ❯ ") + "\n")

email = "matheusalmeidaalmeida189@gmail.com"

password = "m01010011"

link = input("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Insira o link do perfil : ") + " ")

send = int(input("\n " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" Digite o valor: ")) + " ")

try:
	import samino
	from tqdm import tqdm
except:
	import os
	os.system("pip install aiohttp samino==2.5.2 tqdm")
	import samino
	from tqdm import tqdm


count = 0
def subscribe(userId):
	try:
		global count
		subclient.subscribe(userId)
		count += 500

	except:

		subscribe(userId)
		
colored_text1 = "         " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" [1] Entrar no Fã Clube")
colored_text2 = "         " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" [2] Líder comunidade")
colored_text3 = "         " + colored(r=17, g=10, b=3, rb=251, gb=197, bb=49, text=" ❯ ") + colored(rb=99, gb=13, bb=28, r=251, g=197, b=49, text=" [3] Link Blog")

print("\n" + colored_text1 + "\n" + colored_text2 + "\n" + colored_text3 + "\n")



x = int(input("Selecione: "))
if x == 1 or x == 2 or x == 3:
	print("\033[1;40;44m Transfer by Neko 2.0\033[0m")
	client = samino.Client()
	mult = client.get_from_link(link)
	comId = mult.comId
	userId = mult.objectId
	client.login(email, password)
	coins = client.get_wallet_info().totalCoins
	subclient = samino.Local(comId)
	coins = client.get_wallet_info().totalCoins
	print(f"\nSeus coins: {coins}\n")
	if x == 2:
		acm = samino.Acm(comId)
	if x == 2:
		acm.add_influencer(userId, monthlyFee = 500)
	count = 0
	print()
	for i in tqdm(range(send//500)):
		subscribe(userId)
	print(f"Falha ao enviar: {send - count}")
	if x == 2:
		acm.remove_influencer(userId)
else:
	print("Erro: Opção inválida")