# L6_49 - Pet Boarding

Lab 6: Code and Branch Coverage

**Name:** Rishaan Deen | **SRN:** PES2UG24AM134

## Files

| File | Description |
|------|-------------|
| `pet_boarding.py` | The module under test |
| `test_pet_boarding.py` | Starter test file (unchanged) |
| `CodeCoverageTest_pet_boarding.py` | Tests for line (code) coverage |
| `BranchCoverageTest_pet_boarding.py` | Tests for branch coverage |
| `screenshots/` | Terminal output of the coverage runs |

## Results

| Stage | Command | Result |
|-------|---------|--------|
| Starter tests | `coverage run --branch -m pytest test_pet_boarding.py` | 32% line coverage (pet_boarding.py) |
| Code coverage | `coverage run -m pytest CodeCoverageTest_pet_boarding.py` | **100% line coverage** (12 tests) |
| Branch coverage | `coverage run --branch -m pytest BranchCoverageTest_pet_boarding.py` | **100% line and branch coverage** (26/26 branches, 44 tests) |

Run `coverage report -m` after each `coverage run` to see the table.
