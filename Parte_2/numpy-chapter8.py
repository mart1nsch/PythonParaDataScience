# %%
# Broadcasting

# %%
import numpy as np

# %%
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])

# %%
# Adição sobre todos os elementos do array
a + 5

# %%
M = np.ones((3, 3))

# %%
# Adição entre uma matriz e um array
M + a

# %%
# Adição quando as estruturas estão em axis diferentes
a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

a + b