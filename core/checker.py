# 评估字符保留程度：通过调用 checker 模块，测试这些特殊字符在目标应用中的保留情况（是否被过滤、转义或完整保留）

from core.requester import requester
from core.utils import replaceValue,fillHoles
from core.config import xsschecker

from fuzzywuzzy import fuzz
import copy
import re

def checker(url,params,GET,payload,positions):
    checkString = 'wuhu' + payload + 'lahu'
    response = requester(url,replaceValue(params,xsschecker,checkString,copy.deepcopy),GET).text.lower()

    reflectedPositions = []
    for match in re.finditer('wuhu',response):
        reflectedPositions.append(match.start())

    filledPositions = fillHoles(positions,reflectedPositions) # 将两个数字列表按逻辑合并，填补位置差异，生成一个按升序排列的新列表
    # original = [10, 20, 30]（预期反射位置）
    # new = [10, 18, 32]（实际检测到的位置）

    num = 0
    efficiencies = []
    for position in filledPositions:
        allEfficiencies = []
        try: # 这里是计算实际这个时候返回包中的相似度
            reflected = response[reflectedPositions[num]:reflectedPositions[num]+len(checkString)]
            efficiency = fuzz.partial_ratio(reflected,checkString.lower()) # 计算相似度（效率值）
            allEfficiencies.append(efficiency)
        except IndexError:
            pass

        if position: # 这里是从预期位置提取字符串计算相似度
            reflected = response[position:position+len(checkString)]

            efficiency = fuzz.partial_ratio(reflected, checkString) # 具体是检测单引号 / 双引号等特殊字符是否被反斜杠转义
            if reflected[:-2] == ('\\%s' % checkString.replace('wuhu', '').replace('lahu', '')):
                efficiency = 90
            allEfficiencies.append(efficiency)
            efficiencies.append(max(allEfficiencies)) # 最后在这两个之间去一个大一点的
        else:
            efficiencies.append(0)
        num += 1
    return list(filter(None, efficiencies)) # 过滤掉 0 ，返回有效的列表





