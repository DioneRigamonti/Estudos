import sys


def soma(*args):
    if sum(args) > 10:
        raise ValueError('A SOMA DOS ARGUMENTOS NÃO PODEM ULTRAPASSAR 10')
    
    else:
        return sum(args)


if __name__ == '__main__':

    print(soma(int(sys.argv[1]),int(sys.argv[2])))