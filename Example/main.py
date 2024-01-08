# selenium 4
# pip install webdriver_manager
# pip install selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager

# Other
import time

# Other Module
from AutoJLBC import Auto
from CAMD import *

#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
firefox = webdriver.Firefox()
firefox.maximize_window()
domain = "https://salarystaging37.salarynet.local"

# Operation Start's here
TC_1 = Auto(firefox,domain)


def MultipleCAMD(TC_1):

    # Login Part
    CAMD_1_01(TC_1)
    # Go to CompAnalyst Market Data    
    CAMD_1_02(TC_1)
    # Search Job Accountant
    CAMD_1_03(TC_1)
    # Filter Family Select first two checkbox
    #CAMD_1_04(TC_1)

    # Press reset button
    CAMD_1_05(TC_1)

    # Compare Jobs (Need to reset button b4 exectuing this)
    CAMD_1_06_1(TC_1)

    # Select two item the result and add job list
    #CAMD_1_1_06(TC_1)
    # Select the list title
    #CAMD_1_07(TC_1)

    # ------------Remove since it will unselect two selected--------------
    # Select two item the result and add job list
    #CAMD_1_1_06(TC_1)
    # --------------------------

    # Click next scope
    CAMD_2_01(TC_1)

    # Select / Tick 2 checkbox in the Scopes list
    CAMD_02_02_01(TC_1)

    # wait for the page loads after running report (or clicking the Next: Pricing button)
    CAMD_02_03(TC_1)

    # save .pdf .xlxs .csv
    CAMD_02_04(TC_1)

    # going back to job list
    CAMD_02_05(TC_1)

    # click the first job in the list
    CAMD_02_06(TC_1)

    # click adjust button
    CAMD_02_07(TC_1)

    # click save adjusted job
    CAMD_02_08(TC_1)

    # click okay in modal
    CAMD_02_09(TC_1)

    # click okay in modal
    CAMD_02_10(TC_1)

def SingleCAMD(TC_1):

    # Login Part
    CAMD_1_01(TC_1)
    # Go to CompAnalyst Market Data    
    CAMD_1_02(TC_1)
    # Search Job Accountant
    CAMD_1_03(TC_1)
    # Filter Family Select first two checkbox
    #CAMD_1_04(TC_1)

    # Press reset button
    CAMD_1_05(TC_1)

    # Compare Jobs (Need to reset button b4 exectuing this)
    CAMD_1_06(TC_1)

    # Select two item the result and add job list
    #CAMD_1_1_06(TC_1)
    # Select the list title
    #CAMD_1_07(TC_1)

    # ------------Remove since it will unselect two selected--------------
    # Select two item the result and add job list
    #CAMD_1_1_06(TC_1)
    # --------------------------

    # Click next scope
    CAMD_2_01(TC_1)

    # Select / Tick 1 checkbox in the Scopes list
    CAMD_02_02(TC_1)

    # wait for the page loads after running report (or clicking the Next: Pricing button)
    CAMD_02_03(TC_1)

    # save .pdf .xlxs .csv
    CAMD_02_04(TC_1)

    # going back to job list
    CAMD_02_05(TC_1)

    # click the first job in the list
    CAMD_02_06(TC_1)

    # click adjust button
    CAMD_02_07(TC_1)

    # click save adjusted job
    CAMD_02_08(TC_1)

    # click okay in modal
    CAMD_02_09(TC_1)

    # click okay in modal
    CAMD_02_10(TC_1)


SingleCAMD(TC_1)
CAMD_SignOut(TC_1)
MultipleCAMD(TC_1)


print("Doing Old Staging...")

# New login to OLD staging
CAMD_3_01(TC_1)

# Market Data -> Browse Jobs
CAMD_3_02(TC_1)

# Type and Search
CAMD_3_03(TC_1)

# add 2 items in the cart
CAMD_3_04(TC_1)

# Press button scope
CAMD_3_05(TC_1)


