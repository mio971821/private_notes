from django import forms
from .models import *

# 定義好 Form 的欄位之後，
# 透過 views.py 把 form 包在 context 傳給 html，
# 就可以在 html 上，呈現出我們想要讓使用者填的欄位

# 註冊表單(已有model)
class sign_upForm(forms.ModelForm):
    class Meta:
        model = User_Account
        fields = '__all__'

# 登入表單(純粹顯示表單，不需model)
class sign_inForm(forms.Form):
    class Meta:
        model = User_Account
        fields = ('email', 'password')

class MyHouse591HouseForm(forms.ModelForm):
    class Meta:
        model = MyHouse591House
        fields = '__all__'  # 使用所有欄位

class UserHouseForm(forms.ModelForm):
    class Meta:
        model = UserHouse
        fields = '__all__'  # 使用所有欄位

class GroupTenantForm(forms.ModelForm):
    class Meta:
        model = GroupTenant
        fields = '__all__'  # 使用所有欄位