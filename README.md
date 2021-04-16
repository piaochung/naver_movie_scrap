## naver_movie_scrap
네이버 영화 리뷰 데이터와 영화 데이터를 가져오는 프로그램입니다.

#### 파일 목록
|이름|내용|
|-|-|
|movie_scrap.py|영화 제목, 줄거리, 장르를 가져옵니다.|
|review_scrap.py|평점, 리뷰, 유저 아이디를 가져옵니다.|
|util.py|모듈 파일입니다.|

#### movie_scrap 사용 방법
```
from naver_movie import movie_scrap

movie_id = 132626
movie_data = movie_scrap.get_movie_data(movie_id)
```

|인자|내용|
|-|-|
|movie_id|영화 고유 아이디입니다.|


naver_movie 폴더에 있는 movie_scrap.py 파일을 가져와줍니다. movie_scrap의 경우에는 인자로 movie_id만을 가지기 때문에 movie_id값을 지정해서 넣어줍니다.

```
{'genres': ['코미디', '애니메이션', '모험'],
 'story': '전 세계를 점령할 놈들이 온다!\n최고의 악당만을 보스로 섬기는 ‘미니언’\n가족을 위해 악당 은퇴를 선언한 ‘그루’\n그루의 배신에 실망한 미니언들은\n스스로 악당이 되기 위해 그루를 떠난다.\n한편, 같은 얼굴 다른 스펙의 쌍둥이 동생 ‘드루’의 등장으로 인해\n그루는 자신이 역사상 가장 위대한 악당 가문의 후예임을 알게 되고,\n거부할 수 없는 슈퍼배드의 운명을 따르게 되는데…\n돌아온 그루와 미니언들은\n다시 함께할 수 있을까?\n제작노트 보기',
 'title': '슈퍼배드 3'}
 ```
 
 가져온 데이터를 확인하면 위와 같습니다.
 
 ```
from naver_movie import movie_scrap

movie_id = 132626
review_data = review_scrap.get_review_data(movie_id, start_page=1, end_page=50, spoiler='N')
```
 
|인자|내용|
|-|-|
|movie_id|영화 고유 아이디입니다.|
|start_page| |
|end_page| |
|spoiler| |
 
