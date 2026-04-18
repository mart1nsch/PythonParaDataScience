# %%
import numpy as np

# %%
# Criando um array com numpy (são muito mais performáticos)
lista = [2, 5, 7, 3, 6, 0]
np.array(lista)

# %%
# Também podemos definir qual tipo de dados o array terá
np.array(lista, dtype=np.float32)

# %%
# Matriz com arrays np
np.array([lista, lista, lista])

# %%
# Cria um array com 10 elementos 0
np.zeros(10)

# %%
# Cria uma matriz de 3x5 com o valor 3.14 nele
np.full((3, 5), 3.14)

# %%
# Cria um array que começa em 0 e vai até o 20 pulando de 2 em 2
np.arange(0, 20, 2)

# %%
# Cria uma matriz 3x3 com números aleatórios entre 0 e 1
np.random.random((3, 3))

# %%
# Cria uma matriz 3x3 com números aleatórios entre 0 e 1 e desvio-padrão 1
np.random.normal(0, 1, (3, 3))

# %%
# Cria uma matriz 3x3 com inteiros aleatórios entre 0 e 10 (10 não incluso)
np.random.randint(0, 10, (3, 3))