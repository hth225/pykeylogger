import psutil
f = open("ps.txt", "w+")
file = psutil.test()
f.write(str(file))
f.close()