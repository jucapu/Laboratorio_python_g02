import datetime

fecha_1 = datetime.datetime(2023,4, 13)  # tipo de dato datime
fecha_2 = datetime.datetime(2023,4, 18)

if fecha_1 > fecha_2:
    print("Nacieron el mismo dia")
elif fecha_1 < fecha_2:
    print("EL niño 2 es mayor que el niño 1")
else:
    print("El niño 1 es mayor que el niño 2")

#from datetime import datetime

#time_now = datetime.strptime("2024/12/15 12:00:00", "%Y/%m/%d %H:%M:%S").timestamp()
#print("La conversion de nuestro valor time_now es {}".format(time_now))