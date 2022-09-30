#dev

pricegamepad = int(input("Enter how much price $ your gamepad: "))
number=int(input("Enter how much gamepad you need: "))
discount=int(input("Enter which discount you need: "))
znak=str(input("Enter what are you need(all price or one): "))
allprice=int(pricegamepad * number)
procent= discount / 100
res= int(allprice * procent)
res2= int(pricegamepad*procent)
if znak=="all price":
    print(f"All price gamepads cost is {int(allprice-res)}")
elif znak =="one":
    print(f"One gamepad cost is {int(pricegamepad-res2)}")
else:
    print("Error!")
