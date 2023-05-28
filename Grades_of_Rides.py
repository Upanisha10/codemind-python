hf,spf,sf = map(int,input().split())
if hf>50 and spf>60 and sf>100:
    print("10")
elif hf>50 and spf>60 and sf<=100:
    print("9")
elif hf<=50 and spf>60 and sf>100:
    print("8")
elif hf>50 and spf<=60 and sf>100:
    print("7")
elif hf<=50 and spf<=60 and sf<=100:
    print("5")
else:
    print("6")

