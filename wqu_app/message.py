import requests


def retrieve_local_ip_address():
    """Return the IP address of the local system."""
    response = requests.get('https://api.ipify.org')

    return response.text


def get_location(ip_address):
    """Return the geolocation given an IP address."""
    url = f'https://freegeoip.app/json/{ip_address}'
    response = requests.get(url)

    return response.json()


def get_sun_info(ip_address):
    """Return sunrise and sunset data given an IP address."""
    data = get_location(ip_address)
    lat, lon = float(data['latitude']), float(data['longitude'])

    url = 'https://api.sunrise-sunset.org/json'
    params = {'lat': lat, 'lng': lon}
    response = requests.get(url, params=params)

    return response.json()


def generate_sunset_message(ip_address):
    """Return string of sunset message"""
    data = get_sun_info(ip_address)
    sunset_time = data['results']['sunset']

    return f"The sun will set at {sunset_time} UTC."


def main():
    ip_address = retrieve_local_ip_address()
    location_data = get_location(ip_address)
    message = generate_sunset_message(ip_address)

    print(f"Your IP address is: {ip_address}")
    print(f"You are located in {location_data['city']}")
    print(message)


if __name__ == '__main__':
    main()
