from setting import MySetting
ResultShapes = input("Please enter a shape : ")



while ResultShapes not in MySetting:
    ResultShapes = input("You entered the wrong shape, please try again‌ : ")


ResultShapes = MySetting[ResultShapes]