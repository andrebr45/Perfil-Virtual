#Cores
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    VER =	'\033[1;32m' #VERDE 2
    AZUL =	'\033[1;34m' #AZUL
    RED =	'\033[1;31m' #VERMELHO 2
    NEGRITO =	'\033[;1m' #NEGRITO

#Inicio Projeto 
print(f'''{bcolors.WARNING}
 _________________
|                 |
| New Future V2.0 |
|_________________|
{bcolors.RESET}''')
#______________________________________________________________________
#Página de login 
print(f'''{bcolors.VER}
   ---------
   | Login |
   ---------
{bcolors.RESET}''')
username = str(input(f"{bcolors.AZUL}Usuário: {bcolors.RESET}"))
password = str(input(f"{bcolors.AZUL}Senha: {bcolors.RESET}"))
while username != "Admin" or password != "123456":
    print(f"{bcolors.RED}Username e Password Incorretos!!, Tente novamente!{bcolors.RESET}")
    username = str(input(f"{bcolors.AZUL}Usuário: {bcolors.RESET}"))
    password = str(input(f"{bcolors.AZUL}Senha: {bcolors.RESET}"))
print(f'''{bcolors.OK}
Logado Com Sucesso !
{bcolors.RESET}''')
print(f'{bcolors.NEGRITO}Bem vindo',username)
#_______________________________________________________________________
#Data e hora
a = "N"
b = a
while a == b :
    import arrow
    utc = arrow.utcnow()
    local = utc.to('-03:00')
    local.format()
    print(f"{bcolors.WARNING}[ DATA ]{bcolors.RESET}")
    print(f"{bcolors.WARNING}Ano|Mês|Dia| Hora |{bcolors.RESET}")
    print(local.format())
#________________________________________________________________________
#Continuação da interface do programa
    print(f'''{bcolors.WARNING}
           _______________________________________________________________
           |              |              |       |                        |
           | País: Brasil | R$: 1.000,00 | Hab:B | Estado Cívil: Solteiro | 
           |______________|______________|_______|________________________| {bcolors.RESET}''')
#Opções

    print(f'''                     {bcolors.VER}O que deseja fazer ?{bcolors.RESET}{bcolors.AZUL}
    [Opções]
    [1] - Dados Pessoais
    [2] - Carreira Profissional
    [3] - Meus Bens
    [4] - Configurações
    [5] - Funções
    [6] - Encerrar Programa
    {bcolors.RESET}''')

    opcao = input(f"{bcolors.WARNING}O que deseja fazer ? {bcolors.RESET}")

    if opcao == ("1") :
       print(f'Ver dados pessoais')
       print(f'''{bcolors.WARNING}
                 [Meus Dados]
       __________________________________
       |                                |
       | Cidadão: Brasileiro            |
       | RG:XX-XXX-XXX-X                |
       | CPF: XXX-XXX-XXX-XX            |
       | Estado Cívil: Solteiro         |
       | Título de Eleitor: XXX-XXX-XXX |
       | Passagem Pela Polícia: Não     |
       |________________________________|
       {bcolors.RESET}''')
    
    elif opcao == ("2") :
       print(f'''{bcolors.OK}
       [Minha carreira Profissional]{bcolors.RESET} {bcolors.WARNING}
       -----------------------------
       [1] - Trabalhos
       [2] - Cursos
       [3] - Certificados
       -----------------------------{bcolors.RESET}
       ''')
       c = input(f"{bcolors.AZUL}Qual opção:{bcolors.RESET}")
       while c != ("1") and c != ("2") and c != ("3") :
           print(f"{bcolors.FAIL}Opção Invalida!{bcolors.RESET}")
           c = input(f"{bcolors.AZUL}Qual opção:{bcolors.RESET}")
       if c == ("1") :
           print("Seus Trabalhos")
       elif c == ("2") :
           print("Seus cursos")
       elif c == ("3") : 
           print("Seus Certificados")
       
    elif opcao == ("3") :
       print("Meus Bens")
    elif opcao == ("4") :
       print('''Configurações
       -----------------------------
       [1] - Versão
       [2] - Status
       [3] - Configurações Avançadas
       -----------------------------
       ''')
       config = input(f"{bcolors.AZUL}Qual opção:{bcolors.RESET}")
       while config != ("1") and config != ("2") and config != ("3"):
           print(f"{bcolors.FAIL}Opção Invalida!{bcolors.RESET}")
           config = input(f"{bcolors.AZUL}Qual opção:{bcolors.RESET}")
       if config == ("1") :
           print("-- Seu programa está atualizado com a versão mais recente!-- 2.0")
       elif config == ("2"):
           print("O servidor esta: [ONLINE]")
       elif config == ("3") :
           print('''Avançados
           [1] Mudar Conta
           [2] fim 1
           [3] fim 2
           ''')
           avan = input(f"{bcolors.AZUL}Qual opção:{bcolors.RESET}")
           while avan != ("1") and avan != ("2") and avan != ("3"):
               print(f"{bcolors.FAIL}Opção Invalida!{bcolors.RESET}")
               avan = input(f"{bcolors.AZUL}Qual opção:{bcolors.RESET}")
           if avan == ("1"):
               print("Mudar conta")
           elif avan == ("2"):
               print("Fim 1")  
           elif avan == ("3"):
               print("Fim 2")
    elif opcao == ("5") :
        print(f'''{bcolors.RED}[Funções]{bcolors.RESET} {bcolors.OK}
        [1] - Saúde
        [2] - Calculadora {bcolors.RESET}
        ''')
        funcoes = input(f"{bcolors.AZUL}Qual opção:{bcolors.RESET}")
        while funcoes != ("1") and funcoes != ("2"):
            print(f"{bcolors.FAIL}Opção Invalida!{bcolors.RESET}")
            funcoes = input(f"{bcolors.AZUL}Qual opção:{bcolors.RESET}")
        if funcoes == ("1"):
            print(f'''
             {bcolors.OK}Índice{bcolors.RESET} de {bcolors.WARNING}Massa{bcolors.RESET} {bcolors.RED}Corporal{bcolors.RESET}
            --------------------------
            ''')
            print (f'{bcolors.AZUL}Bem vindo ao programa de medida {bcolors.OK}I{bcolors.WARNING}M{bcolors.RED}C{bcolors.RESET}')
            
            peso = float(input (f'{bcolors.WARNING}Qual seu peso: {bcolors.RESET}'))
            altura = float(input (f'{bcolors.WARNING}Qual sua Altura: {bcolors.RESET}'))
            imc = (peso/(altura*altura))
            print ("o resultado é",imc)
            if imc < 17 :
                print (f'{bcolors.RED}Muito abaixo do peso{bcolors.RESET}')
            if imc > 17 and imc <= 18.49 :
                print (f'{bcolors.AZUL}Abaixo do peso{bcolors.RESET}')
            if imc > 18.5 and imc <= 24.99 :
                print (f'{bcolors.OK}Peso normal{bcolors.RESET}')  
            if imc > 25 and imc <= 29.99 :
                print (f'{bcolors.WARNING}Acima do peso{bcolors.RESET}')  
            if imc > 30 and imc <= 34.99 :
                print (f'{bcolors.WARNING}Obesidade I{bcolors.RESET}')
            if imc > 35 and imc <= 39.99 :
                print (f'{bcolors.RED}Obesidade II {bcolors.WARNING}(severa){bcolors.RESET}')    
            if imc > 35 :
                print (f'{bcolors.RED}Obesidade III (mórbida){bcolors.RESET}')
        elif funcoes == ("2"):
            print("Ainda em Desenvolvimento ")
            print(f'''{bcolors.RED}
            Calculadora Inteligente{bcolors.RESET}{bcolors.WARNING}
            -----------------------{bcolors.RESET}
            ''')
            n = 1
            while n != 5 :
              print("Calculadora")
              n1 = int(input(f"{bcolors.OK}Digite o 1°: {bcolors.RESET}"))
              n2 = int(input(f"{bcolors.OK}Digite o 2°: {bcolors.RESET}"))
              soma = n1 + n2
              sub = n1 - n2
              mult = n1 * n2
              div = n1 / n2
              print(f'''{bcolors.AZUL}Opções{bcolors.RESET}
              -------------------------------------------------------
              {bcolors.OK}[1]{bcolors.RESET}{bcolors.WARNING} - Soma{bcolors.RESET}       | {bcolors.OK}[3]{bcolors.RESET}{bcolors.WARNING} - Multiplicação{bcolors.RESET} | {bcolors.OK}[5]{bcolors.RESET}{bcolors.RED} - Encerrar{bcolors.RESET}
              {bcolors.OK}[2]{bcolors.RESET}{bcolors.WARNING} - Subtração{bcolors.RESET}  | {bcolors.OK}[4]{bcolors.RESET}{bcolors.WARNING} - Divisão{bcolors.RESET}       |
              -------------------------------------------------------
              ''')
              n = int(input("Fale: "))
              if n == 1 :
                print("A soma é",soma)
              elif n == 2 :
                print("A subtração é",sub)
              elif n == 3 :
                print("A multiplicação é",mult)
              elif n == 4 :
                print("A divisão é",div)
              elif n == 5 :
                print("Encerrando Programa")
              else:
                print("Opção Invalida, Tente Novamente")
            print("Calculadora Encerrada")
    elif opcao == ("6") :
       print("Programa Encerrado!!!")
       exit()
    else: 
        print(f"{bcolors.FAIL}Opção Invalida!{bcolors.RESET}")
    b = str(input(f"{bcolors.WARNING}Deseja sair{bcolors.RESET} {bcolors.RED}[S/N]:{bcolors.RESET}"))
    if b != "S" and "N":
        while b != "S" and b != "N":
            print(f"{bcolors.FAIL}Opção Invalida!{bcolors.RESET}")
            b = str(input(f"{bcolors.WARNING}Deseja sair{bcolors.RESET} {bcolors.RED}[S/N]:{bcolors.RESET}"))
            print(f"{bcolors.WARNING}Encerrando{bcolors.RESET}")
    else:
        print(f"{bcolors.WARNING}Encerrando{bcolors.RESET}")
print(f"{bcolors.OK}Finalizado{bcolors.RESET}")

