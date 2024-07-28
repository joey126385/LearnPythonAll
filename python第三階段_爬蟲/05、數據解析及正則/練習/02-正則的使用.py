import  re
str1 = '<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" /><link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索"  title="百度搜索2" />'
# 貪婪模式
result01=re.findall('title=".*"',str1)
print(f"01貪婪模式\t {result01} \t 長度 {len(result01)}")
result02=re.findall("title='.*'",str1)
print(f"02貪婪模式\t {result02} \t 長度 {len(result02)}")
# 非貪婪模式
result03=re.findall('title=".*?"',str1)     # 會顯使 title全部值
print(f"03非貪婪模式\t {result03} \t 長度 {len(result03)}")
result04=re.findall('title="(.*?)"',str1)   # () 裡面的值
print(f"04非貪婪模式\t {result04} \t 長度 {len(result04)}")

str2= "aasdhj啊。是a123+多久啊开始123啊但是扩a大阿萨的b牛仔裤超牛卡21312"
# 中文的Unicode的编码范围主要在[\u4e00-\u9fa5]
result=re.findall("[\u4e00-\u9fa5]",str2)
print(result)# 每個字都會分開
print("".join(result))# 拼接裡面的字串 然後變成新的字串

