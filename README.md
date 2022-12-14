[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# Développez une architecture back-end sécurisée en utilisant Django ORM
### Documentation sur Postman
> https://documenter.getpostman.com/view/20501016/VV51rtpy
### Instructions détaillant la configuration
#### Télécharger le projet
```
git clone https://github.com/GuillaumeFerreira/Projet_12.git
```
ou
> https://github.com/GuillaumeFerreira/Projet_12/archive/refs/heads/main.zip
#### Créer l'environnement virtuel
Sous macos ou linux
```
python3 -m venv env
```
Sous windows
```
python -m venv env
```
#### Activer l'environnement virtuel
Sous macos ou linux
```
source env/bin/activate
```
Sous windows
```
env\Scripts\activate.bat
```
#### Installer les librairies necessaires
```
pip install -r requirements.txt
```
#### Lancer le serveur
```
python manage.py runserver
```
### Panel administration
Vous pouvez accéder au panel d'administration de django avec le lien suivant:
#### Lien:
> http://127.0.0.1:8000/admin
### Points de terminaisons
Pour l'utilisation des points de terminaisons de l'api veuillez suivre la [documentation Postman](https://documenter.getpostman.com/view/20501016/VV51rtpy).
### Permissions

<table><tr><td colspan="2">Permissions</td><td>MANAGER</td><td>COMMERCIAL</td><td>SUPPORT</td></tr>
<tr><td rowspan="4">USER</td><td>CREATE</td><td>YES</td><td>NO</td><td>NO</td></tr>
<tr><td>READ</td><td>YES</td><td>NO</td><td>NO</td></tr>
<tr><td>UPDATE</td><td>YES</td><td>NO</td><td>NO</td></tr>
<tr><td>DELETE</td><td>YES</td><td>NO</td><td>NO</td></tr>
<tr><td rowspan="4">CLIENT</td><td>CREATE</td><td>YES</td><td>YES</td><td>NO</td></tr>
<tr><td>READ</td><td>YES</td><td>YES*</td><td>YES*</td></tr>
<tr><td>UPDATE</td><td>YES</td><td>YES*</td><td>NO</td></tr>
<tr><td>DELETE</td><td>YES</td><td>YES*</td><td>NO</td></tr>
<tr><td rowspan="4">CONTRACT</td><td>CREATE</td><td>YES</td><td>YES</td><td>NO</td></tr>
<tr><td>READ</td><td>YES</td><td>YES*</td><td>NO</td></tr>
<tr><td>UPDATE</td><td>YES</td><td>YES*</td><td>NO</td></tr>
<tr><td>DELETE</td><td>YES</td><td>YES*</td><td>NO</td></tr>
<tr><td rowspan="4">EVENT</td><td>CREATE</td><td>YES</td><td>YES</td><td>NO</td></tr>
<tr><td>READ</td><td>YES</td><td>YES*</td><td>YES*</td></tr>
<tr><td>UPDATE</td><td>YES</td><td>YES*</td><td>NO</td></tr>
<tr><td>DELETE</td><td>YES</td><td>YES*</td><td>NO</td></tr>
</table>

YES* --> Oui si l'objet lui est attribué

## Contribuer au projet
Ce projet fait partie dans de la formation Openclassrooms. N'hésitez pas à clôner la source et à contribuer avec vos propres fonctionnalités.
Pour toutes contibutions, veuillez utiliser black et flake8
#### Exécuter black
```
black projet-10
```
#### Exécuter flake8
```
flake8 projet-10
```
## Auteur

Guillaume Ferreira