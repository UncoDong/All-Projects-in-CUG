import pytest
import json
from utils import *
import numpy as np
json_file = open("compare_file1.json",'r',encoding='gbk') 
a = json.load(json_file)
# 读取数据
testname_list = []
for i in range(len(a)):
    testname_list.append('test{0}'.format(i))


# 进行测试
@pytest.mark.parametrize('test_name', testname_list)
def test_compare(test_name):
    data = np.array(a[test_name]['music_data'])
    unit_rate = float(a[test_name]['unit_rate'])
    assert music2note1(data,unit_rate) == music2note2(data,unit_rate)
