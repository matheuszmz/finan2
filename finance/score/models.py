from django.db import models
from user.models import User

from django.utils.translation import ugettext_lazy as _


class Account(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'


class Accountable(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    accountable = models.ForeignKey(Accountable, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_buy = models.DateField()
    description = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    parcel = models.IntegerField()

    def __str__(self):
        return '[{}|{}|{}]: {} - {} - R$ {}'.format(self.user, self.account, self.accountable,
                                                    self.date_buy, self.description, self.value)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class Score(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE)
    parcel = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField()
    paid_date = models.DateField()

    def __str__(self):
        return '{} - R$ {} - Dt. Vencimento: {}'.format(self.parcel, self.value, self.due_date)

    class Meta:
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas'
