from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
import re
import os
import random
from operator import contains
from itertools import imap, repeat
import calendar
import csv
#import win32clipboard
import time
import calendar
from datetime import datetime, time, date
from datetime import datetime
from datetime import date
import time
import datetime
import os

class CommonLibrary:
                
                def __init__(self):
                        pass
    
                def get_unique_id(self):
                    """Returns Unique Value by adding Time Stamp
                    """
                    return 'test'+str(time.localtime().tm_year)+str(time.localtime().tm_mon)+str(time.localtime().tm_mday)+str(time.localtime().tm_hour)+str(time.localtime().tm_min)+str(time.localtime().tm_sec)
                def get_time_stamp(self):
                    """Returns the Current Date and Time
                    """
                    return datetime.datetime.now(est()).strftime('%a %m/%d/%Y %I:%M %p')
                
                def close_alert_message(self):
                    """Returns 'True'if any alert message displayed returns 'False' if not"""
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    try:
                        selenium.get_alert_message()
                        return True
                    except:
                        return False
                
                def get_alert_message(self):
                    """Returns 'True'if any alert message displayed returns 'False' if not"""
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    text = ''
                    try:
                        text=selenium.get_alert_message()
                        return [True,text]
                    except:
                        return [False,text]
                    
                def verify_element_present(self,locator):
                    """Returns 'True' if the element found with the 'locator' in the corresponding page else returns 'False'
                    """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    return selenium._is_element_present(locator)

                def verify_element_visible(self,locator):
                    """Returns 'True' if the element visible with the 'locator' in the corresponding page else returns 'False'
                    """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    return selenium._is_visible(locator)
                
                def is_digit(self,string):
                    return string.isdigit()

                def list_comparison(self, li_actual, li_expected,message=''):
                    """ Takes Two lists as Arguments and Pass if the two lists are equal else Fails"""
                    print 'Expected: %s\n' % str(li_expected)
                    print 'Actual: %s' % str(li_actual)
                    if li_actual == []:
                        raise AssertionError('Actual is empty')                    
                    for index in range(0,len(li_expected)):
                        if li_expected[index] in li_actual:
                            continue
                        for actualIndex in range(0,len(li_actual)):
                            if li_expected[index][:14] in li_actual[actualIndex]:
                                break
                        else:
                            raise AssertionError('Actual does not match expected'+str(message))
                
                def get_element_index(self, table_locator,value):
                    """Returns the index of the value located by the table locator 'table_locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    index = self._get_element_index(table_locator,value)
                    return index

                def type_keys_into_textbox(self, text_locator,value):
                    """Enters text 'value' into 'text_locator' after checking the presence of the locator"""
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium._element_find(text_locator,True,True).send_keys(value)
                def mouse_move(self, locator):
                    """Moves the Mouse to the 'locator'"""
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium.mouse_over(locator)
 
                def wait_for_ajax(self,time_out=5):
                    """ Wailt for given time"""
                    '''selenium = BuiltIn().get_library_instance('Selenium2Library')
                    status = selenium._selenium.get_eval('(window.jQuery || { active : 0 }).active')
                    print status'''
                    timeout = 0
                    while(timeout<time_out):
                        '''status = selenium._selenium.get_eval('(window.jQuery || { active : 0 }).active')
                        if(status):
                            return True'''
                        time.sleep(1)
                        timeout=timeout+1
                    return True
                def _get_element_index(self,locator,expected):
                    """Returns index of the element at which the 'expected' value found """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    elements = selenium.get_matching_xpath_count(locator)
                    for ele in range(int(elements)):
                        newelements = selenium._element_find(locator,False,False)
                        actual = newelements[ele].text
                        if expected in actual:
                            print "header:"+str(newelements[ele].text)
                            print 'matched at'+str(ele+1)
                            return ele+1
                    else:
                        return 0
                def select_my_window(self,windowname=''):
                    """Selects the window by the window name """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    browser = selenium._current_browser()
                    #print browser.get_current_window_info()
                    x=browser.get_window_handles()
                    print x
                    '''if windowname=='':
                        browser.switch_to_window(x[0])'''
                    browser.switch_to_window(x[1])
                    print 'done'
                    '''for handle in range(len(x)):
                        browser.switch_to_window(x[handle])
                        print selenium.get_title()'''
                    return True
                
                def press_down_key(self,locator):
                    """ Presses the down Key starting from the 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium._element_find(locator,True,True).send_keys(Keys.ARROW_DOWN)

                def press_up_key(self,locator):
                    """ Presses the up Key starting from the 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium._element_find(locator,True,True).send_keys(Keys.ARROW_UP)              

                def get_items_in_context_menu(self, locator):
                    """Returns the text from the context menu located by 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    return selenium.execute_javascript("return document.getElementById('dashMenu_4').getElementsByTagName'div')[1].getElementsByClassName('rich-menu-item rich-menu-item-enabled')["+str(locator)+"].getElementsByTagName('span')[1].textContent")

                def get_element_text(self,element,child):
                    """Returns the text found at the 'child' of the 'element' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    id = selenium.get_element_attribute(element+'@id')
                    print "id:"+str(id)
                    return selenium.execute_javascript('return document.getElementById("'+id+'").childNodes['+str(child)+'].textContent')
                    #return selenium.execute_javascript("return document.getElementById('"+id+"').childNodes['"+str(child)+"'][2].getElementsByTagName('td').textContent")

                def input_file_name(self,locator,value):
                    """Enters the 'value' into the field located by 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium._element_find(locator,True,True).send_keys(value)
                    return True

                def get_current_date(self):
                    """ Returns the current date in the format month date year"""
                    cdate = datetime.datetime.now()
                    return cdate.strftime("%m/%d/%Y")

                def delete_space(self,word):
                    """deletes an undesired spce from the 'word' and returns the word """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    words = str(word)
                    deletespace = words.replace(' ','')
                    return deletespace
                    
                def change_date_format(Self, date):
                    """ Returns a date after changing its format from 'month/date/year' to 'Year month date'"""
                    #date = date.replace('/',",")
                    return datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y,%m,%d')
                
                def compare_dates_for_given_range(self, date1, date2):
                    """ Returns True if the 'date1' is less than 'date2' else fails"""
                    date1 = self.change_date_format(str(date1))
                    date2 = self.change_date_format(str(date2))
                    return datetime.date(date1)<datetime.date(date2)
                def list_comp_by_sequence(self, actualList,expectedList):
                    """Takes lists 'actualList' and 'expectedList'as arguments and compares them in the sequence """
                    if cmp(actualList,expectedList)!=0:
                        return False
                    return True
                def get_length_of_list(self, actuallist):
                    """Takes the list 'actuallist' as argument and finds the length of the list. Fails if the length of the list equal to Zero""" 
                    if len(actuallist)==0:
                        raise AssertionError('Actual is empty')
                    return len(actuallist)
                def clear_text(self,locator):
                    """Clears Text From the field located by 'locator'"""
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium._element_find(locator,True,True).clear()
                    

                def select_window_by_title(self,windowtitle):
                    """Select a window by window title"""
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    #browser = selenium._current_browser()
                    windows=selenium.get_window_titles()
                    for window in windows:
                        if window==windowtitle:
                            selenium.select_window(window)                          

                def string_should_contain(self,string,substring):
                    """Returns True if The string contains substring else False' """
                    ind=string.find(substring)
                    if ind>=0:
                        return True
                    return False
                
                def press_down_key(self,locator):
                    """ Presses the down Key starting from the 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium._element_find(locator,True,True).send_keys(Keys.ARROW_DOWN)
                    
                def press_control_and_key(self,locator,key):
                    """Presses the control Key and Specified key 'key' at element located by the 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    loc = selenium._element_find(locator,True,True)
                    loc.send_keys(Keys.CONTROL, 'a')
                    time.sleep(1)
                    loc.send_keys(Keys.CONTROL,key)
                    time.sleep(1)
                    
                def press_up_key(self,locator):
                    """Presses the Up Key at element located by the 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium._element_find(locator,True,True).send_keys(Keys.ARROW_UP)

                def press_page_down_key(self,locator):
                    """Presses the page down Key starting from the 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium._element_find(locator,True,True).send_keys(Keys.PAGE_DOWN)

                def press_page_up_key(self,locator):
                    """Presses the page up Key starting from the 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium._element_find(locator,True,True).send_keys(Keys.PAGE_UP)

                def press_home_key(self,locator):
                    """Presses the Home Key starting from the 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium._element_find(locator,True,True).send_keys(Keys.HOME)

                def press_end_key(self,locator):
                    """Presses the End Key starting from the 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    selenium._element_find(locator,True,True).send_keys(Keys.END)


                def is_list_contains_value(self,statuslist,value):
                    """ checks the given value in the list """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    statuslistvalues = []
                    statuslistvalues = statuslist
                    return value in statuslistvalues

                def get_random_number_in_given_range(self,start,stop):
                    """ Returns the random from given range"""
                    return random.randint(int(start),int(stop))

                def convert_string_case(self,string,case=''):
                    """Converts the Case of the string to Upper if specified else to lower """
                    if case=="upper":
                        return string.upper()
                    else:
                        return string.lower()
                    
                def table_get_column_no(self, table_locator, columnName):
                    """Returns the column number of the column matching 'columnName' from the table located at 'table_locator'."""
                    #try:
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    colCount = int(selenium.get_matching_xpath_count(table_locator+'/div[contains(@class,"dgrid-header dgrid-header-row")]/table[contains(@id,"-header")]/tr/th'))
                    print "colCount:"+str(colCount)
                    for iCounter in range(1,colCount+1):
                        curColName = selenium._get_text(table_locator+'//div[contains(@class,"dgrid-header dgrid-header-row")]/table[contains(@id,"-header")]/tr/th['+str(iCounter)+']')
                        if (curColName.replace(' ','').strip().lower()==columnName.replace(' ','').strip().lower()):
                            print "column name matched at "+str(iCounter)
                            return iCounter
                    return 0

                def get_table_values_into_list(self, locator, columnName):
                    """Returns the list of values displayed under 'columnName' from the table located at 'locator' """
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    #Get the column number
                    iColNo = self.table_get_column_no(locator,columnName)
                    #Get the Number of Records in the Table
                    elements = selenium.get_matching_xpath_count(locator+'/div[@class="dgrid-scroller"]/div[contains(@class,"dgrid-content")]//div[contains(@id,"-row")]')
                    print "elements:"+str(elements)
                    rowValues = []
                    #Get the values from the records
                    for ele in range(1,int(elements)+1):
                        cellValue = selenium._get_text(locator+'/div[@class="dgrid-scroller"]/div[contains(@class,"dgrid-content")]//div[contains(@id,"-row")]['+str(ele)+']/table/tr/td[contains(@class,"dgrid-cell")]['+str(iColNo)+']')
                        rowValues.append(cellValue)
                    return rowValues                 
                def get_table_cell_value(self, table_locator, rowNo,colName):
                    "Returns the text located in the table 'table_locator' with in the Column 'columnName' and matching Row 'iRowNo'"""
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    colNo=self.table_get_column_no(table_locator,colName)
                    return selenium._get_text(table_locator+'/div[@class="dgrid-scroller"]/div[contains(@class,"dgrid-content")]//div[contains(@id,"-row")]['+str(rowNo)+']/table/tr/td[contains(@class,"dgrid-cell")]['+str(colNo)+']')
                def select_the_row(self, table_locator, rowNo):
                    "Returns the text located in the table 'table_locator' with in the Column 'columnName' and matching Row 'iRowNo'"""
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    return selenium.click_element(table_locator+'/div[@class="dgrid-scroller"]/div[contains(@class,"dgrid-content")]//div[contains(@id,"-row")]['+str(rowNo)+']')


