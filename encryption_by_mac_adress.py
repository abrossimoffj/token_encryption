#Julien Abrossimoff 16/08/2020
#Module d'encryption de mdp/token basé sur l'adresse mac
from cryptography.fernet import Fernet
import uuid
import base64
import getpass


def crypt_password(filename):
    key = hex(uuid.getnode())
    #récupère l'adresse mac et la convertie en hexadécimal
    key = key + "=" * (32-len(key))
    #ajoute des = pour que la chaîne atteigne une taille de 32 (taille requise par la bibliothèque de fernet)
    key = base64.urlsafe_b64encode(key.encode())
    #encodage en bytes sur une base64
    cipher_suite = Fernet(key)
    #création de l'instance de fernet
    ciphered_text = cipher_suite.encrypt(getpass.getpass('Input token:').encode())
    #encryption du mdp/token donné en entrée qui a besoin d^etre exprimé en bytes
    with open(filename+'.bin', 'wb') as file_object:
        file_object.write(ciphered_text)
    #sauvegarde du mdp encrypté 


def decrypt_password(filename):
    with open(filename+'.bin', 'rb') as file_object:
        for line in file_object:
            encryptedpwd = line
    # récupération du token crypté dans le binaire
    key = hex(uuid.getnode())
    key = key + "=" * (32-len(key))
    key = base64.urlsafe_b64encode(key.encode())
    cipher_suite = Fernet(key)
    unciphered_text = cipher_suite.decrypt(encryptedpwd).decode("utf-8")
    print(unciphered_text)
    #decryptage du token : l'idée est de la passer directement dans les méthodes ayant besoin de login au lieu de laisser dans une variable



crypt_password("token")
decrypt_password("token")