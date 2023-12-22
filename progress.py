from datetime import datetime

def percent_of_year_passed():
    now = datetime.now()
    start_of_year = datetime(now.year, 1, 1)
    end_of_year = datetime(now.year + 1, 1, 1)
    return ((now - start_of_year).total_seconds() / (end_of_year - start_of_year).total_seconds()) * 100

if __name__ == "__main__":
    print(f"Year Progress: {percent_of_year_passed():.2f}%")
