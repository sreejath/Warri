x="There are %d kinds of people in the world." % 10
binary = "binary"
dont = "don't"
y="Those who understand %s and those who %s." % (binary,dont)
print(x,"\n",y)
print("I said %r" % x)
crowfeet = 'I also said %r'
print(crowfeet % y)
hilarious = True
print("%r" % hilarious)
left = "This is the left half of a string..."
right = "and this is the right side"
print(left+right+"%r" % 5)
print(left+right+"%d" % 5)
print(left+right+"%c" % 5)
print(left+right+"%s" % 5)