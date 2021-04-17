## naver_movie_scrap
---

네이버 영화 리뷰 데이터와 영화 데이터를 가져오는 프로그램입니다.

### 파일 목록
|이름|내용|
|-|-|
|movie_scrap.py|영화 제목, 줄거리, 장르를 가져옵니다.|
|review_scrap.py|평점, 리뷰, 유저 아이디를 가져옵니다.|
|util.py|모듈 파일입니다.|

### movie_scrap 사용 방법
---

```
git clone https://github.com/piaochung/naver_movie_scrap.git
```
가장 먼저 git clone을 실행시켜줍니다.

|인자|내용|타입|
|-|-|-|
|movie_id|영화 고유 아이디입니다.|int|

```
from naver_movie import movie_scrap

movie_id = 132626
movie_data = movie_scrap.get_movie_data(movie_id)
```

naver_movie 폴더에 있는 movie_scrap.py 파일을 가져와줍니다. movie_scrap의 경우에는 인자로 movie_id만을 가지기 때문에 movie_id값을 지정해서 넣어줍니다.

```
{'genres': ['코미디', '애니메이션', '모험'],
 'story': '전 세계를 점령할 놈들이 온다!\n최고의 악당만을 보스로 섬기는 ‘미니언’\n가족을 위해 악당 은퇴를 선언한 ‘그루’\n그루의 배신에 실망한 미니언들은\n스스로 악당이 되기 위해 그루를 떠난다.\n한편, 같은 얼굴 다른 스펙의 쌍둥이 동생 ‘드루’의 등장으로 인해\n그루는 자신이 역사상 가장 위대한 악당 가문의 후예임을 알게 되고,\n거부할 수 없는 슈퍼배드의 운명을 따르게 되는데…\n돌아온 그루와 미니언들은\n다시 함께할 수 있을까?\n제작노트 보기',
 'title': '슈퍼배드 3'}
 ```
 
 가져온 데이터를 확인하면 위와 같습니다.
 
 ### review_scrap 사용 방법
 ---
 
 |인자|내용|타입|
|-|-|-|
|movie_id|영화 고유 아이디입니다.|int|
|start_page|시작 페이지를 지정하는 변수입니다.|int|
|end_page|끝나는 페이지를 지정하는 변수입니다.|int|
|spoiler|스포일러 포함 리뷰를 볼지 결정하는 변수입니다.|str|
 
 ```
from naver_movie import review_scrap

movie_id = 132626
review_data = review_scrap.get_review_data(movie_id, start_page=1, end_page=50, spoiler='N')
```

위의 코드는 1~50페이지까지의 리뷰 데이터를 가져오는 코드입니다.
 
 ```
 {'score': 10, 'text': '다시 봐도 재밌는 영화.미니언은 너무 귀엽고', 'user': '1'},
 {'score': 5, 'text': '그냥 그럭저럭 함.  볼만했음', 'user': '2'},
 {'score': 10, 'text': '진짜진짜 재미있는 영화 입니다 꼭 보세요', 'user': '3'},
 {'score': 10,
  'text': '이 영화는 엄청나게 웃겼다. 그리고 미니언즈들 너무 귀여워','user': '4'},
 {'score': 10, 'text': '존잼!!!!말이 필요없음!!!!', 'user': '5'},
 {'score': 10, 'text': '', 'user': '6'},
 {'score': 10, 'text': '재미있음 스토리 좋음 음악좋음', 'user': '7'},
 {'score': 9,
  'text': '더이상 미니언즈에 의존하지 않아도 충분히 재밌을 수 있다는 것을 보여주다.',
  'user': '8'},
 {'score': 10, 'text': '1편 2편보다 3편이 더 재밌음', 'user': '9'}
 ```
 
 실제로 작동시킬 때에는 user가 숫자로 표현되지 않고 아이디나 닉네임이 표현됩니다.
