def lang_genoeg(lengte):
    if lengte >=120:
        return ("je bent lang genoeg voor de attractie")
    else:
        return ("sorry, je bent te klein")

lengte = eval(input("hoe lang ben je: "))
print((lang_genoeg(lengte)))