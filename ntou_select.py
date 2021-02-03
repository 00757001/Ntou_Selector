import tkinter as tk
import time
import threading
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

def job():
    id = EnterID.get()
    pwd = EnterPwd.get()
    select = EnterSelect.get()
    try:
        web = webdriver.Chrome('./chromedriver')
        web.get("https://ais.ntou.edu.tw/Default.aspx")
        time.sleep(2)
        myElem = WebDriverWait(web, 100).until(EC.presence_of_element_located((By.NAME,'M_PORTAL_LOGIN_ACNT')))
        web.find_element_by_name("M_PORTAL_LOGIN_ACNT").send_keys(id)
        web.find_element_by_name("M_PW").send_keys(pwd)
        web.find_element_by_name("LGOIN_BTN").click()         
    except Exception as e:
        print(e)   
    web.get("https://ais.ntou.edu.tw/Application/TKE/TKE20/TKE2011_01.aspx")  
    web.find_element_by_xpath("//*[@id='Q_COSID']").send_keys(select)
    web.find_element_by_xpath("//*[@id='QUERY_COSID_BTN']").click()
    time.sleep(1)
    while(1):
        try:
            web.find_element_by_xpath("//*[@id='DataGrid1_ctl02_edit']").click()
            a=WebDriverWait(web,10).until(EC.alert_is_present())
            print(a.text)
            a.accept()
            #WebDriverWait(web,10).until(EC.alert_is_present()).accept() 
        except Exception as e:
            print(e)
            continue
        
if __name__ == '__main__':
    root = tk.Tk() 
    root.geometry('300x200')
    text1 = tk.Label(root, text="學號:")
    text1.place(x=0, y=0)
    EnterID = tk.Entry(root)
    EnterID.place(x=40, y=0)
    text2 = tk.Label(root, text="密碼:")
    text2.place(x=0,y=50)
    EnterPwd = tk.Entry(root,show="*")
    EnterPwd.place(x=40, y=50)
    text3 = tk.Label(root, text="欲選課號:")
    text3.place(x=0,y=100)
    EnterSelect = tk.Entry(root)
    EnterSelect.place(x=60, y=100)

    resultButton = tk.Button(root, text = "搶課",width = 20,command=job)
    resultButton.place(x=30, y=150)

    #haltButton = tk.Button(root, text="結束",command=end)
    #haltButton.place(x=200, y=150)

    root.mainloop()


