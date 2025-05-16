from datetime import datetime
from typing import List, Dict, Optional


def sort_by_date(data: ListDict, ascending: Optionalbool = False) -> ListDict:
    """
    Сортирует список словарей по дате в формате ISO 8601

    :param data: список словарей с полем 'date'
    :param ascending: True - по возрастанию, False - по убыванию (по умолчанию)
    :return: отсортированный список словарей
    """

    def parse_date(item):
        date_str = item.get('date')

    if date_str:
        try:
            return datetime.fromisoformat(date_str)
    except ValueError:
    raise ValueError(f"Неверный формат даты: {date_str}")
    return None

    return sorted(data, key=parse_date, reverse=not ascending)