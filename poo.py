class Calculadora:

    def __init__(self) -> None:
        pass

    def calcular(self,op,n1,n2):
        if op == '+':
            return self._somar(n1,n2)
        
        elif op == '-':
            return self._subtrair(n1,n2)
        
        elif op == '*':
            return self._multiplicar(n1,n2)
        
        elif op == '/':
            if n1 != 0 and n2 != 0:
                return self._dividir(n1,n2)
            
            else:
                print('ERRO: Divisão por zero.')

        else:
            print('Operação inválida!')

    def _somar(self,n1,n2):
        return n1 + n2
    
    def _subtrair(self,n1,n2):
        return n1 - n2
    
    def _multiplicar(self,n1,n2):
        return n1 * n2
    
    def _dividir(self,n1,n2):
        return n1 / n2
    
objeto = Calculadora()
resultado = objeto.calcular('+',10,5)
print(resultado)
resultado = objeto.calcular('-',10,3)
print(resultado)
resultado = objeto.calcular('*',10,9)
print(resultado)
resultado = objeto.calcular('/',10,2)
print(resultado)

'''
- - - Output - - -
15
7
90
5.0

'''