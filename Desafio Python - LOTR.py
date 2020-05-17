#Leonardo Rodrigues Teixeira, Paradigmas de Programação - 2020/1 - Introdução Python - Desafio Lord of The Rings

import random

#----------- Personagens e Exércitos -----------#

def lifePointsElf(): #Define os pontos de vida da raça Elfo aleatoriamente
    return random.randrange(20, 40)

def lifePointsDwarf(): #Define os pontos de vida da raça Anão aleatoriamente
    return random.randrange(30, 50)

def createELf(id): #Cria um personagem da raça Elfo
    elf = {'id': id, 'lifePoints': lifePointsElf(), 'attackPoints': 16, 'race': 'Elfo', 'alive': True}
    return elf

def createDwarf(id): #Cria um personagem da raça Anão
    dwarf = {'id': id, 'lifePoints': lifePointsDwarf(), 'attackPoints': 12,  'race': 'Anão', 'alive': True}
    return dwarf

def isDefeated(army): #Verifica se o exército foi derrotado ou não
    for character in army:
        if(character['alive']):
            return False          
    return True

def setAlive(army): #Verifica e atualiza o status de vida do personagem
    for character in army:
        if (character['lifePoints'] <= 0):
            character['alive'] = False

def createArmy(armyElfAmount, armyDwarfAmount, armyElf, armyDwarf): #Cria os exércitos de acordo com a quantia informada pelo usuário 
    for i in range(armyElfAmount):
        armyElf[i] = createELf(i+1)

    for i in range(armyDwarfAmount):
        armyDwarf[i] = createDwarf(i+1)

def printArmy(army): #Exibe ID e pontos de vida de cada personagem de um exército
    for character in army:
        print(character['race'] + " " + str(character['id']) + ": " + str(character['lifePoints']))  

#----------- Batalha -----------#

def battle(armyAtk, armyDef): #Escolhe um adversário para cada personagem de cada exército e aplica os danos causados nos seus pontos de vidas máximos
        for character in armyAtk:
                attacked = random.choice(armyDef)
                attacked['lifePoints'] -= character['attackPoints']
                #print("O " + character['race'] + " de número " + str(character['id']) + " atacou o " + attacked['race'] + " de id " + str(attacked['id']))

def checkCasualities(army): #Checa e remove os mortos do exército
    armyRace = army[0]['race']
    armyLength = len(army)
    i = 0
    while(i < armyLength):
        if(army[i]['alive'] == False):
            army.pop(i)
            i -=1
            armyLength -=1
        i += 1
    checkSurvivors(army, armyRace)

def checkSurvivors(army, armyRace): #Checa os sobreviventes após uma batalha
    print("Restaram: " + str(len(army)) + " " + armyRace + " vivos.")

def startRound(armyElf, armyDwarf): #Inicia uma batalha

    battle(armyElf, armyDwarf)
    battle(armyDwarf, armyElf)

    setAlive(armyElf)
    setAlive(armyDwarf)

    #printArmy(armyElf)
    #printArmy(armyDwarf)

    print("")
    checkCasualities(armyElf)
    checkCasualities(armyDwarf)

def checkWinner(armyElf, armyDwarf): #Checa o vencedor entre os dois exércitos
    if(isDefeated(armyElf) == False):
        print("\nO exército dos Elfos foi vencedor.\n")
    elif(isDefeated(armyDwarf) == False):
        print("\nO exército dos Anões foi vencedor.\n")
    else:
        print("\nAmbos exércitos foram derrotados.\n")

def main():
    armyElfAmount = int(input("\nInforme a quantidade de soldados no exército Élfico: "))
    armyDwarfAmount = int(input("Informe a quantidade de soldados no exército Anão: "))
    armyElf = [0]*armyElfAmount
    armyDwarf = [0]*armyDwarfAmount
    createArmy(armyElfAmount, armyDwarfAmount, armyElf, armyDwarf)

    print("\nSituação inicial dos exércitos: \n")
    #printArmy(armyElf)
    #printArmy(armyDwarf)
    
    round = 1
    while((isDefeated(armyElf) == False) & (isDefeated(armyDwarf) == False)):
        print("\n----------Batalha de número: " + str(round) + "----------\n")
        startRound(armyElf, armyDwarf)
        round += 1

    checkWinner(armyElf, armyDwarf)
   
main()