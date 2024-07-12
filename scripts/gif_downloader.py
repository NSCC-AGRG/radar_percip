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

def scrub_radar_gifs(product, format, radar_station, start_date, end_date, scale = '1.5', type = 'RAIN'):
    base_url = f"https://dd.weather.gc.ca/radar/{product}/{format}/{radar_station}"
    current_date = start_date

    

    while current_date <= end_date:
        formatted_date = current_date.strftime("%Y%m%d%H%M")
        filename = f"{formatted_date}_{radar_station}_{product}_{scale}_{type}.gif"
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

    for radar_station in radar_stations:
        scrub_radar_gifs(product, format, radar_station, start_date, end_date, scale='1.5', type = 'RAIN')
        scrub_radar_gifs(product, format, radar_station, start_date, end_date, scale='1.0', type = 'SNOW')
