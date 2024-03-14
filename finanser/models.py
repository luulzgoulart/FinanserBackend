from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User Data'
        verbose_name_plural = 'Users Data'

    def __str__(self):
        return f"{self.user.username}'s data"


class Institution(models.Model):

    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='institutions/logo/', null=True, blank=True)
    hex_color = models.CharField(max_length=7, null=True, blank=True)
    owner = models.ForeignKey(UserData, related_name="inst_owner", on_delete=models.CASCADE)
    is_global = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'

    def __str__(self):
        if self.is_global:
            return f"{self.name} (Global)"
        else:
            return f"{self.name} ({self.owner.user.username})"


class Account(models.Model):

    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=3, default="BRL")
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserData, related_name="acc_owner", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return f"{self.name} ({self.owner.user.username})"


class IncomeCategory(models.Model):

    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='categories/icon/', null=True, blank=True)
    hex_color = models.CharField(max_length=7, null=True, blank=True)
    owner = models.ForeignKey(UserData, related_name="inc_cat_owner", on_delete=models.CASCADE)
    is_global = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Income Category'
        verbose_name_plural = 'Income Categories'

    def __str__(self):
        if self.is_global:
            return f"{self.name} (Global)"
        else:
            return f"{self.name} ({self.owner.user.username})"


class ExpenseCategory(models.Model):

    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='categories/icon/', null=True, blank=True)
    hex_color = models.CharField(max_length=7, null=True, blank=True)
    owner = models.ForeignKey(UserData, related_name="exp_cat_owner", on_delete=models.CASCADE)
    is_global = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Expense Category'
        verbose_name_plural = 'Expense Categories'

    def __str__(self):
        if self.is_global:
            return f"{self.name} (Global)"
        else:
            return f"{self.name} ({self.owner.user.username})"


class Income(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, related_name="acc_income", on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'

    def __str__(self):
        return f"{self.title} ({self.account.owner.user.username})"


class Expense(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, related_name="acc_expense", on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return f"{self.title} ({self.account.owner.user.username})"
