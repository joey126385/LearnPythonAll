str1 = ['\n                            导演: 李·昂克里奇 Lee Unkrich / 阿德里安·莫利纳 Adrian Molina\xa0\xa0\xa0主演: ...',
        '\n                            2017\xa0/\xa0美国\xa0/\xa0喜剧 动画 奇幻 音乐\n                        ']
# 现在是下面的三个字段 年份 国家 标签 数据没问题   主演和导演数据有点问题 可以先把下面的三个字段拿出来
#
print(''.join(str1).strip().replace(' ','').replace('\xa0', '') .split('\n'))