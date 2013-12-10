import sys
import urllib
import os
import pandas as pd
import curate_util as cu
import numpy as np

def get_year(entry):
    a = str(entry["YYYY/MM/DD"])
    b = re.split("\\s+", a)[1]
    return int(re.split("/", b)[0])


def get_plot_res(years):
    data_dict = cu.grab_data_dict(years[0],years[1],'tristan_curators/clean_data/')
    quakes = cu.grab_data_frame(data_dict)

    max_lat = quakes['LAT'].max()
    min_lat = quakes['LAT'].min()
    max_lon = quakes['LON'].max()
    min_lon = quakes['LON'].min()
    dimensions = ((max_lat-min_lat), (max_lon-min_lon))

    threshold = [1,10,100,1000,10000]
    res = ['f','h','i','l','c']
    area = dimensions[0]*dimensions[1]

    for i in range(5):
        if area <= threshold[i]:
            res = res[i]
            break
        if i == 5:
            res = res[5]
            
    return res


def get_colormap(years):
    num_years = years[1]-years[0]
    year_color = np.arange(0, num_years + 1).astype(float)/(num_years + 1)
    
    colormap = [0]*(num_years+1)
    for i in range(0, num_years + 1):
        colormap[i] = pylab.cm.Reds(year_color[i])
    
    return colormap

def get_quakes_subset(years, quantity):
    
    quakes = cu.grab_data_frame(cu.grab_data_dict(years[0],years[0],'tristan_curators/clean_data/'))[0:quantity]
    
    for year in range(years[0] + 1, years[1] + 1): 
        data_dict = cu.grab_data_dict(year,year,'tristan_curators/clean_data/')
        df = cu.grab_data_frame(data_dict)[0:quantity]
        quakes = pd.DataFrame.append(quakes, df)
        
    return quakes

from mpl_toolkits.basemap import Basemap

def plot_quakes(years, figsize, quantity):
    
    res = get_plot_res(years)
    
    colors = get_colormap(years)
    
    quakes = get_quakes_subset(years, quantity)
    
    lat_0 = quakes['LAT'].mean()
    lon_0 = quakes['LON'].mean()
    fig = matplotlib.pyplot.figure(figsize=figsize)
    m = Basemap(resolution = res, projection='nsper',
                area_thresh = 1000., satellite_height = 200000,
                lat_0 = lat_0, lon_0 = lon_0)
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.fillcontinents(color = 'green', lake_color = 'aqua')
    m.drawmapboundary(fill_color = 'blue')
    x, y = m(quakes.LON, quakes.LAT)
    
    for i in range(0, len(x) - 1):
        color = colors[get_year(quakes[i:i+1])-years[0]]
        m.plot(x[i:i+1], y[i:i+1], color = color, 
               marker = 'o', markersize = (pi*(quakes.MAG[i:i+1]).apply(float)**2), 
               alpha = 0.5)


