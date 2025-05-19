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


