import matplotlib.pyplot as plt
import geopandas
from shapely.geometry import Point

def plot_geolocation_by_cluster(geo_df,
                                cluster=None,
                                title=None,
                                centers=None,
                                filename=None):
    # Set figure size
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')

    # Plot coordinates from geo_df on top of NYC map
    if cluster is not None:

        geo_df.plot(ax=ax, column=cluster, alpha=0.5,
                    cmap='viridis', linewidth=0.8, zorder=2)

        if centers is not None:
            centers_gseries = geopandas.GeoSeries(map(Point, zip(centers[:, 1], centers[:, 0])))
            centers_gseries.plot(ax=ax, alpha=1, marker='X', color='red', markersize=100, zorder=3)

        plt.title(title)
        plt.xlabel('longitude')
        plt.ylabel('latitude')
        plt.show()

        if filename is not None:
            fig.savefig(f'{filename}', bbox_inches='tight', dpi=300)
    else:
        geo_df.plot(ax=ax, alpha=0.5, cmap='viridis', linewidth=0.8, legend=True, zorder=2)

        plt.title(title)
        plt.xlabel('longitude')
        plt.ylabel('latitude')
        plt.show()

    fig.clf()