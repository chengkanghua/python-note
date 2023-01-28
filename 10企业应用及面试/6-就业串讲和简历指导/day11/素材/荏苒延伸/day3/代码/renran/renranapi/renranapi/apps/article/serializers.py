from rest_framework import serializers
from .models import ArticleImage
class ArticleImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ["link"]

    def create(self, validated_data):
        """保存数据"""
        link = validated_data.get("link")
        instance = ArticleImage.objects.create(link=link)
        instance.group = str(instance.link).split("/")[0]
        instance.save()
        return instance

from .models import ArticleCollection
class ArticleCollectionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCollection
        fields = ["id", "name"]

    def validate(self, attrs):
        name = attrs.get("name")
        user = self.context["request"].user
        try:
            ArticleCollection.objects.get(user=user,name=name)
            raise serializers.ValidationError("当年前文集您已经创建了！")
        except ArticleCollection.DoesNotExist:
            pass

        return attrs

    def create(self, validated_data):
        """保存数据"""
        name = validated_data.get("name")
        user = self.context["request"].user
        instance = ArticleCollection.objects.create(user=user, name=name)
        return instance

class ArticleCollectionDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCollection
        fields = ["id", "name"]

    def validate(self, attrs):
        # context 当前序列化器内部的执行上下文
        # context 视图调用序列化器时会自动传递三个变量到序列化器中：request, view, format
        # kwargs 是视图对象下面的参数表，我们调用的视图类继承了GenericsAPIView，所以在视图方法中如果存在自定义参数，我们都可以通过参数表提取出来
        # mobile = self.context["view"].kwargs["mobile"]  # 获取地址栏的路径参数，在路由声明的 　re_path("collection/(?P<pk>\d+)/(?P<mobile>\d+)", views.CollecionDetailAPIView.as_view()),

        id = self.context["view"].kwargs["pk"]
        name = attrs.get("name")
        user = self.context["request"].user
        try:
            ArticleCollection.objects.get(user=user,id=id)
        except ArticleCollection.DoesNotExist:
            raise serializers.ValidationError("当前文集您没有权限修改！")

        try:
            ArticleCollection.objects.get(user=user, name=name)
            raise serializers.ValidationError("当前文集没有进行修改或者与您的其他文件同名了！")
        except ArticleCollection.DoesNotExist:
            pass

        return attrs

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.save()
        return instance

from .models import Article
import re
class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id","title","content","collection","save_id"]

    def validate(self, attrs):
        content = attrs.get("content")
        if len(content)>0:
            # 判断内容是否包含了恶意代码，防止客户端遭到跨站脚本攻击[xss]
            content = re.subn("(<)(.*?script.*?)(>)","&lt;\\2&gt;", content )[0]
            # 正则捕获模式，可以提取正则中的小括号里面的内容
            attrs["content"] = content

        return attrs

    def create(self, validated_data):
        instance = Article.objects.create(
            title=validated_data.get("title"),
            content=validated_data.get("content"),
            collection=validated_data.get("collection"),
            user=self.context["request"].user,
            is_public=True,
        )

        return instance


from .models import Special
class SpecialModelSerializer(serializers.ModelSerializer):
    post_status = serializers.BooleanField(read_only=True, help_text="文章的收录状态")
    class Meta:
        model = Special
        fields = ["id","name","image","article_count","follow_count","collect_count","post_status"]



from users.models import User
class AuthorModelSerializer(serializers.ModelSerializer):
    """文章作者"""
    class Meta:
        model = User
        fields = "__all__" # 自己编写需要显示的字段即可

from .models import ArticleCollection
class CollectionInfoModelSerializer(serializers.ModelSerializer):
    """文集信息"""
    class Meta:
        model = ArticleCollection
        fields = "__all__" # 自己编写需要显示的字段即可

class ArticleInfoModelSerializer(serializers.ModelSerializer):
    user = AuthorModelSerializer()
    collection = CollectionInfoModelSerializer()
    class Meta:
        model = Article
        fields = [
            "title", "content", "user",
            "collection", "pub_date",
            "read_count", "like_count",
            "collect_count", "comment_count",
            "reward_count",
        ]

from drf_haystack.serializers import HaystackSerializer
from .search_indexes import ArticleIndex
from users.models import User
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","nickname","avatar"]

class ArticleIndexSerializer(HaystackSerializer):
    """
    文章索引结果数据序列化器
    """
    class Meta:
        index_classes = [ArticleIndex]
        fields = ('id', 'title', 'content', "author_id", 'author_name', "author_avatar", 'read_count','like_count','comment_count','reward_count')