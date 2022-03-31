#write programe to find factorial of a given number by using a logging module
import logging
format = "%(asctime)s - %(levelname)s : %(pathname)s :: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=format, filename="my_log1.txt",
                    filemode="a")

logging.debug("finding the factorial of a number")
num = int(input("enter a number : "))
factorial = 1
if num < 0:
    logging.warning("must be positive")
elif num == 0:
    logging.info("factorial = 1")

else:
    for i in range(1, num+1):
        factorial = factorial * i

print(factorial)
logging.debug("the factorial value is %d", factorial)