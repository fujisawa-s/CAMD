
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Auto:
    
    def __init__(self, driver ,domain):
        self.domain = domain
        self.driver = driver
    
    def Test(self):
        print("Test")

    def CloseCurrentTab(self):
        self.driver.close()
    
    def SwitchToPrevTab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])


    def TimeLoads(self,url):
        # start the timer
        start_time = time.time()
        # load the website
        self.driver.get(url)
        # end the timer
        end_time = time.time()
        # calculate the elapsed time
        elapsed_time = end_time - start_time
        
        return elapsed_time
        
    def VisitSite(self,path):
        
        url = f"{self.domain}{path}"
        time = self.TimeLoads(url)
        #print(f"Elapsed time: {time:.2f} seconds")
    
    def SelectElement(self,selector,val_selector):
        
        if selector == 'class':
            return self.driver.find_element(By.CLASS_NAME, val_selector)
        elif selector == 'id':
            return self.driver.find_element(By.ID, val_selector)
        elif selector == 'name':
            return self.driver.find_element(By.NAME, val_selector)
        elif selector == 'css':
            return self.driver.find_element(By.CSS_SELECTOR, val_selector)
        elif selector == 'xpath':
            return self.driver.find_element(By.XPATH, val_selector)
        else:
            print("Something went wrong...")
            return
        
    
    def Type(self,selector,val_selector,val):
        
        element = self.SelectElement(selector,val_selector)
        element.send_keys(val)
    
    def FindText(self,text):
    
     
        retry = 3
        
        while True:
        
            if text in self.driver.page_source:
                
                #print("Existed")
                time.sleep(4)
                return True
                            
            elif retry == 0:
                #print("Not Existed")
                time.sleep(4)
                return False
                
            else:
                retry = retry - 1
            
    
    # Not yet optimized
    def WaitUntil(self,selector,val_selector):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((selector, val_selector)))
    
    def WaitPageLoad(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url.contains(text))
    
    # Not working ATM will resort using time.sleep(seconds)
    def Wait(self,seconds):
        self.driver.implicitly_wait(seconds)

    def document_initialised():
        return self.driver.execute_script("return initialised")

    def WaitDocumentLoad(self):
        WebDriverWait(self.driver, timeout=10).until(self.document_initialised())
    
    def Press(self,selector,val):
 
        element = self.SelectElement(selector,val)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    # For testing not working atm 
    def GetElements(self,selector,val_selector):
        element = self.find_elements(selector,val_selector)
        return element
    

    def Log(self,state,text):
    
        if state:
            print(f"✓ - {text}")
        else:
            print(f"☓ - {text}")
    
    def Reload(self):
        self.driver.refresh()

    def ExecuteJSScript(self,script):
        self.driver.execute_script(script)

