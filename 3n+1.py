from turtle import Turtle, mainloop

turtle = Turtle()
turtle.speed("fastest")
turtle.penup()

width, height = turtle.getscreen().screensize()
nums = [2]
last_num = 0

next = nums[-1] * 3 + 1
while next != 1:
    nums += [next]
    next = next / 2 if next % 2 == 0 else nums[-1] * 3 + 1
nums += [1]

for i, n in enumerate(nums):
    last_num = n
    max_num = max(nums)
    target = (-width + i * 10, -height + int(n) / (max_num / 300))

    turtle.goto(target)
    turtle.pendown()
    x, y = turtle.pos()

    turtle.penup()
    if nums[i-1]:
        previous = nums[i-1]
        turtle.goto(x, y + 5 if last_num > previous else y - 20)
    else:
        turtle.goto(x, y + 5)
    turtle.write(int(n), align="center")
    turtle.goto(target)
    turtle.pendown()
mainloop()
