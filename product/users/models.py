from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Course, Group


class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )
    balance = models.DecimalField(default=1000, decimal_places=2, max_digits=10, verbose_name='Баланс')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()




class Subscription(models.Model):
    """Модель подписки пользователя на курс."""

    user = models.ForeignKey(CustomUser, related_name='subscriptions', on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, related_name='subscriptions', on_delete=models.CASCADE, verbose_name='Курс')
    group = models.ForeignKey(Group, related_name='subscriptions', on_delete=models.SET_NULL, null=True, verbose_name='Группа')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)
