import pytest


@pytest.fixture
def card_number():
    return "1234567891012345"


@pytest.fixture
def account_number():
    return "73654108430135874305"


@pytest.fixture
def real_date():
    return "2025-06-06T00:00:00"


@pytest.fixture
def mask_account():
    return "Visa Platinum 7000792289606361"