text = """# ifconfig -a | egrep 'inet|inet6'
   inet addr:69.89.31.226
   inet6 989.359.786.346 addr: FE80:0000:0000:0000:0202:B3FF:FE1E:8329 """
import re
#ipv4_ipv6 = re.compile("(?:\d{1,3}\.){3}\d{1,3}|(?:[0-9A-F]{4}:){7}[0-9A-F]{4}")
ipv4_ipv6 = re.findall("(?:\d{1,3}\.){3}\d{1,3}", text)
#ipv4_ipv6 = re.findall("(?:[0-9A-F]{4}:){7}[0-9A-F]{4}", text)
print(ipv4_ipv6)

x = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
