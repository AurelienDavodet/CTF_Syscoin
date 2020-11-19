# CTF Syscoin

Un CTF (capture the flag) est un mode de jeu visant à enseigner la cybercécurité à travers des challenges. 

Ici, le challenge est orienté vers la crytomonnaie et la blockchain.

Le challenger dispose d'un accès à une cryptomonnaie fictive et fonctionnelle et d'un compte.
Ce compte (comme chaque compte) est représenté sous la forme d'une adresse, d'une clé privée et d'un montant.
Cela lui permet d'effectuter des transactions, d'accéder à la blockchain et aux différents comptes existants et de miner des transactions.

Objectif du challenge : Acheter le flag (représenté par un code secret) pour une valeur de 100 syscoins à l'adresse de Sysdream avec un des comptes disponibles (différent de celui qui est attribué au début)

Résolution : 

Pour atteindre cet objectif, le challenger doit s'identifier sous un autre compte, il doit pour cela connaître la clé publique mais surtout la clé privé de ce compte.

Comment récupérer cette clé privée ?

Ce challenge s'appuie sur l'attaque de Weiner du chiffrement RSA
attaque de Weiner => il est possible de retrouver la clé privée à l'aide de la clé publique en connaissant le modulo et l'exposant constituant cette dernière à condition que la clé privée soit faible (valeur inférieur tier de la puissance 1/4 du modulo)

Il faut donc dans un premier temps parcourir l'ensemble des adresses pour récuper le moduo et l'exposant de la clé publique vulnérable.
Puis, à l'aide d'un algorithme exploitant la faille de Wiener, en renseignant en entrée ces deux informations, on obtient la clé privée.

On peut alors se connecter au compte vulnérable et réaliser la transaction qui permet d'acheter le flag.
