# DRF에서 라우팅과 연동되는 API 추가하기
DRF에서 action을 사용하여 라우터에 자동으로 등록되는 커스텀 API 추가하기.  
기본 url이 `/api/extra/`일 때, `/api/extra/get-lastcomment` 또는 `/api/extra/<pk>/set-password`와 같은 기능 추가


## 사용 모델
ExtraModel - (id, title, desc, password)

## 구현
구현 중