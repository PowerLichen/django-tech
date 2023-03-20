# DRF에서 라우팅과 연동되는 API 추가하기
DRF에서 action을 사용하여 라우터에 자동으로 등록되는 커스텀 API 추가하기.

## 사용 모델
ExtraModel - (id, title, desc, password)

## 구현
`rest_framework.decorators`의 `action` 메소드는 전달되는 값에 따라 extra action을 구현함.
- detail: detail/list 리퀘스트를 구분.
True일 경우 detail 요청(pk 이용)
False일 경우 list 요청
- methods: HTTP 메소드 리스트. 해당 메소드로 요청 시 작동하도록 설정. 기본값은 `["GET"]`
- url_path: 요청 시 url에서 사용할 명칭.
기본값은 메소드 이름.
- url_name: reverse 등에 사용되는 django 내의 사용할 명칭.
기본값은 메소드 이름.

예시에서는 두 가지 기능을 사용
- `get_last`: 전체 리스트를 날짜 내림차순으로 출력하는 요청.
- `set_password`: 특정 인스턴스의 password를 변경하는 요청

```python
class ExtraActionViewSet(ModelViewSet):
    ...
    def get_queryset(self):
        if self.action == "set_password":
            return super().get_queryset().order_by('-created_at')
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == "set_password":
            return ExtraModelPasswordSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=['get'], url_path='last')
    def get_last(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['post'], url_path="password")
    def set_password(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    ...
```