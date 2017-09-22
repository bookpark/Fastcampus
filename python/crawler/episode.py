import os
from urllib.parse import urlencode

import pickle
import requests
from bs4 import BeautifulSoup


class Episode:
    """
    namedtuple 'Episode'와 같은 역할을 할 수 있도록 생성
    """
    def __init__(self, webtoon, no, url_thumbnail, title, rating, created_date):
        self._webtoon = webtoon
        self._no = no
        self._url_thumbnail = url_thumbnail
        self._title = title
        self._rating = rating
        self._created_date = created_date

        self.thumbnail_dir = f'webtoon/{self.webtoon.title_id}_thumbnail'
        self.image_dir = f'webtoon/{self.webtoon.title_id}_images/{self.no}'
        self.save_thumbnail()

    @property
    def has_thumbnail(self):
        """
        현재 경로/webtoon/{self.webtoon.title_id}_thumbnail/{self.no}.jpg
            파일이 있는지 검사 후 리턴
        :return:
        """
        filepath = f'webtoon/{self.webtoon.title_id}_thumbnail/{self.no}.jpg'
        return os.path.exists(filepath)

    @property
    def webtoon(self):
        return self._webtoon

    @property
    def no(self):
        return self._no

    @property
    def url_thumbnail(self):
        return self._url_thumbnail

    @property
    def title(self):
        return self._title

    @property
    def rating(self):
        return self._rating

    @property
    def created_date(self):
        return self._created_date

    @property
    def has_thumbnail(self):
        """
        현재경로/webtoon/{self.webtoon.title_id}_thumbnail/{self.no}.jpg
          파일이 있는지 검사 후 리턴
        :return:
        """
        path = f'{self.thumbnail_dir}/{self.no}.jpg'
        return os.path.exists(path)

    def save_thumbnail(self, force_update=True):
        """
        Episode자신의 img_url에 있는 이미지를 저장한다
        :param force_update:
        :return:
        """
        if not self.has_thumbnail or force_update:
            # webtoon/{self.webtoon.title_id}에 해당하는 폴더 생성
            os.makedirs(self.thumbnail_dir, exist_ok=True)
            response = requests.get(self.url_thumbnail)
            filepath = f'{self.thumbnail_dir}/{self.no}.jpg'
            if not os.path.exists(filepath):
                with open(filepath, 'wb') as f:
                    f.write(response.content)

    def save_images(self):
        """
        자기 자신 페이지 (각 episode 페이지)의 img들을 다운로드
        webtoon
            /{self.webtoon.title_id}_images
                /{self.episode.no}
                    /{각 loop index}.jpg
        :return:
        """
        os.makedirs(self.image_dir, exist_ok=True)
        # 웹툰 본문 페이지 (url_contents)
        params = {
            'titleId': self.webtoon.title_id,
            'no': self.no
        }
        url_contents = 'https://comic.naver.com/webtoon/detail/nhn' \
                       + urlencode(params)
        # url_image_list를 가져오는건 위 URL로의 requests.get결과를 bs4로 파싱
        response = requests.get(url_contents)
        soup = BeautifulSoup(response.text, 'lxml')
        img_list = soup.select_one('.wt_viewer').find_all('img')
        url_image_list = [img['src'] for img in img_list]

        for index, url in enumerate(url_image_list):
            # img에 대한 각 requests.get에는 url_contents가 Referer인 header가
            headers = {
                'Referer': url_contents
            }
            response = requests.get(url,)
            with open(f'{self.image_dir}/{index + 1}.jpg', 'wb') as f:
                f.write(response.content)

    def _make_html(self):
        pass


if __name__ == '__main__':
    el = pickle.load(open('db/697680.txt', 'rb').read())
    e = el[0]
    e._save_images()