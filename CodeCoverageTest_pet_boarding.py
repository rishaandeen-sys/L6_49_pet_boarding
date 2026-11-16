"""Lab 6 - Code (line) coverage tests for pet_boarding.py.

Goal: execute at least 90% of the lines of pet_boarding.py.
Run:  coverage run -m pytest CodeCoverageTest_pet_boarding.py
      coverage report -m
"""
import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


# ---------------------------------------------------------------- boarding_fee
def test_within_included_days():
    assert boarding_fee("dog", 1, False) == 0


def test_unknown_pet_type_raises():
    with pytest.raises(ValueError, match="unknown pet type"):
        boarding_fee("hamster", 3, False)


def test_negative_days_raises():
    with pytest.raises(ValueError, match="invalid days"):
        boarding_fee("cat", -1, False)


def test_dog_extra_days_uses_dog_rate():
    # dog includes 2 days -> 3 extra days * 30
    assert boarding_fee("dog", 5, False) == 90


def test_premium_cat_gets_one_extra_included_day():
    # cat includes 3 (+1 premium) = 4 days -> 2 extra days * 20
    assert boarding_fee("cat", 6, True) == 40


def test_long_stay_dog_surcharge():
    # dog includes 2 days -> 18 extra days, rate 30 + 10 + 5 = 45
    assert boarding_fee("dog", 20, False) == 810


# -------------------------------------------------------------- admission_ok
def test_admission_ok():
    assert admission_ok(4, 2, False) is True


def test_admission_senior_with_three_vaccinations():
    assert admission_ok(10, 3, True) is True


def test_admission_rejects_pet_under_one_year():
    assert admission_ok(0.5, 5, False) is False


# ------------------------------------------------------------ checkout_status
def test_checkout_open_long_stay_weekend():
    assert checkout_status(60, True, True) == "open"


def test_checkout_late_for_short_stay():
    assert checkout_status(10, False, False) == "late"


def test_checkout_closed():
    assert checkout_status(-1, False, False) == "closed"
