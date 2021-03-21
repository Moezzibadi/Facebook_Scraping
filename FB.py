#Il faut autoriser l'automatisation à distance pour le navigateur
#python FB.py -p -u 'username'
import time
from bs4 import BeautifulSoup
#----
import sys #Question pop up
#----
import argparse,getpass
#----
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json #		pour stocker et importer la liste à chaque fois que le code se lance
#-----------------------------Timer-----------------------------------#
from datetime import datetime									                      	#
from threading import Timer										                      	#
															                                    		#
# x=datetime.today()										                        			#
# y=x.replace(day=x.day+1, hour=00, minute=2, second=0, microsecond=0)#
# delta_t=y-x												                             			#
# 																                                  	#
# secs=delta_t.seconds+1										                      		#
#---------------------------------------------------------------------#

class Password:

    DEFAULT = 'Prompt if not specified'

    def __init__(self, value):
        if value == self.DEFAULT:
            value = getpass.getpass('LDAP Password: ')
        self.value = value

    def __str__(self):
        return self.value

class PasswordPromptAction(argparse.Action):
    def __call__(self, parser, args, values, option_string=None):
        # If no value is given on the commandline prompt for password.
        if values:
            # Ideally a security warning could be generated here.
            setattr(args, self.dest, values)
        else:
            setattr(args, self.dest, getpass.getpass())

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-u', '--username', help='Specify username',
    default=getpass.getuser())
parser.add_argument("-p", "--password", type=str, action=PasswordPromptAction, nargs='?')
args = parser.parse_args()

#print(args.username, args.password)
user_id=args.username
password=args.password

#-------------
question="Est-ce que c'est la première fois que vous lancez le code? "

valid=True

def PopUp(question):
    valid = {"oui": True,"non": False}
    while True:
        sys.stdout.write(question)
        choix = input().lower()
        if choix in valid:
            return valid[choix]
        else:
            sys.stdout.write("Veuillez répondre par 'oui' ou par 'non'. ")
valid=PopUp(question) 
#-------------
def TROUVE_ENVOI(user_id,password):
  	     
	##-----Disable asking notification in chrome------
	options = webdriver.ChromeOptions()
	options.add_argument('--disable-notifications')
	##------------------------------------------------
	
	browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
	##------------------------------------------------
	browser.implicitly_wait(10)
	browser.get("https://www.facebook.com")
	time.sleep(3)
	browser.find_element_by_xpath('//*[@title="Tout accepter"]').click()
	
	WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@title="Tout accepter"]'))).click()
	
	
	
	element=browser.find_element_by_id("email")
	element.send_keys(user_id)
	
	passwor=browser.find_element_by_id("pass")
	passwor.send_keys(password)
	time.sleep(3)
	
	
	clicker=browser.find_element_by_xpath('//*[@name="login"]')
	clicker.click()
	
	
	
	time.sleep(3)
	
	browser.get("https://www.facebook.com/me/friends")
	
	time.sleep(3)
	##----Défiler vers le bas-------
	#execute_script: interface allows to execute JavaScript passed as string argument
	while True:
		browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
		time.sleep(1)
		browser.execute_script('window.scrollTo(0,0);')
		time.sleep(1)
		try:
			exit_command=browser.find_element_by_xpath("//*[contains(text(),'Photos de vous')]")
			break
		except:
			continue
	##---------------------------------
	source_page=browser.page_source
	
	soup=BeautifulSoup(source_page,'html.parser')
	friendList=soup.find_all('div',{'class':'buofh1pr hv4rvrfc'})#<div class="buofh1pr hv4rvrfc">
	nn=str(friendList).count('buofh1pr hv4rvrfc')
	amis2=[None] * nn
	Ids2=[None] * nn
	for i in range(0,nn):
		amis2[i]=re.findall('dir="auto">(.*?)</span></a></div><div',str(friendList[i]))
		Ids2[i]=re.findall('w" href="https:\/\/www\.facebook\.com\/(.*?)\/friends_mutual',str(friendList[i]))
		#Le cas de ID
		if not Ids2[i] : Ids2[i]=re.findall('w" href="https:\/\/www\.facebook\.com\/profile\.php\?id=(.*?)&amp',str(friendList[i]))
		if not Ids2[i] : Ids2[i]=re.findall('wi8" href="https:\/\/www\.facebook\.com/(.*?)" role="link" tabindex="0"><span',str(friendList[i]))
#----------lecture des fichiers----------
	if valid==False:	
		with open("List_amis.txt", "r") as ListAm:		
 			    amis1 = json.load(ListAm)
		with open("List_ID.txt", "r") as ListId:
  	    	 	Ids1 = json.load(ListId)		
#----------Mis à jour des fichiers---------
	with open("List_amis.txt", "w") as ListAm: 
		json.dump(amis2, ListAm)
	with open("List_ID.txt", "w") as ListAm: 
		json.dump(Ids2, ListAm)
		
	if valid==True: 
		print('Les fichiers sont crées')
		sys.exit()	
	
	ID=['']
	for i in amis1:
	    if i not in amis2: print(i, "t'a retiré de sa liste") 
	for i in Ids1:
	    if i not in Ids2: ID=i 
	ID=str(ID)	
	ID=ID.replace("'", "")
	ID=ID.replace('[', '')
	ID=ID.replace(']', '')
	
	#-------------Envoie de message---------
	browser.get('https://www.facebook.com/messages/t/'+ID)
	message="Ciao mon ami(e), Merci de ne pas répondre à ce message automatique."
	time.sleep(0.1)
	message_box=browser.find_element_by_css_selector('div.notranslate._5rpu')
	message_box.send_keys(message)
	time.sleep(10)
	Envoi=browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
	Envoi.click()
	time.sleep(5)
TROUVE_ENVOI(user_id,password)
# t = Timer(secs, TROUVE_ENVOI)
# t.start()
# 
