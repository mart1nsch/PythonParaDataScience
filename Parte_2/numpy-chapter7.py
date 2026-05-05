# %%
import numpy as np

# %%
lista = np.random.uniform(0.0, 5.0, 100)

# %%
# Soma
np.sum(lista)

# %%
# Mínimo
np.min(lista)

# %%
# Máximo
np.max(lista)

# %%
import pandas as pd

# %%
# Dados de altura dos presidentes
data = pd.read_csv('../Data/president_heights.csv')
heights = np.array(data['height(cm)'])
heights

# %%
# Média de altura
heights.mean()

# %%
# Standard Deviation
heights.std()

# %%
# Mínimo
heights.min()

# %%
# Máximo
heights.max()

# %%
# Percentile 25%
np.percentile(heights, 25)

# %%
# Mediana
np.median(heights)

# %%
# Percentile 75%
np.percentile(heights, 75)

# %%
import matplotlib.pyplot as plt

# %%
# Gráfico das alturas
plt.hist(heights)
plt.title('Height Distribuition of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')