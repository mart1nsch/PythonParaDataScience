# %%
import numpy as np

# %%
rng = np.random.default_rng(seed=1701)
x = rng.integers(100, size=10)
x

# %%
# Podemos acessar posições de uma lista usando uma lista de indexes
lista_pos = [3, 7, 4]
x[lista_pos]

# %%
# Também podemos definir em que formato vamos receber
# os elementos, por exemplo, podemos colocar as posições numa
# matrix e usar isso como filtro numa lista, o resultado será
# uma matrix montada com o valor de cada posição
matrix_pos = np.array([[3, 7],
                       [4, 5]])
x[matrix_pos]

# %%
# A funcionalidade também inclui matrizes
matriz = np.arange(12).reshape((3, 4))
lista_row = [1, 2]
lista_col = [0, 1]
matriz[lista_row, lista_col]

# %%
# Podemos usar isso para verificar alguns dados aleatórios
mean = [0, 0]
cov = [[1, 2], [2, 5]]
X = rng.multivariate_normal(mean, cov, 100)

import matplotlib.pyplot as plt
plt.scatter(X[:, 0], X[:, 1])

# %%
indices = np.random.choice(X.shape[0], 20, replace=False)
selection = X[indices]
plt.scatter(X[:, 0], X[: 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1])