import re

post_code_pattern = re.compile('\d{2}-\d{3}')
email_pattern = re.compile('*\w{@}*')
date_pattern = re.compile('\d{2} \w{3} \d{3}')


with open("input.txt") as f:
    tekst = f.read()
    kody = post_code_pattern.findall(tekst)
    print(kody)
    data = date_pattern.findall(tekst)
    print(data)
    email = email_pattern.findall(tekst)
    print(data)
