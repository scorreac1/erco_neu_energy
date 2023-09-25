def sort_list(input_list):
    print(input_list)
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j+1] = input_list[j + 1], input_list[j] #fila de error input_list[j], input_list[j] = input_list[j + 1], input_list[j]
    print(input_list)
    return input_list

my_array = [5, 2, 9, 1, 5, 6, 4, 3]  #arreglo creado para evaluar la funcion
sort_list(my_array) #llamado a la funcion


"""El error se encontraba en la fila 6 porque se asignaba dos veces un valor a input_list en la posicion j. El primero era el valor inferior y luego retomaba su valor superior en la misma posicion."""