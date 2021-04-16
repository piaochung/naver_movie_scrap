import re
from .util import get_soup, text_normalize

basic_url_form = 'http://movie.naver.com/movie/bi/mi/basic.nhn?code={}'  # idx


def scrap_basic(idx):
    url = basic_url_form.format(idx)
    soup = get_soup(url)
    infomation = {
        'title': title(soup),
        'genres': genres(soup),
        'story': story(soup),
    }
    return infomation


def title(soup):
    a = soup.select('div[class=mv_info] h3[class=h_movie] a')
    if not a:
        return ''
    return text_normalize(a[0].text)


def genres(soup):
    genres = soup.select('a[href^="/movie/sdb/browsing/bmovie.nhn?genre="]')
    return list({genre.text for genre in genres})


def story(soup):
    try:
        story_soup = BeautifulSoup(str(soup.select("div[class=story_area]")[
                                   0]).replace('<br>', '\n').replace('\xa0', '\n'), 'lxml')
        sents = story_soup.text.split('\n')
        sents = [text_normalize(s) for s in sents if s]
        sents = [s for s in sents if s != '줄거리']
        return '\n'.join(sents)
    except:
        return ''