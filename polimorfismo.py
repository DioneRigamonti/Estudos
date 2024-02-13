'''Polimorfismo:
O polimorfismo é um conceito da programação orientada a objetos que permite que diferentes tipos de objetos sejam tratados de forma uniforme, mesmo que possuam comportamentos diferentes. Isso significa que, para um mesmo método ou função, diferentes objetos podem ter implementações diferentes desse método.

O principal objetivo do polimorfismo é aumentar a flexibilidade e a reutilização do código, permitindo que um mesmo trecho de código possa ser aplicado a diferentes tipos de objetos.

Em resumo, o polimorfismo nos permite escrever código que opera em objetos de maneira genérica, sem precisar se preocupar com os detalhes específicos de cada tipo de objeto, o que torna nosso código mais flexível, modular e fácil de dar manutenção.'''

class Animal:
    def __init__(self, animal) -> None:
        self.animal = animal

    def falar(self):
        match self.animal:
            case 'dog':
                return "AU AU AU"
            case 'cat':
                return "MIAU MIAU"
            case _:
                return "Animal não reconhecido"

class Teste(Animal):
    def __init__(self, animal) -> None:
        super().__init__(animal)


obj = Teste('dog')
print(obj.falar())  # Saída: AU AU AU

obj2 = Teste('cat')
print(obj2.falar())  # Saída: MIAU MIAU

obj3 = Teste('abc')
print(obj3.falar())  # Saída: Animal não reconhecido
