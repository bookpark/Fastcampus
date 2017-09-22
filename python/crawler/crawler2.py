import pickle

import os
from urllib.parse import urlparse, parse_qs

import requests
from bs4 import BeautifulSoup

import utils


class NaverWebtoonCrawler():
    def __init__(self, webtoon_title=None):
        """
        1. webtoon_title이 주어지면
            1-1. 해당 웹툰 검색결과를 가져옴
            1-2. 검색결과가 1개면 해당 웹툰을
                    self.webtoon에 할당
            1-3. 검색결과가 2개 이상이면 선택가능하도록 목록을 보여주고
                    input으로 입력받음
            1-4. 검색결과가 없으면 다시 웹툰을 검색하도록 함

        2. webtoon_title이 주어지지 않으면
            2-1. 웹툰 검색을 할 수 있는 input을 띄워줌
            2-2. 이후는 위의 1-2, 1-3을 따라감

        3. webtoon_id를 쓰던 코드를 전부 수정 (self.webtoon 사용
            self.webtoon은 Webtoon타입 namedtuple
        시작하자마자 웹툰을 선택하도록 함
        """
        self.webtoon_id = webtoon_id
        self.episode_list = list()
        # 객체 생성 시, 'db/{webtoon)id}.txt'파일이 존재하면
        # 바로 load() 해 오도록 작성
        self.load(init=True)

    @property
    def total_episode_count(self):
        """
        webtoon_id에 해당하는 실제 웹툰의 총 episode 수를 리턴
        requests를 사용
        :return: 총 episode의 수(int)
        """
        el = utils.get_webtoon_episode_list(self.webtoon_id)
        return int(el[0].no)

    @property
    def up_to_date(self):
        """
        현재 가지고 있는 episode_list가 웹상의 최신 episode까지 가지고 있는지 확인
        1. cur_episode_count = self.episode_list의 개수
        2. total_episode_count = 웹상의 총 episode 개수
        3. 위 두 변수의 값이 같으면 return True, 아니면 return False
        :return: boolean 값
        """
        # 지금 가지고 있는 총 episode 개수
        #   self. episode_list에 저장되어있음
        #       -> list형 객체
        #       -> list형 객체의 길이를 구하는 함수 시퀀스형 객체는 모두 가능
        #           -> 내장함수 len(s)
        # cur_episode_count = len(self.episode_list)
        #
        # 웹 상의 총 episode 개수
        # total_episode_count = self.total_episode_count
        # if cur_episode_count == total_episode_count:
        #     return True
        # else:
        #     return False
        # return cur_episode_count == total_episode_count
        return len(self.episode_list) == self.total_episode_count

    def find_webtoon(self, title):
        """
        :param title:
        :return:
        """
        # results = []
        # for webtoon in self.get_webtoon_list():
        #     if title in webtoon.title:
        #         results.append(webtoon)
        # return results
        return [webtoon for webtoon in self.get_webtoon_list() if title in webtoon.title]

    def get_webtoon_list(self):
        """
        네이버웹툰의 모든 웹툰들을 가져온다
        :return:
        """
        url = 'http://comic.naver.com/webtoon/weekday.nhn'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        webtoon_list = set()

        daily_all = soup.select_one('.list_area.daily_all')
        days = daily_all.select('div.col')
        for day in days:
            items = day.select('li')
            for item in items:
                img_url = item.select_one('div.thumb').a.img['src']
                title = item.select_one('a.title').get_text(strip=True)

                url_webtoon = item.select_one('a.title')['href']
                parse_result = urlparse(url_webtoon)
                queryset = parse_qs(parse_result.query)
                title_id = queryset['titleId'][0]

                webtoon = utils.Webtoon(title_id=title_id, img_url=img_url, title=title)
                webtoon_list.add(webtoon)

        webtoon_list = sorted(list(webtoon_list), key=lambda webtoon: webtoon.title)
        return webtoon_list

    def update_episode_list(self, force_update=False):
        """
        1. recent_episode_no = self.episode_list에서 가장 최신화의 no
        2. while문 또는 for문 내부에서
            utils.get_webtoon_episode_list를 호출
            반환된 list(episode)들을 해당 episode의 no가
                recent_episode_no보다 클 때 까지만 self.episode_list에 추가

        self.episode_list에 존재하지 않는 episode들을 self.episode_list에 추가
        :param force_update: 이미 존재하는 episode도 강제로 업데이트
        :return: 추가된 episode의 수(int)
        """
        recent_episode_no = self.episode_list[0].no if self.episode_list else 0
        print('- Update episode list start (Recent episode no: %s' % recent_episode_no)
        page = 1
        new_list = list()
        while True:
            print('  Get webtoon episode list (Loop %s)' % page)
            # 계속해서 증가하는 'page'를 이용해 다음 episode list를 가져옴
            el = utils.get_webtoon_episode_list(self.webtoon_id, page)
            # 가져온 episode list를 순환
            for episode in el:
                # 각 episode의 no가 recent_episode_no 보다 클 경우
                # self.episode_list에 추가
                if int(episode.no) > int(recent_episode_no):
                    new_list.append(episode)
                    if int(episode.no) == 1:
                        break
                else:
                    break
            # break가 호출되지 않았을 때
            else:
                # 계속해서 진행해야 하므로 page 값을 증가시키고 continue로 처음으로 돌아
                page += 1
                continue
            break

        self.episode_list = new_list + self.episode_list
        return len(new_list)

    def get_last_page_episode_list(self):
        el = utils.get_webtoon_episode_list(self.webtoon_id, 99999)
        self.episode_list = el
        return len(self.episode_list)

    def save(self):
        """
        현재 폴더를 기준으로 db/<webtoon_id>.txt 파일에
        pickle로 self.episode_list를 저장
        :return: 성공여부
        """
        """
        1. 폴더 생성시
            os.path.isdir(path)
                path가 디렉토리인지 확인
            os.mkdir(path)
                path의 디렉토리를 생성
                
        2. 저장시
            pickle.dump(obj, file)
        """
        if not os.path.isdir('db'):
            os.mkdir('db')

        try:
            obj = self.episode_list
            path = 'db/{}.txt'.format(self.webtoon_id)
            pickle.dump(obj, open(path, 'wb'))
            print('성공적으로 저장하였습니다')
        except IOError:
            print('저장에 실패하였습니다')

    def load(self, path=None, init=False):
        """
        현재 폴더를 기준으로 db/<webtoon_id>.txt 파일의 내용을 불러와
        pickle로 self.episode_list를 복원

        1. 만약 db 폴더가 없으면 or db/webtoon_id.txt 파일이 없으면
            -> "불러올 파일이 없습니다" 출력
        2. 있으면 복원
        :return:
        """
        try:
            path = 'db/{}.txt'.format(self.webtoon_id)
            self.episode_list = pickle.load(open(path, 'rb'))
        except FileNotFoundError:
            if not init:
                print('불러올 파일이 없습니다')

    def save_list_thumbnail(self):
        """
        webtoon/<webtoon_id>_thumbnail/<episode_no>.jpg

        1. webtoon/<webtoon_id>_thumbnail 이라는 폴더가 있는지 확인 후 생성
        2.
        :return:
        """
        thumbnail_dir = f'webtoon/{self.webtoon_id}_thumbnail'
        os.makedirs(thumbnail_dir, exist_ok=True)

        for episode in self.episode_list:
            response = requests.get(episode.img_url)
            filepath = f'{thumbnail_dir}/{episode.no}.jpg'
            if not os.path.exists(filepath):
                with open(filepath, 'wb') as f:
                    f.write(response.content)

    def make_list_html(self):
        """
        self.episode_list를 HTML파일로 만들어준다
        webtoon/<webtoon_id>.html
        
        1. webtoon 폴더가 있는지 검사 후 생성
        2. webtoon/<webtoon_id>.html 파일객체 할당 또는 with 문으로 open
        3. open한 파일에 HTML 앞부분 작성
        4. episode_list를 for문 돌며 <tr>...</tr> 부분 반복 작성
        5. HTML 뒷부분 작성
        6. 파일 닫기 또는 with 문으로 빠져나가기
        7. 해당 파일 경로 리턴
        <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>
            <table>
                <tr>
                    <!-- 이 부분을 episode_list의 길이만큼 반복 --!>
                    <td></td>
                    <td></td>
                    <td></td>
        :return: 
        """"""
        """
        if not os.path.isdir('webtoon'):
            os.mkdir('webtoon')

        filename = 'webtoon/{}.html'.format(self.webtoon_id)
        with open(filename, 'wt') as f:
            f.write(utils.LIST_HTML_TOP)
            # episode_list 순회하며 나머지 코드 작성
            for e in self.episode_list:
                f.write(utils.LIST_HTML_TR.format(
                    img_url=f'./{self.webtoon_id}_thumbnail/{e.no}.jpg',
                    title=e.title,
                    rating=e.rating,
                    created_date=e.created_date
                ))
            f.write(utils.LIST_HTML_BOTTOM)

        return filename


if __name__ == '__main__':
    crawler = NaverWebtoonCrawler(696617)
    crawler.save_list_thumbnail()
    crawler.make_list_html()