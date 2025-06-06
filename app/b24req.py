import requests
from requests.exceptions import RequestException
import json

def call_bitrix_api(user_id, access_token, method, params=None):
    base_url = "https://corp.stankin.ru/rest"
    url = f"{base_url}/{user_id}/{access_token}/{method}"

    try:
        response = requests.get(
            url,
            timeout=10,  # таймаут 10 секунд
            headers={'Accept': 'application/json'},
            params=params
        )

        response.raise_for_status()
        return response.json()

    except RequestException as e:
        print(f"API request failed: {e}")
        if e.response is not None:
            print(f"Status code: {e.response.status_code}")
            try:
                error_details = e.response.json()
                print(f"Error details: {json.dumps(error_details, indent=2)}")
            except ValueError:
                print(f"Raw response: {e.response.text}")
        return None


# Использование функции
result = call_bitrix_api(
    user_id="3735",
    access_token="vqd6nuu339loo2c8",
    method="calendar.section.get.json",
    params={
        "type":"location",
        "ownerId":"0"
    }
)

if result:
    print("Результат запроса:")
    print(json.dumps(result, indent=2, ensure_ascii=False))