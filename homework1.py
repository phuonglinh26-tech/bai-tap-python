#bài 1
price =120000
quantily = 3
Tong_tien = price*quantily
print("Tổng tiền :", Tong_tien, "VND")

#bài 2
price = 500000
discount_percent = 0.1
so_tien_duoc_giam = discount_percent *price
Thanh_toan = price - so_tien_duoc_giam
print("số tiền được giảm : ", so_tien_duoc_giam , "VND")
print("Thanh toán :",Thanh_toan, "VND" )


#bài 3
salary_per_day = 300000
working_days = 22
salary = salary_per_day*working_days

print("tổng lương :", salary)

#bài 4
distance_km = 12
cost_per_km = 5000
phi_van_chuyen = distance_km*cost_per_km
print("Phí vận chuyển :", phi_van_chuyen , "VND")

#bài 5 
total_storage = 256
used_storage = 180
dung_luong_con_lai = total_storage - used_storage
print("Dung lượng còn lại :" , dung_luong_con_lai)


#bài 6

balance = 200000
item_price = 150000
if balance >= item_price :
    print("Thanh toán thành công")
else :
    print("Bạn không đủ tiền trong tài khoản")    


    #bài 7

order_value = 250000
if order_value >= 200000 :
    print("Miễn phí ship")
else:
    print("Đơn hàng có phí ship")    


# bài 8 
is_logged_in = True
is_admin = False
if is_logged_in :
    if is_admin :
        print("quyền admin")
    else :
           print("không có quyền admin")
else:           
    print("Không có quyền đăng nhập")


# bài 9
hour = 14
if  hour >=9  <=18 :
    print("cuộc gọi được chuyển đến nhân viên ")
else:
    print("Ngoài giờ làm việc")    

#bài 10 
email = "user@gmail.com"
if  "@" and "." in  email:
    print("địa chỉ mail hợp lệ ")
else:
    print("địa chỉ mail càn có @ và .")    

# bai 11
order_value = 180000
total = order_value
if order_value >= 200000 :
    print("Tong tien thanh toan :", total)
else: 
    print("tong tien thanh toan :" , total + 30000)


# bai 12

performance_score = 8.2
if performance_score >= 9 :
    print("Thuong :"  , 5000000)
elif 9>  performance_score >= 7 :
    print("Thuong :"  , 2000000)
else:
    print(" Khong co thuong")



# bai 13
status_code = 2 
if status_code == 1:
    print("Pending")
elif status_code == 2 :
        print("Shipping")
elif status_code == 3 :
    print("Delivered")        
else : 
    print("unknown")    

#bai 14
age = 15
if age <12 :
    print(50000)
elif 12<=age <=17 :
    print(70000)
else :
    print (100000)

#bai 15 
total_spent = 1200000
if total_spent >= 1000000:
    print("VIP")
elif 500000 <= total_spent <= 1000000:
    print("Gold")
else:
    print("Nomal")   


#bai16 
kwh = 135
if 0 <= kwh <= 50 :
    print("Thanh toan:", kwh*1678 )
elif 51 <= kwh <= 100 :
    print("Thanh toan :" , kwh*1734)
elif 101 <= kwh <= 200 :
    print("thanh toan :", kwh*2014)
else :
    print("bac tien dien chua quyet dinh")

#bai 17
base_salary = 10000000
kpi = 0.85
if kpi >=9 :
    print("thuong:", base_salary*0.3)
elif 8 <= kpi <9:
    print("thuong:",base_salary*0.1)
else:
    print("khong thuong")

# bai18 
distance =12
if distance <= 1:
    Print("Thanh toan :",15000)
elif 1 < distance < 10:
    print("thanh toan:", 15000+(distance -1)*12000)
else:
    print("thanh toan:",15000+9*12000+(distance-10)*10000)

#bai19
income = 15000000
debt = 3000000
if income > 100000 and debt <=0.5*income:
    print("du dieu kien cho vay")
else:
    print("Khong du dieu kien vay")


#bai20
price = 1000000
is_member = True
voucher = 100000
giam_gia = price*0.1
thanh_toan = price-giam_gia-voucher
if  thanh_toan>=0:
    if is_member:
        print("thanh toan : ", thanh_toan)
    else:
        print("thanh toan:", price -voucher)
else:
    print("Khong the thanh toan")
    
