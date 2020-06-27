import yaml

with open('./data_02.yml', 'r', encoding='utf-8')as f:
    data = yaml.safe_load(f)
    print('返回字典数据：', data)
    print('返回数据类型：', type(data))
