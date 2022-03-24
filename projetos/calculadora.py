def loop ():
    
    print("==================")
    print("calculadora basica")
    print("==================")
    print(
        'temos as operaçoes:' 
        '\n ================= '
        '\n 1=Multiplicação '
        '\n 2=Divisão '
        '\n 3=Subitração '
        '\n 4=Adição '
        '\n 5=porcentagem  '
        '\n =================')

    entrada = int(input("Digite qual opção vc quer usar:"))

    if entrada == 1:
        n = 1
        while n != 0:
            n1 = float(input("Digite o primeiro valor:"))
            n2 = float(input("Digite o segundo valor :"))
            s = n1 * n2
            print("A resposta da sua multiplicação e {:.2f}".format(s))
            print(' ========== \n 1=repetir \n 0=cancelar \n ==========')
            n = int(input('Digite a opção Que voce quer usar:'))
    elif entrada == 2:
        n = 1
        while n != 0:
            n1 = float(input("Digite o primeiro valor:"))
            n2 = float(input("Digite o segundo valor:"))
            if n2 == 0:
                print("O numero 0 nao e divisivel")
            else:
                d = n1 / n2
                print("a resposta da sua Divisão e {:.2f}".format(d))
        print(' ========== \n 1=repetir \n 0=cancelar \n ==========')
        n = int(input('Digite a opção que vc quer usar:'))
    elif entrada == 3:
        n = 1
        while n != 0:
            n1 = float(input("Digite o primeiro valor:"))
            n2 = float(input("Digite o segundo  valor:"))
            s = n1 - n2
            print("A resposta da sua subitraçao e {:.2f}".format(s))
        print(' ========== \n 1=repetir \n 0=cancelar \n ==========')
        n = int(input('Digite a opção Que voce quer usar:'))
    elif entrada == 4:
        n = 1
        while n != 0:
            n1 = float(input("Digite o primeiro valor:"))
            n2 = float(input("Digite o segundo  valor:"))
            s = n1 + n2
            print("A resposta da sua soma e {:.2f}".format(s))
            print(' ========== \n 1=repetir \n 0=cancelar \n ==========')
            n = int(input('Digite a opção que voce quer usar:'))
    elif entrada == 5:
        n = 1
        while n != 0:
            print(' ===========\n 1=diminuir \n 2=aumentar \n ===========')
            entrada = int(input('Digite qual operação você Quer usar:'))
            if entrada == 1:
                n1 = float(input('Digite o valor:'))
                n2 = float(input('Digite a porcentagem:'))
                percentual = n2 / 100.0  #
                valor_final = n1 - (percentual * n1)
                print('O valor final e :{:.2f}'.format(valor_final))
            else:
                n1 = float(input('Digite o valor:'))
                n2 = float(input('Digite a porcentagem:'))
                porcentagem = n2 / 100.0
                valor_final = n1 + (porcentagem*n1)
                print('O valor final e:{:.2f}'.format(valor_final))
            print(' ========== \n 1=repetir \n 0=cancelar \n ==========')
            n = int(input('Digite a opção que voce quer usar:'))
    else:
        print("===================================")
        print("voçê nao digitou a operação correta!")
        print("===================================")
def finalizar():
    entry2 = int(input("1-Fechar \n"
                       "2-Novamente \n"
                       ": "))
    match entry2:
        case 1:
            print("Finalizado")
        case 2:
            loop();
            finalizar()
loop()
finalizar()
print('========================')
print("crditos:Diomar Gonçalves")
print('========================')
