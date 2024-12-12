# %% [markdown]
# # Estado

# %%
import geopandas as gpd
from matplotlib_scalebar.scalebar import ScaleBar
from shapely.geometry.point import Point
import matplotlib.pyplot as plt
import pandas as pd
import mapclassify as mc

# %%
subbacia = gpd.read_file(r'G:\Meu Drive\RibeiraoPinhal\shapes\sub_bacias\subs1.shp')
subbacia 

# %%
df = pd.read_excel(r'G:\Meu Drive\pinhal_output\estado\sub.xlsx')
df

# %%
df1 = pd.pivot_table(df, values=['WYLDmm'], index=['YEAR','SUB'], aggfunc='mean')
df1.reset_index(inplace=True)
df2=df1.loc[0:3, :]
df2

# %%
df1

# %%
shape = pd.merge(subbacia, df2, how='inner', on='SUB')
shape

# %%
shape.info()

# %%
# pinhal.boundary.plot(ax=ax, color='black') #column
# shape.plot(ax=ax, column='WYLDmm', scheme='boxplot', k=4)
shape.plot(column='WYLDmm', scheme='Quantiles', k=3, cmap='viridis', figsize=(10, 5), legend=True, legend_kwds={'loc': 'lower left', 'bbox_to_anchor': (0, 0.01)})
plt.show()


