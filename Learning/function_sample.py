# coding: UTF-8

# x = 4
def double(x): # double function
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

tab_string = "\t" # tab記号を表す
print(len(tab_string))  # 文字列の長さは１

not_tab_string = r"\t" # '\'と't'の2文字を表す
print(len(not_tab_string)) # 文字列の長さは2

multi_line_string = """
=================
最初の行
2番めの行
3番めの行
"""
print(multi_line_string)

"""
Pythonでは、エラーが発生していなくてもコードを明快にするために
例外を使うことがある。
"""

try:
    print(0/0)
except ZeroDivisionError:
    print("cannnot divide by zero")

# リスト

integer_list = [1,2,3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, [] ]

list_length = len(integer_list)
list_sum = sum(integer_list)
print(list_length, list_sum)

# n番目の要素の値を取り出したり、値を設定するには角カッコを使います。

x = list(range(10)) # Python3では、リスト型は以下のように書く　http://blog.tstylestudio.com/2017/04/04/python2%E3%81%A83%E3%81%A7range%E3%82%92%E4%BD%BF%E3%81%86%E6%99%82%E3%81%AE%E9%81%95%E3%81%84%E3%81%A8%E3%80%81typeerror%E3%81%AE%E6%99%82/
# x = range(10) 
# Python2では、このように書く
zero = x[0]
one = x[1]
nine = x[-1] # Pythonでは、最後の要素を表すので9
eight = x[-2] # Pythonには、最後の1つ前の要素を表すので、8
x[0] = -1 # without first and last [-1,1,2,･･･,9]
print(x[0])

# 繝ｪ繧ｹ繝医・繧ｹ繝ｩ繧､繧ｹ(蠢・ｦ・Κ蛻・・縺ｿ蜃ｺ縺励◆繧ゅ・)

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

print(first_three)
print(three_to_end)
print(one_to_four)
print(last_three)
print(without_first_and_last)
print(copy_of_x)

# in演算子を使って、リストに要素が含まれることを調べる
1 in [1, 2, 3] #True
0 in [1, 2, 3] #False

# listの連結
x = [1,2,3]
x.extend([4, 5, 6])
print(x)

# listの変更をしたくない場合はlistの加算を行う
x = [1,2,3]
y = x + [4,5,6]
print(y)

# 要素の追加は頻繁に行われる
x = [1,2,3]
x.append(0) # [1,2,3,0]
y = x[-1] # 0
z = len(x) # 4

# list展開
x, y = [1, 2] # x = 1, y = 2
# 不要な値には、アンダースコアを割り当てたりする
_, y = [1, 2] # y = 2, _ は無視

"""
・タプル リストに似ているが、要素が変更できない
・要素を変更すること以外にリストに対して可能な操作は、タプルに対しても可能
・リストには[]角カッコを使いますが、
・タプルは()丸括弧またカッコを使わない方法で示す
"""

my_list = [1, 2] #list
my_tuple = (1, 2) # tuple(value_lock)
other_tuple = 3, 4
my_list[1] = 3 
print(my_list) # [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("タプルは変更できない")

def sum_and_product(x, y):
    return(x + y),(x * y)
sp = sum_and_product(2,3)
s, p = sum_and_product(5,10)
print(sp , s, p) # (5, 6) 15 50

# タプル(及びリストには)、多重割当が可能
x, y = 1, 2
x, y = y, x
print(x,y) # Python的な値の交換。Ｙ = 2, y = 1

# 辞書型;Key Value型の構造を持つ、キーに対する値を即座に取り出せる
empty_dict = {} # Python的
empty_dict2 = dict() # ややPython的
grades = {"joel" : 80 , "Tim" : 95} # 辞書のリテラル表現
#[]を使ってキーに対する値を取りだせる
joels_grade = grades["joel"] 
print(joels_grade)

# 辞書に存在しないキーを指定した場合、KeyErrorになる。
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)
no_ones_grade = grades.get("No One")

grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)

# dictionary is very useful and simple for representing data structure.
tweet = {
	"user" : "joelgrus",
	"text" : "Data Science is Awesome",
	"retweet_count" : 100,
	"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
	}
# dictionary can search All elements.
tweet_keys = tweet.keys() # キーのリスト
tweet_values = tweet.values() # value list
tweet_items = tweet.items() # tuple(key,value) list

"user" in tweet_keys #　"user" is 
"user" in tweet # Python的な手法であり、高速な辞書に格納される
"joelgrus" in tweet_values # 
"""
 辞書のキーは変更不能なオブジェクトでなければならない
 具体的にいうと、リストはキーとして使う事が出来ない。
 キーの値として複数組み合わせる必要が有るなら、タプルを使うか文字列としての表現を検討しなければならない
"""

# defaultdict class
# 以下の３つはスマートな方法ではない、
# 単語の出現数を数える
document = """Here's all the code and examples from my book Data Science from Scratch. The code directory contains Python 2.7 versions, and the code-python3 direction contains the Python 3 equivalents. (I tested them in 3.5, but they should work in any 3.x.) 
Each can be imported as a module, for example (after you cd into the /code directory):"""

#1 すでに登録されているなら１を加え、登録されていないなら１として登録
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

#2 登録していないキーにアクセスした際の例外を処理する方法
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

#3 キーが登録されていない場合でもエラーとならないgetメソッドを使う方法
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

# defaultdict 
 
from collections import defaultdict
    
    
