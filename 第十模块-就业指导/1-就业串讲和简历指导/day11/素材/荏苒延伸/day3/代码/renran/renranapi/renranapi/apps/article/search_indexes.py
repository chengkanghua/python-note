from haystack import indexes
from .models import Article

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    """
    文章索引数据模型类
    """
    id = indexes.IntegerField(model_attr='id')
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')
    read_count = indexes.IntegerField(model_attr='read_count')
    like_count = indexes.IntegerField(model_attr='like_count')
    comment_count = indexes.IntegerField(model_attr='comment_count')
    reward_count = indexes.IntegerField(model_attr='reward_count')
    author_id = indexes.IntegerField(model_attr="user_id")
    author_name = indexes.CharField(model_attr="user_nickname")
    author_avatar = indexes.CharField(model_attr="user_avatar")
    # 文档字段，这个字段不属于模型的，可以通过这个索引字段，到数据库中进行多个字段的搜索匹配
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """返回建立索引的模型类"""
        return Article

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.filter(is_public=True)

