# DRF에서 이미지 전처리 진행하기
DRF에서 이미지 업로드 수행 전 전처리를 하는 방법 구현.

## 사용 모델
ImageProcess - (id, img)

## 구현
이미지 업로드는 시리얼라이저에서 수행 됨.  
`create` 메소드를 오버라이딩하여, 생성작업 수행 전 `validated_data`를 변경하는 것으로 구현.

```python
class ImgProcSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProcess
        fields = ['id', 'img']

    def img_resize(self, img: InMemoryUploadedFile) -> InMemoryUploadedFile:
        # 이미지 전처리 수행
        return result


    def create(self, validated_data):
        result = self.img_resize(validated_data['img'])
        validated_data['img'] = result
        return super().create(validated_data)
```
