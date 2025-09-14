# 根据 htmlParser 解析出的反射上下文（如 HTML 标签内、属性值、脚本代码、注释等），
# 筛选出当前场景下生成 XSS payload 必需的特殊字符（如 <、>、引号、</script>、-> 等）

from core.checker import checker


def filterChecker(url,params,GET,occurences):
    positions = occurences.keys()
    sortedEfficiencies = {}

    environments = set(['<','>'])
    for i in range(len(positions)):
        sortedEfficiencies[i] = {}

    for i in occurences:
        occurences[i]['score'] = {}


    for environment in environments: # 这里就是在计算每一种 ' < > " "等等的分数，看哪些可能被过滤了
        if environment:
            efficiencies = checker(url,params,GET,environment,positions)
            efficiencies.extend([0] * (len(occurences) - len(efficiencies))) # 若某些反射位置未检测到该字符（导致 efficiencies 较短），则用 0 填充（表示该位置字符完全被过滤）
            for occurence, efficiency in zip(occurences, efficiencies):
                occurences[occurence]['score'][environment] = efficiency # 每个 occ 位置对应不同 < > 之类的得分

    return occurences