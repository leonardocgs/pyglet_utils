import random

import pyglet
import pyglet.shapes


class Tabuleiro:
    def __init__(self):
        self.pec = list()

    def adiciona(self, ind, peca):
        self.pec.insert(ind, peca)

    def mostra(self):
        for i in self.pec:
            print(f"{i} ", end="")
        print()


# a classe da peça, com os dois números e a forma de printar
class Peca:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "[%.d:%.d]" % (self.p1, self.p2)

    def __retr__(self):
        return "[%.d:%.d]" % (self.p1, self.p2)


# o jogador, que também seria um vetor de peças
class Jogador:
    def __init__(self):
        self.pecas = list()

    def mostra(self):
        for i in self.pecas:
            print(f"{i} ", end="")
        print()


class Computador(Jogador):
    pass


# Aqui seria um vetor com todas as peças
todas_as_pecas = [
    Peca(0, 0),
    Peca(0, 1),
    Peca(1, 1),
    Peca(0, 2),
    Peca(1, 2),
    Peca(2, 2),
    Peca(0, 3),
    Peca(1, 3),
    Peca(2, 3),
    Peca(3, 3),
    Peca(0, 4),
    Peca(1, 4),
    Peca(2, 4),
    Peca(3, 4),
    Peca(4, 4),
    Peca(0, 5),
    Peca(1, 5),
    Peca(2, 5),
    Peca(3, 5),
    Peca(4, 5),
    Peca(5, 5),
    Peca(0, 6),
    Peca(1, 6),
    Peca(2, 6),
    Peca(3, 6),
    Peca(4, 6),
    Peca(5, 6),
]


# Bugo, enfim, deu pra entender kkkk
# só arrumar algumas coisas
# sim, isso, minha ideia era pra cada jogada fazer um draw
# não sei se vai funcionar, tem que testar
# eh isso, tem que melhorar o passar também que eu acho que
# tá bugado, na real o problema aqui eh se nem o jogador
# nem o computador tiverem peças 'boas', ai teria que colcoar
# um cava, pq seriam só 2 jogadores nesse código, mas isso
# a gente vê depois, o negócio eh ter algo que funcione
# enfim, você acha que eu compartilhando esse código
# você consegue montar algo com as imagens, enquanto eu tento
# com o shapes lá ? oq for mais viável a gente faz, sim


# no jogo, a gente sorteia as peças pro computador e pro
# jogador
class Jogo:
    def __init__(self):
        self.t = Tabuleiro()

    def sorteia_pecas(self, j):
        while True:
            ind = random.randint(0, 26)
            if todas_as_pecas[ind] != 0:
                j.pecas.append(todas_as_pecas[ind])
                todas_as_pecas[ind] = 0
            if len(j.pecas) == 7:
                break

    def jogada(self, peca):
        tam = len(self.t.pec)
        if self.t.pec[0].p1 == peca.p1:
            p = Peca(peca.p2, peca.p1)
            self.t.adiciona(0, p)
            return True
        elif self.t.pec[0].p1 == peca.p2:
            self.t.adiciona(0, peca)
            return True
        elif self.t.pec[tam - 1].p2 == peca.p1:
            self.t.adiciona(tam, peca)
            return True
        elif self.t.pec[tam - 1].p2 == peca.p2:
            p = Peca(peca.p2, peca.p1)
            self.t.adiciona(tam, p)
            return True
        else:
            return False


j = Jogo()

p1 = Jogador()
j.sorteia_pecas(p1)
p2 = Computador()
j.sorteia_pecas(p2)
j.t.adiciona(0, Peca(6, 6))


while True:
    print("---------------TABULEIRO---------------")
    j.t.mostra()
    print("---------------SUAS PEÇAS---------------")
    p1.mostra()
    print("Escolha uma peça: [0-6] - 9 Para passar")
    x = int(input())
    if x != 9:
        aux = j.jogada(p1.pecas[x])
        if aux == True:
            p1.pecas.pop(x)
        else:
            while aux != True:
                print("JOGUE NOVAMENTE")
                x = int(input())
                if x == 9:
                    break
                aux = j.jogada(p1.pecas[x])
                if aux == True:
                    p1.pecas.pop(x)
    if len(p1.pecas) == 0:
        j.t.mostra()
        print("VOCÊ GANHOU")
        break
    tam_ini = len(p2.pecas)
    for i in range(0, len(p2.pecas)):
        aux = j.jogada(p2.pecas[i])
        if aux:
            p2.pecas.pop(i)
            break
    if tam_ini == len(p2.pecas):
        print("COMPUTADOR PASSOU")
    if len(p2.pecas) == 0:
        j.t.mostra()
        print("COMPUTADOR GANHOU")
        break
