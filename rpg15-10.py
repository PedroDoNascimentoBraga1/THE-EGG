import os
import random
personagem = [0]

honra = 0
os.system("clear")

def batalha(oponenteNome , oponenteVida , oponenteDano , oponenteraca , matar = 1): ##Uma função que recebe o nome do oponente, vida, dano, raça e se é possivel fugir da batalha ou não.##

    if oponenteraca == 1 :
        oponenteraca = "Humano"

    elif oponenteraca == 2:
        oponenteraca = "Elfo"
        
    elif oponenteraca == 3:
        oponenteraca = "Troll"

    elif oponenteraca == 4:
        oponenteraca = "Animal"



    contador = 0
    personagemVida = 10
    abreacao(10,"BATALHA INICIADA!!!")

    print("   Informações do oponente:")
    print(f" Nome            :  {oponenteNome}")
    print(f"  Raça            :  {oponenteraca}")
    print(f"   Vida Total      :  {oponenteVida}")
    print(f"    Força Total     :  {oponenteDano}") 
    
    print()

    print("   Suas informações:")
    print(" Nome            :  " + nome)
    print(f"  Raça            :  {personagem[0]}")
    print(f"   Vida Total       :  {personagemVida}" )
    print(f"    Força Total      :  {personagem[1]}" )
    print(f"     Furtividade      :  {personagem[2]}")

    while personagemVida > 0 and oponenteVida > 0:
        print(44 * "_")
        print(44 * "-")
        contador += 1
        print(f"   round | {contador} |")
        print(f" Vida INIMIGA : {oponenteVida}")
        print(f" Sua VIDA {personagemVida}")
        if matar == 1:
            while True:    
                atacarFugir = input("Atacar (a) ou tentar Fugir (f): ")
                if atacarFugir == "a" or atacarFugir == "f": break
        else: 
            while True:
                atacarFugir = input("Atacar (a): ")
                if atacarFugir == "a": break
            
        if atacarFugir == "a":
            numero = random.randint(personagem[1], personagem[1] + 2)
            oponenteVida -= numero
            
        elif atacarFugir == "f":
            print(personagem[2])
            numero = random.randint(0,10)
            if numero < personagem[2]:
                break
            
        numero = random.randint(oponenteDano , oponenteDano + 2)
        personagemVida -= numero

    print(44 * "_")
    print(44 * "-")
    contador += 1
    print("Resultado Final: ")
    print (f" Vida INIMIGA : {oponenteVida}")
    print (f" Sua VIDA {personagemVida}")
    fechaacao(11,"Fim da Batalha!!!")
    if personagemVida < oponenteVida:
        print("  ___     ___    _______    ______    ______    _______   __     __")
        print(" |   \   /   |  /  ___  \  |  __  \  |  __  \  |  _____| |  |   |  |")
        print(" |    \_/    | |  /   \  | | |__|  | | |__|  | |  |___   |  |   |  |")
        print(" |  |\___/|  | | |     | | |  _   /  |  _   /  |   ___|  |  |   |  |")
        print(" |  |     |  | |  \___/  | |  |\  \  |  |\  \  |  |____  |  \___/  |")
        print(" |__|     |__|  \_______/  |__| \__\ |__| \__\ |_______|  \_______/")
        while 0 < 1 :
            x = 1
    else:
        print(f"É o fim para o(a) {oponenteNome}")
        print()

def titulo(espaco , titulo):##Uma função para a execução de um título, é usada no início da história##
    print(88 * "=" )
    print(espaco * " " + titulo)
    print(88 * "=")

def abreacao(espaco , nomeacao):##Uma função para a abertura de situações diferentes da narração, por exemplo a loja e uma batalha.##
    print(44 *"_")
    print("/|"+" " * espaco +f"{nomeacao}"+ " " * espaco + "|\\")
    print(44 *"-")

def fechaacao(espaco , nomeacao):##Uma função para o encerramento das situações diferentes da narração, por exemplo a loja e uma batalha.##
    print(44 *"_")
    print("\\|"+" " * espaco +f"{nomeacao}"+ " " * espaco + "|/")
    print(44 * "=")

def prosseguir():##Uma função para separar os diálogos e narrações em blocos para facilitar a leitura do usuário.##
    print ()
    print ()
    input(30 * " "+ "* Enter para prosseguir *")
    print ()
    print ()
    print ()

dialogo = lambda nome, conteudo :print(" "*3,nome ," - " ,conteudo)##Uma função lambda, por ser mais simples, para a fala dos diálogos. Tem como imput o nome do personagem que vai falar e sua devida fala##


print(88 * "_")

print("|        ________    __    __    _______        _______    _______    _______          |")
print("|       |__    __|  |  |  |  |  |   ____|      |   ____|  |   ____|  |   ____|         |")
print("|          |  |     |  |__|  |  |  |___        |  |___    |  |  __   |  |  __          |")
print("|          |  |     |   __   |  |   ___|       |   ___|   |  | |_ |  |  | |_ |         |")       
print("|          |  |     |  |  |  |  |  |____       |  |____   |  |__| |  |  |__| |         |")
print("|          |__|     |__|  |__|  |_______|      |_______|  |_______|  |_______|         |")
print("|" + 86 * "_" +"|")
print("|" + 86 * " " +"|")

print("| Informe abaixo suas caracteristicas:" + 49 * " " + "|")

print("|" + 86 * " " +"|")

nome = input("|   Nome: ")
print("|   Raça:                                                                              |")
print("|" + 86 * " " +"|")
print("| 1 Humano  <->   3/10   -  Força    |   3/10   -  Furtividade    |   5/5  -  moedas   |")
print("| 2 Elfo    <->   3/10   -  Força    |   10/10  -  Furtividade    |   1/5  -  moedas   |")
print("| 3 Troll   <->   10/10  -  Força    |   1/10   -  Furtividade    |   1/5  -  moedas   |")
print("|" + 86 * " " +"|")
print("|  *A escolha de raça apenas infuenciará na divisão de atributos" + 23 * " " + "|")
print("|" + 86 * " " + "|")

teste2 = 1
while teste2 == 1:
    while True :
        personagem[0] = input("| Escolha sua raça (1, 2 ou 3): ") #Escolha de raça
        if personagem[0] == "1" or personagem[0] == "2" or personagem[0] == "3":
            break

    while True:
        if personagem[0] == "1" :
            teste = input("|Você tem certeza de que é um HUMANO? (s/n): ")

        elif personagem[0] == "2":

            teste = input("|Você tem certeza de que é um ELFO? (s/n): ")
        
        else:
            teste = input("|Você tem certeza de que é um TROLL? (s/n): ")
            
        if teste == "s":
            teste2 = 0
            break

        if teste == "n":
            break

print("|" + 86 * " " + "|")

if personagem[0] == "1" :          #Recebimento do atributo Humano

    personagem = ["Humano",3,3,5]

    #raca = "Humano"
    #forca = 3
    #furtividade = 3
    #moedas = 5
    print("|Pronto... você é um HUMANO!!"+ 58 * " " + "|")

elif personagem[0] == "2":         #Recebimento do atributo Elfo

    personagem = ["Elfo",3,10,1]

    #raca = "Elfo" 
    #forca = 3
    #furtividade = 10
    #moedas = 1
    print("|Pronto... você é um ELFO!!"+ 60 * " " + "|")
    
else:                   #Recebimento do atributo Troll
    personagem = ["Troll",10,1,1]

    #raca = "Troll"
    #forca = 10
    #furtividade = 1
    #moedas = 1
    print("|Pronto... você é um TROLL!!"+ 59 * " " + "|")

print("|" + 86 * "_" + "|")

prosseguir()

os.system("clear")

titulo(33 , "Começo da história")



print(f"    Em uma manhã nublada, ao levandar cedo para fazer o café da manhã, {nome} repara que")
print(f"  o ovo acabou e teria que ir comprar.")

prosseguir()

print(f"    Rapidamente {nome} pega seus equipamentos e saí para o reino mais próximo em busca de ")
print("  ovos, ele vai para Silicon Valey...")

prosseguir()

print(f"    {nome} está andando pela floresta...")

prosseguir()

print(f"    De repente avista um Lobo vindo rapidamente em sua direção, e percebe que uma")
print(f"  luta está à vir, se prepara para a batalha.")

prosseguir()

batalha("Lobo" , 5 , 5 , 4)

print(f"    Rapidamente {nome} se livrou do Lobo, e continuou seu caminho.")

prosseguir()

print("    Andando pela floresta, ele percebe que está avistando a entrada do reino.")

prosseguir()

print("    Ao aproximar-se do portão do reino ele repara que há um guarda na entrada.")

prosseguir()

print("    Ao se aproxímar, ele conversa com o guarda: ")

prosseguir()

dialogo("Guarda","Me dê seu passe.")

prosseguir()

dialogo(nome, "Como assim? há cinco meses não precisei de passe.")

prosseguir()

dialogo("Guarda","São as novas regras, amigo. O novo Rei não permite a entrada de estrangeiros.")

prosseguir()

print(f"    {nome} Dá meia volta, e se esconde atraz de uma arvore para decidir o que fazer.")

prosseguir()

while 1==1 :
    teste = input("    Voltar e batalhar com o Guarda, ou tentar passar sorrateiramente? (b/s): ")
    if teste == "b":
        honra -= 1
        batalha ("Guarda",9,3,1,0)
        break
    elif teste == "s":
        numero = random.randint(0, 10)
        if numero < personagem[2]:
            honra += 1
            print()
            print("    Você passou SORRATEIRAMENTE pelo guarda!!! agora já está dentro do reino.")
            break
        else:
            honra -= 1
            print()
            print("    Você FOI VISTO!! Apenas lhe resta LUTAR.")
            prosseguir()
            batalha ("Guarda",9,3,1,0)
            break

prosseguir()

print(f"    Finalmente {nome} conseguiu passar dele. Ao entrar no reino, {nome} se depara com um reino triste e")
print("  frio, muito diferente do que havia visto alguns meses atrás.")

prosseguir()

print("    Ele avista um pequeno vendedor de frutas, todas estavam velhas e murchas...")

prosseguir()

print("    Ao se aproxímar, ele conversa com o comerciante:")

prosseguir()

dialogo(nome,"Olá amigo, onde eu posso comprar ovos por aqui?")

prosseguir()

dialogo("Comerciante","Shhiiiuuu!!! Você acha isso engraçado? Nós podemos ser presos!!!")

prosseguir()

dialogo(nome,"Presos? Como assim?")

prosseguir()

dialogo("Comerciante","Como assim? Você não é daqui? Mas como? Esquece, melhor eu")
print(17*" ","não saber como um forasteiro veio parar aqui.")

prosseguir()

dialogo("Comerciante" , "É o seguinte, o novo rei proibiu absolutamente todos os suditos de comerem ou venderem ovos, inclusive eu mesmo")
print(17*" ","era um dos que levava a vida vendendo ovos... As coisas firaram bem dificies des de então.")

prosseguir()

dialogo("Comerciante","Agora APENAS o REI pode COMER ovos.")

prosseguir()

dialogo(nome,"Como assim? Há algum lugar para uma pessoa como eu arranjar alguns ovos?")

prosseguir()

dialogo("Comerciante","Há sim, mas isso vai lhe 1 moeda.")

prosseguir()
while True:
    teste = input(f"    Você possui {personagem[3]} moedas. Pagar 1 moeda, ou ameaçar e roubar uma moeda dele? (p/a): ")
    if teste == "p":
        personagem[3] -= 1
        honra += 1
        print()
        dialogo(nome,"Tá aqui seu dinheiro")
        print()
        break
    elif teste == "a":
        honra -= 1
        personagem[3] +=1
        print()
        dialogo(nome, "Eu que estava precisando de uma moeda... Espero que eu não tenha que tomar.")
        prosseguir()
        dialogo("Comerciante","Sim, não me bata por favoorr. É que realmente são tempos difícies por aqui, tome sua moeda.")
        break

prosseguir()

dialogo("Comerciante","Tá qui, um mapa, eu não estava mentindo, apenas o rei possui ovos.")

prosseguir()

dialogo(nome,"Um mapa?")

prosseguir()

dialogo("Comerciante","há alguém que pode lhe oferecer a chave para o portão, e esse mapa irá lhe levar até ela.")

prosseguir()

dialogo("Comerciante","Diga que o Gary te mandou.")

prosseguir()

dialogo("Comerciante","An é mesmo, NÃO COMPRE nada COM ELE, dizem que os itens são de origem DEMONIACA.")

prosseguir()

if honra <= -2:
    dialogo(nome,"Ok, na proxíma tente não chantager ninguém. Fique atento ou eu volto para pegar o resto das moedas.")
else:
    dialogo(nome, "Muito obrigado Gary!!, desejo boa sorte nas vendas.")

prosseguir()

print(f"    {nome} vai à localização do amigo do Gary")

prosseguir()

print(f"    Cada passo que {nome} dava era mais macabro, becos repletos de escuridão e neblina.")

prosseguir()

print(f"    Chegando na localização passada pelo comerciante, {nome} encontra uma antiga loja de tons de verde.")

prosseguir()

print(f"    Altas prateleiras, repletas de livros empoeirados, espadas e armaduras enferrujadas, entre outras antiguidades.")

prosseguir()

print("    Ao avistar o vendedor, sem nenhuma palavra.")

prosseguir()

if honra <= 0:
    print("   Se sente desconfortavel, e se pergunta de isso tem haver com a origem dos itens da loja.")

else:
    print("    Se sente confortavel, como se algo o atraisse para o vendedor, se sente confiante em iniciar um conversa.")

prosseguir()

print(f"    Após algum silêncio, {nome} inicia um diálogo:")

prosseguir()

dialogo(nome,"Boa noite, fui enviado por gary. Estou atras de uma tal chave.")

prosseguir()

dialogo("Vendedor",f"Boa noite, {nome}. Eu tenho a chave que você procura, isso irá lhe custar um certo preço.")

prosseguir()

dialogo("Vendedor","Porém, antes disso dê uma lhada nos itens que eu tenho à oferecer a um guerreiro como você:")

prosseguir()

abreacao(13,"Loja Suspeita")

print(f"Você possui {personagem[3]} moedas, gaste com sabedoria.")
print()
print("  1 Anel Encantado      <->   10  -  Força    |   5   -  Furtividade    |   2  -  moedas")
print("  2 Luvas Encantadas    <->   15  -  Força    |   0   -  Furtividade    |   2  -  moedas")
print("  3 Botas Encantadas    <->    5  -  Força    |  10   -  Furtividade    |   2  -  moedas")
print()
print("*Ao comprar um item, os atributos do item são somados aos seus atributos atuais*")
print()

print("Seus atributos atuais:")
print(f"    Força Total :  {personagem[1]}" )
print(f"    Furtividade :  {personagem[2]}")

print()

while True: 
    teste = input("  Deseja fazer negócios com o homem? (s/n)? :")
    if teste == "s" or teste == "n":
        break
if teste == "s":
    print(f"  {nome} - Eu tenho interesse.")
    honra -= 2
    print()
    while True :
        teste = input("Qual item deseja comprar? (escolha um por vez): ")
        if teste == "1":
            if personagem[3] >= 2:
                personagem[3] -= 2
                personagem[1] += 10
                personagem[2] += 5
                print()
                print("Seus atributos atuais:")
                print(f"    Força Total :  {personagem[1]}" )
                print(f"    Furtividade :  {personagem[2]}")
                print()
                if personagem[3] >= 2:
                    print()
                    print("Você não tem dinheiro o suficiente!!!")
                    break
            else:
                print()
                print("Você não tem dinheiro o suficiente!!!")
                break
        elif teste == "2":
            if personagem[3] >= 2:
                personagem[3] -= 2
                personagem[1] += 15
                print()
                print("Seus atributos atuais:")
                print(f"    Força Total :  {personagem[1]}" )
                print(f"    Furtividade :  {personagem[2]}")
                print()
                if personagem[3] >= 2:
                    print()
                    print("Você não tem dinheiro o suficiente!!!")
                    break
            else:
                print("Você não tem dinheiro o suficiente!!!")
                break
        elif teste == "3":
            if personagem[3] >= 2:
                personagem[3] -= 2
                personagem[2] += 10
                personagem[1] += 5
                print()
                print("Seus atributos atuais:")
                print(f"    Força Total :  {personagem[1]}" )
                print(f"    Furtividade :  {personagem[2]}")
                print()
                if personagem[3] >= 2:
                    print()
                    print("Você não tem dinheiro o suficiente!!!")
                    break
            else:
                print("Você não tem dinheiro o suficiente!!!")
                break

else:
    print("Não me interessa")

fechaacao(13,"Loja Suspeita")

prosseguir()

dialogo("Vendedor","Ok, Está foi a escolha certa?")

prosseguir()

dialogo(nome,"Como assim? E a chave?")

prosseguir()

dialogo("Vendedor","Ah, é mesmo né...")

prosseguir()

dialogo("Vendedor",f"Vejo que você possui {personagem[3]} moedas, não se preocupe.")

prosseguir()

dialogo("Vendedor","Pela chava, você terá que pagar com a sua honra.")

prosseguir()

dialogo("Vendedor",f"Suas escolhas até esse momento, o levaram a possuir uma honra {honra}.")

prosseguir()

dialogo("Vendedor","Pela chave... que preciso de cinco pontos de honra.")

print("    Vendedor - Pela chave... que preciso de cinco pontos de honra.")

prosseguir()

print (f"    Vendedor - Você ficaria com {honra - 5} de honra.")

prosseguir()

print("Vendedor - Porém, como um gesto de boa fé. Também te daria esse anel de rubi, com dez de força.")

prosseguir()

while True:
    teste = input("Aceitar a oferta ou Lutar contra o Vendedor? (a/l)")
    if teste == "a" or teste == "l" : break
if teste == "a":
    honra -= 5
    personagem[1] += 10
    print("    Vendedor - Aqui está sua chave e seu anel de rubi, boa viajem. Você vai precisar")

else:
    batalha ("Diabo",10,4,1,1)

prosseguir()

print(f"    Após a batalha {personagem[0]} consegue a chave e vai para o grande castelo.")

prosseguir()

