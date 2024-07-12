import os
import requests
from datetime import datetime, timedelta

def download_gif(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {save_path}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")




def scrub_radar_gifs(product, format, radar_station, start_date, end_date, type = 'RAIN'):
    # ie: https://dd.weather.gc.ca/radar/CAPPI/GIF/CASMB/202407102006_CASMB_CAPPI_1.5_RAIN.gif
    # ie:https://dd.weather.gc.ca/radar/DPQPE/GIF/CASMB/20240710T2006Z_MSC_Radar-DPQPE_CASMB_Rain.gif
    base_url = f"https://dd.weather.gc.ca/radar/{product}/{format}/{radar_station}"
    current_date = start_date
    
    if product == "CAPPI":
        tString,zString = '',''
        # ie _CASMB_CAPPI_1.5_RAIN
        if type == 'RAIN':
            product_string = f"_{radar_station}_CAPPI_1.5_RAIN"
        elif type == 'SNOW':
            product_string = f"_{radar_station}_CAPPI_1.0_SNOW"
    elif product == "DPQPE":
        # ie: Z_MSC_Radar-DPQPE_CASMB_Rain
        tString,zString = 'T','Z'
        if type == 'RAIN':
            product_string = f"_MSC_Radar-DPQPE_{radar_station}_Rain"
        elif type == 'SNOW':
            product_string = f"_MSC_Radar-DPQPE_{radar_station}_Snow"


    while current_date <= end_date:
        formatted_date = current_date.strftime(f"%Y%m%d{tString}%H%M{zString}")
        filename = f"{formatted_date}{product_string}.gif"
        url = f"{base_url}/{filename}"
        save_dir = os.path.join('data', 'radar',product,format,radar_station)
        save_path = os.path.join(save_dir, filename)

        os.makedirs(save_dir, exist_ok=True)
        if not os.path.exists(save_path):
            download_gif(url, save_path)

        current_date += timedelta(minutes=6)  # Assuming radar images are updated every 6 minutes

if __name__ == "__main__":
    product = "CAPPI" 
    format = "GIF"
    # radar_station = "CASGO" # halifax
    radar_station = "CASMB" # sydney
    radar_station = "CASCM" # fredericton
    start_date = datetime(2024, 7, 10, 18, 0)  # Start date and time
    end_date = datetime(2024, 7, 12, 19, 0)  # End date and time

    radar_stations = ["CASGO", "CASMB", "CASCM"] # Halifax, Sydney, Fredericton
    # radar_stations = ["CASGO"] # Halifax, Sydney, Fredericton

    products = ["CAPPI", "DPQPE"] # both product types
    # products = ["DPQPE"]

    for product in products:
        for radar_station in radar_stations:
            scrub_radar_gifs(product, format, radar_station, start_date, end_date, type = 'RAIN')
            scrub_radar_gifs(product, format, radar_station, start_date, end_date, type = 'SNOW')
