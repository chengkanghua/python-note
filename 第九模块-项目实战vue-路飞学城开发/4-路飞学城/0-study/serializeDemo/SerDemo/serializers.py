from rest_framework import serializers
from .models import Book


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)

# 插入数据样式
book_obj = {
        "title": "Alex的使用教程",
        "w_category": 1,
        "pub_time": "2018-10-09",
        "publisher_id": 2,
        "author_list": [1, 2]
    }

# 自定义校验方法 ， 与局部校验方法优先级最高
def my_validate(value):
    if "敏感信息" in value.lower():
        raise serializers.ValidationError("不能含有敏感信息")
    else:
        return value

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)  # required=False 反序列化时候不用传这个值
#     title = serializers.CharField(max_length=32,validators=[my_validate]) # validators 添加自定义校验方法
#     CHOICES = ((1, "Python"), (2, "Go"), (3, "Linux"))
#     category = serializers.ChoiceField(choices=CHOICES, source="get_category_display", read_only=True) # source="get_category_display" 获取对应的中文
#     w_category = serializers.ChoiceField(choices=CHOICES, write_only=True)  # write_only=True 只反序列化使用， read_only=True 只序列化使用
#     pub_time = serializers.DateField()
#
#     publisher = PublisherSerializer(read_only=True)
#     publisher_id = serializers.IntegerField(write_only=True)
#     author = AuthorSerializer(many=True,read_only=True)  # many 多对多关系
#     author_list = serializers.ListField(write_only=True)
#
#     def create(self, validated_data):
#         book = Book.objects.create(title=validated_data['title'],category=validated_data['w_category'],
#                                    pub_time=validated_data['pub_time'],publisher_id=validated_data['publisher_id'])
#         book.author.add(*validated_data['author_list'])
#         return book
#
#     def update(self,instance,validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.category = validated_data.get("category", instance.category)
#         instance.pub_time = validated_data.get("pub_time", instance.pub_time)
#         instance.publisher_id = validated_data.get("publisher_id", instance.publisher_id)
#         if validated_data.get("author_list"):
#             instance.author.set(validated_data["author_list"])
#         instance.save()
#         return instance
#
#     # 字段校验钩子方法 validate_字段名
#     def validate_title(self, value):
#         if "python" not in value.lower():
#             raise serializers.ValidationError("标题必须含有python")
#         return value
#     # 全局校验方法
#     def validate(self, attrs):
#         if attrs["w_category"] == 1 and attrs["publisher_id"] == 1:
#             return attrs
#         else:
#             raise serializers.ValidationError("分类以及标题不符合要求")

class BookSerializer(serializers.ModelSerializer):
    category_display = serializers.SerializerMethodField(read_only=True)
    publisher_info = serializers.SerializerMethodField(read_only=True)  # 自定义字段方法 get_publisher 注释depth=1
    authors = serializers.SerializerMethodField(read_only=True)
    def get_category_display(self,obj):
        return obj.get_category_display()

    def get_authors(self,obj):
        authors_query_set = obj.author.all()
        return [{"id":author_obj.id, "name": author_obj.name} for author_obj in authors_query_set]

    def get_publisher_info(self, obj):
        # obj 是我们序列化的每个Book对象
        publisher_obj = obj.publisher
        return {"id": publisher_obj.id, "title": publisher_obj.title}

    class Meta:
        model = Book
        fields = "__all__"
        # depth = 1  # 根据外键关系向下找1层
        extra_kwargs = {"category":{"write_only":True},"publisher":{"write_only":True},
                        "author":{"write_only":True}}














