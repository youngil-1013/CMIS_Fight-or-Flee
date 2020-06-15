#New things I've learned: 
#1. random.randint
#The randint function, which comes from the random package generates a number between two numbers. it can be used by calling random.randint(initial, final, step). The initial value sets the first number(inclusive) and the final value sets the last number(also inclusive). The step value determine how much each value will "skip". For example, random.randint(0, 10, 2) will return a value from {0, 2, 4, 6, 8, 10}. Even though the name of the function is randint, it is not "truly" random in the sense that a pattern can be found if the program is run several time(This goes onto crpytography, so I'll end here.)
#2. time.sleep 
#The sleep function does what it sounds like. It "stops" the program for a set amount of time and resumes it after the set time. It can be used by calling time.sleep(time). The time value can be either an integer or a float.
#Note: If a recursion error happens during the game, it is because the monster's defense is equal or greater than the player's damage. I haven't found a way to solve this, so if such an error occurs, it is game over.

#Mob Data
#level, hp, str, def, xp
import random
import time
null = [0, 0, 0, 0, 0]
OldFrog = ("Old Frog", [0, 1, 5, 2, 5])
Fly = ("Fly", [0, 1, 5, 2, 5])
Goblin = ("Goblin", [1, 1, 6, 1, 7])
TwistedFlower = ("Twisted Flower", [1, 1, 5, 0, 7])
Golem = ("Golem", [2, 3, 7, 2, 8])
WierdFish = ("Wierd Fish", [2, 4, 7, 1, 8])
FireGolem = ("Fire Golem", [3, 7, 8, 2, 10])
Ghost = ("Ghost", [3, 5, 8, 0, 10])
Dragon = ("Dragon", [4, 10, 9, 2, 10])
ChariotRider = ("Chariot Rider", [4, 9, 9, 2, 10])

#Equip Data
#str, def
nullequip = []
WoodenShield = ("Wooden Shield", [0, 0.5])
WoodenWeapon = ("Wooden Weapon", [0.5, 0])
StoneShield = ("Stone Shield", [0, 0.7])
StoneWeapon = ("Stone Weapon", [0.7, 0])
MetalShield = ("Metal Shield", [0, 1.0])
MetalWeapon = ("Metal Weapon", [1.0, 0])
HeroShield = ("A Hero's Shield", [0, 1.0])
HeroWeapon = ("A Hero's Weapon", [1.0, 0])
LegendShield = ("Lost Legend Shield", [0, 1.0])
LegendWeapon = ("Lost Legend Weapon", [1.0, 0])

def intro():
  print ("Welcome to 'Fight or Flee!'")
  character = input("What class would you like to be? Warrior: 1, Archer: 2")
  if character == "1":
    PlayerData = [1, 15, 2, 2, 0]
  if character == "2":
    PlayerData = [1, 10, 4, 1, 0]
  return PlayerData
  
def fight(PD):
  Mob = random.randint(1, 2)
  mob = null
  if PD[4] <= 10:
    if Mob == 1:
      mob = OldFrog
      BattleScene(mob, PD)
    if Mob == 2:
      mob = Fly
      BattleScene(mob, PD)
  if PD[4] > 10 and PD[4] <= 25:
    if Mob == 1:
      mob = Goblin
      BattleScene(mob, PD)
    if Mob == 2:
      mob = TwistedFlower
      BattleScene(mob, PD)
  if PD[4] > 25 and PD[4] <= 40:
    if Mob == 1:
      mob = Golem
      BattleScene(mob, PD)
    if Mob == 2:
      mob = WierdFish
      BattleScene(mob, PD)
  if PD[4] > 40 and PD[4] <= 60:
    if Mob == 1:
      mob = Ghost
      BattleScene(mob, PD)
    if Mob == 2:
      mob = FireGolem
      BattleScene(mob, PD)
  if PD[4] > 60 and PD[4] <= 80:
    if Mob == 1:
      mob = Dragon
      BattleScene(mob, PD)
    if Mob == 2:
      mob = ChariotRider
      BattleScene(mob, PD)

#level, hp, str, def, xp
def BattleScene(Entity, Player):
  Fight = input("""
A level {} {} appears, it has {} health, {} strength and {} armour.
You are level {}, have {} health, {} strength and {} armour
Would you fight it? (Y/N)""".format(Entity[1][0], Entity[0], Entity[1][1],Entity[1][2],Entity[1][3], Player[0], Player[1], Player[2], Player[3]))
  if Fight == "Y":
    result(Player, Entity)
  if Fight == "N":
    Death()
    
def result(Player, Entity):
  HPPlayer = CalPlayerHP(Player, Entity)
  HPEntity = CalEntityHP(Player, Entity)
  if HPPlayer > 0 and HPEntity <= 0:
      contin(Player, Entity, HPPlayer)
  if HPPlayer > 0 and HPEntity > 0:
    result(Player, Entity)
  if HPPlayer <= 0:
    Death()

def EndFightCal(Weap, Shield):
    EquipN = random.randint(1,5)
    if EquipN == 1 or 3:
      NewE = Weap
    if EquipN == 2:
      NewE = Shield
    nullequip.append(NewE)
    return NewE
    
def EquipList(equips):
  reply = input("Would you like to view your items?(Y/N)")
  if reply == "Y":
    print ("+--------------------items--------------------+")
    for equip in equips:
      print ("""{}: {} Strenth, {} Armour
      """.format(equip[0], equip[1][0], equip[1][1]))
  print ("+---------------------------------------------+")

def StatChoice():
  List = [0, 0, 0]
  choice = int(input("""What stat would you like to increase?
Stregth: (1) gives 1 point to Strength
Armour: (2) gives 1 point to Armour
Health: (3) retrieves 7 points of Health
  """))
  if choice == 1:
    List = [1, 0, 0]
  elif choice == 2:
    List = [0, 1, 0]
  elif choice == 3:
    List = [0, 0, 7]
  else:
    print("invalid input!")
    StatChoice()
  return List
  
def contin(Playerdata, Mobdata, NewHP):
  GainXP = Mobdata[1][4]
  XP = Playerdata[4] + GainXP
  print ("""
You gained {} XP!
""".format(GainXP))
  if XP > 0 and XP <20 :
    NHP = 1
    NewHP += NHP
    NewE = EndFightCal(WoodenWeapon, WoodenShield)
  if XP >= 20 and XP <40 :
    NHP = 2
    NewHP += NHP
    NewE = EndFightCal(StoneWeapon, StoneShield)
  if XP >= 40 and XP <60 :
    NHP = 3
    NewHP += NHP
    NewE = EndFightCal(MetalWeapon, MetalShield)
  if XP >= 60 and XP <80 :
    NHP = 4
    NewHP += NHP
    NewE = EndFightCal(LegendWeapon, LegendShield)
  if XP >= 80:
    End(nullequip)
    exit(0)
  Playerdata.remove(Playerdata[4])
  Playerdata.insert(4, XP)
  time.sleep(1)
  print ("""Your current stats:
Health: {}
Strength: {}
Armour: {}
Experience: {}
""".format(Playerdata[1], Playerdata[2], Playerdata[3], Playerdata[4]))
  List = StatChoice()
  time.sleep(1)
  Playerdata.remove(Playerdata[1])
  Playerdata.insert(1, NewHP)
  Playerdata[1] += List[2]
  NewSTR = Playerdata[2] + NewE[1][0] + List[0]
  NewDEF = Playerdata[3] + NewE[1][1] + List[1]
  Playerdata.remove(Playerdata[2])
  Playerdata.insert(2, NewSTR)
  Playerdata.remove(Playerdata[3])
  Playerdata.insert(3, NewDEF)
  print ("""
You retrieved {} HP
You found a {}

Your current stats:
Health: {}
Strength: {}
Armour: {}
Experience: {}
""".format(NHP, NewE[0], Playerdata[1], Playerdata[2], Playerdata[3], Playerdata[4]))
  EquipList(nullequip)
  fight(Playerdata)

def Death():
  print ("""
    You took the easy way out.
          ________  
         |        |  
        |          |
        |   RIP    |    _   _
        |          |   *+* *+*
        |          |    |   |
    """)
  
def End(equipments):
  EquipP = 0
  for equipment in equipments:
    EquipP += equipment[1][0] + equipment[1][1]
  print ("""Good job, you've beaten the game. Here is your overall point: {}""".format(EquipP))


def CalPlayerHP(Player, Entity):
  PlayerhpLeft = Player[1] - (Entity[1][2] - Player[3])
  return PlayerhpLeft

def CalEntityHP(Player, Entity):
  EntityhpLeft = Entity[1][1] - (Player[2] - Entity[1][3])
  return EntityhpLeft

def main():
  fight(intro())
  exit(0)
  
main()
