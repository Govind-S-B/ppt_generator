from ppt_data_gen import slide_data_gen
from ppt_gen import ppt_gen

data = slide_data_gen("Creativity in Engineering")

print(data)

ppt_gen(data)
