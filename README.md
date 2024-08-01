# 기능 목록

1. 좋아요
2. 댓글 작성
3. 댓글 삭제


## 챌린지 과제

1. ajax를 이용한 검색(미완성일때도 관련 게시글 보이게)
2. 실제 인스타 ui에 맞춰서 구현하기
3. 사진 스토리처럼 넘어가도록 구현
4. 유저 검색기능 추가( 게시글 유저 ) ( 유저모델 생성해야함 )
5. 정렬기능
6. 대댓글

# 구현한 기능 설명
최상단 로고 - 홈 리디렉션
최상단 + 버튼 - 글쓰기

게시글에 이미지 여러 개 삽입 가능
게시글 이미지 좌우 넘기기 가능
- 좌우 넘길 때 좌측 끝에는 좌측 슬라이더가, 우측 끝에는 우측 슬라이더가 사라짐.

하트 버튼 누르면 like, 칠해진 하트 누르면 like 취소
사진 더블클릭하면 like 기능

댓글 작성, 삭제 가능. 작성자 표시

게시글 작성 기능
- 게시글 작성 시 이미지 여러 장 첨부, 미리보기 가능

---
## 작업 순서
django-admin startproject config .
django-admin startapp pirostagram
    앱은 하나만 있어도 충분할 것 같았음. -> 일단 확장성 좋게 수정
settings 에서 installed apps, static, templates 정의
    => 기본세팅 commit
pirostagram 앱 models 정의
    필요한 기능: 게시글 좋아요, 댓글, 댓글삭제, (챌린지: 게시글 검색 - 기준이 뭐지?, 유저 검색, 정렬, 대댓글, 사진 여러장 넘어가게)
    1. post
        - post id (PK)
        - user (FK)
        - image
        - text
        - likes
        - created_at
    2. comment
        - text
        - user (FK)
        - post id (FK)
        - created_at
    - User모델은 새로 앱 파기
    apps.user
좋아요 기능 구현: Post의 likes(FK) 필드 활용, 유저에 따라 게시물 좋아요 버튼 toggle 되는 식으로 구현함 - Ajax 활용
댓글 기능(추가, 삭제) 구현: 댓글도 Ajax 활용하도록 구현.