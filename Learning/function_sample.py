# x = 4
def double(x): # あああああ
    return x * 2

def apply_to_one(f):
    return f(3) # https://qiita.com/yoichi22/items/35c692e8af805411927b

my_double = double 
x = apply_to_one(my_double) # 2
print(x)

y = apply_to_one(lambda x: x * 4) 
print(y)

def my_print(message = "my default messages"):
    print(message)
my_print("hello")
my_print()

def subtract(a=0,b=0):
    return a - b
print(subtract(10, 5))
print(subtract(0, 5))
print(subtract(b = 5))

single_quoted_string = 'data science'
double_quoted_string = "data science"

print(single_quoted_string)
print(double_quoted_string)

tab_string = "\t" # タブ記号を表す
print(len(tab_string))  # 文字列の長さは１

not_tab_string = r"\t" # '\'と't'の２文字を表す
print(len(not_tab_string)) # 文字列の長さは2

multi_line_string = """
=================
最初の行
2行目
3行目
"""
print(multi_line_string)







