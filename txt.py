test = open('test1.txt', 'w')
test.write("Hola mundo!!\n")
test.close()

test = open('test1.txt', 'a')
test.write("Hola mundo de nuevo!!")
test.close()