# Facebook_Scraping
 Scraping dynamique
---
title: "| Facebook-Scraping : \n| Dites \"\\textit{Ciao!}\" au contact qui vous supprime
  de la liste d'amis  \n"
author: "Lucic A., Moezzibadi, M., Mbengue M."
date: "Mars 2021"

Dans le script on utilise deux outils pricipals:
* Selenium automatise l'interaction du navigateur Web à partir de python en utilisant un exécutable (*webdriver*) afin de contrôler *Chrome (Firebox)* (on clic sur les boutons avec Selenium).
* Beautifulsoup récupére l'information d'une balise HTML précise

Liens outils :

* [beautifulsoup](https://pypi.org/project/beautifulsoup4/)
* [Selenium](https://www.selenium.dev)
* [chromedriver](https://chromedriver.storage.googleapis.com/index.html)


# Introduction

### Objectifs :
1) Scraping des données sur Facebook
2) Comparer la liste d'amis périodiquement
3) Envoi-de message automatique 


# Autoriser l’automatisation à distance pour le navigateur

Avant tous, il faut autoriser l'automatisation à distance pour le navigateur. Google Chrome ou Firefox doit être installé sur votre ordinateur.

<center> 

![Automatisation à distance](Auto.png)

<center>

# Ligne de commande

Pour faire tourner le code dans Terminal on tape la commande suivante (remplacer *username* par votre identifiant):
```{python, echo=TRUE}
python FB.py -p -u 'username'
```
Ensuite il faut taper votre mot de passe (ça s'affiche pas dans Terminal pour des raisons de sécurité).

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



# Plan du code

![Différents parties du code](Struc.png)

# Scraping 
Having a blank slide at the end with the title "References" will put the detailed bibliography at the end.

See [@Robertson1956-wn] for details.

# References
