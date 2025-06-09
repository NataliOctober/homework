import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 2345"


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "**4305"

def test_wrong_mask_account():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("3421341241234213")

    assert str(exc_info.value) == ("Номер счёта должен содержать 20 цифр")

def test_wrong_card_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("ass")


        # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == ("Номер карты должен содержать 16 цифр")


