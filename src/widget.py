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


def mask_account_card(data: str) -> str:
        """
        Маскирует номер карты или счёта в зависимости от типа.

        Принимает строку формата:
        - "Visa Platinum 7000792289606361"
        - "Maestro 7000792289606361"
        - "Счет 73654108430135874305"

        Возвращает строку с замаскированным номером:
        - "Visa Platinum 7000 79** **** 6361" для карт
        - "Счет **4305" для счетов

        :param data: входная строка с типом и номером
        :return: строка с маскированным номером
        """
        parts = data.split()

        # Для счетов
        if parts[0] == "Счет":
            account_number = parts[-1]
            return f"Счет **{account_number[-4:]}"

        # Для карт
        card_number = parts[-1]
        card_name = " ".join(parts[:-1])

        # Маскировка карты
        masked_card = (
            f"{card_name} "
            f"{card_number[:4]} "  # первые 4 цифры
            f"{card_number[4:6]}** "  # следующие 2 цифры и **
            f"**** "  # четыре звёздочки
            f"{card_number[-4:]}"  # последние 4 цифры
        )

        return masked_card
