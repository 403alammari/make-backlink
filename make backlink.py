from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()

lines = []
with open("websiteList.txt") as file:
    for line in file: 
        try:
            line = line.strip() #or some other preprocessing
            driver.get(line)
            click = driver.find_element(By.NAME,"submit")
            #comment section
            comment = driver.find_element(By.NAME,"comment")
            comment.clear()
            comment.send_keys("so amazing ,, thanks alot about that : )")
            #end comment section
            #url section
            url = driver.find_element(By.NAME,"url")
            url.clear()
            url.send_keys("https://www.url.net/post/")
            #end url section  
            #email section
            email = driver.find_element(By.NAME,"email")
            email.clear()
            email.send_keys("test@test.com")
            #end email section 
            #author section
            author = driver.find_element(By.ID,"author")
            author.clear()
            author.send_keys("403alammari")
            #end author section
            click.send_keys(Keys.RETURN)
            f = open("sucess_send_save_here.txt", "a")
            f.writelines(driver.current_url)
            f.writelines("\n")
            f.close()
        except:
            pass