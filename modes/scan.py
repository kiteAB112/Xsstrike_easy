from urllib.parse import urlparse
import sys
import os
import copy

from core.requester import requester
from core.utils import getParams,getUrl
from core.config import xsschecker
from core.htmlParser import htmlParser
from core.filterChecker import filterChecker
from core.generator import generator
from core.checker import checker

# import core.config  
# from core.log import setup_logger

# logger = setup_logger(__name__)

def scan(target,paramData):
    GET,POST = (False,True) if paramData else (True,False)
    # # If the user hasn't supplied the root url with http(s),we will handle it
    # if not target.startswith('http'):
    #     try:
    #         response = requester('http://'+target)
    #     except:
    #         target = 'https://' + target

    # logger.debug(f"Scanning {target}")

    print('Scan target {}'.format(target))

    response = requester(target,{},GET) # 所以这里的 rep 原来是为了检查 dom 才操作的吗,所以这里的 data 参数会是空的啊，因为下面的 response = requester(url,paramsCopy,GET) 这部分要一个一个测试
    # print(response.text)
    # 这里原版是写的先检查 DOM 型的 XSS 这里就直接操作 反射型了，后面写完符合 xss-labs 之后再接着完善

    host = urlparse(target).netloc # Extract host out of the url
    print('Host to scan: {}'.format(host))
    url = getUrl(target,GET)
    params = getParams(target,paramData,GET)

    if not params:
        print('No parameters to test.')
        quit()
    
    # WAF = wafDetector()


    for paramName in params.keys():
        # print(paramName)
        paramsCopy = copy.deepcopy(params)
        paramsCopy[paramName] = xsschecker # 逐个参数进行测试

        response = requester(url,paramsCopy,GET)

        # print(response.text)
        # 开始检查返回包里面能不能找到我们的测试 payload -- wuhulahu
        occurences = htmlParser(response) # {316: {'position': 316, 'context': 'html', 'details': {}}}
        positions = occurences.keys()

        if not occurences:
            pass
        else:
            print('Reflaction found %i' % len(occurences))
        print('Analysing reflections')

        efficiencies = filterChecker(url,paramsCopy,GET,occurences) # 给每个位置可能会需要加的 < > ' 之类的分别计算得分

        print('Scan efficiencies: {}'.format(efficiencies)) # Scan efficiencies: {316: {'position': 316, 'context': 'html', 'details': {}, 'score': {'<': 100, '>': 100}}}

        print('Generating payloads......................................')

        vectors = generator(occurences,response.text)

        total = 0
        for v in vectors.values():
            total +=len(v)
        if total == 0:
            print('No vector were crafted')
            continue
        print('Payload generated: %i' % total)

        for confidence,vects in vectors.items():
            progress = 0
            for vect in vects:
                loggerVector = vect
                progress += 1  # 累计已测试的 payload 数量
                print('Progress: %i/%i\r' % (progress, total))  # 实时显示进度（如 "Progress: 5/20"）
                if not GET:
                    pass
                efficiencies = checker(url,paramsCopy,GET,vect,positions) # positions = occurences.keys() , vect = payload，也就是测试当前payload在每个位置的效率
                if not efficiencies:
                    for i in range(len(occurences)):
                        efficiencies.append(0)

                bestEfficiency= max(efficiencies) # 这个 payload 在这个参数测试后，在每个反射位置最后得到的最高分
                if bestEfficiency == 100 or (vect[0] == '\\' and bestEfficiency >= 95):
                    print('-------------------------------------------------------')
                    print('Payload: %s' % loggerVector)
                    print('Efficiency: %i' % bestEfficiency)
                    print('Confidience: %i ' % confidence)

                    choice = input(
                        '%s Would you like to continue scanning [y/N] ').lower
                    if choice != 'y':
                        quit()
                elif bestEfficiency > 90:
                    print('Payload: %s' % loggerVector)
                    print('Efficiency: %i' % bestEfficiency)
                    print('Confidience: %i ' % confidence)



















    
    host = urlparse(target).netloc # 
    return 111




# target = "http://localhost:82/vul/xss/xss_reflected_get.php?message=%3Cscript%3Ealert(%22caker%22)%3C%2fscript%3E&submit=submit"
# target = "http://xss-labs/level1.php?name=test"
# host = urlparse(target).netloc

# print(host)



    











