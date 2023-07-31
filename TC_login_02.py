from selenium import webdriver
from selenium.webdriver.edge.service import service

service = service(executable_path="C:\\Users\\Saran G\\Downloads\\edgedriver_win64\\msedgedriver.exe")
driver = webdriver.edge(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("InvalidPassword")
driver.find_element_by_id("btnLogin").click()
act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.close()
