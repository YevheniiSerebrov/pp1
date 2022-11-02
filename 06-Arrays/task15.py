ar=["yellow", "black", "red", "purple", "green", "white", "blue"]
with open("text1.txt", "w") as t:
    for i in ar:
        t.write(i)
        t.write("\n")
