from random import randint
import socket
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import Style
from colorama import init
init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
#First Function Is random

def ips() :
	while True :
		a = randint(0,225)
		b = randint(0,225)
		c = randint(0,225)
		d = randint(0,225)
		make = ('{}.{}.{}.{}'.format(a,b,c,d))
		print(make)
		with open('ips-random.txt','a') as file :
			file.write(make+'\n')
			file.close()

def check(i) :
		try :
			i = i.strip()
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(5)
			result = sock.connect_ex((i, 80))
			if str(result)!='0':
				print('{}[DEAD] {} '.format(fr,i))
			elif str(result)=='0':
				print('{}[LIVE] {} '.format(fg,i))
				with open('ips-Live.txt','a') as desk :
					desk.write(i+'\n')
					desk.close()
		except :
			pass
def go() :
  print("""  CHECKER IPS By muneebwanee
                      \n """)
  file_name = input("List Ips  ?  : ")
  TEXTList = open(file_name, 'r').read().splitlines()
  p = Pool(int(input('THREAD ? : ')))
  p.map(check, TEXTList)
def main() :
	print('\n \n [1] Random Ips \n \n [2] Checker Ips \n')
	choose = int(input('[+] Choose Number => '))
	if choose == 1 :
		ips()
	elif choose == 2 :
		go()
	else :
		main()
main()