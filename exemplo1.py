continuar = True
while continuar == True:
    try:            # tentativa
        a = int(input('Informe o primeiro número positivo: '))
        b = int(input('Informe o segundo número positivo:  '))
        if a < 0 or b < 0:
            raise TypeError
        c = a / b
        print('Resultado da divisão: ', c)
    except TypeError:
        print('Erro. O numero deve ser positivo')
    except ValueError:
        print('Erro. Ocorreu um erro de valor')
    except ZeroDivisionError:
        print('Erro. Ocorreu uma divisão por zero')
    except Exception as erro:   
        # qualquer outro erro
        print('Erro inesperado:', erro)
    else:
        # quando nenhuma exceção ocorrer
        print('Operação realizada com sucesso')
        continuar = False
    finally:
        # excutado sempre
        print('Fim do programa !!!')
    


