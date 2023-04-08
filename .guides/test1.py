from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

try:
    # Replace this try block with your test code.
    from os import environ
    driver.get(f'https://{environ["CODIO_BOX_DOMAIN"]}/student_code/index.html')
    driver.implicitly_wait(1)
    driver.find_element_by_id('btn_createGrid').click()
    elm = driver.find_element_by_id('n1')
    assert(elm)
finally:
    driver.close()