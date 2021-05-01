import re
from tqdm import trange
from bs4 import BeautifulSoup
from .util import get_soup, text_normalize, clean_text

# 17488876 191개의 리뷰를 가지고 있다.
target_url = "https://movie.naver.com/movie/point/af/list.nhn?st=nickname&target=after&sword={}&page={}"


def get_user_review(sword, mininum_count, start_page, end_page=-1):
    comments = []
    url = target_url.format(sword, end_page)
    total_review_count = calc_page(url)

    if total_review_count > mininum_count:
        for page in trange(start_page, total_review_count+1):
            url = target_url.format(sword, page)
            current_page_comments = get_a_page(get_soup(url))
            comments += current_page_comments
            return comments


def calc_page(url):
    total_review_count = is_useful_user(get_soup(url))
    page = math.ceil(total_review_count / 10)
    return total_review_count


def is_useful_user(soup):
    user_review_count = soup.select('strong[class="c_88 fs_11"]')[
        0].text.strip()
    return int(user_review_count)


def return_comment_form(user_number, movie_title, movie_id, score, text, user_name):
    comment = {
        'user_number': user_number,
        'movie_title': movie_title,
        'movie_id': movie_id,
        'score': score,
        'text': text,
        'user_name': user_name
    }
    return comment


def get_a_page(soup):
    comments = []
    for row in soup.select('table[class="list_netizen"] tbody tr'):
        user_number = get_user_number(row)
        movie_title = get_movie_title(row)
        movie_id = get_movie_id(row)
        score = get_score(row)
        text = get_text(row)
        user_name = get_user_name(row)
        comments.append(return_comment_form(
            user_number, movie_title, movie_id, score, text, user_name))
    return comments


def get_user_number(row):
    user_number = str(row.select('td[class="ac num"]')).strip()
    return clean_text(user_number)


def get_movie_title(row):
    movie_title = row.select('td[class="title"] a')[0].text.strip()
    return movie_title


def get_score(row):
    score = row.select('div[class="list_netizen_score"] em')[0].text.strip()
    return score


def get_text(row):
    text = row.select('td[class="title"]')[0].text.strip()
    return text.split('\n')[4]


def get_movie_id(row):
    movie_id = row.select('td[class="title"] a')[0].get('href')
    return clean_text(movie_id)


def get_user_name(row):
    user_name = row.select('td[class="num"] a')[0].text.strip()
    return user_name