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

tab_string = "\t" # tab險伜捷繧定｡ｨ縺・
print(len(tab_string))  # 譁・ｭ怜・縺ｮ髟ｷ縺輔・・・

not_tab_string = r"\t" # '\'縺ｨ't'縺ｮ2譁・ｭ励ｒ陦ｨ縺・
print(len(not_tab_string)) # 譁・ｭ怜・縺ｮ髟ｷ縺輔・2

multi_line_string = """
=================
譛蛻昴・陦・
2逡ｪ繧√・陦・
3逡ｪ繧√・陦・
"""
print(multi_line_string)

"""
Python縺ｧ縺ｯ縲√お繝ｩ繝ｼ縺檎匱逕溘＠縺ｦ縺・↑縺上※繧ゅさ繝ｼ繝峨ｒ譏主ｿｫ縺ｫ縺吶ｋ縺溘ａ縺ｫ
萓句､悶ｒ菴ｿ縺・％縺ｨ縺後≠繧九・
"""

try:
    print(0/0)
except ZeroDivisionError:
    print("cannnot divide by zero")

# 繝ｪ繧ｹ繝・

integer_list = [1,2,3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, [] ]

list_length = len(integer_list)
list_sum = sum(integer_list)
print(list_length, list_sum)

# n逡ｪ逶ｮ縺ｮ隕∫ｴ縺ｮ蛟､繧貞叙繧雁・縺励◆繧翫∝､繧定ｨｭ螳壹☆繧九↓縺ｯ隗偵き繝・さ繧剃ｽｿ縺・∪縺吶・

x = list(range(10)) # Python3縺ｧ縺ｯ縲√Μ繧ｹ繝亥梛縺ｯ莉･荳九・繧医≧縺ｫ譖ｸ縺上http://blog.tstylestudio.com/2017/04/04/python2%E3%81%A83%E3%81%A7range%E3%82%92%E4%BD%BF%E3%81%86%E6%99%82%E3%81%AE%E9%81%95%E3%81%84%E3%81%A8%E3%80%81typeerror%E3%81%AE%E6%99%82/
# ﾂx = range(10) 
# Python2縺ｧ縺ｯ縲√％縺ｮ繧医≧縺ｫ譖ｸ縺・
zero = x[0]
one = x[1]
nine = x[-1] # Python縺ｧ縺ｯ縲∵怙蠕後・隕∫ｴ繧定｡ｨ縺吶・縺ｧ9
eight = x[-2] # Python縺ｫ縺ｯ縲∵怙蠕後・1縺､蜑阪・隕∫ｴ繧定｡ｨ縺吶・縺ｧ縲・
x[0] = -1 # without first and last [-1,1,2,・･・･・･,9]
print(x[0])

# 郢晢ｽｪ郢ｧ・ｹ郢晏現繝ｻ郢ｧ・ｹ郢晢ｽｩ郢ｧ・､郢ｧ・ｹ(陟｢繝ｻ・ｦ繝ｻﾎ夊崕繝ｻ繝ｻ邵ｺ・ｿ陷・ｽｺ邵ｺ蜉ｱ笳・ｹｧ繧・・)

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

# in貍皮ｮ怜ｭ舌ｒ菴ｿ縺｣縺ｦ縲√Μ繧ｹ繝医↓隕∫ｴ縺悟性縺ｾ繧後ｋ縺薙→繧定ｪｿ縺ｹ繧・
1 in [1, 2, 3] #True
0 in [1, 2, 3] #False

# list縺ｮ騾｣邨・
x = [1,2,3]
x.extend([4, 5, 6])
print(x)

# list縺ｮ螟画峩繧偵＠縺溘￥縺ｪ縺・ｴ蜷医・list縺ｮ蜉邂励ｒ陦後≧
x = [1,2,3]
y = x + [4,5,6]
print(y)

# 隕∫ｴ縺ｮ霑ｽ蜉縺ｯ鬆ｻ郢√↓陦後ｏ繧後ｋ
x = [1,2,3]
x.append(0) # [1,2,3,0]
y = x[-1] # 0
z = len(x) # 4

# list螻暮幕
x, y = [1, 2] # x = 1, y = 2
# 荳崎ｦ√↑蛟､縺ｫ縺ｯ縲√い繝ｳ繝繝ｼ繧ｹ繧ｳ繧｢繧貞牡繧雁ｽ薙※縺溘ｊ縺吶ｋ
_, y = [1, 2] # y = 2, _ 縺ｯ辟｡隕・

"""
繝ｻ繧ｿ繝励Ν 繝ｪ繧ｹ繝医↓莨ｼ縺ｦ縺・ｋ縺後∬ｦ∫ｴ縺悟､画峩縺ｧ縺阪↑縺・
繝ｻ隕∫ｴ繧貞､画峩縺吶ｋ縺薙→莉･螟悶↓繝ｪ繧ｹ繝医↓蟇ｾ縺励※蜿ｯ閭ｽ縺ｪ謫堺ｽ懊・縲√ち繝励Ν縺ｫ蟇ｾ縺励※繧ょ庄閭ｽ
繝ｻ繝ｪ繧ｹ繝医↓縺ｯ[]隗偵き繝・さ繧剃ｽｿ縺・∪縺吶′縲・
繝ｻ繧ｿ繝励Ν縺ｯ()荳ｸ諡ｬ蠑ｧ縺ｾ縺溘き繝・さ繧剃ｽｿ繧上↑縺・婿豕輔〒遉ｺ縺・
"""

my_list = [1, 2] #list
my_tuple = (1, 2) # tuple(value_lock)
other_tuple = 3, 4
my_list[1] = 3 
print(my_list) # [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("繧ｿ繝励Ν縺ｯ螟画峩縺ｧ縺阪↑縺・)

def sum_and_product(x, y):
    return(x + y),(x * y)
sp = sum_and_product(2,3)
s, p = sum_and_product(5,10)
print(sp , s, p) # (5, 6) 15 50

# 繧ｿ繝励Ν(蜿翫・繝ｪ繧ｹ繝医↓縺ｯ)縲∝､夐㍾蜑ｲ蠖薙′蜿ｯ閭ｽ
x, y = 1, 2
x, y = y, x
print(x,y) # Python逧・↑蛟､縺ｮ莠､謠帙ゑｼｹ = 2, y = 1

# 霎樊嶌蝙・Key Value蝙九・讒矩繧呈戟縺､縲√く繝ｼ縺ｫ蟇ｾ縺吶ｋ蛟､繧貞叉蠎ｧ縺ｫ蜿悶ｊ蜃ｺ縺帙ｋ
empty_dict = {} # Python逧・
empty_dict2 = dict() # 繧・ｄPython逧・
grades = {"joel" : 80 , "Tim" : 95} # 霎樊嶌縺ｮ繝ｪ繝・Λ繝ｫ陦ｨ迴ｾ
#[]繧剃ｽｿ縺｣縺ｦ繧ｭ繝ｼ縺ｫ蟇ｾ縺吶ｋ蛟､繧貞叙繧翫□縺帙ｋ
joels_grade = grades["joel"] 
print(joels_grade)

# 霎樊嶌縺ｫ蟄伜惠縺励↑縺・く繝ｼ繧呈欠螳壹＠縺溷ｴ蜷医゜eyError縺ｫ縺ｪ繧九・
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
tweet_keys = tweet.keys() # 繧ｭ繝ｼ縺ｮ繝ｪ繧ｹ繝・
tweet_values = tweet.values() # value list
tweet_items = tweet.items() # tuple(key,value) list

"user" in tweet_keys #縲"user" is 
"user" in tweet # Python逧・↑謇区ｳ輔〒縺ゅｊ縲・ｫ倬溘↑霎樊嶌縺ｫ譬ｼ邏阪＆繧後ｋ
"joelgrus" in tweet_values # 
"joelgrus" in tweet_values # True
"""
 霎樊嶌縺ｮ繧ｭ繝ｼ縺ｯ螟画峩荳崎・縺ｪ繧ｪ繝悶ず繧ｧ繧ｯ繝医〒縺ｪ縺代ｌ縺ｰ縺ｪ繧峨↑縺・
 蜈ｷ菴鍋噪縺ｫ縺・≧縺ｨ縲√Μ繧ｹ繝医・繧ｭ繝ｼ縺ｨ縺励※菴ｿ縺・ｺ九′蜃ｺ譚･縺ｪ縺・・
 繧ｭ繝ｼ縺ｮ蛟､縺ｨ縺励※隍・焚邨・∩蜷医ｏ縺帙ｋ蠢・ｦ√′譛峨ｋ縺ｪ繧峨√ち繝励Ν繧剃ｽｿ縺・°譁・ｭ怜・縺ｨ縺励※縺ｮ陦ｨ迴ｾ繧呈､懆ｨ弱＠縺ｪ縺代ｌ縺ｰ縺ｪ繧峨↑縺・
"""

# defaultdict class
# 莉･荳九・・薙▽縺ｯ繧ｹ繝槭・繝医↑譁ｹ豕輔〒縺ｯ縺ｪ縺・・
# 蜊倩ｪ槭・蜃ｺ迴ｾ謨ｰ繧呈焚縺医ｋ
document = """Here's all the code and examples from my book Data Science from Scratch. The code directory contains Python 2.7 versions, and the code-python3 direction contains the Python 3 equivalents. (I tested them in 3.5, but they should work in any 3.x.) 
Each can be imported as a module, for example (after you cd into the /code directory):"""

#1 縺吶〒縺ｫ逋ｻ骭ｲ縺輔ｌ縺ｦ縺・ｋ縺ｪ繧会ｼ代ｒ蜉縺医∫匳骭ｲ縺輔ｌ縺ｦ縺・↑縺・↑繧会ｼ代→縺励※逋ｻ骭ｲ
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

#2 逋ｻ骭ｲ縺励※縺・↑縺・く繝ｼ縺ｫ繧｢繧ｯ繧ｻ繧ｹ縺励◆髫帙・萓句､悶ｒ蜃ｦ逅・☆繧区婿豕・
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

#3 繧ｭ繝ｼ縺檎匳骭ｲ縺輔ｌ縺ｦ縺・↑縺・ｴ蜷医〒繧ゅお繝ｩ繝ｼ縺ｨ縺ｪ繧峨↑縺・et繝｡繧ｽ繝・ラ繧剃ｽｿ縺・婿豕・
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

# defaultdict 
 
from collections import defaultdict
    
word_counts = defaultdict(int) # int()縺ｯ0繧定ｿ斐☆
for word in document:
    word_counts[word] += 1
print(word_counts)

dd_list = defaultdict(list) #list()縺ｯ遨ｺ縺ｮ繝ｪ繧ｹ繝医ｒ霑斐☆
dd_list[2].append(1) #dd_list縺ｯ縲＋2:[1]}繧貞性繧
print(dd_list) 

dd_dict = defaultdict(dict) # dict()縺ｯ遨ｺ縺ｮ霎樊嶌繧定ｿ斐☆
dd_dict["Joel"]["City"] = "Seattle" # dd_dict縲縺ｯ,{"Joel" : {"City":"Seattle"}}繧貞性繧
print(dd_dict)

dd_pair = defaultdict(lambda: [0,0])
dd_pair[2][1] = 1 # dd_pair縺ｯ縲＋2 : [0,1]}繧貞性繧
print(dd_pair)
# 縺薙ｌ繧峨・譁ｹ豕輔・縲∽ｽ輔ｉ縺九・繧ｭ繝ｼ縺斐→縺ｮ蛟､繧貞庶髮・☆繧矩圀縺ｫ縲√◎縺ｮ繧ｭ繝ｼ縺後☆縺ｧ縺ｫ霎樊嶌縺ｫ逋ｻ骭ｲ縺輔ｌ縺ｦ縺・ｋ縺九ｒ驛ｽ蠎ｦ遒ｺ隱阪＠縺溘￥縺ｪ縺・ｴ蜷医↓菴ｿ逕ｨ縺輔ｌ繧・

# Counter繧ｯ繝ｩ繧ｹ
# Counter縺ｯ縲・邯壹″縺ｮ蛟､繧壇efaultdict(init)
from collections import Counter
c = Counter([0, 1, 2, 0,3 ]) # c 縺ｯ {0:2, 1:1, 2:1, 3:1}縺ｨ縺ｪ繧九・
word_counts = Counter(document) # 蜊倩ｪ槭・蜃ｺ迴ｾ謨ｰ繧呈焚縺医ｋ蝠城｡・
print(c)
print(word_counts)

# Counter繧ｪ繝悶ず繧ｧ繧ｯ繝医↓縺ｯ縲∝・迴ｾ謨ｰ縺ｮ螟壹＞鬆・↓隕∫ｴ繧定ｿ斐☆most_common繝｡繧ｽ繝・ラ縺檎畑諢上＆繧後※縺・ｋ縲・
# 蜃ｺ迴ｾ謨ｰ縺ｮ螟壹＞鬆・↓繝吶せ繝・0繧定｡ｨ遉ｺ縺吶ｋ
for word, count in word_counts.most_common(10):
    print (word, count)

# 髮・粋
"""
髮・粋繧剃ｽｿ縺・ｸｻ縺ｪ逅・罰
・托ｼ朱撼蟶ｸ縺ｫ鬮倬溘↓蜍穂ｽ懊☆繧狗せ(螟ｧ驥上・繝・・繧ｿ縺ｮ荳ｭ縺九ｉ隕∫ｴ縺悟性縺ｾ繧後ｋ蠢・ｦ√′縺ゅｋ縺ｪ繧峨・寔蜷医・譛繧る←縺励◆繝・・繧ｿ讒矩)
・抵ｼ朱㍾隍・・縺ｪ縺・寔縺ｾ繧翫′蠕励ｉ繧後ｋ
"""
s = set()
s.add(1) # s 縺ｯ{1}
s.add(2) # {1, 2}縺ｨ縺ｪ繧・
s.add(2) # 縺薙％縺ｧ繧ゅ∪縺{1, 2}縺ｮ縺ｾ縺ｾ
x = len(s) # x = 2
y = 2 in s # y = True
z = 3 in s # z = False

# ・代▽逶ｮ縺ｮ逅・罰
stopwords_list = ["a", "an", "at"] + list("hundreds_of_other_words") + ["yet", "you"] #Python3縺縺ｨ縲∝梛謖・ｮ壹ｒ縺励▲縺九ｊ
"zip" in stopwords_list # False縺ｨ縺ｪ繧九ゅ☆縺ｹ縺ｦ縺ｮ隕∫ｴ縺ｧ繝√ぉ繝・け縺輔ｌ繧九・
stopwords_set = set(stopwords_list)
"zip" in stopwords_set # "zip"縺悟性縺ｾ繧後ｋ縺句凄縺九・鬮倬溘↓繝√ぉ繝・け蜿ｯ閭ｽ
print(stopwords_list)
print(stopwords_set)
# ・偵▽逶ｮ縺ｮ逅・罰
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list)
num_distinct_items = len(item_set)
distinct_item_list = list(item_set)
print(item_list)
print(num_items,",隕∫ｴ謨ｰ縺ｯ・・)
print(item_set,",髮・粋縺吶ｋ縺ｨ驥崎､・′蜿悶ｊ髯､縺九ｌ縲＋1, 2, 3}縺ｨ縺ｪ繧・)
print(num_distinct_items, ",隕∫ｴ謨ｰ縺ｯ・・)
print(distinct_item_list, ",驥崎､・・縺ｪ縺・Μ繧ｹ繝・1, 2, 3]")

# 螳溯｡碁・宛蠕｡
if 1 > 2:
    message = "繧ゅ＠縲・ｼ代′・偵ｈ繧雁､ｧ縺阪＞縺ｨ縺励◆繧・
elif 1 > 3:
    message = "elif 縺ｯ窶抛lse if窶昴ｒ陦ｨ縺・
else:
    message = "縺吶∋縺ｦ縺ｮ譚｡莉ｶ縺ｫ蠖薙※縺ｯ縺ｾ繧峨↑縺代ｌ縺ｰ縲‘lse縺瑚ｩｲ蠖薙☆繧・縺ｪ縺上※繧ゅ＞縺・"
print(message) # "縺吶∋縺ｦ縺ｮ譚｡莉ｶ縺ｫ蠖薙※縺ｯ縺ｾ繧峨↑縺代ｌ縺ｰ縲‘lse縺瑚ｩｲ蠖薙☆繧・縺ｪ縺上※繧ゅ＞縺・"

# 1陦後〒if-then-else繧呈嶌縺・
x = 2
parity = "even" if x % 2 == 0 else "odd"
print(parity)

# While繝ｫ繝ｼ繝・
x = 0
while x < 10:
    print(x)
    x += 1
# for , in縺ｮ邨・∩蜷医ｏ縺帙′繝昴ヴ繝･繝ｩ繝ｼ

for x in range(10):
    print(x, " 縺ｯ縲・0繧医ｊ蟆上＆縺・)
"""
0  縺ｯ縲・0繧医ｊ蟆上＆縺・
1  縺ｯ縲・0繧医ｊ蟆上＆縺・
・･繝ｻ繝ｻ
9  縺ｯ縲・0繧医ｊ蟆上＆縺・
"""

# 繧医ｊ隍・尅縺ｪ蜃ｦ逅・↑繧峨…ontinue,break
for x in range(10):
    if x == 3:
        continue # 螳溯｡御ｸｭ縺ｮ繝ｫ繝ｼ繝励・蜈磯ｭ縺ｫ謌ｻ繧翫∝・逅・ｒ邯咏ｶ壹☆繧・
    if x == 5:
        break # 繝ｫ繝ｼ繝励ｒ閼ｱ蜃ｺ縺吶ｋ
    print(x) # 0,1,2,4

# True, False
one_is_less_than_two = 1 < 2 # 莉｣蜈･縺輔ｌ繧句､縺ｯTrue
true_equals_false = True == False # 莉｣蜈･縺輔ｌ繧句､縺ｯFalse

# 蛟､縺梧欠螳壹＆繧後※縺・↑縺・ｂ縺ｮ縺ｯ縲¨one縺ｧ陦ｨ縺吶ゆｻ悶・險隱槭〒縺ｯNull
x = None
print (x) == None #Python逧・〒縺ｯ縺ｪ縺・さ繝ｼ繝・True)
print (x) is None #Python逧・↑繧ｳ繝ｼ繝・True)

# False縺ｮ萓・
"""
繝ｻFalse
繝ｻNone
繝ｻ[]遨ｺ縺ｮ繝ｪ繧ｹ繝・
繝ｻ{}遨ｺ縺ｮ霎樊嶌
繝ｻ""
繝ｻset()
繝ｻ・・
繝ｻ0.0
"""

# False縺ｮ萓倶ｻ･螟悶・True縺ｨ縺励※謇ｱ繧上ｌ繧九√▽縺ｾ繧翫Μ繧ｹ繝医∬ｾ樊嶌縲∵枚蟄怜・縺ｪ縺ｩ縺後°繧峨〒縺ゅｋ縺句凄縺九ｒif繧剃ｽｿ縺｣縺ｦ邁｡蜊倥↓隱ｿ縺ｹ繧峨ｌ繧・
# pp32
def some_function_that_returns_a_string():
    s =  some_function_that_returns_a_string()
    if s:
        first_char = s and s[0]
    else:
        first_char = ""
print(s)

# all髢｢謨ｰ・医Μ繧ｹ繝医・隕∫ｴ蜈ｨ縺ｦ縺卦rue縺ｨ縺励※謇ｱ縺医ｋ蝣ｴ蜷医↓True繧定ｿ斐☆・・
# any髢｢謨ｰ・郁ｦ∫ｴ縺ｮ縺・★繧後°荳縺､縺卦rue縺ｪ繧峨・縲ゝrue繧定ｿ斐☆any髢｢謨ｰ・・
all([True, 1, { 3 }]) # True
all([True, 1, {}]) # {}縺ｯFalse縺ｨ隗｣驥医＆繧後ｋ縺ｮ縺ｧ縲∫ｵ先棡縺ｯFalse
any([True, 1, {}]) # True縺鯉ｼ代▽縺ゅｋ縺ｮ縺ｧ縲∫ｵ先棡縺ｯTrue
all([]) # 繝ｪ繧ｹ繝亥・縺ｫFalse縺ｨ隗｣驥医＆繧後ｋ隕∫ｴ縺後↑縺・・縺ｧ縲∫ｵ先棡縺ｯTrue
any([]) # 繝ｪ繧ｹ繝亥・縺ｫTrue縺ｨ隗｣驥医＆繧後ｋ隕∫ｴ縺後↑縺・・縺ｧ縲∫ｵ先棡縺ｯFalse