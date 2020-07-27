class VKUser:
    def __init__(self, token: str, user_id: int, params=None, headers=None):
        self.token_VK = token
        self.user_id = user_id
        self.params = params
        self.headers = headers

    def get_params(self, add_params: dict = None):
        params = {
            'access_token': self.token_VK,
            'v': '5.77'
        }
        if add_params:
            params.update(add_params)
        return params

    def get_request(self, url, params, headers=None):
        response = requests.get(url, params=params)
        return response.json()

    def put_request(self, url, params, headers):
        response = requests.put(url, params=params, headers=headers)
        return response.json()

    def get_photos(self):
        # доп параметры для скачивания фото
        photo_down_params = self.get_params(
            add_params={
                'owner_id': id_VK,
                'album_id': 'profile',
                'extended': 1
            }
        )
        response = self.get_request('https://api.vk.com/method/photos.get', photo_down_params)
        photo_url_set = set()
        # сохранение ссылок на фото
        for photo_number in range(len(response['response']['items'])):
            max_height = []
            max_width = []
            max_url = []
            for max_size in response['response']['items'][photo_number]['sizes']:
                max_height.append(max_size['height'])
                max_width.append(max_size['width'])
                max_url.append(max_size['url'])
            photo_url_set.add(max_url[max_width.index(max(max_width))])
        likes_list = []
        dates_list = []
        # имя файла по лайкам
        for likes in response['response']['items']:
            likes_list.append(likes['likes']['count'])
            dates_list.append(likes['date'])
        for index in range(1, len(likes_list)):
            if likes_list[index] == likes_list[index - 1]:
                likes_list[index] = f'{likes_list[index]}-{dates_list[index]}'
        print(f'Будем сохранять {len(photo_url_set)} следующих фото: {photo_url_set}')

        json_output = []
        files_for_upload = []
        for number, photo in enumerate(photo_url_set):
            response_img = requests.get(photo)
            with open(f'{likes_list[number]}.jpg', 'wb') as f:
                f.write(response_img.content)
                # создание JSON-отчета
                temp_dic = {'file_name': likes_list[number], 'size': getsize(f'{likes_list[number]}.jpg')}
                json_output.append(temp_dic)
                files_for_upload.append(f'{likes_list[number]}.jpg')
            print(f'Успешно скачан файл {likes_list[number]}.jpg по ссылке: {photo}')
            # сохраняю в json
            with open('output.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(json_output, ensure_ascii=False))
        print('Успешно сохранен лог файл: output.json')
        return files_for_upload