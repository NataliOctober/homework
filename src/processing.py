# src/processing.py
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date

from typing import List, Dict, Optional


def filter_by_state(data: List[Dict], state: Optional[str] = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'

    :param data: список словарей
    :param state: значение состояния для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список словарей
    """
    return [item for item in data if item.get('state') == state]

def get_transaction_date(tra: dict) -> str:
    date = tra["date"]
    return date


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    result = sorted(data, key=get_transaction_date, reverse=reverse)
    return result


data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(sort_by_date(data))

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
from typing import List, Dict, Optional


def filter_by_state(data: ListDict, state: Optionalstr = 'EXECUTED') -> ListDict:
    """
    Фильтрует список словарей по значению ключа 'state'

    :param data: список словарей
    :param state: значение состояния для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список словарей
    """
    return [item for item in data if item.get('state') == state]
