from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.gis.db import models as gis_models

# 創建自訂使用者模型的管理器
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)

# 自訂使用者模型
class User_Account(AbstractBaseUser):
    first_name = models.TextField()
    last_name = models.TextField()
    telephone = models.TextField()
    gender = models.TextField()
    email = models.TextField(unique=True)
    password = models.TextField()
    is_active = models.BooleanField(default=True)  # 該用戶是否為活躍狀態
    is_staff = models.BooleanField(default=False)  # 該用戶是否可登入admin後端

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']  # 添加必需的欄位
    
    #def get_username(self):
    #    return self.name

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

class MyHouse591House(models.Model):
    # 主鍵
    id = models.BigAutoField(primary_key=True)

    # 房屋基本信息
    房型 = models.CharField(max_length=4, db_column='房型')
    建物類型 = models.CharField(max_length=8, db_column='建物類型')
    地址 = models.CharField(max_length=32, db_column='地址')
    樓層 = models.IntegerField(db_column='樓層')
    合租缺額 = models.IntegerField(db_column='合租缺額')
    格局_房數 = models.IntegerField(db_column='格局_房數')
    格局_衛浴數 = models.IntegerField(db_column='格局_衛浴數')
    格局_廚房數 = models.IntegerField(null=True, blank=True, db_column='格局_廚房數')
    格局_客廳數 = models.IntegerField(db_column='格局_客廳數')
    格局_陽台數 = models.IntegerField(db_column='格局_陽台數')
    插座數 = models.IntegerField(null=True, blank=True, db_column='插座數')
    坪數 = models.DecimalField(max_digits=5, decimal_places=2, db_column='坪數') # 總位數為 5，小數點位數為 2，坪數的範圍:0~999.99
    
    # 家具相關
    提供家具_桌子 = models.BooleanField(db_column='提供家具_桌子？')
    提供家具_椅子 = models.BooleanField(db_column='提供家具_椅子？')
    提供家具_沙發 = models.BooleanField(db_column='提供家具_沙發？')
    提供家具_衣櫃 = models.BooleanField(db_column='提供家具_衣櫃？')
    提供家具_收納櫃 = models.BooleanField(db_column='提供家具_收納櫃？')
    提供家具_床 = models.BooleanField(db_column='提供家具_床？')
    
    # 設備相關
    提供設備_洗衣機 = models.BooleanField(db_column='提供設備_洗衣機？')
    洗衣機類型 = models.CharField(max_length=2, null=True, blank=True, db_column='洗衣機類型')
    提供設備_烘衣機 = models.BooleanField(db_column='提供設備_烘衣機？')
    烘衣機類型 = models.CharField(max_length=2, null=True, blank=True, db_column='烘衣機類型')
    提供設備_冰箱 = models.BooleanField(db_column='提供設備_冰箱？')
    冰箱類型 = models.CharField(max_length=2, null=True, blank=True, db_column='冰箱類型')
    提供設備_冷氣 = models.BooleanField(db_column='提供設備_冷氣？')
    冷氣類型 = models.CharField(max_length=2, null=True, blank=True, db_column='冷氣類型')
    提供設備_室內窗 = models.BooleanField(db_column='提供設備_室內窗？')
    室內窗類型 = models.CharField(max_length=2, null=True, blank=True, db_column='室內窗類型')
    提供設備_電梯 = models.BooleanField(db_column='提供設備_電梯？')
    提供設備_熱水器 = models.BooleanField(db_column='提供設備_熱水器？')
    提供設備_天然瓦斯 = models.BooleanField(db_column='提供設備_天然瓦斯？')
    提供設備_電視 = models.BooleanField(db_column='提供設備_電視？')
    提供設備_第四台 = models.BooleanField(db_column='提供設備_第四台？')
    提供設備_網路 = models.BooleanField(db_column='提供設備_網路？')
    
    # 租金相關
    價格 = models.IntegerField(db_column='價格')
    押金 = models.IntegerField(db_column='押金')
    電費類型 = models.CharField(max_length=2, null=True, blank=True, db_column='電費類型')
    自訂電費價格 = models.IntegerField(null=True, blank=True, db_column='自訂電費價格')
    水費類型 = models.CharField(max_length=2, null=True, blank=True, db_column='水費類型')
    自訂水費價格 = models.IntegerField(null=True, blank=True, db_column='自訂水費價格')
    
    # 車位和管理費
    提供停車位 = models.BooleanField(db_column='提供停車位？')
    停車位費用 = models.IntegerField(null=True, blank=True, db_column='停車位費用')
    需要管理費 = models.BooleanField(db_column='需要管理費？')
    管理費費用 = models.IntegerField(null=True, blank=True, db_column='管理費費用')
    
    # 租屋條件和其他
    廣告標題 = models.CharField(max_length=32, db_column='廣告標題')
    最短租期 = models.IntegerField(db_column='最短租期')
    最短租期單位 = models.CharField(max_length=1, db_column='最短租期單位')
    刊登者類型 = models.CharField(max_length=3, db_column='刊登者類型')
    有性別限制 = models.BooleanField(db_column='有性別限制？')
    性別限制 = models.CharField(max_length=2, null=True, blank=True, db_column='性別限制')
    有身分限制 = models.BooleanField(db_column='有身分限制？')
    身分限制_學生 = models.BooleanField(db_column='身分限制_學生？')
    身分限制_上班族 = models.BooleanField(db_column='身分限制_上班族？')
    身分限制_家庭 = models.BooleanField(db_column='身分限制_家庭？')
    有寵物限制 = models.BooleanField(db_column='有寵物限制？')
    是否可伙 = models.BooleanField(db_column='是否可伙？')
    有產權登記 = models.BooleanField(db_column='有產權登記？')
    
    # 來源平台和圖片路徑
    來源平台 = models.CharField(max_length=8, db_column='來源平台')
    來源編號 = models.CharField(max_length=255, null=True, blank=True, db_column='來源編號')
    圖片路徑 = models.CharField(max_length=4096, null=True, blank=True, db_column='圖片路徑')

    class Meta:
        managed = False  # 不由Django管理資料表，假設該表已經存在於資料庫(這種情況下，需要手動管理資料庫表的變更)
        db_table = 'myhouse_591house'  # 使用指定的資料表

class UserHouse(models.Model):
    姓氏 = models.CharField(max_length=32, null=True, blank=True)
    名字 = models.CharField(max_length=32, null=True, blank=True)
    性別 = models.CharField(max_length=2, null=True, blank=True)
    稱謂 = models.CharField(max_length=10, null=True, blank=True)
    電話 = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=64, null=True, blank=True)
    房屋編號 = models.ForeignKey('MyHouse591House', null=True, blank=True, on_delete=models.SET_NULL, related_name='user_houses', db_column='房屋編號')  #on_delete:當對應的資料被刪除時，此欄位的資料:SET NULL
    # related_name='user_houses' 將允許 通過 user_houses 屬性來訪問與 MyHouse591House 關聯的 UserHouse 對象

    class Meta:
        managed = False  # 不由Django管理資料表，假設該表已經存在於資料庫
        db_table = 'user_house'  # 使用指定的資料表

class GroupTenant(models.Model):
    id = models.BigAutoField(primary_key=True)
    合租人姓名 = models.TextField()
    合租人電話 = models.IntegerField()
    合租人信箱 = models.TextField()
    留言 = models.TextField()

    houseid = models.ForeignKey(
        'MyHouse591House',
        on_delete=models.SET_NULL,
        null=True,
        db_column='houseid',
    )
    userid = models.ForeignKey(
        'User_Account',
        on_delete=models.SET_NULL,
        null=True,
        db_column='userid',
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['houseid', 'userid'], name='houseID_userID_PK'),
        ]
        managed = False  # 不由Django管理資料表，假設該表已經存在於資料庫
        db_table = 'grouptenant'  # 使用指定的資料表
"""
class ImageArea(models.Model):
    image = models.ImageField(upload_to='images/')
    coords = models.CharField(max_length=100)  # Example: "x1,y1,x2,y2"
    default_content = models.CharField(max_length=200)

    def __str__(self):
        return self.default_content

class House(models.Model):
    money = models.DecimalField(max_digits=10, decimal_places=2)
    place = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
"""