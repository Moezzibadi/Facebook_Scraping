# Facebook_Scraping
 Scraping dynamique
---
title: "| Facebook-Scraping : \n| Dites \"\\textit{Ciao!}\" au contact qui vous supprime
  de la liste d'amis  \n"
author: "Lucic A., Moezzibadi, M., Mbengue M."
date: "Mars 2021"

Dans le script on utilise trois outils :
* Selenium automatise l'interaction du navigateur Web à partir de python en utilisant un exécutable (*webdriver*) afin de contrôler *Chrome (Firebox)* (on clic sur les boutons avec Selenium).
* Beautifulsoup récupére l'information d'une balise HTML précise

* [beautifulsoup](https://pypi.org/project/beautifulsoup4/)
* [Selenium](https://www.selenium.dev)
* [chromedriver](https://chromedriver.storage.googleapis.com/index.html)


Associated with the above are five functions to download/manage the binaries:

* Scraping des données sur Facebook  
* Comparer la liste d’amis périodiquement
* Envoi-de méssage automatique


# Introduction

- **Envie de savoir qui vous a supprimé de ses amis en FB!**

### Objectifs :
1) Scraping des données sur Facebook
2) Comparer la liste d'amis périodiquement
3) Envoi-de message automatique 


# Pourqoui Selenium?

- Facebook n'est pas un site régulier avec un budget limité
- Un système anti-bot très puissant
- urllib.request => Document HTML incomplet
- Selenium utilise un exécutable (*webdriver*) afin de contrôler *Chrome (Firebox)*
- Une combinaison de Beautiful Soup et Selenium pour le **Scraping dynamique**

### Importer les modules utilisés dans le but du Scraping 
```{python, echo=TRUE}
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```


# Plan du code

![Différents parties du code](Struc.png)

# Autoriser l’automatisation à distance pour le navigateur

Avant tous, il faut autoriser l'automatisation à distance pour le navigateur.

<center> 

![Automatisation à distance](Auto.png){width=27%}

<center>

# Ligne de commande

Pour faire tourner le code dans Terminal on tape la commande suivante (remplacer *username* par votre identifiant):
```{python, echo=TRUE}
python FB.py -p -u 'username'
```
Ensuite il faut taper votre mot de passe (ça s'affiche pas dans Terminal)

# Initialiser les fichiers des contacts
- 3 ème partie : Créer un message pop-up pour initialiser les fichiers 
```{python, eval=FALSE, size="tiny"}
import sys #Question pop up
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
```


# 4ème partie : Scraping 


- Désactiver les notifications
<center> 

![Demande d'affichage des notifications par FB](Notif.png){width=37%}

<center>

```{python, eval=FALSE, size="scriptsize"}
# Créer une instance de ChromeOptions class :
	options = webdriver.ChromeOptions()
# Ajouter chrome switch pour désactiver la notification :
	options.add_argument('--disable-notifications')
# Passer l'instance de ChromeOptions à ChromeDriver Constructor :
	browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
```

# 4ème partie : Scraping 

- Se connecter avec les identifiants:

```{python, eval=FALSE, size="scriptsize"}
browser.implicitly_wait(10)
browser.get("https://www.facebook.com")
time.sleep(3)
browser.find_element_by_xpath('//*[@title="Tout accepter"]').click()
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@title="Tout\
... accepter"]'))).click()
element=browser.find_element_by_id("email")
element.send_keys(user_id)
passwor=browser.find_element_by_id("pass")
passwor.send_keys(password)
time.sleep(3)
clicker=browser.find_element_by_xpath('//*[@name="login"]')
clicker.click()
```

\todo{Ça y est! On a réussi à se connecter.}

# Scraping 

- Charger la page de la liste d'amis:

```{python, eval=FALSE, size="scriptsize"}
	time.sleep(3)
	browser.get("https://www.facebook.com/me/friends") 
```

- *execute_script*: Une interface qui permet d'executer les commandes de JavaScript:

```{python, eval=FALSE, size="scriptsize"}
	time.sleep(3)
	##----Défiler vers le bas-------
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
```

# Scraping 
Having a blank slide at the end with the title "References" will put the detailed bibliography at the end.

See [@Robertson1956-wn] for details.

# References
