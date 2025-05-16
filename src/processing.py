from typing import List, Dict, Optional


def filter_by_state(data: ListDict, state: Optionalstr = 'EXECUTED') -> ListDict:
    """
    Фильтрует список словарей по значению ключа 'state'

    :param data: список словарей
    :param state: значение состояния для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список словарей
    """
    return [item for item in data if item.get('state') == state]
