import time
import random
import requests
import os


def crawl(level, keyword):
    for i in range(1, 101):
        start = (i - 1) * 10
        headers = {
            'authority': 'www.indeed.com',
            'upgrade-insecure-requests': '1',
            'dnt': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'sec-fetch-dest': 'document',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'referer': 'https://www.indeed.com/jobs?q={}&explvl={}&start={}'.format(keyword, level, start - 10),
            'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ja;q=0.6,id;q=0.5,so;q=0.4,und;q=0.3,la;q=0.2,da;q=0.1',
        }
        params = (
            ('q', 'product analyst'),
            ('explvl', '{}'.format(level)),
            ('start', '{}'.format(start)),
            # ('pp',
            #  'gQAyAAAAAAAAAAAAAAABfK8RTQBpAQIBDzAHJv0pm9NCml_RK_2TXXkchQItJ0BYRVA-0enCJS_28bYQE-75s-ga4gWGL3Q1tYUXHKQ9umAmyFMGB30R_RbgZXqMkiRz-WB0wLv7ZXt2vOa8JvlG41K8ETagij2EYydHX9GQACIBACX2PPjph75clcj-gjVtQiypIH9FiwNtmLWTSTUirg8q'),
        )
        response = requests.get('https://www.indeed.com/jobs', headers=headers, params=params)
        print(level)
        print(response.url)
        print(response.status_code)

        if response.status_code == 200:
            with open('htmls/{}/p{}.html'.format(level, i), 'w') as f:
                f.write(response.text)

            random_t = random.randint(1, 2)
            time.sleep(random_t)
            print('progress: {}/101'.format(i))


if __name__ == '__main__':
    base_dir = 'htmls/'
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    keyword = "product analyst"
    if ' ' in keyword:
        keyword = "+".join(keyword.split())

    levels = ['mid_level', 'entry_level']
    for level in levels:
        print(level, ' start')
        level_dir = base_dir + level
        if not os.path.exists(level_dir):
            os.mkdir(level_dir)
        crawl(level, keyword)
        print(level, ' end')
    print('done.')
