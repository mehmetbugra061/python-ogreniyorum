maas = int(input("aldığınız maaş "))
borc = int(input("ne kadar borcunuz var"))

karlilik = maas - borc
if(karlilik == 0):
  print("borcunuz bulunmamaktadır")
elif(karlilik > 0):
    print("bu ay ki maaşınızdan kazancınız  var")
else:
    print("bu ay ki maaşınızdan zararınız var")     
