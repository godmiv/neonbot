import requests
from requests.exceptions import RequestException
from datetime import datetime, timedelta
import json


def call_bitrix_api(user_id, access_token, method, params=None):
    """
    Универсальная функция для вызова API Bitrix24
    """
    base_url = "https://corp.stankin.ru/rest"
    url = f"{base_url}/{user_id}/{access_token}/{method}"

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10,
            headers={'Accept': 'application/json'}
        )
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        print(f"Ошибка запроса: {e}")
        if e.response:
            print(f"Код ошибки: {e.response.status_code}")
            print(f"Ответ сервера: {e.response.text}")
        return None


def get_resource_bookings():
    """
    Получает список всех переговорок и их бронирований
    """
    # 1. Сначала получаем список всех ресурсов
    resources = call_bitrix_api(
        user_id="3735",  # Замените на реальный ID
        access_token="vqd6nuu339loo2c8",  # Замените на реальный токен
        method="calendar.resource.list.json"
    )

    if not resources or not resources.get('result'):
        print("Не удалось получить список переговорок")
        return

    # 2. Для каждой переговорки получаем бронирования
    for resource in resources['result']:
        print(f"\nПереговорка: {resource['NAME']} (ID: {resource['ID']})")

        params = {
            "resource_id": resource['ID'],
            "from": datetime.now().strftime("%Y-%m-%d"),
            "to": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        }

        bookings = call_bitrix_api(
            user_id="3735",  # Замените на реальный ID
            access_token="vqd6nuu339loo2c8",  # Замените на реальный токен
            method="calendar.resource.booking.list.json",
            params=params
        )

        if not bookings or not bookings.get('result'):
            print("  Нет бронирований")
            continue

        for booking in bookings['result']:
            print(f"  - Бронирование: {booking.get('TITLE', 'Без названия')}")
            print(f"    Время: {booking.get('DATE_FROM')} - {booking.get('DATE_TO')}")
            print(f"    Организатор: {booking.get('CREATED_BY', 'Неизвестно')}")


# Запускаем функцию
get_resource_bookings()