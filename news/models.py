from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Author(models.Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.user.username

    def update_rating(self):
        posts_rating = sum([post.vote * 3 for post in self.post_set.all()])  # Рейтинги постов автора
        author_comment_rating = sum([comment.rate for comment in self.comment_set.all()])  # рейтинги комментов автора
        post_comment_ratings = sum([post.get_summary_comments_rating() for post in self.post_set.all()])
        self.rating = posts_rating + post_comment_ratings + author_comment_rating
        self.save()
        return self.rating


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=255, unique=True, verbose_name='Название')

    def __str__(self):
        return self.name


class Post(models.Model):
    # objects = None
    post = 'PS'
    news = 'NS'

    TITLE = [
        (post, "Статья"),
        (news, "Новость")
    ]

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_in']
    post_or_news = models.CharField(max_length=2, choices=TITLE, default=post, verbose_name='Статья')
    time_in = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    post_category = models.ManyToManyField(Category, through='PostCategory', verbose_name='Темы')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    vote = models.IntegerField(default=0, verbose_name='Рейтинг')

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def like(self):
        self.vote += 1
        self.save()
        return self.vote

    def dislike(self):
        self.vote -= 1
        self.save()
        return self.vote

    def get_summary_comments_rating(self):
        return sum([comment.rate for comment in self.comment_set.all()])


class PostCategory(models.Model):
    class Meta:
        verbose_name = 'Категория статьи'
        verbose_name_plural = 'Категории статьи'
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(max_length=255, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время записи')
    rate = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return f'{self.text}'

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()
