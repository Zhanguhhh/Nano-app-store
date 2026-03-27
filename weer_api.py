import requests

def toon_weer():
        loc_resp = requests.get("https://ipinfo.io/json", timeout=10)
        loc_resp.raise_for_status()
        loc_data = loc_resp.json()

        city = loc_data.get("city", "onbekende stad")
        loc_str = loc_data.get("loc", "0,0")
        lat, lng = map(float, loc_str.split(","))

        weer_url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lng}"
            f"&current=temperature_2m,wind_speed_10m"
        )
        weer_resp = requests.get(weer_url, timeout=10)
        weer_resp.raise_for_status()
        weer_data = weer_resp.json()

        temp = weer_data['current']['temperature_2m']
        temp_unit = weer_data['current_units']['temperature_2m']
        wind = weer_data['current']['wind_speed_10m']
        wind_unit = weer_data['current_units']['wind_speed_10m']

        print(f"In {city} is het nu {temp} {temp_unit}. De windsnelheid is {wind} {wind_unit}.")
