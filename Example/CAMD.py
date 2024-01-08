from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from datetime import datetime

# Sign Out

def CAMD_SignOut(OP):
    TC_1 = OP
    time.sleep(10)

    #$('.sa-navbar-global-menu .sa-navbar-global-account .caret').click()
    # Show Dropdown Items
    TC_1.ExecuteJSScript("$('.sa-navbar-global-menu .sa-navbar-global-account .caret').click()")
    time.sleep(3)

    # Hit Logout Button
    # I used direct accesss link since when it pressed it disabled the button
    # /companalyst/cloud/Account/cpal_logout
    # TC_1.ExecuteJSScript("$('.sa-navbar-global-menu .sa-navbar-global-account .caret').click()")
    TC_1.VisitSite("/companalyst/cloud/Account/cpal_logout")

    TC_1.Log(True,'Logout the account')
    time.sleep(3)

# Login
def CAMD_1_01(OP):
    TC_1 = OP
    
    TC_1.VisitSite("/companalyst/cloud/Account/cpal_login")
    
    # Populate login credentials
    # type - selector val - text to be input
    #TC_1.Type('id','loginid','lisa0021')
    TC_1.ExecuteJSScript("$('#loginid').val('lisa0021')")
    #TC_1.Type('id','password','Admin@1234')
    TC_1.ExecuteJSScript("$('#password').val('Admin@1234')")
    TC_1.Press('class','btn-login')
    
    if TC_1.FindText('Welcome'):
        TC_1.Log(True,'Login Page')
    else:
        TC_1.Log(False,'Login Page')
    
# Go to CompAnalyst Market Data    
def CAMD_1_02(OP):
    
    TC_1 = OP
    
    # Reveal Dropdown CompAnalyst Market Data
    TC_1.ExecuteJSScript("$('#nav-global-marketdata').css('display','block')")
    # Press CompAnalyst Market Data
    # TC_1.ExecuteJSScript("$('#nav-global-marketdata').css('display','block')")
    # When pressing this it disable the button, it not re-direct the user to corresponding web page
    time.sleep(3)
    TC_1.VisitSite('/companalyst/cloud/camd/Cpal_Camd_Landing')

    if TC_1.FindText('CompAnalyst Market Data'):
        TC_1.Log(True,'CompAnalyst Market Data Page')
    else:
        TC_1.Log(False,'CompAnalyst Market Data Page')
        
# Search Job Accountant
def CAMD_1_03(OP):
    TC_1 = OP

    TC_1.Type('id','searchBoxInput','Accountant' + Keys.RETURN )
    logtext = 'Search a Job'

    # Wait
    TC_1.Wait(10)

    if TC_1.FindText('Accountant I'):
        TC_1.Log(True,logtext)
    else:
        TC_1.Log(False,logtext)

# Filter Family select first two checkbox
def CAMD_1_04(OP):
    TC_1 = OP

    if TC_1.FindText('Accountant I'):
        # TC_1.Log(True,'1.01 CompAnalyst Market Data Page')
        # Collapse Family Filter Dropdown
        # TC_1.Press('id','familyfilterdropdown')
        TC_1.ExecuteJSScript("$('#familyfilterdropdown .dropdown-toggle').click()")
        time.sleep(5)
        # Click the first checkbox
        # TC_1.Press('css','#FamilyFilter #familyDiv ul li:nth-child(3)')
        TC_1.ExecuteJSScript("$('#FamilyFilter #familyDiv ul li:nth-child(4) label').click()")
        TC_1.Log(True,'Dropdown Family Filter Clicked')
        time.sleep(5)
        # Click the Apply Button
        # TC_1.Press('css','#FamilyFilter #familyDiv ul .filters-footer .btn-apply')
        TC_1.ExecuteJSScript("$('#FamilyFilter #familyDiv ul .filters-footer .btn-apply').click()")
        TC_1.Log(True,'Button Apply Clicked')

        TC_1.Log(True,'Filter Job Family')
        time.sleep(5)

    else:
        TC_1.Log(False,'Filter Job Family')

    time.sleep(5)
           
# Press the reset button
def CAMD_1_05(OP):
    TC_1 = OP
    while True:
        try:
            # Press the reset all button
            TC_1.Press('css','#reset-all a')
            TC_1.Log(True,'Button reset clicked')
            # TC_1.Wait(10)
            break
        except:
            continue
            
    time.sleep(5)

# Select one item the result and compare job
def CAMD_1_06(OP):
    TC_1 = OP

    if(TC_1.FindText('#camd-search-results')):

        # Execute Javascript
        # Select 2 items in the list 
        TC_1.ExecuteJSScript("$('#camd-search-results tbody .tr_checkbox .sa-table-cell-check label')[1].click()")
        #TC_1.ExecuteJSScript("$('#camd-search-results tbody .tr_checkbox .sa-table-cell-check label')[2].click()")

        TC_1.Wait(3000)

        # Click Compare
        # sa-wizard-marketprice2
        TC_1.Press('css','#sa-wizard-marketprice2 ul li:nth-child(1)')

        # Assert
        if TC_1.FindText('Compare Jobs'):
            TC_1.Log(True,'Compare Job')

            time.sleep(10)
            
            # Press back to job list
            TC_1.Press('css','#CompareJob .CompareJobHeader div:nth-child(1) #backToJobList a')
            
            # # Click Hybrid
            # if TC_1.FindText('CompAnalyst Market Data'):
            #     TC_1.Press('css','#sa-wizard-marketprice2 ul li:nth-child(2)')

            #     TC_1.Wait(2)
                
            #     TC_1.Log(True,'Hybrid')
                


            #     if TC_1.FindText('Create Hybrid Job'):
            #         # Enter Hybrid Job Title
            #         current_datetime = datetime.now()
            #         # TC_1.Type('css','#hybridjobtitle', f'Lloyd Automation {current_datetime}')
            #         TC_1.ExecuteJSScript(
            #             f"""
            #                 $('#hybridjobtitle').val('Lloyd Automation {current_datetime}')    
            #             """
            #         )


            #     else:
            #         TC_1.Log(False,'Hybrid')

               


            # else:
            #     TC_1.Log(False,'Hybrid')

        else:
            TC_1.Log(False,'Compare Job')



    else:
        TC_1.Log(False,'Something went wrong, cannot select 3 items in the list')
    
    time.sleep(5)
    # TC_1.VisitSite('/CompAnalyst/Cloud/camd/Cpal_Camd_SearchResultList')

# Select two item the result and compare job
def CAMD_1_06_1(OP):
    TC_1 = OP

    if(TC_1.FindText('#camd-search-results')):

        # Execute Javascript
        # Select 2 items in the list 
        TC_1.ExecuteJSScript("$('#camd-search-results tbody .tr_checkbox .sa-table-cell-check label')[1].click()")
        TC_1.ExecuteJSScript("$('#camd-search-results tbody .tr_checkbox .sa-table-cell-check label')[2].click()")

        TC_1.Wait(3000)

        # Click Compare
        # sa-wizard-marketprice2
        TC_1.Press('css','#sa-wizard-marketprice2 ul li:nth-child(1)')

        # Assert
        if TC_1.FindText('Compare Jobs'):
            TC_1.Log(True,'Compare Job')

            time.sleep(10)
            
            # Press back to job list
            TC_1.Press('css','#CompareJob .CompareJobHeader div:nth-child(1) #backToJobList a')
            
            # # Click Hybrid
            # if TC_1.FindText('CompAnalyst Market Data'):
            #     TC_1.Press('css','#sa-wizard-marketprice2 ul li:nth-child(2)')

            #     TC_1.Wait(2)
                
            #     TC_1.Log(True,'Hybrid')
                


            #     if TC_1.FindText('Create Hybrid Job'):
            #         # Enter Hybrid Job Title
            #         current_datetime = datetime.now()
            #         # TC_1.Type('css','#hybridjobtitle', f'Lloyd Automation {current_datetime}')
            #         TC_1.ExecuteJSScript(
            #             f"""
            #                 $('#hybridjobtitle').val('Lloyd Automation {current_datetime}')    
            #             """
            #         )


            #     else:
            #         TC_1.Log(False,'Hybrid')

               


            # else:
            #     TC_1.Log(False,'Hybrid')

        else:
            TC_1.Log(False,'Compare Job')



    else:
        TC_1.Log(False,'Something went wrong, cannot select 3 items in the list')
    
    time.sleep(5)
    # TC_1.VisitSite('/CompAnalyst/Cloud/camd/Cpal_Camd_SearchResultList')

# Select two item in the result and click the add job list button
def CAMD_1_1_06(OP):
    TC_1 = OP

    if(TC_1.FindText('#camd-search-results')):

        # Execute Javascript
        # Select 2 items in the list 
        TC_1.ExecuteJSScript("$('#camd-search-results tbody .tr_checkbox .sa-table-cell-check label')[1].click()")
        TC_1.ExecuteJSScript("$('#camd-search-results tbody .tr_checkbox .sa-table-cell-check label')[2].click()")

        TC_1.Wait(3000)

        # Click Save to Job List
        #TC_1.Press('css','#sa-wizard-marketprice2 ul li:nth-child(3)')

        TC_1.Log(True,'Selected two items')

    else:
        TC_1.Log(False,'Selected two items')
    
    time.sleep(5)
    # TC_1.VisitSite('/CompAnalyst/Cloud/camd/Cpal_Camd_SearchResultList')

# (Save to job list) select the list title
def CAMD_1_07(OP):
    
    TC_1 = OP

    # Wait 5 secs
    time.sleep(5)

    # Saved to Job List
    # TC_1.Press('css','#sa-wizard-marketprice2 ul li:nth-child(3)')
    TC_1.ExecuteJSScript("$('#sa-wizard-marketprice2 ul li:nth-child(3) a').click()")

    time.sleep(5)
    # Type in box
    if TC_1.FindText('Save to Job List'):

    
        TC_1.ExecuteJSScript(
            """
                $('#existinglistname').val('0 Jobs for min wage test in specific countries')  
            """
        )

        TC_1.Log(True,'Save to Job List')
    else:
        TC_1.Log(False,'Save to Job List')

#  Click next scope
def CAMD_2_01(OP):
     
    TC_1 = OP

    # Wait 5 secs
    time.sleep(5)

    # Click Next Scope
    TC_1.ExecuteJSScript("$('#divJob2Panel .sa-wizard-btn-next').click()")

    TC_1.Log(True,'Click Next Scopes')

# Select / Tick 1 checkbox in the Scopes list
def CAMD_02_02(OP):
    TC_1 = OP

    # Wait 5 secs
    time.sleep(5)

    # Click Next Scope
    TC_1.ExecuteJSScript("$('#saved-scope-sec .sa-wizard-scope label')[0].click()")
    TC_1.Log(True,'Select 1st scope in the scope list')

    time.sleep(3)
    # Click the next pricing
    TC_1.ExecuteJSScript("nextToMarketPricing()")
    TC_1.Log(True,'Click Next: Pricing')

    time.sleep(10)

# Select / Tick 2 checkbox in the Scope list
def CAMD_02_02_01(OP):
    TC_1 = OP

    # Wait 5 secs
    time.sleep(5)

    # Click Next Scope
    TC_1.ExecuteJSScript("$('#saved-scope-sec .sa-wizard-scope label')[0].click()")
    TC_1.Log(True,'Select 1st scope in the scope list')

    # Click Next Scope
    TC_1.ExecuteJSScript("$('#saved-scope-sec .sa-wizard-scope label')[1].click()")
    TC_1.Log(True,'Select 2nd scope in the scope list')

    time.sleep(3)
    # Click the next pricing
    TC_1.ExecuteJSScript("nextToMarketPricing()")
    TC_1.Log(True,'Click Next: Pricing')

    time.sleep(10)

# wait for the page loads after running report (or clicking the Next: Pricing button)
def CAMD_02_03(OP):

    TC_1 = OP

    # Wait 5 secs
    time.sleep(5)

    if TC_1.FindText('Job Pricing Report'):

        TC_1.Log(True,'Run report successfully')
    else:
        TC_1.Log(False,'Run report successfully')
    
# save .pdf .xlxs .csv
def CAMD_02_04(OP):
    TC_1 = OP

    # Wait 5 secs
    time.sleep(5)

    # Click to reveal the download options
    TC_1.ExecuteJSScript("$('.sa-camd-toolbar .btn-group:nth-child(2) button').click()")

    # =================================================================
    # OPERATION DOWNLOAD THE .PDF

    # Call the function to generate the .pdf report
    TC_1.ExecuteJSScript("exportToFile_New('2')")
    # Explicitly add a delay of 10 seconds before hitting the download button
    time.sleep(10)
    # Hit the download button
    TC_1.ExecuteJSScript("$('#reportCompleted button').click()")

    TC_1.Log(True,'PDF Report Downloaded')
    time.sleep(5)
    # Close the current window
    TC_1.SwitchToPrevTab()
    time.sleep(10)

    # =================================================================

    # =================================================================
    # OPERATION DOWNLOAD THE .excel

    # Call the function to generate the .excel report
    TC_1.ExecuteJSScript("exportToFile('excel')")
    # Explicitly add a delay of 10 seconds before hitting the download button
    time.sleep(10)
    # Hit the download button
    TC_1.ExecuteJSScript("$('#reportCompleted button').click()")

    TC_1.Log(True,'Excel Report Downloaded')
    time.sleep(5)
    # Close the current window
    #TC_1.SwitchToPrevTab()
    time.sleep(10)

    # =================================================================

    # =================================================================
    # OPERATION DOWNLOAD THE .csv

    # Call the function to generate the .scv report
    TC_1.ExecuteJSScript("exportToFile('csv')")
    # Explicitly add a delay of 10 seconds before hitting the download button
    time.sleep(10)
    # Hit the download button
    TC_1.ExecuteJSScript("$('#reportCompleted button').click()")

    TC_1.Log(True,'CSV Report Downloaded')
    time.sleep(10)
    # Close the current window
    #TC_1.SwitchToPrevTab()
    time.sleep(10)

    # =================================================================

# back to job list
def CAMD_02_05(OP):
    TC_1 = OP

    TC_1.ExecuteJSScript("$('#backToJobList a').click()")

    if TC_1.FindText('CompAnalyst Market Data'):
        TC_1.Log(True,'Back to job list')
    else:
        TC_1.Log(False,'Back to job list')

    time.sleep(10)

# select the first job in the list
def CAMD_02_06(OP):
    TC_1 = OP

    TC_1.ExecuteJSScript("$('#camd-search-results tbody .tr_checkbox .sa-table-primarycol a')[0].click()")

    TC_1.Log(True,'Click the first job in the list')

    time.sleep(15)

# adjust button click
def CAMD_02_07(OP):
    TC_1 = OP

    TC_1.ExecuteJSScript("$('.actionfortrial .btn-cta').click()")

    TC_1.Log(True,'Click adjust button')

    time.sleep(10)

# Click save adjusted job
def CAMD_02_08(OP):
    TC_1 = OP

    TC_1.ExecuteJSScript("$('.sa-addscope-sel-actions .btn-saveAdjustJob').click()")

    TC_1.Log(True,'Click save adjusted job')

    time.sleep(10)

# click confirm modal if any
def CAMD_02_09(OP):
    TC_1 = OP

    TC_1.ExecuteJSScript("$('.confirm').click()")

    TC_1.Log(True,'Click ok in modal')

    time.sleep(10)

# click final save button if any
def CAMD_02_10(OP):
    TC_1 = OP

    TC_1.ExecuteJSScript("$('#editAdjustJobTitleModal .btn-cta').click()")

    TC_1.Log(True,'Click final save button')

    time.sleep(10)

# Login page (Old Staging)
def CAMD_3_01(OP):
    TC_1 = OP
    
    TC_1.VisitSite("/companalyst/cloud/Account/cpal_login")
    
    # Populate login credentials
    # type - selector val - text to be input
    TC_1.Type('id','loginid','celin.xi')
    TC_1.Type('id','password','Admin@1234')
    TC_1.Press('class','btn-login')
    
    if TC_1.FindText('Welcome'):
        TC_1.Log(True,'Login Page')
    else:
        TC_1.Log(False,'Login Page')

# Click Market Data
def CAMD_3_02(OP):
    TC_1 = OP
    time.sleep(5)
    
    # Show Sub Menus
    TC_1.ExecuteJSScript("$('#MKD').css({'visibility':'visible'})")
    TC_1.Log(True,'Show Sub Menus')
    time.sleep(5)

    # Click Market Data
    TC_1.ExecuteJSScript("$('#MKD div a')[0].click()")
    TC_1.Log(True,'Click MarketData')
    time.sleep(15)

# Type and Search Accountant
def CAMD_3_03(OP):
    TC_1 = OP
    time.sleep(5)

    # Type Accountant
    TC_1.ExecuteJSScript("$('#keywords').val('Accountant')")
    TC_1.Log(True,'Type Accountant')
    time.sleep(5)

    # $('.search_btn_area').click()
    TC_1.ExecuteJSScript("$('.search_btn_area').click()")
    TC_1.Log(True,'Press Search Button')
    time.sleep(20)

# Select Two Items
def CAMD_3_04(OP):
    TC_1 = OP
    time.sleep(7)
    # select two items
    time.sleep(2)
    TC_1.ExecuteJSScript("$('#tmp_rearchresults div:nth-child(1) .search-result-section-a ul:nth-child(1) .searchresult_item_plus_background').click()")
    time.sleep(2)
    TC_1.ExecuteJSScript("$('#tmp_rearchresults div:nth-child(2) .search-result-section-a ul:nth-child(1) .searchresult_item_plus_background').click()")
    time.sleep(2)

    TC_1.Log(True,'2 Items added to the cart')

# Click Button Scope
def CAMD_3_05(OP):
    TC_1 = OP
    time.sleep(5)

    # Click Button Scope
    TC_1.ExecuteJSScript("BtnScope()")

    time.sleep(2)
    # Click expand
    TC_1.ExecuteJSScript("$('.icon2').click()")
    
    # pop up export options
    time.sleep(2)
    TC_1.ExecuteJSScript("$('.sidebarSubItem .title')[0].click()")

    # more options
    time.sleep(2)
    TC_1.ExecuteJSScript("$('#divDataSheet .verticalLine .arrowStyle').click()")

    # choose excel and download
    time.sleep(2)
    TC_1.ExecuteJSScript("$('#divDataSheetExcel').click()")
