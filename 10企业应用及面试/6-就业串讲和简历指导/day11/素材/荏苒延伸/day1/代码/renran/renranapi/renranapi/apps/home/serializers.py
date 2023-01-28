from rest_framework import serializers
from article.models import Article
from users.models import User
class ArticleAuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id","nickname"]
        model = User
class ArticleListModelSerializer(serializers.ModelSerializer):
    user = ArticleAuthorModelSerializer()
    class Meta:
        model = Article
        fields = ["id","title","content","user","like_count","reward_count","comment_count"]