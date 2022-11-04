import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s=Service('C:/Users/Vylka/vylkar22/chromedriver.exe')
driver = webdriver.Chrome(service=s)
#Открыть сайт и залогиниться
driver.get("https://qa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("ErwinRommel2474@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("Rommel1488!")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)

#Открыть форму паспорта
driver.find_element(By.CSS_SELECTOR, ".document-tile:nth-child(1) > .document-name").click()

#Заполнение формы
driver.find_element(By.ID, 'surname').clear()
driver.find_element(By.ID, 'surname').send_keys("Роммель")
driver.find_element(By.ID, 'name').send_keys("Эрвин")
driver.find_element(By.ID, 'patronymic').send_keys("Йоханнес")
driver.find_element(By.NAME, 'date').send_keys("15.11.1891")
driver.find_element(By.ID, 'passportSeries').click()
time.sleep(1)
#Ввести серию паспорта
driver.find_element(By.ID, 'passportSeries').clear()
driver.find_element(By.ID, 'passportSeries').send_keys("1784")
time.sleep(1)
#Ввести номер паспорта
driver.find_element(By.ID, 'passportNumber').clear()
driver.find_element(By.ID, 'passportNumber').send_keys("178903")
time.sleep(1)
#Ввести дату выдачи
driver.find_element(By.XPATH, '//*[@id="dateOfIssue"]/div/input').send_keys("12.09.1905")
time.sleep(1)
#Ввести код подразделения и СНИЛС
def fill_field(name, value):
    driver.find_element(By.ID, name).send_keys(Keys.HOME)
    driver.find_element(By.ID, name).send_keys(value)
fill_field('code', '123456')
fill_field('cardId', '12345678910')
time.sleep(1)
#Ввести пункт выдачи паспорта
driver.find_element(By.ID, 'issued').send_keys("ТП ВОСТОЧНЫЙ ОУФМС РОССИИ")
time.sleep(1)
driver.execute_script("window.scrollTo(0, 1080)")
#Ввести адресс проживания
address = driver.find_element(By.XPATH, '//*[@id="address"]/div/div/input')
address.send_keys("г Краснодар, ул Берлинская, д 1")
time.sleep(1)
address.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
address.send_keys(Keys.ENTER)
address.send_keys(Keys.RETURN)
time.sleep(1)
#Ввести номер телефона
driver.find_element(By.ID, 'phone').clear()
driver.find_element(By.ID, 'phone').send_keys("9998887777")
time.sleep(1)
#Прекрипить Паспорт
filePath ='C:\\Test\\1.jpg'
driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div.form.passport-form.document-form > div.body > div.upload-widget.upload-widget > input[type=file]').send_keys(filePath)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(2)
#Загрузить Диплом
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(2) > .document-name").click()
time.sleep(1)
filePath ='C:\\Test\\1.jpg'
driver.find_element(By.CSS_SELECTOR, "#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div.form.contract-form.document-form > div.body > div.upload-widget.upload-widget > input[type=file]").send_keys(filePath)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(1)
#Загрузить Договор
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div:nth-child(3) > div.body.documents-tiles > div:nth-child(1)").click()
time.sleep(1)
filePath ='C:\\Test\\1.jpg'
driver.find_element(By.CSS_SELECTOR, "#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div.form.contract-form.document-form > div.body > div.upload-widget.upload-widget > input[type=file]").send_keys(filePath)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(1)
#Загрузить Заявление
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div:nth-child(3) > div.body.documents-tiles > div:nth-child(2)").click()
time.sleep(1)
filePath ='C:\\Test\\1.jpg'
driver.find_element(By.CSS_SELECTOR, "#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div.form.contract-form.document-form > div.body > div.upload-widget.upload-widget > input[type=file]").send_keys(filePath)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(1)
#Загрузить Согласие
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div:nth-child(3) > div.body.documents-tiles > div:nth-child(3)").click()
time.sleep(1)
filePath ='C:\\Test\\1.jpg'
driver.find_element(By.CSS_SELECTOR, "#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div.form.contract-form.document-form > div.body > div.upload-widget.upload-widget > input[type=file]").send_keys(filePath)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(1)
#Перейти на админку и подтвердить документы
driver.get("https://adminqa.neapro.site/login")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("ErwinRommel2474@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("Rommel1488!")
driver.find_element(By.CSS_SELECTOR, ".btn").click()

