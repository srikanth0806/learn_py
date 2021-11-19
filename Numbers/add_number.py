import logging

file = r"C:\Users\sRIKANTH\Desktop\logs\sum.log"
format = "%(asctime)s - %(levelname)s :: %(message)s"

logging.basicConfig(filename=file, format=format, level=logging.INFO)

logging.debug("program begines")
num1 = int(input("enter num1: \n"))
logging.info("user enter  a number %d" %num1)
num2 = int(input("enter num2: "))
logging.info("user enter  a number %d" %num2)
sum = num1+num2

logging.debug("user total sum  a number %d" %sum)
logging.debug("execution completed")
