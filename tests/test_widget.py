import pytest
from datetime import datetime
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("date, expected", [("2025-06-06T00:00:00", "06.06.2025"),
                                            ("2024-05-02T01:10:20", "02.05.2024")])
def test_get_date(date, expected):
    assert get_date(date) == expected


def test_mask_account_card(mask_account):
    assert mask_account_card(mask_account) == "Visa Platinum 7000 79** **** 6361"



