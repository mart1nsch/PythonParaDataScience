# %%
import numpy as np

# %%
# Podemos definir um número aleatório com seed para termos consistência nos arrays que formos gerar de maneira aleatória
rng = np.random.default_rng(seed=1701)
rng

# %%
# Array unidimensional
x1 = rng.integers(10, size=6)
x1

# %%
# Array bidimensional
x2 = rng.integers(10, size=(3, 4))
x2

# %%
# Array tridimensional
x3 = rng.integers(10, size=(3, 4, 5))
x3

# %%
# Acessando uma posição
x1[0]

# %%
# Última posição do array
x1[-1]

# %%
# Acessando uma posição num array bidimensional
x2[0, 2]

# %%
# Modificando valor de um índice
x1[0] = 2
x1[0]

# %%
# Retornar o array fatiado x1[start:stop:step]
x1[1:4]

# %%
# Primeiros três elementos
x1[:3]

# %%
# Retorna os elementos do array pulando de 2 em 2
x1[::2]

# %%
# Todos elementos até o terceiro
x1[:3]

# %%
# Inverte o array
x1[::-1]

# %%
# Fatiamento bidimensional, retornando duas primeiras linhas e três primeiras colunas
x2[:2, :3]

# %%
# Copiar um array
x1_copy = x1.copy()
x1_copy

# %%
# Uma cópia a partir de um pedaço do array bidimensional
x2_copy = x2[:2, :2].copy()
x2_copy

# %%
# Transformando um array unidimensional de nove elementos em uma matriz 3x3
lista = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
lista.reshape(3, 3)

# %%
# Junta dois arrays
lista.reshape(1, 9)
np.concatenate([x1, lista])