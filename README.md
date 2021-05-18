## naver_movie_scrap
네이버 영화 리뷰 데이터와 영화 데이터를 가져오는 프로그램입니다.

## 파일 목록
|이름|내용|
|-|-|
|movie_scrap.py|영화 제목, 줄거리, 장르를 가져옵니다.|
|review_scrap.py|평점, 리뷰, 사용자 아이디를 가져옵니다.|
|user_review_info_scrap.py|번호, 영화 제목, 영화 아이디, 점수, 리뷰, 사용자 고유 번호, 사용자 아이디|
|user_sword_scrap.py|사용자 고유 번호를 가져옵니다.|
|util.py|모듈 파일입니다.|

## movie_scrap 사용 방법
#### movie_id에 따른 영화 정보를 가져오는 프로그램입니다.

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
 
## review_scrap 사용 방법
#### movie_id에 따른 사용자 리뷰를 가져오는 프로그램입니다.

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

## user_sword_scrap 사용 방법
#### 사용자 고유 번호를 가져오는 프로그램입니다.

|인자|내용|타입|
|-|-|-|
|movie_id|영화 고유 아이디입니다.|int|
|start_page|시작 페이지를 지정하는 변수입니다.|int|
|end_page|끝나는 페이지를 지정하는 변수입니다.|int|

```
from naver_movie import user_sword_scrap

movie_id = 93756
user_sword = user_sword_scrap.get_user_code(movie_id, start_page=1, end_page=1)
```
위의 코드는 1페이지에 있는 유저의 sword를 가져오는 코드입니다.

```
[{'user': '17495925'},
 {'user': '17495924'},
 {'user': '17493654'},
 {'user': '17491694'},
 {'user': '17491578'},
 {'user': '17491524'},
 {'user': '17488876'},
 {'user': '17486052'},
 {'user': '17478672'},
 {'user': '17471693'}]
```
1페이지당 10개의 user가 존재합니다.

## user_review_info_scarp 사용
#### 사용자 고유 번호에 따른 리뷰 데이터를 가져오는 프로그램입니다.

|인자|내용|타입|
|-|-|-|
|sword|사용자 고유 아이디입니다.|int|
|minimum_count|스크랩하기 위한 최소한의 리뷰 개수입니다.|int|
|maximum_count|리뷰 개수의 최대값을 지정합니다.|int|

```
from naver_movie import user_review_info_scrap

user_sword = user_review_info_scrap.get_user_review(17471693, 10, 50)
```

사용자 17471693이 10개 이상의 리뷰를 작성하였다면 50개의 리뷰 데이터를 가져오는 코드입니다.

```
[{'movie_id': '93756',
  'movie_title': '명량',
  'score': '1',
  'sword': 17471693,
  'text': '민족 성웅 이순신과 그의 가장 극적인 전투 명량해전을 소재로 삼아놓고 이따위 수준 밖에 만들어내지 못한 감독은 한국 영화 업계 앞에 반성해라. 애국심을 팔아먹을거면 차라리 피규어를 만들든지. ',
  'user_name': 'voyo****',
  'user_number': '17471693'},
 {'movie_id': '172174',
  'movie_title': '어느 가족',
  'score': '9',
  'sword': 17471693,
  'text': '고를거라면 도둑이 아닌 아빠를 고르겠지만 결국 그를 아빠로 고른 것처럼... 가족을 고른 사람들 ',
  'user_name': 'voyo****',
  'user_number': '16944498'},
 {'movie_id': '153729',
  'movie_title': '간츠: 오',
  'score': '10',
  'sword': 17471693,
  'text': '이 정도면 원작을 능가했다고 본다. 만화, 영화, 통 틀어서 최고의 작품. ',
  'user_name': 'voyo****',
  'user_number': '15394130'},
  .
  .
  .
```

결과값이 많아 3개의 데이터만 보여주었습니다.

## Dependency
- python3
- BeautifulSoup
- request
- tqbm
- re
