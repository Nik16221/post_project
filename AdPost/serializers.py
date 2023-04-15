from django.core.exceptions import ValidationError
from rest_framework import serializers
from AdPost.models import User, Post, Comment


class UserSerializers(serializers.ModelSerializer):
    def valid_password(self, password):
        min_length = 8
        if len(password) < min_length:
            raise ValidationError(f'Пароль слишком короткий, минимальное количество символов {min_length}')
        if sum(c.isdigit() for c in password) < 1:
            raise ValidationError('Пароль должен содержать минимум 1 цифру')
        return password

    def valid_email(self, email):
        stop_domen = ['mail.ru', 'yandex.ru']
        for i in stop_domen:
            if i in email:
                return ValidationError('Вы используете запрещенный email!')
            return email

    class Meta:
        model = User
        fields = '__all__'


class PostSerializers(serializers.ModelSerializer):
    def valid_age(self, author_post):
        min_age = 18
        if author_post < min_age:
            raise ValidationError('Вам нет 18 лет!')
        return author_post

    def valid_text(self, text):
        stop_words = ['ерунда', 'глупость', 'чепуха']
        for word in stop_words:
            if word in text:
                return ValidationError('Вы используете запрещенные слова!')
            return text

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
