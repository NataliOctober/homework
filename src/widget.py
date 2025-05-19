from datetime import datetime
from typing import Optional


def sort_by_date(date_string: str, format_string: Optional[str] = '%d.%m.%Y') -> str:
    """
    Форматирует дату из формата ISO 8601 в указанный формат

    :param date_string: строка с датой в формате ISO 8601
    :param format_string: формат вывода даты (по умолчанию '%d.%m.%Y')
    :return: отформатированная дата
    """
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime(format_string)
    except ValueError:
        raise ValueError(f"Неверный формат даты: {date_string}")


from masks import mask_card, mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счёта, используя существующие функции из masks.py

    :param data: входная строка с типом и номером
    :return: строка с маскированным номером
    """
    parts = data.split()

    if parts[0] == "Счет":
        return mask_account(data)
    else:
        return mask_card(data)