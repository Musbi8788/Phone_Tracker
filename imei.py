import requests
# from p_number import imei_number

def lookup_imei(imei_number):
    # Replace with your actual API endpoint and key
    api_url = f"https://dash.imei.info/api{imei_number}"
    api_key = "634c740f-5a82-452b-a268-0628c5baffe4"  # Make sure to replace with your API key

    params = {
        'imei': imei_number,
        'api_key': api_key
    }

    # Make a request to the API
    response = requests.get(api_url + imei_number, params=params)



    if response.status_code == 200:
        data = response.json()
        print("IMEI Information:")
        print(f"Model: {data.get('model')}")
        print(f"Brand: {data.get('brand')}")
        print(f"Status: {data.get('status')}")
        print(f"Blacklisted: {data.get('blacklisted')}")
    else:
        print("Error: Unable to fetch IMEI data.")

# Example usage with your IMEI number
imei_number = "356857514570681"
lookup_imei(imei_number)

