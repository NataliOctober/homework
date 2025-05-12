def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX

    :param card_number: номер карты
    :return: замаскированный номер карты
    """
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета в формате **XXXX

    :param account_number: номер счета
    :return: замаскированный номер счета
    """
    return f"**{account_number[-4:]}"