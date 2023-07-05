#KLADD 
kommandoer = []


def start_kommando():
	kommandoer.append("en")
	kommandoer.append("conf t")


test_cisco = open("running-config.txt", "r")
tekst = test_cisco.read()

#print (tekst)
tull = []
for ch in tekst:
	tull.append(ch)
	if ch == "hostname Appelsin":
		start_kommando()
		kommandoer.append(ch)

	#print(ch.join(""))

test_cisco.close()
print(tull)








   # if ch == "interface".lower(): 
	#    kommandoer.append("int GI\n")
	
	
print(kommandoer)