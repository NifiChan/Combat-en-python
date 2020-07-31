from model.player import Player
from model.weapon import Weapon

hammer_ban = Weapon("hammer ban", 20)
player1 = Player("Poisson", 20, 3)

# donne un couteau faisant 3 dégats au joueur !
player1.set_weapon(hammer_ban)
print(player1.get_pseudo(), "s'est equipé de l'arme hammer ban")
player2 = Player("Bob", 20, 5)
print(player2.get_pseudo(), "dit : bande de fils de put* !")

player1.attack_player(player2)
print(player1.get_pseudo(), "ban", player2.get_pseudo())

print(player1.get_pseudo(), "/ Points de vie:", player1.get_health(), "/ Attaque:", player1.get_attack_value())
print(player2.get_pseudo(), "/ Points de vie:", player2.get_health(), "/ Attaque:", player2.get_attack_value())

if player1.get_health() < 0:
    print(player1.get_pseudo(),"est bannis.")
else:
    print(player1.get_pseudo(),"est toujours en vie")

if player2.get_health() < 0:
    print(player2.get_pseudo(),"est bannis.")
else:
    print(player2.get_pseudo(),"est toujours en vie")