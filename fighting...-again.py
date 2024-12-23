##INCOMPLETE

## Idea
# a challenging (not impossible), medieval fantasy game
# the player and enemy takes turns fighting
# the player can burn the enemy BUT the enemy can use poison
# use // in mathematical operations for rounded-down division

import random
import time

# In order: health [0], attack power [1], mana [2], stamina [3]
enemy = [100, 13, 5, 75]
player = [100, 14, 25, 100]

attempt = 0

stun = False # STUN
burn = False # BURN
burnTake = 0
burnMax = 5
poison = False # POISON
poisonTake = 0
poisonMax = 5

print("oh no enemy\n")
print("CONTROLS: attack, stun, block, dodge, heal, weaken, run\n")
## To do
# insert: attack [DONE], stun [DONE], block [DONE], dodge [DONE], heal [DONE], burn [DONE], poison, run [ DONE]
# mark "lucks" with "#- luck"
### FOCUS ON ENEMY TURNS
def inspecPlayer(): ### inspect player def
  print("PLAYER'S STATUS")
  print("HEALTH:", player[0])
  print("ATTACK POWER:", player[1])
  print("MANA:", player[2])
  print("STAMINA:", player[3])
def inspecEnemy(): ### inspect enemy def
  print("ENEMY'S STATUS")
  print("HEALTH:", enemy[0])
  print("ATTACK POWER:", enemy[1])
  print("MANA:", enemy[2])
  print("STAMINA:", enemy[3])

def attack(): ### attack def
  luck = random.randint(1, 100) #- luck
  
  if luck >= 80: ## SUCCESSFUL ATTACK
    print("successful attack!")
    enemy[0] -= player[1]
  elif luck <= 20: ## COUNTER
    print("enemy countered! u attack urself!")
    player[0] -= player[1]
  else: ## MISSED ATTACK
    print("miss")

def stun(): ### stun def
  luck = random.randint(1, 100) #- luck
  
  if luck <= 40: ## SUCCESSFUL STUN
    print("successful stun!")
    stun == True
  elif luck >= 85: ## ENEMY HITS
    print("enemy hits you!")
    player[0] -= enemy[1]
  else: ## MISSED STUN
    print("stun missed!")

def block(): ### block def
  luck = random.randint(1, 100) #- luck
  
  if luck >= 80: ## COUNTER ENEMY
    print("player countered! enemy hits itself!")
    enemy[0] -= enemy[1]
  elif luck <= 20: ## HIT
    print("enemy hits u!")
    player[0] -= enemy[1]
  elif luck <= 45: ## DAMAGE REDUCED
    print("enemy attacks! damage reduced!")
    player[0] -= random.randint(enemy[1] // 2, enemy[1] - 3)
  else: ## SUCCESSFUL BLOCK
    print("successful block!")

def dodge(): ### dodge def
  luck = random.randint(1, 100) #- luck
  
  if luck <= 30: ## TOO SLOW
    print("enemy hits u!")
    player[0] -= enemy[1] + 2
  else: ## SUCCESSFUL DODGE
    print("successful dodge!")
def heal(): ### heal def
  luck = random.randint(1, 100) #- luck
  
  if luck >= 85: ## EXPLOSION
    print("an explosion occurs! u & enemy take damage!")
    player[0] -= 27
    enemy[0] -= 27
  elif luck < 20: ## CRITICAL HIT
    print("enemy critically hits u!")
    player[0] -= enemy[1] + 6
  else: ## SUCCESSFUL HEAL
    print("you heal some hp!")
    if player[0] >= 73:
      player[0] = 100
    else:
      player[0] += random.randint(21, 27)

def burn(): ### burn def
  luck = random.randint(1, 100) #- luck
  
  if luck <= 20: ## ENEMY HITS (W/ EXTRA DAMAGE)
    print("fail! enemy hits you w/ extra damage!")
    player[0] -= enemy[1] + 2
  elif luck <= 60: ## SUCCESSFUL BURN
    print("successful burn! enemy is burning!")
    burn = True
  else: ## MISS
    print("miss")

def enemyAttack():
  luck = random.randint(1, 100) #- luck

  if luck >= 85: ## SUCCESSFUL ATTACK
    print("enemy attacks!")
    player[0] -= enemy[1]
  elif luck <= 15: ## COUNTER ATTACK
    print("you counter! enemy attacks itself")
    enemy[0] -= enemy[1]
  else: ## MISS
    print("it missed!")

def enemyStun(): ###### CONTINUE ON THIS
  luck = random.randint(1, 100) #- luck

while True: ##### MAIN GAME #####
  inspecPlayer()
  print("\n")
  inspecEnemy()
  print("\n")

  print("ATTEMPT", attempt)
  
  ### PLAYER'S TURN ###
  if stun == True: ## STUNNED
    print("you are stunned! your turn is skipped")
  else: ## NOT STUNNED
    print("what will u do?")
    choice = input("ACTION: ")
    print()
    
    if choice.lower() == "attack": ### ATTACK ###
      if player[3] < 25: # not enough stamina
        print("you dont have enough stamina")
      else:
        attack()
        player[3] -= 25
    elif choice.lower() == "stun": ### STUN ###
      if player[3] < 30: # not enough stamina
        print("you dont have enough stamina")
      else:
        stun()
        player[3] -= 30
    elif choice.lower() == "block": ### BLOCK ###
      block()
      player[3] += 20
      player[2] += 6
    elif choice.lower() == "dodge": ### DODGE ###
      if player[3] < 35: # not enough stamina
        print("you don't have enough stamina")
      else:
        dodge()
        player[2] += 16
        player[3] -= 35
    elif choice.lower() == "heal": ### HEAL ###
      if player[2] < 45: # not enough  mana
        print("you don't have enough mana")
      else:
        heal()
        player[2] -= 45
    elif choice.lower() == "burn": ### BURN ###
      if player[2] < 42: # not enough  mana
        print("you don't have enough mana")
      else:
        burn()
        player[2] -= 42
    elif choice.lower() == "run": ### COWARDICE ###
      print("Coward!")
    else: ## ERROR
      print("not an action or you mispelt it.")
    attempt += 1
    
    if poison == True: ### POISON
      print()
      player[0] -= 3
      
      print("poison effects take place! -3 hp!")
      
      if poisonTake == poisonMax:
        print("poison effects run out!")
        poison = False
        poisonTake = 0
      else:
        poisonTake += 1
    print("---")

  ### ENEMY'S TURN ###
  if stun == True: ## STUNNED (ENEMY)
    print("the enemy is stunned! its turn is skipped")
  else:
    print("it is the enemy's turn")
    print("...")
    time.sleep(1.5)
    
    enemchoice = random.randint(1, 100)
  print("\n-------------------------")
