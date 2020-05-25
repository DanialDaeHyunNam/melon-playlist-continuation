# Melon Playlist Continuation
[카카오 베이스라인 github](https://github.com/kakao-arena/melon-playlist-continuation)를 사용했음.

### 폴더 구조 및 split_data 사용법
```bash
$> tree -d
.
├── arena_data
│   ├── answers
│   ├── orig
│   └── questions
├── res
├── ipynb
│   ├── dan
│   └── your_name
```
- res : 카카오 아레나에서 제공한 .json 파일들.
- arena_data : 베이스라인 github에서 제공한 split_data.py를 이용하여 train split한 데이터가 들어감.

```bash
$> python split_data.py run res/train.json 0.8
```
train_size를 파라미터로 추가함. 위 예제처럼 실행하면 8:2(train:test)로 split 됨.

### 주의사항
- *.csv, *.pkl, *.json 등 용량이 큰 파일들은 git으로 push 하지 않을 것. (이미 .gitignore로 처리됨)
- 가상환경 사용할 것


