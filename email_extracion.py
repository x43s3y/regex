import re

sentence = input()
pattern = r"\s(?P<user>[A-Za-z0-9]+[A-Za-z0-9\.\_\-]*)\@(?P<host>[A-Za-z]+[A-Za-z\-]*(\.[A-Za-z]+[A-Za-z\-]*)+)"
hosts = re.finditer(pattern, sentence)
for host in hosts:
    print(host.group())