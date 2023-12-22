from progress import percent_of_year_passed

def test_percent_of_year_passed():
    assert 0 <= percent_of_year_passed() <= 100
