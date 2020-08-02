import requests
from tqdm import tqdm
import time

#CONSTANTS
YD_URL = 'https://cloud-api.yandex.net:443/v1/disk'
YANDEX_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
######!!!!!!!!!!!!!!!!!!!!!!!
#TOKEN_YD = 'AgAAAAAy_UpkAADLW4DINWqLNUrUml_SsYrvX7U'
TOKEN_YD = input('Пожалуйста, введите токен учетной записи Яндекс, куда будем сохранять копию фото: ')
YD_OAUTH = {'Authorization': f'OAuth {TOKEN_YD}'}
yandex_oauth_header = {
    'Accept': 'application/json',
    'Authorization': f'OAuth {TOKEN_YD}'
}
print('Сохранен токен Яндекс: ', TOKEN_YD)

id_VK = 552934290  # id_korovin

###########Yandex class
class YDUser:
    # def __init__(self, token: str, user_id: int, params=None, headers=None):
    #     self.token_VK = token
    #     self.user_id = user_id
    #     self.params = params
    #     self.headers = headers

    def put_request(self, url, params, headers):
        response = requests.put(url, params=params, headers=headers)
        return response.json()

    def yandex_folder(self):
        yandex_folder_url = f'{YD_URL}{"/resources"}'
        # доп параметры для создания папки ЯД
        yandex_folder_params = {
            'path': f'{"id_VK-"}{id_VK}',
            'overwrite': 'true'
        }
        response = self.put_request(yandex_folder_url, params=yandex_folder_params, headers=yandex_oauth_header)
        return response

    def yandex_upload(self, files_for_upload):
        for file in files_for_upload:
            # доп параметры для получения ссылки на загрузку файла
            yandex_upload_params = {
                'path': f'{"id_VK-"}{id_VK}{"/"}{file}',
                'overwrite': 'true'
            }
            response = requests.get(YANDEX_UPLOAD_URL, params=yandex_upload_params, headers=yandex_oauth_header)
            put_url = response.json().get('href')
            # открыть файл на БИНАР чтение, передать его в яндекс!
            with open(file, 'rb') as f:
                data_4upload = f.read()
            response_upload = requests.put(put_url, data=data_4upload)

            # Прогресс бар upload
            for i in tqdm(range(2)):
                time.sleep(1)
            print(f'Файл: "{file}" - успешно загружен!')
            print()

        return print(f'Все файлы надежно сохранены в Яндекс.диск!')