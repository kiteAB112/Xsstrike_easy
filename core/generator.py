from core.config import xsschecker, badTags, fillings, eFillings, lFillings, jFillings, eventHandlers, tags, functions
from core.utils import genGen

# {316: {'position': 316, 'context': 'html', 'details': {}, 'score': {'<': 100, '>': 100}}}
def generator(occurences,response):
    index = 0
    vectors = {11: set(), 10: set(), 9: set(), 8: set(), 7: set(),
               6: set(), 5: set(), 4: set(), 3: set(), 2: set(), 1: set()}
    
    for i in occurences:
        context = occurences[i]['context']
        if context == 'html':
            lessBracketEfficiency = occurences[i]['score']['<']
            greatBracketEfficiency = occurences[i]['score']['>']
            ends = ['//']
            badTag = occurences[i]['details']['badTag'] if 'badTag' in occurences[i]['details'] else ''
            
            if greatBracketEfficiency == 100:
                ends.append('>') # 如果 < 保留下来，就需要在最后添加 > 来进行闭合
            if lessBracketEfficiency:
                payloads = genGen(fillings, eFillings, lFillings,eventHandlers, tags, functions, ends, badTag)
                for payload in payloads:
                    vectors[10].add(payload)
                    # print(payload)

        else:
            pass

        return vectors