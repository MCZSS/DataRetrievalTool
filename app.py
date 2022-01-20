from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

def save(names, file_name):
	with open(file_name, "w") as file:
		for name in names:
			file.write("{}\n".format(name))

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://ilearn.sfsu.edu/local/hub/index.php?wantsurl=https%3A%2F%2Filearn.sfsu.edu%2F")
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/section/div/div/div[2]/div[1]/div/p[1]/a").click()
wait = WebDriverWait(driver, 60)
load_element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/section[1]/aside/section/div/h5")))
while True:
	names = []
	courses = str(input("Enter Done if you are done"))
	if courses == "Done":
		save(names, "names.txt")
		break
	driver.get(courses)
	sleep(3)
	try:
		driver.find_element(By.ID, "page-wrapper").find_elements(By.TAG_NAME, "button")[0].click()
		sleep(3)
		if len (driver.find_elements(By.ID, "MathJax_Message")) == 0:
			driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/nav[1]/ul/li[2]/a").click()
		else:
			driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/nav[1]/a[2]").click()
	except:
		driver.find_element(By.ID, "page-wrapper").find_elements(By.TAG_NAME, "button")[0].click()
		sleep(3)
		if len (driver.find_elements(By.ID, "MathJax_Message")) == 0:
			driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/nav[1]/ul/li[2]/a").click()
		else:
			driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/nav[1]/a[2]").click()
	sleep(3)									
	name_table = driver.find_element(By.ID, "page-content").find_element(By.TAG_NAME, "tbody")
	#name_table = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/section[1]/div[2]/div[2]/div[3]/table/tbody")
	for row in name_table.find_elements(By.TAG_NAME, "tr"):
		name = row.find_elements(By.TAG_NAME, "a")[0]
		#names.append(name.text)
		print(name.text)


	try:
		while True:
			pages = driver.find_element(By.TAG_NAME, "ul.m-t-1.pagination")
			page = pages.find_elements(By.TAG_NAME, "li")[-1]
			page.click()
			sleep(3)
			name_table = driver.find_element(By.ID, "page-content").find_element(By.TAG_NAME, "tbody")
			#name_table = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/section[1]/div[2]/div[2]/div[3]/table/tbody")
			for row in name_table.find_elements(By.TAG_NAME, "tr"):
				name = row.find_elements(By.TAG_NAME, "a")[0]
				#names.append(name.text)
				print(name.text)
	except:
		pass



driver.close()

		
#/html/body/div[2]/div[2]/div/div/section[1]/div[2]/div[3]/form/div/div[1]/div[3]/table/tbody
#"/html/body/div[2]/div[4]/nav[1]/ul/li[2]/a"
#/html/body/div[2]/div[4]/nav[1]/a[2]