from sqlalchemy import create_engine
import pandas as pd
import geopandas

user = 'postgres'
password = 'postgres'
port='5433'
host='localhost'
DB='postgres'

def get_conn():
    from sqlalchemy import create_engine
    from sqlalchemy_utils import database_exists, create_database
    db_string = f"""postgresql://{user}:{password}@{host}:{port}/{DB}"""
    driver = create_engine(db_string)
    try:
        database_exists(driver.url)
        conn = driver.connect()
    except:
        create_database(driver.url)
        conn = driver.connect()

    return conn

def data_transform(df):
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['week'] = df.datetime.dt.week
    df['origin_coord'] = geopandas.GeoSeries.from_wkt(df['origin_coord'])
    df['destination_coord'] = geopandas.GeoSeries.from_wkt(df['destination_coord'])
    gdf = geopandas.GeoDataFrame(df, geometry='origin_coord')
    gdf['distance'] = gdf.origin_coord.distance(gdf.destination_coord, align=False)
    return gdf

def upload_csv_sql(dic,conn):
    for file in dic:
        df = pd.read_csv(dic[file])
        df.to_sql(file, con=conn, index=False)

if __name__ == '__main__':
    dic = {'trips': 'csvs/trips.csv'}
    conn = get_conn()
    upload_csv_sql(dic,conn)


