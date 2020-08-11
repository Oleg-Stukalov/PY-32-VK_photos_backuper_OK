from PY_32_VK_photos_backuper_VK_interface import TOKEN_VK, id_VK, VKUser
from PY_32_VK_photos_backuper_YD_interface import YDUser


user0 = VKUser(TOKEN_VK, id_VK)
files = user0.get_photos()

user1 = YDUser()
user1.yandex_folder()
user1.yandex_upload(files)
