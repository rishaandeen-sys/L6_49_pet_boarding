"""Lab 6 - Branch coverage tests for pet_boarding.py.

Goal: take BOTH outcomes (True and False) of every decision in the module.
Run:  coverage run --branch -m pytest BranchCoverageTest_pet_boarding.py
      coverage report -m
"""
import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


# ---------------------------------------------------------------- boarding_fee
def test_unknown_pet_type_raises():
    with pytest.raises(ValueError, match="unknown pet type"):
        boarding_fee("hamster", 3, False)


def test_unknown_pet_checked_before_days():
    with pytest.raises(ValueError, match="unknown pet type"):
        boarding_fee("hamster", -1, False)


def test_negative_days_raises():
    with pytest.raises(ValueError, match="invalid days"):
        boarding_fee("cat", -1, False)


def test_zero_days_is_free():
    assert boarding_fee("dog", 0, False) == 0


@pytest.mark.parametrize("pet, days, premium, expected", [
    # extra <= 0 branch (True) and extra == 0 boundary
    ("dog", 1, False, 0),
    ("dog", 2, False, 0),
    ("cat", 3, False, 0),
    ("rabbit", 4, True, 0),
    # extra > 0, extra <= 10, dog rate (30) vs other rate (20)
    ("dog", 5, False, 90),
    ("cat", 6, False, 60),
    ("rabbit", 6, False, 40),
    # premium true and pet != rabbit  -> +1 included day
    ("dog", 5, True, 60),
    ("cat", 6, True, 40),
    # premium true but pet == rabbit -> no bonus day
    ("rabbit", 6, True, 40),
    # extra == 10 boundary: no surcharge yet
    ("dog", 12, False, 300),
    ("cat", 13, False, 200),
    # extra > 10: surcharge +10, plus +5 more for dogs
    ("dog", 13, False, 495),
    ("dog", 20, False, 810),
    ("cat", 14, False, 330),
    ("rabbit", 20, False, 480),
])
def test_boarding_fee_all_paths(pet, days, premium, expected):
    assert boarding_fee(pet, days, premium) == expected


# -------------------------------------------------------------- admission_ok
@pytest.mark.parametrize("age, vaccs, senior, expected", [
    (10, 3, True, True),     # senior with enough vaccinations
    (10, 2, True, False),    # senior, too few vaccinations
    (0.5, 3, True, True),    # senior flag wins over the age check
    (0.5, 5, False, False),  # under one year
    (0.99, 2, False, False),  # just under the age boundary
    (1, 2, False, True),     # exactly one year, enough vaccinations
    (4, 2, False, True),     # normal admission
    (4, 1, False, False),    # not enough vaccinations
])
def test_admission_ok_all_paths(age, vaccs, senior, expected):
    assert admission_ok(age, vaccs, senior) is expected


# ------------------------------------------------------------ checkout_status
@pytest.mark.parametrize("minutes, long_stay, weekend, expected", [
    # short stay, weekday  (cutoff 15)
    (15, False, False, "open"),
    (14, False, False, "late"),
    (0, False, False, "late"),
    (-1, False, False, "closed"),
    # long stay, weekday  (cutoff 30)
    (30, True, False, "open"),
    (29, True, False, "late"),
    (15, True, False, "late"),
    (14, True, False, "closed"),
    # short stay, weekend  (cutoff 35)
    (35, False, True, "open"),
    (34, False, True, "late"),
    (20, False, True, "late"),
    (19, False, True, "closed"),
    # long stay, weekend  (cutoff 50)
    (50, True, True, "open"),
    (49, True, True, "late"),
    (35, True, True, "late"),
    (34, True, True, "closed"),
])
def test_checkout_status_all_paths(minutes, long_stay, weekend, expected):
    assert checkout_status(minutes, long_stay, weekend) == expected
