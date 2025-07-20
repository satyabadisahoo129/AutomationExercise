import re

text='Rs 2000.40'
act_price=re.search(r'\d+\.\d+',text)
print(act_price.group())