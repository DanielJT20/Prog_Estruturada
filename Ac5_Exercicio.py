


import random as rd

def main():
    rodada = 1
    vida1 = 100
    defe = rd.randint(1, 5)
    vida2 = rd.randint(60, 80)
    atk1 = rd.randint(10, 20)
    atk2 = rd.randint(20, 30)
    print("Aventureiro:", vida1, "- att ", atk1)
    print("Monstro:", vida2, "- att", atk2)
    print("Rodada", rodada)
    while vida1 > 0 and vida2 > 0:
        rodada += 1
        vida2 -= rd.randint(1, atk1)
        vida1 -= ((rd.randint(1, atk2)) - defe)
        print("Aventureiro: vida", max(vida1, 0), "- att", atk1)
        print("Monstro: vida", max(vida2, 0), "- att", atk2)
        print("Rodada:", rodada)
      
    if vida1 <= 0 and vida2 <= 0:
          print("Empate!")
    elif vida1 <= 0:
          print("Você morreu!")
    elif vida2 <= 0:
          print("O monstro morreu!")
  
main()
