import pytest
import json
from utils import *
json_file = open("note_file.json",'r',encoding='gbk')
json_file2 = open("note_file2.json",'r',encoding='gbk')  
a = json.load(json_file)
b = json.load(json_file2)
# 读取数据
testname_list = []
for i in range(len(a)):
    testname_list.append('test{0}'.format(i))


# 进行测试
@pytest.mark.parametrize('test_name', testname_list)
def test_str2note(test_name):    
    print(a[test_name])

testname_list2 = []
for i in range(len(b)):
    testname_list2.append('test{0}'.format(i))
# 进行测试2
@pytest.mark.parametrize('test_name', testname_list)
def test_str2note2(test_name):
    assert b[test_name]['note_ans'] == str2tone(b[test_name]['note_str'])
    print(b[test_name])
