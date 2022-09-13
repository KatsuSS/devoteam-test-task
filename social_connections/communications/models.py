from django.db import models
from django.contrib.auth.models import User


class Communication(models.Model):
    initiator_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто взаимодействовал',
                                       related_name='initiator')
    acceptor_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='С кем взаимодействовал',
                                      related_name='acceptor')

    class Meta:
        verbose_name = 'Журнал взаимодействий'
        verbose_name_plural = 'Журнал взаимодействий'

    def __str__(self):
        return f'{self.initiator_user.get_full_name()} - {self.acceptor_user.get_full_name()}'
