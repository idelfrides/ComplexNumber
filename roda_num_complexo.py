import ComplexNumberModule as ncm
import time as t

def run_app_numComp():
    # criar objeto da classe NumeroComplexo
    ncm_obj = ncm.ComplexNumberModule()

    ncm_obj.app_info()
    # define the inicializing mode
    init_mode = ncm_obj.menu_init()

    # chama um dos metodos de inicializacao
    if init_mode is 1:     # init with real part only
        p_real = ncm_obj.set_values(1, 1)
        ncm_obj.inicializeReal(p_real)
    elif init_mode is 2:   # init with real and imaginary parts
        p_real, p_imagi = ncm_obj.set_values(1, 2)
        ncm_obj.inicializeComplex(p_real, p_imagi)
    elif init_mode is 3:   # init with none parameters
        ncm_obj.inicializeNull()
    elif init_mode is 0:   # operation availible: sum
        print('\n\n O/A Sr(a) Escolheu SAIR. \n Aplicacao sera encerrada. \n\n')
        t.sleep(5)
        exit(1)
    else:
        pass

    ncm_obj.showCompNumber_1()
    ncm_obj.set_value_2(2)
    ncm_obj.showCompNumber_2()

    # choice one operation mode
    real_oper = True
    while real_oper is True:  # assumed that the operation is  availible
        oper = ncm_obj.menu_operations()
        if oper is 1:     # operation availible: sum
            # ncm_obj.set_values(2, 2)
            ncm_obj.sum_method()
        elif oper is 2:   # operation availible: subtract
            # ncm_obj.set_values(2, 2)
            ncm_obj.subtract_method()
        elif oper is 3:   # operation availible: multiples
            # ncm_obj.set_values(2, 2)
            ncm_obj.multiplies_method()
        elif oper is 4:   # operation availible: divide
            # ncm_obj.set_values(2, 2)
            ncm_obj.divide_method()
        elif oper is 5:   # operation availible: sum
            #p_real2, p_imagi2 = ncm_obj.set_values(2, 2)
            ncm_obj.itsIgual()
        elif oper is 0:  #  GO BACK TO MAIN MENU
            print('\n\n O/A Sr(a) Escolheu VOLTAR \n\n')
            t.sleep(2)
            return run_app_numComp()
        else:
            pass

    print('\n\n\n')


# ----------------- start app -----------------------

run_app_numComp()