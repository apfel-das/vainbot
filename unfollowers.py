from selenium import webdriver
from time import sleep 
import getpass


class InstaBot:
    def __init__(self,username,pw):

        self.username = username
        # visit page
        self.driver=webdriver.Chrome(executable_path ="C:/Users/user/Desktop/vain/drivers/chromedriver.exe")
        self.driver.get("https://instagram.com")
        sleep(4)    

        #detect fields - prompt to login screen
        self.driver.find_element_by_xpath("//a[contains(text(),'Log in')]").click()

        sleep(3)

        #fill up credentials and then log in
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)

        sleep(5)    

        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        
        sleep(5)

        #skip "Turn On Notifications" part
        self.driver.find_element_by_xpath("//button[contains(text() , 'Not Now')]").click()
        sleep(5)

    def get_unfollowers(self):

        #navigate to user's profile
        self.driver.find_element_by_xpath("//a[contains(@href , '/{}')]".format(self.username)).click()



if __name__ == "__main__":
    print("Type your Instagram credentials below (Case Sensitive Input)..")

    usr = input("Username: ").strip()
    ps = getpass.getpass(prompt='Password: ', stream=None)
    
    #instantiate a bot 
    bot = InstaBot(usr, ps)