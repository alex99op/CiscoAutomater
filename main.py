#import standard config txt
import shutil


def vlan():
	print("Write your Vlans")
 
 
def port():
	print("Wich port u want to use? 1,2,3 or 1-5")
 
 
def noshut():
	print("What ")

def hostname():
    hostname = input("Write your new hostname\n> ")
    #En kommando som endrer hostname i eksport fila.
     
def running_config():
	print("Showing current config made:")


def switch():
	"Main menu for switch"
	src_file = 'file.txt'
	dst_file = 'new_file.txt'

shutil.copy(src_file, dst_file)
    #En kommando som kopierer switch mal til ny output fil.
	print("\n### Switch menu ###")
	print("1. Create Vlan")	
	print("2. Create Trunk")
	print("3. Change noshutdown")
	print("4. Change hostname")
	print("5. Show config")
	user_input = input("> ")
  
	menu = {
	"1": lambda: vlan(),
	"2": lambda: port(),
	"3": lambda: noshut(),
	"4": lambda: hostname(),
	"5": lambda: running_config(),
	}
	return menu[user_input]() if user_input in menu else print("Did not understand that")


def ruter():
	print("ruter")


device = input("Ruter or Switch?\n> ").lower().strip()
if device == "switch":
	switch()
elif device == "ruter":
	ruter()
else:
	print("Did not understand what you wrote")
