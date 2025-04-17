from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("This Bot uses Selenium to open spam an URL\n")

url = str(input("Enter the URL to spam : "))

n_input = input("How many tabs (0 for infinite) : ")
n = int(n_input) if n_input else 0

delay_input = input("Delay in seconds (0 for instant) : ")
delay = float(delay_input) if delay_input else 0

options = Options()
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=options)

driver.get(url)
if delay > 0:
    time.sleep(delay)

if n == 0:
    while True:
        driver.execute_script(f"window.open('{url}', '_blank');")
        if delay > 0:
            time.sleep(delay)
else:
    for _ in range(n - 1):
        driver.execute_script(f"window.open('{url}', '_blank');")
        if delay > 0:
            time.sleep(delay)

print(f"{'Infinite' if n == 0 else n} tabs opened with a delay of {delay} sec")
input("Enter to close tabs...")
driver.quit()
print("Tabs have been closed")