#!/usr/bin/env python
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
import cartopy.feature as cfeature

def plot_stations(lons, lats):
    """
    Plots water pump station location given the longitudes and latitudes
    
    Parameters
    ----------

    lons : numpy 1D array of floats
         : longitudes of stations in degrees

    lats : numpy 1D array of floats
         : latitudes of stations in degrees

    Returns 
    -------
    Nothing
    """

    fig = plt.figure(figsize=(16,8))
    ax = fig.add_subplot(121, projection=ccrs.PlateCarree())
    ax2 = fig.add_subplot(122, projection=ccrs.PlateCarree())

    ax.scatter(lons,lats,alpha=1, label='Stations')
    ax2.scatter(lons,lats,alpha=0.01, label='Stations')

    ax.coastlines(zorder=2, resolution='50m', color='black', linewidth=1, alpha=1)
    ax.set_extent([27,42,-15,0])
    ax.add_feature(cfeature.BORDERS, edgecolor="darkgreen", linewidth=2, label='Country borders')
    ax.add_feature(cfeature.OCEAN, color="skyblue", alpha=0.4)
    gl = ax.gridlines(draw_labels=True, linewidth=0, color='gray', alpha=1, linestyle='--')

    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xlabels_bottom = True
    gl.ylabels_left = True
    plt.legend(loc='best')
    ax2.coastlines(zorder=2, resolution='50m', color='black', linewidth=1, alpha=1)
    ax2.set_extent([27,42,-15,0])
    ax2.add_feature(cfeature.BORDERS, edgecolor="darkgreen", linewidth=2, label='Country borders')
    ax2.add_feature(cfeature.OCEAN, color="skyblue", alpha=0.4)
    gl = ax2.gridlines(draw_labels=True, linewidth=0, color='gray', alpha=1, linestyle='--')

    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xlabels_bottom = True
    gl.ylabels_left = True

    ax.set_title("Station locations")
    ax.set_xlabel('Longitude ($^{\circ}$)')
    ax.set_ylabel('Latitude ($^{\circ}$)')
    ax2.set_title("Station locations with 1% opacity")

    plt.show()
    return 