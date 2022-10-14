height=180
feet=int(height//30.48)
inches = round((height/30.48-feet)*12)
print(f"I am {height} tall, i.e. {feet} feet and {inches} inches.")
