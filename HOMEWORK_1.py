velo1 = int(input("Please enter the average take-off velocity (m/s): "))
velo2 = int(input("Please enter the average flight velocity (m/s): "))
velo3 = int(input("Please enter the average landing velocity (m/s): "))

take_off = 300000
flight = 384400000
landing = 100000


takeoffseconds = (take_off/ velo1)
flightseconds = (flight / velo2)
landingseconds = (landing / velo3)

saniyeler = takeoffseconds + flightseconds + landingseconds



saatler = 0
gunler = 0
dakikalar = 0

sn = int(saniyeler)

for i in range(1,(sn//86400)+1):
    gunler += 1
sn %= 86400

for k in range(1,(sn//3600)+1):
    saatler += 1
sn %= 3600

if saatler >=24:
    for z in range(1,(saatler//24)+1):
        gunler +=1
    saatler = saatler % 24

for j in range(1,(sn//60)+1):
    dakikalar += 1
sn %= 60

if dakikalar >= 60:
    for h in range(1,(dakikalar//60)+1):
        saatler += 1
    dakikalar = dakikalar % 60



if sn >= 60:
    for s in range(1,(sn//60) +1):
        dakikalar += 1
    sn = sn % 60
sn = (saniyeler % 86400) % 3600 % 60
my_string = "The mission will take {} day(s), {} hour(s), {} minute(s), {} second(s)."
print("The mission will take", format(gunler,'.0f'), "day(s),", format(saatler,'.0f'), "hour(s),", format(dakikalar,".0f"), "minute(s),", format(sn,".2f"), "second(s).")
