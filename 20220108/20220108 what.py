import turtle  
#for i in range(5):    
   # for t in range(4):
    #    turtle.forward(100)
    #    turtle.right(90)
    #turtle.left(90)
    #for e in range(4):    
    #    turtle.backward(100)
    #    turtle.left(90)
    #turtle.right(90)
#turtle.done()

# turtle.penup()
# turtle.color('red')
# turtle.shape('turtle')
# for t in range(0,501,3):
#     turtle.stamp()
#     turtle.right(30)
#     turtle.forward(t)
# turtle.done()

# for y in range(5):
#     turtle.stamp()
#     turtle.forward(100)
#     turtle.right(144)
    
# turtle.done() 

x = 0
while x != "exit":
    x = input("請輸入編號:")
    if x == '1':
        print('蘋果')
        continue
    elif x == '2':
        print('柳橙')
        continue
    elif x == '3':
        print('葡萄')
        continue
    else:
        print('not found 404')
    