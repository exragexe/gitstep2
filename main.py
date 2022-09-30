#feature/lab1_ex_py
user=int(input("Enter how many seconds have passed since the day began? "))
altime=86400 #in second
end = altime - user
if end >= 0 :
    print(f"Your time:{int(user/3600)}:{int((user%3600)/60)}:{int(user%3600)%60}" )
    h= int(end/3600)
    min=int(end%3600)/60
    sec=int(end%3600)%60
    print(f"Last time: {int(h)}:{int(min)}:{int(sec)}")
else:
    print("ERROR!")