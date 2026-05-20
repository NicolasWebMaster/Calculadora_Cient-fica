import math

while True:
    print("\n=== CALCULADORA CIENTÍFICA ===")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - exponenciação")

    print("6 - raiz quadrada")
    print("7 - raiz cúbica")
    print("8 - porcentagem")
    print("9 - módulo (resto)")
    print("10 - valor absoluto")

    print("11 - logaritmo base 10")
    print("12 - logaritmo natural (ln)")
    print("13 - fatorial")
    print("14 - exponencial (e^x)")
    print("15 - arredondamento")

    print("16 - seno (sin) ")
    print("17 - cosseno (cos)")
    print("18 - tangente (tan)")
    print("19 - maximo divisor comum (mdc)")
    print("20 - minimo multiplo comum ( mmc)")

    print("digite sair para encerrar o programa")

    opcao = input("selecione a operação: ").lower()

    if opcao == "sair":
        print("encerrando...")
        break

    # -------- SOMA --------
    elif opcao == "1":

      #digita o primeiro número (obrigatório)
        while True:
            try:
                n1 = float(input("primeiro número: "))
                break
            except ValueError:
                print("Erro! digite apenas números")

     #digita o segundo núemro (obrigatório)
        while True:
            try:
                n2 = float(input("segundo número: "))
                n1 += n2
                break
            except ValueError:
                print("Erro! digite apenas números")

    #pergunta se deseja continuar somando
        while True:
            continuar = input("somar mais? (sim/nao): ").lower()
            if continuar not in ["sim", "nao", "não"]:
                print("digite apenas sim ou nao")
                continue

            if continuar == "sim":
                while True:
                    try:
                        n2 = float(input("próximo número: "))
                        n1 += n2
                        break
                    except ValueError:
                        print("Erro! digite apenas números")
            else:
                break

        print("resultado:", n1)

    # -------- SUBTRAÇÃO --------
    elif opcao == "2":

      #digita o primeiro número (obrigatório)
        while True:

          try:

            n1 = float(input("primeiro número: "))
            break

          except ValueError:
            print("Erro! digite apenas números")

      #digita o segundo número (obrigatório)
        while True:
          try:

            n2 = float(input("segundo número: "))
            n1 -= n2
            break

          except ValueError:
            print("Erro! digite apenas números")

     #pergunta se quer continuar subtraindo
        while True:
            continuar = input("continuar? (sim/nao): ").lower()
            if continuar not in ["sim", "nao", "não"]:
                print("digite apenas sim ou nao")
                continue

            if continuar == "sim":
                while True:
                    try:
                        n2 = float(input("próximo número: "))
                        n1 -= n2
                        break
                    except ValueError:
                        print("Erro! digite apenas números")
            else:
                break

        print("resultado:", n1)

    # -------- MULTIPLICAÇÃO --------
    elif opcao == "3":
      #digita o primeiro número (obrigatório)
        while True:
            try:
                n1 = float(input("primeiro número: "))
                break

            except ValueError:
              print("Erro! digite apenas números")

      #digita o segundo número (obrigatório)

        while True:

          try:

            n2 = float(input("segundo número: "))
            n1 *= n2
            break

          except ValueError:
                print("Erro! digite apenas números")

      #pergunta se quer continuar multiplicando

        while True:
            continuar = input("continuar? (sim/nao): ").lower()
            if continuar not in ["sim", "nao", "não"]:
                print("digite apenas sim ou nao")
                continue

            if continuar == "sim":
                while True:
                    try:
                        n2 = float(input("próximo número: "))
                        n1 *= n2
                        break
                    except ValueError:
                        print("Erro! digite apenas números")
            else:
                break

        print("resultado:", n1)

    # -------- DIVISÃO --------
    elif opcao == "4":
      #digita o primeiro número (obrigatório)
        while True:
            try:
                n1 = float(input("primeiro número: "))
                break
            except ValueError:
                print("Erro! digite apenas números")

      #digita o segundo número (obrigatório)

        while True:
            try:
                n2 = float(input("segundo número: "))
                if n2 == 0:
                    print("não pode dividir por zero")
                else:
                  n1 /= n2
                  break
            except ValueError:
                print("Erro! digite apenas números")

       #pergunta se quer continuar dividindo

        while True:
            continuar = input("continuar? (sim/nao): ").lower()
            if continuar not in ["sim", "nao", "não"]:
                print("digite apenas sim ou nao")
                continue

            if continuar == "sim":
                while True:
                    try:
                        n2 = float(input("próximo número: "))

                        if n2 == 0:
                            print("não pode dividir por zero")
                        else:
                          n1 /= n2
                          break
                    except ValueError:
                        print("Erro! digite apenas números")
            else:
                break

        print("resultado:", n1)

    # -------- EXPONENCIAÇÃO --------
    elif opcao == "5":
      #digita o primeiro número (obrigatório)
        while True:
            try:
                base = float(input("base: "))
                break

            except ValueError:
              print('digite apenas números')

       #digita o segundo número (obrigatório)

        while True:
          try:

            expoente = float(input("expoente: "))
            break

          except ValueError:
                print("Erro! digite apenas números")

        print("resultado:", math.pow(base, expoente))

    # -------- RAIZ QUADRADA --------
    elif opcao == "6":

      #digita um número

        while True:
            try:
                n = float(input("número: "))
                if n < 0:
                    print("não existe raiz de número negativo")
                else:
                    break
            except ValueError:
                print("Erro! digite apenas números")

        print("resultado:", math.sqrt(n))

    # -------- RAIZ CÚBICA --------
    elif opcao == "7":

      #digita um número

        while True:
            try:
                n = float(input("número: "))
                break
            except ValueError:
                print("Erro! digite apenas números")

        if n < 0:
            resultado = -math.pow(abs(n), 1/3)
        else:
            resultado = math.pow(n, 1/3)

        print("resultado:", resultado)

    # -------- PORCENTAGEM --------
    elif opcao == "8":
      #menu
        print("1 - calcular %")
        print("2 - aumentar valor")
        print("3 - diminuir valor")

        while True:
            escolha = input("escolha: ")
            if escolha in ["1", "2", "3"]:
                break
            print("opção inválida")

        while True:
            try:
                valor = float(input("valor: "))
                break

            except ValueError:
              print("Erro! digite apenas números")

        while True:
          try:

            porcento = float(input("porcentagem: "))
            break

          except ValueError:
            print("Erro! digite apenas números")

        if escolha == "1":
            print("resultado:", (valor * porcento) / 100)
        elif escolha == "2":
            print("resultado:", valor * (1 + porcento / 100))
        else:
            print("resultado:", valor * (1 - porcento / 100))

    # -------- MÓDULO --------
    elif opcao == "9":

      #digita o primeiro número (obrigatório)
        while True:
            try:
                n1 = int(input("primeiro número: "))
                break
            except ValueError:
                print("Erro! digite apenas números inteiros")

      #digita o segundo número (obrigatório)

        while True:
            try:
                n2 = int(input("segundo número: "))
                if n2 == 0:
                    print("não pode ser zero")
                else:
                    break
            except ValueError:
                print("Erro! digite apenas números inteiros")

        print("resto:", n1 % n2)

    # -------- VALOR_ABSOLUTO --------
    elif opcao == "10":

      #digite um número

        while True:
            try:
                n = float(input("número: "))
                break
            except ValueError:
                print("Erro! digite apenas números")

        print("resultado:", math.fabs(n))

    #----------Logaritmo_Base_10---------

    elif opcao == "11":

      #digita um número
      while True:

        try:

          n = float(input("número: "))

          if n <= 0:

            print("não é permitido 0 ou números negatívos")
            continue

          break

        except ValueError:

          print("Erro! digite apenas números")

      print("resultado", math.log10(n))

    #---------Logaritmo_natural--------------

    elif opcao == "12":
      while True:
        try:

          #adiciona número

          n = float(input("digite um número: "))

          if n <= 0:
            print("não é permitido 0 ou números negativos")
            continue

          break

        except ValueError:
          print("Erro! digite apenas números")

      print("resultado", math.log(n))

    #-----------Fatorial--------------
    elif opcao == "13":
      while True:
        try:

          #adiciona número
          n = int(input("digite um número: "))

          if n < 0:
            print("não é permitido números negativos")

            continue

          break

        except ValueError:
          print("Erro! digite apenas números inteiros")

      print("resultado", math.factorial(n))

    #-----------exponencial_(e^x)------------
    elif opcao == "14":
      while True:
        try:

          #adiciona número
          n = float(input("digite um número: "))
          break

        except ValueError:
          print("Erro! digite apenas números")

      print('resultado', math.exp(n))

    #----------arredondamento-------------------
    elif opcao == "15":
      # menu
      print("1- arredondamento normal")
      print("2- arredondamento para cima")
      print("3- arredondamento para baixo")
      print("4- truncar (cortar decimal)")

      # loop escolha
      while True:
        escolha = input("escolha: ")
        if escolha in ["1", "2", "3", "4"]:
          break

        else:
          print("opção inválida")

      # número
      while True:
        try:
          n = float(input("digite um número: "))
          break
        except ValueError:

          print("Erro! digite apenas números")

      # operações
      if escolha == "1":

        while True:

          try:
            casas = int(input('digite o número de casas: '))
            resultado = round(n, casas)
            break
          except ValueError:
            print("Erro! digite apenas números inteiros")

      elif escolha == "2":
        resultado = math.ceil(n)

      elif escolha == "3":

        resultado = math.floor(n)

      elif escolha == "4":
        resultado = math.trunc(n)

      print("resultado", resultado)

    #------------seno_(sin)----------------
    elif opcao == "16":

      #proteção de números
      while True:
        try:
          angulo = float(input("digite o ângulo em graus: "))
          break

        except ValueError:
          print('Erro! digite apenas números')

      #calculo
      resultado = math.sin(math.radians(angulo))

      print("resultado", resultado)

    #---------cosseno_(cos)-----------------
    elif opcao == "17":
      #proteção de números
      while True:
        try:
          angulo = float(input("digite o ângulo em graus: "))
          break

        except ValueError:
          print("Erro! digite apenas números")

      #calculo
      resultado = round(math.cos(math.radians(angulo)), 5)

      print("resultado", resultado)

    #-------tangente_(tan)-----------------
    elif opcao == "18":
      #proteção de números
      while True:
        try:
          angulo = float(input("digite o ângulo em graus: "))
          break

        except ValueError:
          print("Erro! digite apenas números")

      #converta para radiano
      rad = math.radians(angulo)

      #proteção contra tangente indefinida
      if abs(math.cos(rad)) < 1e-10:
        print("Erro! tangente indefinida (divisão por zero )")

      else:
        resultado = math.tan(rad)
        print("resultado", round(resultado, 5))

    #--------------mdc-------------------
    elif opcao == "19":

      # primeiro número
      while True:
        try:
          n1 = int(input("digite o primeiro número: "))
          break
        except ValueError:

          print("Erro! digite apenas números inteiros")

      # segundo número
      while True:
        try:
          n2 = int(input("digite o segundo número: "))
          break
        except ValueError:
          print("Erro! digite apenas números inteiros")

      # cálculo do MDC
      resultado = math.gcd(n1, n2)

      print("MDC:", resultado)

    #-----------------mmc--------------------
    elif opcao == "20":

      # primeiro número
      while True:
        try:
          resultado = int(input("digite o primeiro número: "))
          break
        except ValueError:
          print("Erro! digite apenas números inteiros")

      # próximo número
      while True:
        try:
          n = int(input("digite outro número: "))
          break
        except ValueError:
          print("Erro! digite apenas números inteiros")

      # cálculo do MMC usando MDC
      resultado = abs(resultado * n) // math.gcd(resultado, n)

      print("MMC final:", resultado)
