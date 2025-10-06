from utils.driver_factory import create_driver
import time

driver = create_driver()

time.sleep(5)

driver.quit()