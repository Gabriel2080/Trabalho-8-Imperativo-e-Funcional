# 1. Usando  os  conceitos  de  programação  funcional  e  considerando  o  universo  dos  números inteiros,  implemente  a  função  foldr  em  Python,  C  ou  C++  20  tomando  como  base  o funcionamento  desta  função  em  Haskell.  Sem,  é  claro,  usar  qualquer  função,  objeto,  ou biblioteca disponíveis na linguagem que você escolher. 

# def foldr(f, z, xs):
#     if len(xs) == 0:
#         return z
#     else:
#         return f(xs[0], foldr(f, z, xs[1:]))

foldr = lambda f, z, xs: z if len(xs) == 0 else f(xs[0], foldr(f, z, xs[1:]))

soma = lambda x, y: x + y

# 2. Usando  os  conceitos  de  programação  funcional  e  considerando  o  universo  dos  números inteiros, implemente a função abs em Python, C ou C++ 20 que devolva o valor absoluto de um número dado. Sem, é claro, usar qualquer função, objeto, ou biblioteca disponíveis na linguagem que você escolher.

abs = lambda x: x if x >= 0 else abs(-x)

# 3. Usando  os  conceitos  de  programação  funcional  e  considerando  o  universo  dos  números reais, implemente a função media em Python, C ou C++ 20 que devolva a média aritmética entre  dois  números  dados.  Sem,  é  claro,  usar  qualquer  função,  objeto,  ou  biblioteca disponíveis na linguagem que você escolher.

media = lambda x: x[0] if len(x) == 1 else (x[len(x) - 1] + ((len(x) - 1) * media(x[:len(x) - 1]))) / len(x)

#media = lambda xs: 0 if len(xs) == 0 else soma(media(xs[1:]), xs[0]) / 2.0
#media = lambda x: media() if len(x) >= 0 else (x[1] + x[0]) / 2

# 4. Usando os conceitos de programação funcional e a linguagem Python, C ou C++ 20 escreva uma  função  que  devolva  a  lista  de  todos  os  números  de  Fibonacci  até  um  valor  dado considerando que a  sequência de Fibonacci começa em zero. Sem, é  claro, usar qualquer função, objeto, ou biblioteca disponíveis na linguagem que você escolher.

fib = lambda x: [] if x == 0 else [0] if x == 1 else [0, 1] if x == 2 else fib(x - 1) + [fib(x - 1)[len(fib(x - 1)) - 1] + fib(x - 1)[len(fib(x - 1)) - 2]]
#fib = lambda n: 0 if n == 0 else 1 if n == 1 else fib(n - 1) + fib(n - 2)

# 5. Você tem uma lista de tuplas onde o primeiro campo é o nome de um aluno e o segundo sua nota. Crie uma função, usando o Python, C ou C++ 20 e os conceitos de programação funcional para  criar uma  função que  ordene  listas  de  tuplas,  como  a  tupla  descrita neste enunciado.  Sem,  é  claro,  usar  qualquer  função,  objeto,  ou  biblioteca  disponíveis  na linguagem que você escolher.

# Exemplo de lista de tuplas:
# [('Joao', 10), ('Maria', 7), ('Jose', 8), ('Ana', 9), ('Paulo', 6), ('Pedro', 8), ('Paula', 9), ('Joana', 10), ('Marcos', 7), ('Mariana', 8)]

# Exemplo de lista de tuplas ordenada:
# [('joao', 10), ('joana', 10), ('ana', 9), ('paula', 9), ('jose', 8), ('mariana', 8), ('pedro', 8), ('maria', 7), ('marcos', 7), ('paulo', 6)]

# Exemplo de uso:
# ordena_tuplas([('Joao', 10), ('Maria', 7), ('Jose', 8), ('Ana', 9), ('Paulo', 6), ('Pedro', 8), ('Paula', 9), ('Joana', 10), ('Marcos', 7), ('Mariana', 8)])

ordena_tuplas = lambda x: [] if len(x) == 0 else ordena_tuplas([y for y in x[1:] if y[1] > x[0][1]]) + [x[0]] + ordena_tuplas([y for y in x[1:] if y[1] <= x[0][1]])

print("foldr: entrada: soma, 0, [5, 8, 10, 2, 3] ; resultado: " + str(foldr(soma, 0, [5, 8, 10, 2, 3])))

print("abs: entrada: -5 ; resultado: " + str(abs(-5)))

print("media: entrada: [5, 8, 10, 2, 3] ; resultado: " + str(media([5, 8, 10, 2, 3])))

print("fib: entrada: 5 ; resultado: " + str(fib(5)))

lista_aluno = [('Joao', 10), ('Maria', 7), ('Jose', 8), ('Ana', 9), ('Paulo', 6), ('Pedro', 8), ('Paula', 9), ('Joana', 10), ('Marcos', 7), ('Mariana', 8)]

print("ordena_tuplas: entrada: " + str(lista_aluno) + " ; \nresultado: "+ str(ordena_tuplas(lista_aluno)))
