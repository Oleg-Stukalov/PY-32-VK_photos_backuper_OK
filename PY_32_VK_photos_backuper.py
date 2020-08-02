from PY_32_VK_photos_backuper_VK_interface import VKUser
from PY_32_VK_photos_backuper_YD_interface import YDUser

#CONSTANTS
OAUTH_VK_URL = 'https://oauth.vk.com/authorize'
YD_URL = 'https://cloud-api.yandex.net:443/v1/disk'
YANDEX_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
# APP_ID = 7533990  #получен СОИ по ссылке https://vk.com/editapp?act=create
TOKEN_VK = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'  # получен в Нетологии
######!!!!!!!!!!!!!!!!!!!!!!!
TOKEN_YD = 'AgAAAAAy_UpkAADLW4DINWqLNUrUml_SsYrvX7U'
# TOKEN_YD = input('Пожалуйста, введите токен учетной записи Яндекс, куда будем сохранять копию фото: ')
YD_OAUTH = {'Authorization': f'OAuth {TOKEN_YD}'}
yandex_oauth_header = {
    'Accept': 'application/json',
    'Authorization': f'OAuth {TOKEN_YD}'
}
print('Сохранен токен Яндекс: ', TOKEN_YD)

id_VK = 552934290  # id_korovin


# id_VK = input('Пожалуйста, введите id пользователя Вконтакте, копию фото которого надо сделать (при пустом вводе будет использован id552934290): ')









user0 = VKUser(TOKEN_VK, id_VK)
files = user0.get_photos()

user1 = YDUser()
user1.yandex_folder()
user1.yandex_upload(files)
