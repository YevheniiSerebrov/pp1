x=0
y=-9
if x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the 1st quadrant")
elif x > 0 and y < 0:
    print(f"Point P({x},{y}) is in the 2nd quadrant")
elif x <0 and y < 0:
    print(f"Point P({x},{y}) is in the 3rd quadrant")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the 4th quadrant")
elif x == 0 and y == 0:
    print(f"Point P({x},{y}) is in the 0 point")
elif x == 0 and y !=0:
    print(f"Point P({x},{y}) is on axis y")
elif y == 0 and x !=0:
    print(f"Point P({x},{y}) is on axis x")