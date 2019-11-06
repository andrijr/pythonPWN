import os
import time
print(os.getcwd())
print(os.listdir('.'))
print(os.listdir('/')) # pokazanie katalogu domowego

print(time.ctime(os.path.getctime("zwierzeta.txt")))