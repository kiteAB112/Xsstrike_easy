import re

from core.config import xsschecker

def htmlParser(response):
    response = response.text
    reflections_num = response.count(xsschecker)
    position_and_context = {}
    environment_details= {}
    clean_response = re.sub(r'<!--[.\s\S]*?-->', '', response) # 移除注释

    if len(position_and_context) < reflections_num: # 这里因为测试的 xss-labs 第一关是在 html 上下文中，直接先写一个这个
        html_context = re.finditer(xsschecker,clean_response)
        for occurence in html_context:
            thisPosition = occurence.start()
            if thisPosition not in position_and_context:
                position_and_context[occurence.start()] = 'html'
                environment_details[thisPosition] = {}
                environment_details[thisPosition]['details'] = {}

    database = {}
    for i in sorted(position_and_context):
        database[i] = {}
        database[i]['position'] = i
        database[i]['context'] = position_and_context[i]
        database[i]['details'] = environment_details[i]['details']

    # print(database)
    # {316: {'position': 316, 'context': 'html', 'details': {}}}
    return database





database = {
    100:{
        'position' :100,
        'context' :'attribute',
        'details' :{
            'tag' : 'h2',
            'type' : ' ',
            'value' : 'wuhulahu'
        }

    }
}