# URL Tab Opener Script

![](https://raw.githubusercontent.com/Dimitri-Blanchard/url_spam_bot/refs/heads/main/images/selenium.png)

## Description

This Python script uses Selenium to automatically open a specified URL in multiple browser tabs. You can control the number of tabs to open and the delay between each opening.

## Features

* Opens a user-specified URL.
* Allows setting a specific number of tabs to open.
* Option to open an infinite number of tabs (until stopped manually).
* Configurable delay (in seconds) between opening each new tab.
* Uses Google Chrome via Selenium WebDriver.

## Requirements

* Python 3.13.3
* Selenium library for Python
* Google Chrome browser installed
* ChromeDriver executable compatible with your installed Chrome version.

## Installation

1.  **Install Python:** Make sure you have Python 3.13.3 installed. You can download it from [python.org](https://www.python.org/).
2.  **Install Selenium:** Open your terminal or command prompt and run:
    ```bash
    pip install selenium
    ```
3.  **Download ChromeDriver:**
    * Check your Google Chrome version (Go to `chrome://settings/help`).
    * Download the corresponding ChromeDriver version from the [official ChromeDriver website](https://chromedriver.chromium.org/downloads) or the [Chrome for Testing availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/).
    * Place the downloaded `chromedriver` executable either in the same directory as the Python script or in a directory included in your system's PATH environment variable.

## Usage

1. Clone repo :

```bash
git clone github.com/Dimitri-Blanchard/url_spam_bot
```

3. Enter the repo folder

```bash
cd url_spam_bot
```

4.  Run the script using Python:
```bash
python bot.py
```

5.  The script will prompt you for the following information:
    * **URL to spam:** Enter the full URL you want to open (e.g., `https://www.example.com`)
    * **How many tabs (0 for infinite):** Enter the desired number of tabs. Enter `0` to keep opening tabs indefinitely
    * **Delay (seconds) between opening (0 for instant):** Enter the time delay in seconds between opening each tab. Enter `0` for no delay (instant opening)
6.  The script will open the specified number of tabs with the given delay.
7.  Once the script has finished opening tabs (or if you want to stop the infinite mode), go back to the terminal where the script is running
8.  Press `Enter` when prompted to close the browser window and all opened tabs.

## ⚠️ Warning

* Opening a very large number of tabs, especially with no delay, can consume significant system resources (RAM and CPU) and may cause your browser or even your entire system to become unresponsive or crash
* Use this script responsibly. Avoid using it to overload websites or servers, as this could be disruptive and potentially violate their terms of service. The author is not responsible for any misuse of this script
