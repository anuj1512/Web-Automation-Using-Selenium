"""
Aim of this script was to login a website and then by selecting options in drop down menu, it
reflect some reports and then we download those reports.These reports were distributed in mainly 3 pages,
so we have to move to other page once we have downloaded all the files in current page.

In Web automation we define each and every single step, like selecting a web element, clicking,pushing values inside text field etc.
Every operation that a user do, we can replicate same using Selenium

"""




# First import Selenium module, user can use Pip install selenium to download the module
from selenium import webdriver
import time

#You need Chromedriver if you want to run your automated scripts in Chrome browser,
# You can choose geeko-driver(Mozilla) also

driver=webdriver.Chrome(executable_path=r'C:\Users\euakumn\Downloads\chromedriver.exe')

# Enter the URL link, where u want to enter
driver.get("http://13.14.01.11/home/Login.aspx")
login_btn=driver.find_element_by_id('Login')
login_btn.click()

# Search for email input box
email_bx=driver.find_element_by_id('email')

#Writing mail ID in above selected field
email_bx.send_keys('xyz@gmail.com')
pwd_bx=driver.find_element_by_id('attentive')

# passing the password for login
pwd_bx.send_keys('i!rb#FgG')
login_btn=driver.find_element_by_id('btnLogin')
login_btn.click()
temp=driver.find_element_by_xpath("//option[contains(text(),'worst cell')]")
temp.click()
#  we will frequently add sleep timer so that all the web elements are uploaded, otherwise it will throw error like element not found
time.sleep(15)
fromdate=driver.find_element_by_id('ctl00_ContentPlaceHolder1_t1')
fromdate.send_keys('08/22/2020')
time.sleep(5)
todate=driver.find_element_by_id('ctl00_ContentPlaceHolder1_t2')
todate.send_keys('08/22/2020')
view_btn=driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnView')
view_btn.click()
time.sleep(5)
search_box=driver.find_element_by_id('ctl00_ContentPlaceHolder1_txtSearch')

# Name of the report that we want to download
search_box.send_keys('_4G_Quality_24Hrs_')
go_btn=driver.find_element_by_id('ctl00_ContentPlaceHolder1_Button1')
go_btn.click()
time.sleep(10)
#  We have maximun 10 files in one web page
k=['02','03','04','05','06','07','08','09','10','11']
for i in k:
    if i=='05':
        # Selecting a particular file checking the zipfilecheckbox       
        circle1=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle1.click()
        # Locating download button       
        download_btn=driver.find_element_by_id('ctl00_ContentPlaceHolder1_btndwnload')
        #  Clicking Download button       
        download_btn.click()
        time.sleep(30)
        circle1=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle1.click()
    else:
        circle1=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle1.click()
        download_btn=driver.find_element_by_id('ctl00_ContentPlaceHolder1_btndwnload')
        download_btn.click()
        time.sleep(30)
        circle1=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle1.click()
time.sleep(5)    

# Going for Page 2
page2=driver.find_element_by_xpath("//tr[@class='paging']//table//tbody//tr//td//a[contains(text(),'2')]")  
page2.click()
time.sleep(10)

#  Repeating the same process as we did in page 1
k=['02','03','04','05','06','07','08','09','10','11']
for i in k:
    if i=='8' or i=='09' or i=='11':
        circle2=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle2.click()
        download_btn=driver.find_element_by_id('ctl00_ContentPlaceHolder1_btndwnload')
        download_btn.click()
        time.sleep(300)
        circle2=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle2.click()
        
    else:
        circle2=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle2.click()
        time.sleep(5)
        download_btn=driver.find_element_by_id('ctl00_ContentPlaceHolder1_btndwnload')
        download_btn.click()
        time.sleep(30)
        circle2=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle2.click()
        time.sleep(3)
        
time.sleep(5)    
page3=driver.find_element_by_xpath("//tr[@class='paging']//table//tbody//tr//td//a[contains(text(),'3')]")
page3.click()
time.sleep(15)
k=['02','03','04','05','06','07','08','09','10','11']
for i in k:
    if i=='03':
        circle3=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle3.click()
        download_btn=driver.find_element_by_id('ctl00_ContentPlaceHolder1_btndwnload')
        download_btn.click()
        time.sleep(300)
        circle3=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle3.click()
    else:
        circle3=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle3.click()
        download_btn=driver.find_element_by_id('ctl00_ContentPlaceHolder1_btndwnload')
        download_btn.click()
        time.sleep(30)
        circle3=driver.find_element_by_id(f'ctl00_ContentPlaceHolder1_gvReports_ctl{i}_ZipFileChckBx')
        circle3.click()
