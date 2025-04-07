import os
import numpy as np

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


def main():
    # -- set environment variable CARTOPY_USER_BACKGROUNDS
    os.environ['CARTOPY_USER_BACKGROUNDS'] = 'Week4/imgs'

    # -- set projection
    projection = ccrs.UTM(29)

    # -- create two plots next to each other
    # -- 1. on the left ax.stock_img() is used for map background
    # -- 2. on the right the high resolution image from Natural Earth Data is used

    plt.switch_backend('agg')

    fig = plt.figure(figsize=(8, 8))

    ax1 = fig.add_subplot(1, 2, 1, projection=projection)
    ax1.set_title('ax.stock_img()')
    ax1.set_extent([5., 20., 35.0, 60.0])
    ax1.stock_img()
    ax1.coastlines(resolution='10m')
    gl1 = ax1.gridlines(draw_labels=True)
    gl1.xlines = False
    gl1.ylines = False
    gl1.right_labels = False

    ax2.set_title('ax.background_img() - NaturalEarth')
    ax2.set_extent([5., 20., 35.0, 60.0])
    ax2.background_img(name='NaturalEarthRelief', resolution='high')
    ax2.coastlines(resolution='10m')
    gl2 = ax2.gridlines(draw_labels=True)
    gl2.xlines = False
    gl2.ylines = False
    gl2.left_labels = False

    plt.savefig('plot_high_resolution_background_image.png', bbox_inches='tight', dpi=100)


if __name__ == '__main__':
    main()