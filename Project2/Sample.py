import sys
import platform
import datetime


print("Python Version:")
print(sys.version)
print(platform.python_version())
print(platform.python_version_tuple())

print("Version info:")
print(sys.version_info)

print(25+5)

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are!

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \n Twinkle, twinkle, little star,\n\tHow I wonder what you are!")

time= datetime.datetime.now()
print(time.strftime("%d-%m-%y %H:%M:%S"))