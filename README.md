# Cricket Score App

## Introduction

The Cricket Score App is a software application designed to provide users with real-time updates on cricket scores. The app utilizes Tkinter, a standard Python library for creating graphical user interfaces, to offer a user-friendly and interactive experience. Additionally, the application employs web scraping techniques to extract live cricket scores from Cricbuzz, a popular cricket-related website.

## Features

- Displays live cricket scores from Cricbuzz.
- User-friendly graphical interface built with Tkinter.
- Automatically updates scores at regular intervals.

## Requirements

- Python 3.x
- Tkinter library
- Requests library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cricket-score-app.git
   cd cricket-score-app
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. The GUI window will appear, displaying live cricket scores.

3. Scores will be automatically updated at regular intervals.

## Configuration

- You can adjust the update interval by modifying the `UPDATE_INTERVAL` variable in the `main.py` file.

## Dependencies

- [Tkinter](https://docs.python.org/3/library/tkinter.html): Python's standard GUI (Graphical User Interface) package.
- [Requests](https://docs.python-requests.org/en/latest/): HTTP library for making requests to Cricbuzz API.

## Credits

- The web scraping functionality is implemented using the Cricbuzz API.
- Tkinter documentation: [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)
- Requests library documentation: [https://docs.python-requests.org/en/latest/](https://docs.python-requests.org/en/latest/)

## Disclaimer

This application is for educational purposes only. Use it responsibly and respect the terms of service of the data providers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
