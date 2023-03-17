# DRF에서 테스트 코드 작성
DRF에서 APITestCase를 활용한 테스트 코드 작성.

실행 명령어: `python .\manage.py test ./api/testcode/tests`


## 사용모델
User - Django 기본 유저 모델  
Notice - (id, user, title, context)

## 구현 내역
### DRF 기본 테스트 코드
테스트 폴더의 `test_notice_update.py`  
setUpTestData와 setUp 메소드를 사용하여 전처리 수행

### reverse 사용
```python
...
# cls.url = f"/api/testcode/notice/{cls.notice.id}/"
cls.url = reverse('notice-detail', kwargs={"pk": cls.notice.id})
...
```
url에 reverse 적용
