from django.db import models


# Create your models here.
class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article_author = models.CharField('Автор статьи', max_length=50)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField()


class Comment(models.Model):

    # связывает комментарии со статьями. Параметр on_delete удаляет все комментарии для статьи, в случае ее удаления
    article = models.ForeignKey(Article, on_delete = models.CASCADE)

    author_name = models.CharField('Автор комментария', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=300)
