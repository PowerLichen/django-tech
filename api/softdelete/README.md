# DRF에서 논리삭제 구현
DRF에서 삭제 플래그 속성을 사용하여 논리삭제 구현.  
외래키를 가진 모델은 `SerializerMethodField`를 사용하여 NULL 처리를 구현함.


## 사용모델
Bean - (id, desc, origin, price, DEL_FL)  
Coffee - (id, bean, syrup, price)

## 구현
항상 Active인 상태를 보여주기 위해서 Custom Manager를 사용.

```python
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(DEL_FL=False)
```

destroy 이벤트를 update를 호출하도록 오버라이딩.  
시리얼라이저의 update를 오버라이딩
```python
class BeanDestroySerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        if instance.DEL_FL == True:
            raise NotAcceptable
        instance.DEL_FL = True
        instance.save()
        return instance
```

Coffee의 경우, Bean이 삭제되었을 때 null 처리를 위하여 `SerializerMethodField`를 사용함.  

```python
class CoffeeSerializer(serializers.ModelSerializer):
    bean = serializers.SerializerMethodField()

    class Meta:
        model = Coffee
        fields = ['id', 'bean', 'syrup', 'price']

    def get_bean(self, obj):
        if (obj.bean == None) or (obj.bean.DEL_FL == None):
            return None
        return obj.bean
```