# src/processing.py
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


def process_data(data: dict) -> dict:
    """
    Обрабатывает входные данные и возвращает словарь с замаскированными данными

    :param data: словарь с данными
    :return: словарь с обработанными данными
    """
    processed_data = {}

    for key, value in data.items():
        if key == "card_number":
            processed_data[key] = mask_account_card(value)
    elif key == "account_number":
    processed_data[key] = get_mask_account(value)
    elif key == "date":
    processed_data[key] = get_date(value)
    else:
    processed_data[key] = value

    return processed_data


def validate_data(data: dict) -> bool:
    """
    Валидирует входные данные

    :param data: словарь с данными
    :return: True если данные валидны, иначе False
    """
    required_fields = {"card_number", "account_number", "date"}
    if not required_fields.issubset(data.keys()):
        return False

    if not isinstance(data.get("card_number"), str):
        return False

    if not isinstance(data.get("account_number"), str):
        return False

    if not isinstance(data.get("date"), str):
        return False

    return True