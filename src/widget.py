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