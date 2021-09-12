# Cours 3 - MangoDB

## Installation 

### Linux

```bash
sudo apt install -y mongodb
```

Vérifier le fonctionnement du service

```bash
sudo systemctl status mongodb
```

L'information suivante devrait s'afficher

```bash
● mongodb.service - An object/document-oriented database
   Loaded: loaded (/lib/systemd/system/mongodb.service; enabled; vendor preset: 
   Active: active (running) since Fri 2020-03-13 14:58:30 EDT; 44s ago
     Docs: man:mongod(1)
 Main PID: 13458 (mongod)
    Tasks: 23 (limit: 4915)
   CGroup: /system.slice/mongodb.service
           └─13458 /usr/bin/mongod --unixSocketPrefix=/run/mongodb --config /etc

```

Pour désactiver mongoDB et le partir au besoin

```bash
sudo systemctl disable mongodb

sudo systemctl start mongodb
```

Vérifier la connection au serveur

```bash
$ mongo --eval 'db.runCommand({ connectionStatus: 1 })'

MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
{
	"authInfo" : {
		"authenticatedUsers" : [ ],
		"authenticatedUserRoles" : [ ]
	},
	"ok" : 1
}
```

### Windows

1- Ouvrez votre navigateur Web et allez sur : https://www.mongodb.com/

2- Cliquez sur le menu **Products** > **MongoDB Server**

3- Sélectionnez **MongoDB Community Server** (Version: current release, OS: Windows 64-bit, Package: MSI)

4- Cliquez sur le bouton **Download**

5- Enregistrez le fichier à télécharger et ensuite ouvrez-le pour exécuter l’installation

6- Cliquez sur le bouton **Next** sur la fenêtre d’installation

7- Cochez sur **_I accept the terms in the License Agreement_** et cliquez sur **Next**

8- Cliquez sur le bouton **Complete** et ensuite deux fois sur **Next**

9- Cliquez sur le bouton **Install** pour démarrer l’installation

10- Une fois l’installation terminée, cliquez sur **Finish**.

11- Vous aurez peut-être à redémarrer votre machine pour finaliser l’installation

**Note:** Lien vers le guide d’installation: <https://docs.mongodb.com/manual/administration/install-community/>

### PyMongo

```bash
python -m pip install pymongo
```

## Exemples

 - conn.py
 - ajouter.py
 - lireCollection.py

## Pour désactiver mongoDB et le partir au besoin

```bash
sudo systemctl disable mongodb

sudo systemctl start mongodb
```
## Ligne de commandes
Vérifier l'ajout avec les commandes suivantes:

```bash
$ mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
(...)
> show dbs
admin   0.000GB
config  0.000GB
demo    0.000GB
local   0.000GB
> use demo
switched to db demo
> show collections
contacts
> db.contacts.find()
{ "_id" : ObjectId("5e6bfd2b9248af44ddb06bde"), "nom" : "Gill", "prenom" : "Stephane", "telephone" : "15143895921", "email" : "Stephane.Gill@CollegeAhuntsic.qc.ca", "__v" : 0 }
> exit
bye
$
db.events.find().sort({date:-1, time:-1}).limit(10)
```

Effacer la base de données demo

```bash
> use demo
switched to db demo
> db.dropDatabase()
```

## Utiliser MongoDB pour la journalisation

- <https://www.mongodb.com/blog/post/mongodb-is-fantastic-for-logging>
- <https://www.mongodb.com/blog/post/capped-collections>


## Références
 - [https://pymongo.readthedocs.io/en/stable/tutorial.html](https://pymongo.readthedocs.io/en/stable/tutorial.html)
 - [https://pymongo.readthedocs.io/en/stable/](https://pymongo.readthedocs.io/en/stable/)
 - [https://pypi.org/project/pymongo/](https://pypi.org/project/pymongo/)



