
# the class hold 20 methods used to build this project
class ComplexNumberModule(object):
    parte_real2 = 0
    parte_imaginaria2 = 0
    var = 'i'

    def __init__(self):
        pass

    def app_info(self):
        print('\n\n ----------------------------------------------'
              '\n\n This app work with complex number\n'
                     'It´s make several operations on complex numbers'
                    '\n\n ----------------------------------------------\n\n')

    def menu_operations(self):
        op_oper = -1
        print('\n\n MENU DE OPERACOES \n\n '
              '1 -> SOMA \n '
              '2 -> SUBTRACAO \n '
              '3 -> MULTIPLICACAO \n '
              '4 -> DIVISAO \n '
              '5 -> IGUALDADE \n '
              '0 -> VOLTAR')

        help_me = True
        while help_me is True:
            try:
                op_oper = int(input('\n Escolha uma operacao:  '))
            except Exception as erro_tipo:
                if op_oper < 0 or op_oper > 5:
                    print('\n\n ******************************************'
                          '\n WARNING:'
                          '\n Tipo de opracao invalido!! '
                          '\n Escolhe um tipo listado a seguir ')
                    print('\n TIPO DE ERRO: \n  {}'.format(erro_tipo))
                    print('*******************************************')
                else:
                    help_me = False
            help_me = False  # get out from the while loop
        return op_oper

    def inicializeComplex(self, parte_real, parte_imaginaria):
        self.parte_real = parte_real
        self.parte_imaginaria = parte_imaginaria

    def inicializeReal(self, parte_real):
        self.parte_real = parte_real
        self.parte_imaginaria = 0

    def inicializeNull(self):
        self.parte_real = 0
        self.parte_imaginaria = 0

    def showCompNumber_1(self):
        print('\n\n IMPRESSAO DO NUMERO COMPLEXO \n')
        # print('\n PARTE REAL {} \n PARTE IMAGINARIA {} '.format(self.parte_imaginaria, self.parte_imaginaria))
        print('\n Notacao do numero complexo: a + bi \n\n')
        print('{} + {}{}'.format(self.parte_real, self.parte_imaginaria, self.var))
        print('\n\n')

    def showCompNumber_2(self):
        print('\n\n IMPRESSAO DO SEDUNDO NUMERO COMPLEXO \n')
        print('\n Notacao do numero complexo: a + bi \n\n')
        print('{} + {}{}'.format(self.parte_real2, self.parte_imaginaria2, self.var))
        print('\n\n')

    def itsIgual(self):
        print('\n\n ===========================================')
        print('\n    RESULTADO DE COMPARACAO: \n')
        if self.parte_real == self.parte_real2 and self.parte_imaginaria == self.parte_imaginaria2:
            print('\n\t\t TRUE')
        else:
            print('\n\t\t FALSE')
        print('\n ===========================================')

    def sum_method(self):
        preais = self.parte_real + self.parte_real2
        pimagi = self.parte_imaginaria + self.parte_imaginaria2
        self.show_result_sm(preais, pimagi, 1)

    def multiplies_method(self):
        preais = self.parte_real * self.parte_real2 - self.parte_imaginaria * self.parte_imaginaria2
        pimagi = self.parte_real * self.parte_imaginaria2 + self.parte_imaginaria*self.parte_real2
        self.show_result_sm(preais, pimagi, 3)

    def subtract_method(self):
        preais = self.parte_real - self.parte_real2
        pimagi = self.parte_imaginaria - self.parte_imaginaria2

        if pimagi < 0:
            simb = '-'
            pimagi = (-1) * pimagi
            self.show_result_bd(preais, pimagi, simb, 2)
        else:
            simb = '+'
            self.show_result_bd(preais, pimagi, simb, 2)

    def divide_method(self):
        numerador_real = self.parte_real * self.parte_real2 + self.parte_imaginaria * self.parte_imaginaria2
        numerador_imagi = self.parte_imaginaria * self.parte_real2 - self.parte_real * self.parte_imaginaria2
        denominador = self.parte_real2**2 + self.parte_imaginaria2**2

        if denominador is not 0:
            preais = numerador_real / denominador
            pimagi = numerador_imagi / denominador
            if pimagi < 0:
                simb = '-'
                pimagi = (-1) * pimagi
                self.show_result_bd(preais, pimagi, simb, 4)
            else:
                simb = '+'
                self.show_result_bd(preais, pimagi, simb, 4)
        else:
            print('\n WARNING: DIVISION IMPOSSIBLE. \n THE FIRST COMPLEX NUMBER IS ZERO\n')

    def menu_init(self):
        # op_init = -1
        print('\n\n MENU DE INICIALIZACAO \n\n '
              '[1] Apenas com parte real \n '
              '[2] Com parte real e parte imaginaria \n '
              '[3] Sem valores \n '
              '[0] SAIR')

        help_me = True
        while help_me is True:
            try:
                op_init = int(input('\n Escolha um modo de Inicializacao:  '))
                if type(op_init) is int and op_init >= 0 and op_init <= 3:  #ok
                    help_me = False   # get out from the while loop
                else:
                    help_me = True
            except Exception as erro:
                # if type(op_init) is not int:   # char
                    print('\n\n ******************************************'
                          '\n WARNING:'
                          '\n modo de inicializacao invalido!!'
                          '\n Escolhe um modo listado acima')
                    print('\n TIPO DE ERRO: \n  {}'.format(erro))
                    print('*******************************************')
                    help_me = True    # continue in the while loop

        return op_init

    def menu_listagem(self, codigo):
        print('\n\n MENU DAS NOTAS \n')
        indice = 1
        tam = self.linsta_notas.__len__()

        for ind in range(tam):  # 0 ate tam-1
            print('\n [{}] {} '.format(indice, self.linsta_notas[ind]))
            indice = indice + 1
        print('\n [0] SAIR')

        opcao = int(input('\n\n Escolha uma nota pra ler/alterar: '))

        if codigo is 1:
            if opcao >= 1 and opcao <= tam:
                self.ler_nota(opcao - 1)
                return
            elif opcao is 0:
                print('Sr(a) escolheu Sair.\n')
                return opcao
            else:
                print('AVISO: OPCAO INVALIDA.\n Aplicao sera encerrada. \n\n')
                exit(0)
        elif codigo is 2:  # alterar
            if opcao >= 1 and opcao <= tam:
                self.alterar_nota(opcao - 1)
                return
            elif opcao is 0:
                print('Sr(a) escolheu Sair.\n')
                return opcao
            else:
                print('AVISO: OPCAO INVALIDA.\n Aplicao sera encerrada. \n\n')
                exit(0)
        else:
            pass

    def set_values(self, order, mode):
        if order is 1: # receber pimeiro num complexo: parte real e parte imaginaria
            print('\n ENTRYING VALUES FOR FIRST(1) COMPLEXR NUMBER \n\n ')
            if mode is 1:   # just real part
                p_real = self.init_values(mode)
                return p_real
            elif mode is 2:  # both real and imaginary parts
                p_real, p_imagi = self.init_values(mode)
                return p_real, p_imagi
            else:
                pass
        else:
            pass

    def set_value_2(self, order):
        if order is 2: # receber pimeiro num complexo: parte real e parte imaginaria
            print('\n ENTRYING VALUES FOR SECOND(2) COMPLEXR NUMBER \n\n ')
            p_real2, p_imagi2 = self.init_values(order)
            self.parte_real2 = p_real2
            self.parte_imaginaria2 = p_imagi2
        else:
            pass

    def init_values(self, mode):
        if mode is 1:  # receber o avalor pra a parte real
            print('\n VALUE JUST FOR REAL PART \n\n ')
            help_me = True
            while help_me is True:
                p_real = int(input('\n Digite a parte REAL:  '))

                if type(p_real) is int:
                    help_me = False  # get out from while loop
                elif type(p_real) is str:
                    print('WARNING: valor digitado eh invalido!!\n'
                          'Digite um numero inteiro.\n')
                    help_me = True  # continue in the while loop
                else:
                    pass
            return p_real

        elif mode is 2:  # receber os valores de ambs as partes
            print('\n VALUES FOR REAL AND IMAGINARY PARTS \n\n ')
            help_me = True
            while help_me is True:
                p_real = int(input('\n Digite a parte REAL:  '))
                p_imagi = int(input('\n Digite a parte IMAGINARIA:  '))

                if type(p_real) is int and type(p_imagi) is int:
                    help_me = False  # get out from while loop
                elif type(p_real) is str or type(p_imagi) is str:
                    print('WARNING: valor digitado eh invalido!!\n'
                          'Digite um numero inteiro.\n')
                    help_me = True  # continue in the while loop
                else:
                    pass

            return p_real, p_imagi

    def show_result_sm(self, preais, pimagi, code):
        if code is 1:  # sum result 1
            print('\n\n ===========================================')
            print('\n   RESULTADO DA SOMA \n\n\t {} + {}{}'.format(preais, pimagi, self.var))
            print('\n ===========================================')
        elif code is 3:  # multiples 3
            print('\n\n ===========================================')
            print('\n    RESULTADO DA MULTIPLICACO \n\n\t {} + {}{}'.format(preais, pimagi, self.var))
            print('\n ===========================================')
        else:
            pass

    def show_result_bd(self, preais, pimagi, simb, code):
        if code is 2:  # sum result
            print('\n\n ===========================================')
            print('\n   RESULTADO DA SUBTRACAO \n\n\t {} {} {}{}'.format(preais, simb, pimagi, self.var))
            print('\n ===========================================')
        elif code is 4:  # multiples
            print('\n\n ===========================================')
            print('\n  RESULTADO DA DIVISAO \n\n\t {:.3f} {} {:.3f}{}'.format(preais, simb, pimagi, self.var))
            print('\n ===========================================')
        else:
            pass