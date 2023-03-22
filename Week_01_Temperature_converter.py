while True :
    menu = int(input("1) fahrenheit to celsius   2) celsius to fahrenheit  3) exit"))

    if menu == 1:
        Fahrenheit = float(input('Enter temperature in Fahrenheit'))
        Celsius = (Fahrenheit-32.0) * (5.0) / (9.0)
#print("화씨 %.2lf도는 섭씨 %.2lf도 입니다." % (Fahrenheit, Celsius))
#print(f"화씨 {Fahrenheit:.2f}도는 섭씨 {Celsius:.2f}도 입니다.")
        print("Fehrenheit {0:.2f} degree is Celsius {1:.2f} degree.".format(Fahrenheit, Celsius))

    elif menu == 2:
        Celsius = float(input('Enter temperature in Celsius'))
        Fahrenheit = (Celsius * 9.0 / 5.0) + 32.0
        print("Celsius {0:.2f} degrees are Fehrenheit {1:.2f} degrees.".format(Celsius, Fahrenheit))

    elif menu == 3:
        break

    else :
        print("Please choose from the given menu!")
# (0°C × 9/5) + 32 = 32°F