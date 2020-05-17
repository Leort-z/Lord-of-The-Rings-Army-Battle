#Leonardo Rodrigues Teixeira, Paradigmas de Programação - 2020/1 - Introdução Python - Desafio Lord of The Rings

import random

#----------- Personagens e Exércitos -----------#

def lifePointsElf(): #Define os pontos de vida da raça Elfo aleatoriamente
    return random.randrange(20, 40)

def lifePointsDwarf(): #Define os pontos de vida da raça Anão aleatoriamente
    return random.randrange(30, 50)

def createELf(id): #Cria um personagem da raça Elfo
    elf = {'id': id, 'lifePoints': lifePointsElf(), 'attackPoints': 16, 'race': 'Elfos da Primeira Era', 'alive': True}
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

def findAttacked(armyDef): #Encontra um adversário que possa ser atacado
    attacked = random.choice(armyDef)
    while(attacked['alive'] == False):
        attacked = random.choice(armyDef)
    if(attacked['alive']):
        return attacked

def battle(armyAtk, armyDef): #Escolhe um adversário para cada personagem de cada exército e aplica os danos causados nos seus pontos de vidas máximos
        for character in armyAtk:
            if(character['alive']):
                attacked = findAttacked(armyDef)
                attacked['lifePoints'] -= character['attackPoints']
                #print("O " + character['race'] + " de número " + str(character['id']) + " atacou o " + attacked['race'] + " de id " + str(attacked['id']))

def checkSurvivors(army): #Checa os sobreviventes após uma batalha
    count = 0
    for character in army:
        if(character['alive']):
            count += 1
    print("Restaram: " + str(count) + " " + character['race'] + " vivos.")

def startRound(armyElf, armyDwarf): #Inicia uma batalha

    battle(armyElf, armyDwarf)
    battle(armyDwarf, armyElf)

    setAlive(armyElf)
    setAlive(armyDwarf)

    #printArmy(armyElf)
    #printArmy(armyDwarf)

    print("")
    checkSurvivors(armyElf)
    checkSurvivors(armyDwarf)

def checkWinner(armyElf, armyDwarf): #Checa o vencedor entre os dois exércitos
    if(isDefeated(armyElf)):
        print("\nO exército dos Elfos foi derrotado.\n")
    elif(isDefeated(armyDwarf)):
        print("\nO exército dos Anões foi derrotados.\n")
    else:
        print("\n Ambos exércitos foram derrotados.\n")

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