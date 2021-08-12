from selenium import webdriver
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt
from time import sleep
import pandas as pd

#Define the url to scrape
my_url = 'https://w1.golfstixvalueguide.com/TaGetManufacturers.aspx?type=brand&siteguid=C7E07275-40D7-4FEF-A18E-80A10E946ED4'
chrome = webdriver.Chrome(executable_path="C:/Users/HP Revolve G3/Selenium.click/chromedriver.exe")
chrome.get(my_url)
sleep(5)

#Read info
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#Parse info
page_soup = soup(page_html, "html.parser")

#Main brands in bold
featured_brand_lib = {
"Adams": '//*[contains(text(), "Adams")]',
"Callaway": '//*[contains(text(), "Callaway")]',
"Cleveland": '//*[contains(text(), "Cleveland")]',
"Cobra": '//*[contains(text(), "Cobra")]',
"Mizuno": '//*[contains(text(), "Mizuno")]',
"Nike": '//*[contains(text(), "Nike")]',
"Odyssey": '//*[contains(text(), "Odyssey")]',
"Ping": '//*[contains(text(), "Ping")]',
"PXG": '//*[contains(text(), "PXG")]',
"Scotty Cameron": '//*[contains(text(), "Scotty Cameron")]',
"Taylormade": '//*[contains(text(), "Taylormade")]',
"Titleist": '//*[contains(text(), "Titleist")]'}

#All other brands
specialty_brand_lib = {
"ARGOLF": '//*[contains(text(), "ARGOLF")]',
"Artisan": '//*[contains(text(), "Artisan")]',
"Axis 1": '//*[contains(text(), "Axis 1")]',
"Ben Hogan": '//*[contains(text(), "Ben Hogan")]',
"Bettinardi": '//*[contains(text(), "Bettinardi")]',
"Bloodline": '//*[contains(text(), "Bloodline")]',
"Bobby Grace": '//*[contains(text(), "Bobby Grace")]',
"Bridgestone": '//*[contains(text(), "Bridgestone")]',
"Bushnell": '//*[contains(text(), "Bushnell")]',
"Cure": '//*[contains(text(), "Cure")]',
"Edel": '//*[contains(text(), "Edel")]',
"Epon": '//*[contains(text(), "Epon")]',
"Evnroll": '//*[contains(text(), "Evnroll")]',
"Fourteen": '//*[contains(text(), "Fourteen")]',
"grindworks": '//*[contains(text(), "grindworks")]',
"Guerin Rife": '//*[contains(text(), "Guerin Rife")]',
"Honma": '//*[contains(text(), "Honma")]',
"JP Golf": '//*[contains(text(), "JP Golf")]',
"Kenny Giannini": '//*[contains(text(), "Kenny Giannini")]',
"Krank": '//*[contains(text(), "Krank")]',
"L.A.B. Golf": '//*[contains(text(), "L.A.B. Golf")]',
"mg Golf": '//*[contains(text(), "mg Golf")]',
"Miura": '//*[contains(text(), "Miura")]',
"New Level": '//*[contains(text(), "New Level")]',
"Piretti": '//*[contains(text(), "Piretti")]',
"Royalty": '//*[contains(text(), "Royalty")]',
"Scratch": '//*[contains(text(), "Scratch")]',
"See More": '//*[contains(text(), "See More")]',
"Sik": '//*[contains(text(), "Sik")]',
"Sonartec": '//*[contains(text(), "Sonartec")]',
"Sub 70": '//*[contains(text(), "Sub 70")]',
"Sureshot": '//*[contains(text(), "Sureshot")]',
"Swing Science": '//*[contains(text(), "Swing Science")]',
"Tommy Armour": '//*[contains(text(), "Tommy Armour")]',
"Top Flite": '//*[contains(text(), "Top Flite")]',
"Toulon Design": '//*[contains(text(), "Toulon Design")]',
"Tour Edge": '//*[contains(text(), "Tour Edge")]',
"TP Mills": '//*[contains(text(), "TP Mills")]',
"Tyson Lamb": '//*[contains(text(), "Tyson Lamb")]',
"Vega": '//*[contains(text(), "Vega")]',
"Vertical Groove Golf": '//*[contains(text(), "Vertical Groove Golf")]',
"Wilson": '//*[contains(text(), "Wilson")]',
"XE1": '//*[contains(text(), "XE1")]',
"XXIO": '//*[contains(text(), "XXIO")]',
"Yes": '//*[contains(text(), "Yes")]',
"Yonex": '//*[contains(text(), "Yonex")]'}

#Club type selection
club_type_lib = {
"Chipper": '//*[contains(text(), "Chipper")]',
"Driver": '//*[contains(text(), "Driver")]',
"Fairway Wood": '//*[contains(text(), "Fairway Wood")]',
"GPS Rangefinder": '//*[contains(text(), "GPS Rangefinder")]',
"Hybrid": '//*[contains(text(), "Hybrid")]',
"Iron Set": '//*[contains(text(), "Iron Set")]',
"Putter": '//*[contains(text(), "Putter")]',
"Single Iron": '//*[contains(text(), "Single Iron")]',
"Wedge": '//*[contains(text(), "Wedge")]'}

#Function to select brand
def brand_click(chrome, brand):
	return chrome.find_element_by_xpath(brand).click()

#Function to select club type
def club_type_click(chrome, club_type):
	try:
		WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.XPATH, club_type))).click()
	except ElementClickInterceptedException:
		sleep(3)
		chrome.find_element_by_xpath(club_type).click()
	except TimeoutException:
		pass
#Create empty list for data
data = []


for key, value in featured_brand_lib.items():
	
	#Select dropdown
	chrome.find_element_by_id("taWgtStepSelectTxt_Step1").click()
	sleep(2)
	
	#Click on selected brand
	brand_click(chrome, featured_brand_lib[key])
	sleep(2)
	
	#Click on the selected club type
	club_type_click(chrome, club_type_lib["Driver"])
	sleep(2)

#Define where different club models are
	models = chrome.find_elements_by_xpath('//*[@class="taWgtModelProduct"]')

#Print the club model Title
	for model in models:
		model.click()
		model_title = WebDriverWait(chrome, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'taWgtLBoxModelTitle'))).text
		print(model_title)
	
		#RETURN NEW PRICE
		new_price = WebDriverWait(chrome, 20).until(
		EC.element_to_be_clickable((By.XPATH, '//*[@id="feature2"]/option[1]'))).click()

		new_price = chrome.find_element_by_id("buyBackPrice").text
		print("New Price = " +(new_price))

		#RETURN BELOW AVERAGE PRICE
		below_average_price = WebDriverWait(chrome, 20).until(
		EC.element_to_be_clickable((By.XPATH, '//*[@id="feature2"]/option[2]'))).click()

		below_average_price = chrome.find_element_by_id('buyBackPrice').text
		print("Below Average Price = " +(below_average_price))

		#RETURN AVERAGE PRICE
		average_price = WebDriverWait(chrome, 20).until(
		EC.element_to_be_clickable((By.XPATH, '//*[@id="feature2"]/option[3]'))).click()

		average_price = chrome.find_element_by_id('buyBackPrice').text
		print("Average Price = " +(average_price))


		data.append((model_title, new_price, below_average_price, average_price))

		#CLOSE LIGHTBOX WINDOW
		close_button = WebDriverWait(chrome, 20).until(
		EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/button'))).click()

#Create DataFrame and send to .csv file
df = pd.DataFrame(data, columns=['model name', 'new price', 'below average price', 'average price'])
df.to_csv(f'Adams_Drivers{dt.now().strftime("%Y%m%d_%H%M")}.csv')
