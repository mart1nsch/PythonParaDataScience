# %%
import numpy as np

# %%
x = np.array([1, 2, 3, 4, 5])

# %%
# Retorna uma lista de quais elementos são menores que 3
x < 3

# %%
# Retorna uma lista de quais elementos são maiores que 3
x > 3

# %%
# Retorna uma lista de quais elementos são menores ou iguais a 3
x <= 3

# %%
# Retorna uma lista de quais elementos são maiores ou iguais a 3
x >= 3

# %%
# Retorna uma lista de quais elementos são iguais a 3
x == 3

# %%
# Retorna uma lista de quais elementos são diferentes de 3
x != 3

# %%
# Também podemos fazer condições compostas
(x < 4) & (x > 1)

# %%
# Também funcionam com matrizes
z = np.arange(9).reshape((3, 3))
z >= 5

# %%
# Conta quantos registros são verdadeiros
np.count_nonzero(x > 3)

# %%
# Verificar se existe ao menos algum verdadeiro
print(np.any(x > 4))
print(np.any(x > 5))

# %%
# Verifica se todos são verdadeiros
print(np.all(x > 0))
print(np.all(x == 3))

# %%
# Fazendo filtro
print(x[x > 3])
filtro = x <= 2
print(x[filtro])