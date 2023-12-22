from datetime import datetime

def percent_of_year_passed():
    now = datetime.now()
    start_of_year = datetime(now.year, 1, 1)
    end_of_year = datetime(now.year + 1, 1, 1)
    return ((now - start_of_year).total_seconds() / (end_of_year - start_of_year).total_seconds()) * 100

def create_progress_bar(percentage, bar_length=40):
    # Using a block for filled part and a dot for unfilled
    filled_length = int(round(bar_length * percentage / 100))
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    return bar

if __name__ == "__main__":
    name = f"{datetime.now().strftime('%Y-%m-%d')}"
    progress_percentage = percent_of_year_passed()
    progress_bar = create_progress_bar(progress_percentage)
    readme_content = f"# Year Progress\n{name}\n{progress_bar} {progress_percentage:.2f}%"
    with open('README.md', 'w') as file:
        file.write(readme_content)