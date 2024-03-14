from django.contrib import admin
from finanser.models import (UserData, Institution, Account, IncomeCategory, Income, ExpenseCategory, Expense)

admin.site.register(UserData)
admin.site.register(Institution)
admin.site.register(Account)
admin.site.register(IncomeCategory)
admin.site.register(ExpenseCategory)
admin.site.register(Income)
admin.site.register(Expense)
