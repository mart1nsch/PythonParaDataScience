# %%
# Mostra o docstring de algo que você pedir
print(help(len))
print('------------------------')
print(help(list))

# %%
# Também podemos usar o ? para acessar a documentação (sim,
# mostra como se tivesse um erro, mas o símbolo ? só é
# entendido pelo Jupyter, Python puro nao sabe o que é
len?

# %%
# Docstrings
def square(a):
    '''Retorna o quadrado de a.''' # <-- Isso é uma docstring
    return a ** 2

# %%
# O Jupyter também pode mostrar o código fonte usando ??
square??