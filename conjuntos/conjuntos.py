

conjunto1 = {'A', 'B', 'C', 'D'}
conjunto2 = {'C', 'D', 'E', 'F'}

print('Conjunto 1\n{}\nConjunto 2\n{}'.format(conjunto1,conjunto2))

conjuntof = conjunto1|conjunto2

print('Conjunto de union\n{}'.format(conjuntof))

# &
conjuntoi = conjunto1&conjunto2

print('Conjunto de interseccion\n{}'.format(conjuntoi))

# Diferencia simetrica
conjuntods = conjunto1^conjunto2

print('Conjunto de Diferencia simetrica\n{}'.format(conjuntods))

# Diferencia
conjuntod = conjunto1-conjunto2


print('Conjunto de Diferencia\n{}'.format(conjuntod))


