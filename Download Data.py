import os


import requests
import os
from multiprocessing.dummy import Pool
from functools import partial
import zipfile

def download_file(url, export_directory="", filename=None):
    print("Download file %s to directory %s"%(url, export_directory))
    if filename ==  None:
        local_filename = os.path.join(export_directory,url.split('/')[-1])
    else:
        local_filename = os.path.join(export_directory,filename)
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

#Set working directory to script directory:
script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

###Create Folders for Data:
##if not os.path.exists("Data"):
##    os.mkdir("Data")
##
##if not os.path.exists(os.path.join("Data","New York Taxi")):
##    os.mkdir(os.path.join("Data","New York Taxi"))
##
##if not os.path.exists(os.path.join("Data","OSM GPX")):
##    os.mkdir(os.path.join("Data","OSM GPX"))
##
###Download New York Taxi Data for Yellow Cabs in 2017:
##download_taxi_data = partial(download_file, export_directory=os.path.join("Data","New York Taxi"))
##request_strings = [r"https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2017-%02d.csv"%i for i in range(1,13)]
##pool = Pool(processes=4)
##pool.map(download_taxi_data, request_strings)
##
###Download New York Taxi Data for Green Cabs in 2017:
##download_taxi_data = partial(download_file, export_directory=os.path.join("Data","New York Taxi"))
##request_strings = [r"https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2017-%02d.csv"%i for i in range(1,13)]
##pool = Pool(processes=4)
##pool.map(download_taxi_data, request_strings)
##
###Download shapefile of New York Taxi Zones:
##print("Download Taxi Zones Shapefiles.")
##zip_path = download_taxi_data(r"https://s3.amazonaws.com/nyc-tlc/misc/taxi_zones.zip")
##print("Unzip Taxi Zones Shapefiles.")
##with zipfile.ZipFile(zip_path, "r") as z:
##    z.extractall(os.path.dirname(zip_path))
##os.remove(zip_path)

#Download OSM path data:
osm_path = download_file(r"https://ptv2box.ptvgroup.com/index.php/s/9sTUmxdF80NU2nr/download", export_directory=os.path.join("Data","OSM GPX"), filename="OSM_GPX.parquet")




