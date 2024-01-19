from django.shortcuts import render, redirect                # 導向/跳轉網頁介面
from django.http import HttpResponse, JsonResponse           # 網頁回應
from django.views.decorators.csrf import csrf_protect, csrf_exempt        # 資料傳送的合法保護:csrf標誌; Ajax

from .models import *          # 引進自己寫的models
from .forms import *                                         # 引進自己寫的forms
from django.contrib import auth
from django.contrib import contenttypes                      # 是Django内容类型系统，它允许权限与你创建的模型关联。
from django.contrib.auth import authenticate, login, logout  # 驗證使用者所輸入的帳號及密碼是否正確
from django.contrib.auth.decorators import login_required    # 為了防止使用者在沒有進行登入的動作時，直接透過網址存取首頁
                                                             # 在需要登入才可存取的檢視函式(View Function)上，加上@login_required標籤，並且設定登入頁面的名稱
                                                             # @login_required(login_url="Sign_in")
                                                             # 當使用者未登入，而存取首頁的網址時，Django就會自動將使用者導向到登入畫面。
import math                                 # 算數
import json                                 # 後端傳前端
from django.db import connection            # 連db
from django.contrib.gis.geos import Point   # map
import googlemaps                           # map
from datetime import datetime               # 爬蟲 時間
from decimal import Decimal


# 首頁
def home(request):
    context = {
#      "username": User_Account.get_username(), 
    } # 新增字典

    return render(request, "home.html", context)

# 租房
def tenant(request):
    context = {} # 新增字典
    return render(request, "tenant.html", context)

from django.contrib import messages
# 租房(A)
def tenant_a(request):
    isGetHouse = False;
    # 取得所有房屋
    query_result = MyHouse591House.objects.select_related('user_houses').all()

    # 從前端接收的篩選條件
    house_type_values = request.GET.getlist('房型[]', None)
    building_type_values = request.GET.getlist('建築類型[]', None)
    rent_type_values = request.GET.getlist('價格[]', None)
    roomCount_values = request.GET.get('格局_房數', None)
    socket_values = request.GET.get('插座數', None)
    other_type_values = {}
    fields_to_check = [
        '室內窗類型', '冷氣類型', '洗衣機類型', '烘衣機類型',
        '冰箱類型', '提供設備_電梯', '提供設備_熱水器', '提供設備_天然瓦斯',
        '提供設備_電視', '提供設備_第四台', '提供設備_網路', '電費類型',
        '水費類型', '提供停車位', '刊登者類型', '有寵物限制', '是否可伙',
        '性別限制',
    ]
    for field in fields_to_check:  # 一個一個GET
        other_type_values[field] = request.GET.get(field, None)

    # 獲取排序狀態
    order_type = request.GET.get('order_type', 'asc')  # 默認升序

    # 根據篩選條件過濾房屋
    if house_type_values and '不限' not in house_type_values:
        query_result = query_result.filter(房型__in=house_type_values)  # __in 表示篩選在指定列表中的值
    if building_type_values and '不限' not in building_type_values:
        query_result = query_result.filter(建物類型__in=building_type_values)
    if rent_type_values:  # '15000' '20000' '以上'
        if '以上' in rent_type_values:
            # 如果 '以上' 在租金範圍中，則篩選租金 >= 15000 的房屋
            query_result = query_result.filter(價格__gte=rent_type_values[0])
        else:
            # 否則，篩選租金在 15000 ~ 20000 之間的房屋
            query_result = query_result.filter(價格__range=[rent_type_values[0], rent_type_values[1]])
    if roomCount_values and roomCount_values != '不限':
        query_result = query_result.filter(格局_房數=roomCount_values)
    if socket_values and socket_values != '不限' :
        query_result = query_result.filter(插座數__gte=socket_values)
    for field, value in other_type_values.items():
        if value :  # 有GET到，就過濾
            query_result = query_result.filter(**{field: value})

    # 最終查不到資料，推薦資料給使用者
    if not query_result.exists():
        # 重新獲取所有房屋
        isGetHouse = False
        query_result = MyHouse591House.objects.select_related('user_houses').all()
        # 繼續進行後續的篩選和排序
        if house_type_values and '不限' not in house_type_values:
            query_result = query_result.filter(房型__in=house_type_values)
    else:
        isGetHouse = True

    # 排序
    if order_type == 'asc':
        query_result = query_result.order_by('價格')
    elif order_type == 'desc':
        query_result = query_result.order_by('-價格')

    # 轉成JSON格式
    result_data = {
        'query_result': list(query_result.values(
            'id', '房型', '建物類型', '地址', '樓層', '格局_房數', '格局_衛浴數',
            '格局_廚房數', '格局_客廳數', '格局_陽台數', '插座數', '坪數', '提供家具_桌子',
            '提供家具_椅子', '提供家具_沙發', '提供家具_衣櫃', '提供家具_收納櫃', '提供家具_床',
            '提供設備_洗衣機', '洗衣機類型', '提供設備_烘衣機', '烘衣機類型', '提供設備_冰箱',
            '冰箱類型', '提供設備_冷氣', '冷氣類型', '提供設備_室內窗', '室內窗類型', '提供設備_電梯',
            '提供設備_熱水器', '提供設備_天然瓦斯', '提供設備_電視', '提供設備_第四台', '提供設備_網路',
            '價格', '押金', '電費類型', '自訂電費價格', '水費類型', '自訂水費價格', '提供停車位',
            '停車位費用', '需要管理費', '管理費費用', '廣告標題', '最短租期', '最短租期單位',
            '刊登者類型', '有性別限制', '性別限制', '有身分限制', '身分限制_學生', '身分限制_上班族',
            '身分限制_家庭', '有寵物限制', '是否可伙', '有產權登記', '來源平台', '來源編號', '圖片路徑',
            '合租缺額', 'user_houses__姓氏', 'user_houses__名字', 'user_houses__性別',
            'user_houses__稱謂', 'user_houses__電話', 'user_houses__email', 'user_houses__房屋編號'
        )),
        # 不使用query_result.values()是因為，若使用select_related()關聯的話，
        # 直接用.values()只會回傳原本MyHouse591House物件的欄位，所以需要手動加上user_houses的欄位。
        # 雙下劃線 __ 表示對關聯字段的查詢，user_houses 是一個關聯字段(看models)，它指向另一個模型，而 __ 用於在模型之間建立關聯

        'isGetHouse': isGetHouse,  # 添加 isGetHouse 到 result_data
    }

    context = {
        'result_data': result_data
    } # 新增字典

    # 判斷請求是否為 Ajax 請求，若是則回傳 JSON 格式的資料，否則正常回傳 HTML 頁面
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        print(request.GET)
        return JsonResponse(result_data)
    
    return render(request, "tenant_a.html", context)

# 租房(B)
gmaps = googlemaps.Client(key='AIzaSyCZgvusoZLMa3yZYDsZCRK0vzHl93yOZPA')

def search_house (request):
    #areas = ImageArea.objects.all()
    context = {
        #'areas': areas
    }  # 字典
    return render(request, "tenant_b.html", context)

def sort_key(house):
    return (-house["符合點"], house["總距離"])

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


def tenant_b(request):
    
    if request.method == 'GET':
        selected_points = json.loads(request.GET.get('selectedPoints', '[]'))
        labels = [item['label'] for item in selected_points]
        print("OWO")
        print(labels)

        cursor = connection.cursor() # 創造一指標操作database
        cursor.execute("SELECT * FROM myhouse_591house")
        myhouse_data = cursor.fetchall()
        # 檢查每一行是否為元組，如果不是，則跳過該行
        myhouse_data_dicts = []
        for row in myhouse_data:
            if isinstance(row, tuple):
                # 使用 zip 將鍵和值分離，再使用 dict() 建構子建立字典
                myhouse_data_dicts.append(dict(zip([col.name for col in cursor.description], row)))

            
        for house in myhouse_data_dicts:
            total_matches = 0
            total_distance = 0
            #print( house["來源編號"])

            for label in labels:
                # 在這裡檢查 house 是否符合 label 表中的條件，計算距離等
                sql_statement = f"SELECT * FROM {label} WHERE CAST(\"來源編號\" AS INTEGER) = %s"

                # 要检查的来源编码
                source_code_to_check = house["id"]

                # 执行SQL语句
                cursor.execute(sql_statement, (source_code_to_check,))

                # 获取查询结果
                a = cursor.fetchall()

                if a:
                    
                    total_matches += 1
                    total_distance += int (a[0][len(a[0]) -1])  # 假设有一个 "distance" 列

            # 在這裡你可以更新 house 數據，添加 "符合點" 和 "總距離" 列
            house["符合點"] = total_matches
            house["總距離"] = total_distance
            #print(house)

        # 返回符合条件的房屋信息
        # 使用 sorted 函數對列表進行排序
        sorted_houses = sorted(myhouse_data_dicts, key=sort_key)
        # 取得所有房屋
        

        # 轉成JSON格式
        result_data = {
            'query_result': sorted_houses,
            
        }

        context = {
            'result_data': result_data
        } # 新增字典

        # 判斷請求是否為 Ajax 請求，若是則回傳 JSON 格式的資料，否則正常回傳 HTML 頁面
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            
            print(request.GET)
            return JsonResponse(result_data)
    
        return render(request, "tenant_b.html", context)

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item_detail.html', {'item': item})

# 分析

def analysis(request):
    category_a = ''
    category_b = ''
    citynames = []
    average_rents_a = []
    objectnames = []
    average_rents_b = []

    if 'category_a' in request.GET or 'category_b' in request.GET:
        category_a = request.GET.get('category_a', '獨立套房')  # 獲取名為category的GET參數，如果沒有指定，則默認為獨立套房
        category_b = request.GET.get('category_b', '新北市')  # 獲取名為category的GET參數，如果沒有指定，則默認為新北市

        # A ------------------------------------------------------------------------
        with connection.cursor() as cursor:
            cursor.execute("SELECT cityname, 平均月租金 FROM " + category_a)
            rows = cursor.fetchall()

        citynames = [row[0] for row in rows]
        average_rents_a = [row[1] for row in rows]
        
        # 將 Decimal 數值轉換為整數
        average_rents_a = [int(rent) for rent in average_rents_a]

        # B ------------------------------------------------------------------------
        with connection.cursor() as cursor:
            cursor.execute("SELECT objectname, 平均月租金 FROM " + category_b)
            rows = cursor.fetchall()

        objectnames = [row[0] for row in rows]
        average_rents_b = [row[1] for row in rows]

        # 將 Decimal 數值轉換為整數
        average_rents_b = [int(rent) for rent in average_rents_b]

    context = {
        'citynames': citynames,
        'objectnames': objectnames,
        'average_rents_a': average_rents_a,
        'average_rents_b': average_rents_b,
        'selected_category_a': category_a,
        'selected_category_b': category_b,
    }

    # 判斷請求是否為 Ajax 請求，若是則回傳 JSON 格式的資料，否則正常回傳 HTML 頁面
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(context)
    else:
        return render(request, 'analysis.html', context)

# 出租
def rent_choose(request):
    context = {} # 新增字典
    return render(request, "rent_choose.html", context)

from uuid import uuid4  # 生成唯一標識符
from django.core.files.storage import FileSystemStorage # 使用 FileSystemStorage 儲存文件
from django.conf import settings
import os

@login_required(login_url="Sign_in")
def rent_a(request):
    context = {} # 新增字典
    form = MyHouse591HouseForm()

    if request.method == 'POST':
        pictures = request.FILES.getlist('picture_multi')  # 從 request.FILES 中獲取名為 picture_multi 的上傳文件列表

        # 生成唯一標識符
        unique_identifier = str(uuid4())

        # 存儲所有圖片的路徑
        paths = []

        for picture in pictures:
            # 創建了一個 FileSystemStorage 對象，它將文件存儲在 MEDIA_ROOT/houseFile 目錄中。MEDIA_ROOT 是在 Django 設置中配置的媒體文件根目錄
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'houseFile'))
            # 構建新的文件名，例如 "unique_identifier_filename.jpg"
            new_filename = f"{unique_identifier}_{picture.name}"
            filename = fs.save(new_filename, picture)  # 保存文件，參數:1.文件名 2.文件對象

            # 將圖片路徑加入列表
            paths.append(os.path.basename(filename))  # 使用 os.path.basename() 取得文件名而非完整路徑

        # 試著接受 Form 的 POST
        # 收到的 form 如果合法，我們就存到 DB 去
        form = MyHouse591HouseForm(request.POST)
        # 刪除不需要的字段
        if 'picture_multi' in form.fields:
            del form.fields['picture_multi']

        if form.is_valid():
            # 將圖片路徑存入表單
            form.instance.圖片路徑 = paths
            house_instance = form.save()  # 存入房屋資訊

            # 創建 user_house form 對象
            user_title = request.user.first_name + request.user.gender
            user_house = UserHouse(
                姓氏=request.user.first_name,
                名字=request.user.last_name,
                性別=request.user.gender,
                稱謂=user_title,
                電話=request.user.telephone,
                email=request.user.email,
                房屋編號=house_instance
            )

            user_house.save() # 將 user_house 保存到資料庫

            success_message = "已成功送出表單！"
            response = HttpResponse(f'<script>alert("{success_message}"); window.location.href="/welcome/home";</script>')
            return response
        else:
            print("表單錯誤!")
            print(request.POST)
            print("具體錯誤:")
            print(form.errors.as_data())
            

    return render(request, "rent_a.html", context)

@login_required(login_url="Sign_in")
def rent_b(request):
    context = {} # 新增字典
    form = MyHouse591HouseForm()

    if request.method == 'POST':
        pictures = request.FILES.getlist('picture_multi')  # 從 request.FILES 中獲取名為 picture_multi 的上傳文件列表

        # 生成唯一標識符
        unique_identifier = str(uuid4())

        # 存儲所有圖片的路徑
        paths = []

        for picture in pictures:
            # 創建了一個 FileSystemStorage 對象，它將文件存儲在 MEDIA_ROOT/houseFile 目錄中。MEDIA_ROOT 是在 Django 設置中配置的媒體文件根目錄
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'houseFile'))
            # 構建新的文件名，例如 "unique_identifier_filename.jpg"
            new_filename = f"{unique_identifier}_{picture.name}"
            filename = fs.save(new_filename, picture)  # 保存文件，參數:1.文件名 2.文件對象

            # 將圖片路徑加入列表
            paths.append(os.path.basename(filename))  # 使用 os.path.basename() 取得文件名而非完整路徑

        # 試著接受 Form 的 POST
        # 收到的 form 如果合法，我們就存到 DB 去
        form = MyHouse591HouseForm(request.POST)
        # 刪除不需要的字段
        if 'picture_multi' in form.fields:
            del form.fields['picture_multi']

        if form.is_valid():
            # 將圖片路徑存入表單
            form.instance.圖片路徑 = paths
            house_instance = form.save()  # 存入房屋資訊

            # 創建 user_house form 對象
            user_title = request.user.first_name + request.user.gender
            user_house = UserHouse(
                姓氏=request.user.first_name,
                名字=request.user.last_name,
                性別=request.user.gender,
                稱謂=user_title,
                電話=request.user.telephone,
                email=request.user.email,
                房屋編號=house_instance
            )

            user_house.save() # 將 user_house 保存到資料庫

            success_message = "已成功送出表單！"
            response = HttpResponse(f'<script>alert("{success_message}"); window.location.href="/welcome/home";</script>')
            return response
        else:
            print("表單錯誤!")
            print(request.POST)
            print("具體錯誤:")
            print(form.errors.as_data())
    return render(request, "rent_b.html", context)

@login_required(login_url="Sign_in")
def rent_c(request):
    context = {} # 新增字典
    form = MyHouse591HouseForm()

    if request.method == 'POST':
        pictures = request.FILES.getlist('picture_multi')  # 從 request.FILES 中獲取名為 picture_multi 的上傳文件列表

        # 生成唯一標識符
        unique_identifier = str(uuid4())

        # 存儲所有圖片的路徑
        paths = []

        for picture in pictures:
            # 創建了一個 FileSystemStorage 對象，它將文件存儲在 MEDIA_ROOT/houseFile 目錄中。MEDIA_ROOT 是在 Django 設置中配置的媒體文件根目錄
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'houseFile'))
            # 構建新的文件名，例如 "unique_identifier_filename.jpg"
            new_filename = f"{unique_identifier}_{picture.name}"
            filename = fs.save(new_filename, picture)  # 保存文件，參數:1.文件名 2.文件對象

            # 將圖片路徑加入列表
            paths.append(os.path.basename(filename))  # 使用 os.path.basename() 取得文件名而非完整路徑

        # 試著接受 Form 的 POST
        # 收到的 form 如果合法，我們就存到 DB 去
        form = MyHouse591HouseForm(request.POST)
        # 刪除不需要的字段
        if 'picture_multi' in form.fields:
            del form.fields['picture_multi']

        if form.is_valid():
            # 將圖片路徑存入表單
            form.instance.圖片路徑 = paths
            house_instance = form.save()  # 存入房屋資訊

            # 創建 user_house form 對象
            user_title = request.user.first_name + request.user.gender
            user_house = UserHouse(
                姓氏=request.user.first_name,
                名字=request.user.last_name,
                性別=request.user.gender,
                稱謂=user_title,
                電話=request.user.telephone,
                email=request.user.email,
                房屋編號=house_instance
            )

            user_house.save() # 將 user_house 保存到資料庫

            success_message = "已成功送出表單！"
            response = HttpResponse(f'<script>alert("{success_message}"); window.location.href="/welcome/home";</script>')
            return response
        else:
            print("表單錯誤!")
            print(request.POST)
            print("具體錯誤:")
            print(form.errors.as_data())
    return render(request, "rent_c.html", context)

@login_required(login_url="Sign_in")
def rent_d(request):
    context = {} # 新增字典
    form = MyHouse591HouseForm()

    if request.method == 'POST':
        pictures = request.FILES.getlist('picture_multi')  # 從 request.FILES 中獲取名為 picture_multi 的上傳文件列表

        # 生成唯一標識符
        unique_identifier = str(uuid4())

        # 存儲所有圖片的路徑
        paths = []

        for picture in pictures:
            # 創建了一個 FileSystemStorage 對象，它將文件存儲在 MEDIA_ROOT/houseFile 目錄中。MEDIA_ROOT 是在 Django 設置中配置的媒體文件根目錄
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'houseFile'))
            # 構建新的文件名，例如 "unique_identifier_filename.jpg"
            new_filename = f"{unique_identifier}_{picture.name}"
            filename = fs.save(new_filename, picture)  # 保存文件，參數:1.文件名 2.文件對象

            # 將圖片路徑加入列表
            paths.append(os.path.basename(filename))  # 使用 os.path.basename() 取得文件名而非完整路徑

        # 試著接受 Form 的 POST
        # 收到的 form 如果合法，我們就存到 DB 去
        form = MyHouse591HouseForm(request.POST)
        # 刪除不需要的字段
        if 'picture_multi' in form.fields:
            del form.fields['picture_multi']

        if form.is_valid():
            # 將圖片路徑存入表單
            form.instance.圖片路徑 = paths
            house_instance = form.save()  # 存入房屋資訊

            # 創建 user_house form 對象
            user_title = request.user.first_name + request.user.gender
            user_house = UserHouse(
                姓氏=request.user.first_name,
                名字=request.user.last_name,
                性別=request.user.gender,
                稱謂=user_title,
                電話=request.user.telephone,
                email=request.user.email,
                房屋編號=house_instance
            )

            user_house.save() # 將 user_house 保存到資料庫

            success_message = "已成功送出表單！"
            response = HttpResponse(f'<script>alert("{success_message}"); window.location.href="/welcome/home";</script>')
            return response
        else:
            print("表單錯誤!")
            print(request.POST)
            print("具體錯誤:")
            print(form.errors.as_data())
    return render(request, "rent_d.html", context)

# 關於我們
def about(request):
    context = {} # 新增字典
    return render(request, "about.html", context)

# 註冊
def sign_up(request):
    context = {} # 新增字典

    # 試著接受 Form 的 POST
    # 收到的 form 如果合法，我們就存到 DB 去
    form = sign_upForm()
    if request.method == "POST":
        form = sign_upForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/welcome/home")  # 跳轉到這個網址去

    return render(request, "signup.html", context)

# 登入
def sign_in(request):
    context = {} # 新增字典

    # 登入時，就可以將使用者所輸入的帳號及密碼，傳入authenticate方法(Method)進行驗證，
    # 如果通過，則利用login()方法(Method)將使用者進行登入的動作
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)  # 自動判斷:使用自己寫的驗證系統
        # auth.authenticate方法接受兩個引數，分別是username和password，
        # 如果帳密資訊正確，authenticate方法會回給我們一個具名用戶的User物件，否則我們會拿到None
        if user is not None:
            auth.login(request, user) 
            # auth.login需要一個HttpRequest物件和一個User物件當做引數，
            # 他會利用Django的session 將這個具名用戶保存在該session中，
            # 這也代表了該用戶的登入狀態得以跨頁面的保存直到session結束或登出。
            return redirect('/welcome/home')  #重新導向到登入後頁面
        else:
            return redirect('/welcome/login')  #重新導向到可登入頁面


    return render(request, "login.html", context)

# 登出
def log_out(request):
    context = {} # 新增字典
    auth.logout(request)
    return redirect('/welcome/home/') #重新導向到首頁

# 物件詳細資料頁面(動態生成)
def item_detail(request, item_id):
    # 使用 item_id 檢索特定項目的數據
    # ...
    context = {
        'item_id': item_id,
    } # 新增字典
    return render(request, 'item_detail.html', context)

# 合租
def group_tenant(request):
    houseid = request.GET.get('house_id', None)
    house_data = MyHouse591House.objects.get(id=houseid)
    group_tenant_value = house_data.合租缺額

    group_tenant_data = GroupTenant.objects.filter(houseid=houseid)
    group_tenant_users = []
    for data in group_tenant_data:
        user_info = {
            'group_tenant_user_name': data.合租人姓名,
            'group_tenant_user_phone': data.合租人電話,
            'group_tenant_user_email': data.合租人信箱,
            'group_tenant_user_input': data.留言,
        }
        group_tenant_users.append(user_info)

    context = {
        'group_tenant_value': group_tenant_value,
        'group_tenant_users': group_tenant_users
    } # 新增字典

    return JsonResponse(context)

from django.db.models import F
from django.shortcuts import get_object_or_404
def join_group(request):
    if request.method == 'POST':
        houseid = request.POST.get('houseid')
        user_input = request.POST.get('user_input')
        user = request.user   # 假設用戶已經登入
        username = user.first_name + user.last_name
        # 執行加入操作
        form_data = {
            'houseid': houseid,
            'userid': user.id,
            '合租人姓名': username,
            '合租人電話': user.telephone,
            '合租人信箱': user.email,
            '留言': user_input
        }

        form = GroupTenantForm(form_data)
        if form.is_valid():
            form.save()
            # 更新 MyHouse591House 表中對應 ID 的資料的合租缺額值
            my_house = get_object_or_404(MyHouse591House, id=houseid)  # 找不到自動引發HTTP404異常
            my_house.合租缺額 = F('合租缺額') - 1  # F表達式在資料庫層面操作，而非從資料庫取值、python計算後更新回資料庫，避免併發問題
            my_house.save()

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def leave_group(request):
    if request.method == 'POST':
        houseid = request.POST.get('houseid')
        user = request.user  # 假設你的用戶已經登入

        # 執行取消操作
        try:
            group_tenant = GroupTenant.objects.get(houseid=houseid, userid=user.id)
            group_tenant.delete()
            # 更新 MyHouse591House 表中對應 ID 的資料的合租缺額值
            my_house = get_object_or_404(MyHouse591House, id=houseid)  # 找不到自動引發HTTP404異常
            my_house.合租缺額 = F('合租缺額') + 1  # F表達式在資料庫層面操作，而非從資料庫取值、python計算後更新回資料庫，避免併發問題
            my_house.save()

            return JsonResponse({'status': 'success'})
        except GroupTenant.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'GroupTenant not found'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})