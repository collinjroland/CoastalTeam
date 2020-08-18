"""
Total sediment erosion (assumes limitless supply)
Based on totalsedimenterosionmudsine.m by Giulio Mariotti
Does not incorporate averaging over multiple tidal cycles or linear increase in critical shear stress with depth
"""
# imports
import numpy as np
import matplotlib.pyplot as plt
from landlab import RasterModelGrid, imshow_grid
from landlab.components import TidalFlowCalculator
from landlab.io import read_esri_ascii
from landlab.grid.mappers import map_max_of_link_nodes_to_link


def totalsedimenterosion_mudsine(roughness, grid, taucr, mud_erodability):

    
#xi = -lev_atlink-tidal_rangev/2
#xi[xi<0] = 0
#taucr += xi*tcrgradeint


fupeak = np.pi/2
#total sed erosion for loop
ntdcy = 10 #number of tidal cycles
E = grid.add_zeros('Erosion',at = 'cell')
print(mud_erodability)
print(" ")

# get rid of for loop
#for i in range(ntdcy):
utide = grid.at_cell['flood_tide_flow__velocity']*fupeak*np.sin(np.pi/2) #intra-tidal velocity
tauC = 1025*9.81*roughness**2 * utide**2 * grid._water_depth_at_cells**(-1/3)
E += mud_erodability*(np.sqrt(1+(tauC/taucr)**2)-1)
print(max(E))

print(grid.at_cell.keys())    
#print(np.maximum(E))