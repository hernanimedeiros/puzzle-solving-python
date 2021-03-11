print("Disclaimer: Este programa é apenas uma prova\n"+
      "de conceito e a minha estreia absoluta em Python.\n"+
      "Não tive qualquer cuidado com a apresentação e\n"+
      "muito menos com design patterns (DRY aqui foi 0).\n"+
      "O programa está muito ao estilo funcional (tipo C)\n" +
      "mas muito mal escrito e otimizado.\n" +
      "Se algum dia meter a coisa bonita será \"mau sinal\" \n"+
      "porque o meu foco está longe de ser Python.\n"+
      "Fora os apartes, gostei da linguagem e vejo Python\n"+
      "como um substituto de Portugol em futuras edições do curso!\n"
      "P.S. Aguentem mais um bocado que a Força Bruta está a trabalhar\n")
# Initialize list
enigma = [0,0,0,0,0,0,0,0,0,0]
enigmaBrute = [0,0,0,0,0,0,0,0,0,0]

# Stop conditions for while loop
def stop_conditions():
    for x in enigma:
        #print(enigma)
        if enigma.count(x)>1:
                return 0


# Main conditions
while(stop_conditions()==0):

    # A
    if enigma[8] > enigma[9]:
        if 7 in enigma:
            enigma[0] = 3
        elif 3 in enigma:
            enigma[0] = 7
    else:
        if 4 in enigma:
            enigma[0] = 8
        elif 8 in enigma:
            enigma[0] = 4

    # B
    if enigma[9] > enigma[0]:
        if 9 in enigma:
            enigma[1] = 0
        elif 0 in enigma:
            enigma[1] = 9
    else:
        if 3 in enigma:
            enigma[1] = 2
        elif 2 in enigma:
            enigma[1] = 3

    # C
    if enigma[0] > enigma[1]:
        if 5 in enigma:
            enigma[2] = 7
        elif 7 in enigma:
            enigma[2] = 5
    else:
        if 1 in enigma:
            enigma[2] = 0
        elif 0 in enigma:
            enigma[2] = 1

    # D
    if enigma[1] > enigma[2]:
        if 2 in enigma:
            enigma[3] = 1
        elif 1 in enigma:
            enigma[3] = 2
    else:
        if 9 in enigma:
            enigma[3] = 4
        elif 4 in enigma:
            enigma[3] = 9
    enigma[3] = 4 #Force to condition values in the center of the array


    # E
    if enigma[2] > enigma[3]:
        if 6 in enigma:
            enigma[4] = 9
        elif 9 in enigma:
            enigma[4] = 6
    else:
        if 5 in enigma:
            enigma[4] = 3
        elif 3 in enigma:
            enigma[4] = 5

    # F
    if enigma[3] > enigma[4]:
        if 4 in enigma:
            enigma[5] = 2
        elif 2 in enigma:
            enigma[5] = 4
    else:
        if 1 in enigma:
            enigma[5] = 6
        elif 6 in enigma:
            enigma[5] = 1

    # G
    if enigma[4] > enigma[5]:
        if 6 in enigma:
            enigma[6] = 5
        elif 5 in enigma:
            enigma[6] = 6
    else:
        if 7 in enigma:
            enigma[6] = 0
        elif 0 in enigma:
            enigma[6] = 7

    # H
    if enigma[5] > enigma[6]:
        if 4 in enigma:
            enigma[7] = 1
        elif 1 in enigma:
            enigma[7] = 4
    else:
        if 9 in enigma:
            enigma[7] = 8
        elif 8 in enigma:
            enigma[7] = 9

    # I
    if enigma[6] > enigma[7]:
        if 8 in enigma:
            enigma[8] = 0
        elif 0 in enigma:
            enigma[8] = 8
    else:
        if 7 in enigma:
            enigma[8] = 6
        elif 6 in enigma:
            enigma[8] = 7
    enigma[8] = 0 #Force to condition values in the center of the array

    # J
    if enigma[7] > enigma[8]:
        if 8 in enigma:
            enigma[9] = 3
        elif 3 in enigma:
            enigma[9] = 8
    else:
        if 5 in enigma:
            enigma[9] = 2
        elif 2 in enigma:
            enigma[9] = 5

else:
    print("Resposta -> Modo Iterativo:")
    print("[A, B, C, D, E, F, G, H, I, J]")
    print(enigma)
    print("\n")




generator = range(8274000000, 10000000000, 1)
counter=0
for number in generator:
    tempString = str(number)
    k = 0

    for x in tempString:
        enigmaBrute[k] = int(x)
        k+=1

    # A
    if enigmaBrute[8] > enigmaBrute[9]:
        if(enigmaBrute[0] == 3 or enigmaBrute[0] == 7):
            counter+=1
    else:
        if(enigmaBrute[0] == 8 or enigmaBrute[0] == 4):
            counter += 1
    # B
    if enigmaBrute[9] > enigmaBrute[0]:
        if(enigmaBrute[1] == 0 or enigmaBrute[1] == 9):
            counter+=1
    else:
        if(enigmaBrute[1] == 2 or enigmaBrute[1] == 3):
            counter += 1

    # C
    if enigmaBrute[0] > enigmaBrute[1]:
        if(enigmaBrute[2] == 5 or enigmaBrute[2] == 7):
            counter+=1
    else:
        if(enigmaBrute[2] == 0 or enigmaBrute[2] == 1):
            counter += 1

    # D
    if enigmaBrute[1] > enigmaBrute[2]:
        if(enigmaBrute[3] == 1 or enigmaBrute[3] == 2):
            counter+=1
    else:
        if(enigmaBrute[3] == 4 or enigmaBrute[3] == 9):
            counter += 1

    # E
    if enigmaBrute[2] > enigmaBrute[3]:
        if(enigmaBrute[4] == 6 or enigmaBrute[4] == 9):
            counter+=1
    else:
        if(enigmaBrute[4] == 3 or enigmaBrute[4] == 5):
            counter += 1

    # F
    if enigmaBrute[3] > enigmaBrute[4]:
        if(enigmaBrute[5] == 2 or enigmaBrute[5] == 4):
            counter+=1
    else:
        if(enigmaBrute[5] == 1 or enigmaBrute[5] == 6):
            counter += 1

    # G
    if enigmaBrute[4] > enigmaBrute[5]:
        if(enigmaBrute[6] == 5 or enigmaBrute[6] == 6):
            counter+=1
    else:
        if(enigmaBrute[6] == 0 or enigmaBrute[6] == 7):
            counter += 1

    # H
    if enigmaBrute[5] > enigmaBrute[6]:
        if(enigmaBrute[7] == 1 or enigmaBrute[7] == 4):
            counter+=1
    else:
        if(enigmaBrute[7] == 8 or enigmaBrute[7] == 9):
            counter += 1

    # I
    if enigmaBrute[6] > enigmaBrute[7]:
        if(enigmaBrute[8] == 0 or enigmaBrute[8] == 8):
            counter+=1
    else:
        if(enigmaBrute[8] == 6 or enigmaBrute[8] == 7):
            counter += 1

    # J
    if enigmaBrute[7] > enigmaBrute[8]:
        if (enigmaBrute[9] == 3 or enigmaBrute[9] == 8):
            counter += 1
    else:
        if (enigmaBrute[9] == 2 or enigmaBrute[9] == 5):
            counter += 1

    # NOT REPEAT
    counterSingle=0
    for x in enigmaBrute:
        if enigmaBrute.count(x) == 1:
            counterSingle += 1
        if counterSingle>9:
            counter += 1

    #print(enigmaBrute)
    #print(counter)

    #STOP CONDITIONS
    if counter>10:
        print("\nResposta -> Modo Força Bruta:")
        print("[A, B, C, D, E, F, G, H, I, J]")
        print(enigmaBrute)
        #print(counter)
        break
    else:
        counter=0

