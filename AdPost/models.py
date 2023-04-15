from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    create = models.DateField(verbose_name='дата создания', auto_now=True)
    edit = models.DateField(verbose_name='дата редактирования', auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel):
    login = models.CharField(verbose_name='логин', max_length=100, unique=True)
    password = models.CharField(verbose_name='пароль', max_length=100, unique=True)
    email = models.EmailField(verbose_name='почта')
    phone_number = PhoneNumberField(verbose_name='номер телефона',
                                    unique=True, null=False, blank=False)
    date_of_birth = models.DateField(verbose_name='дата рождения')

    def __str__(self):
        return f'{self.login}, {self.phone_number}, {self.date_of_birth}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"


class Comment(BaseModel):
    author_comment = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    text = models.TextField(verbose_name='текст')

    def __str__(self):
        return f'{self.author_comment}, {self.text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"


class Post(BaseModel):
    title = models.CharField(verbose_name='заголовок', max_length=100)
    text = models.TextField(verbose_name='текст')
    image = models.ImageField(upload_to='image/', verbose_name='изображение')
    author_post = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    comments = models.ForeignKey(Comment, verbose_name='комментарии', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.author_post}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"
