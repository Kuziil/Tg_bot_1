import requests
import logging
from urllib3.exceptions import InsecureRequestWarning

api_url = 'https://demo1c.sibstrin.ru/student_mobileapp1_0/hs/products/get_products'

try:
    # Отключаем предупреждения о небезопасном соединении и проверке SSL-сертификата
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    # Устанавливаем параметр verify=False для отключения проверки SSL-сертификата сервера
    response = requests.get(api_url, verify=False)
    if response.status_code == 200:
        logging.info('Information from API received')
        response = response.json()
    else:
        logging.info(response.status_code)
except requests.exceptions.RequestException as e:
    logging.info('An error occurred: ', e)
