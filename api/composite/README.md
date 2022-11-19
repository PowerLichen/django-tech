# DRF에서 복합키 사용
DRF에서 pk로 인스턴스를 찾는 방법이 아닌, 복합키 속성으로 인스턴스를 찾는 방법을 구현.


## 사용 모델
CoffeeBean - (id, origin, date, price)
Django model의 constraints 옵션을 통해 `['origin', 'date']`를 복합키로 지정

## 구현
`views.py`의 get_object 메소드를 오버라이딩.

기본 코드의 다음 부분을 오버라이딩

```python
def get_object(self):
    ...
    lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
    filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
    obj = get_object_or_404(queryset, **filter_kwargs)
    ...
```

filter_kwargs를 lookup_field 하나만이 아닌 여러개로 변경하는 것으로 구현.
