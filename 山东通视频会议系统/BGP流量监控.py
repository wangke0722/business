import os
import re
from datetime import datetime


def read_files(directory_path, num_files):
    #获取目录下所有文件
    file_list = os.listdir(directory_path)
    #对获取到的文件根据目录进行根据文件创建时间进行排序
    sorted_files = sorted(file_list, key=lambda x: os.path.getctime(os.path.join(directory_path, x)), reverse=True)
    #根据文件列表获取最新的三个文件
    latest_files = sorted_files[:num_files]
    #创建空列表，用于存储最新的三条数据
    file_contents = []
    #遍历三个文件，读取文件内容，将内容添加到空列表内
    for file_name in latest_files:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'r') as file:
            file_content = file.read().strip()
            file_contents.append(file_content)
    return file_contents

def read_text(directory_path, num_files):
    # 获取目录下所有文件
    file_list = os.listdir(directory_path)
    # 对获取到的文件根据目录进行根据文件创建时间进行排序
    sorted_files = sorted(file_list, key=lambda x: os.path.getctime(os.path.join(directory_path, x)), reverse=True)
    # 根据文件列表获取最新的三个文件
    latest_files = [os.path.splitext(file)[0] for file in sorted_files][:num_files]
    return latest_files

def convert_to_datetime(time_strings):
    datetime_objects = []
    for time_str in time_strings:
        datetime_obj = datetime.strptime(time_str, '%Y%m%d%H%M%S')
        datetime_objects.append(datetime_obj)
    return datetime_objects

def convert_to_mb(lst):
    converted_lst = []
    rufuse_list = []
    for item in lst:
        # value = float(item[:-2])  # 提取数字部分并转换为浮点数
        # unit = item[-2:]  # 提取单位部分
        match = re.match(r"([\d.]+)\s*([a-zA-Z]+);(.+)", item)
        value = float(match.group(1))
        unit = match.group(2).lower()
        date_time_info = match.group(3).strip()
        if unit == 'b':
            value /= 1024 ** 2  # Convert bytes to MB
        elif unit == 'kb':
            value /= 1024  # Convert KB to MB
        elif unit == 'mb':
            pass  # The value is already in MB
        elif unit == 'gb':
            value *= 1024  # Convert GB to MB
        elif unit == 'tb':
            value *= 1024 ** 2  # Convert TB to MB
        converted_lst.append(str(value))  # 将转换后的值和单位拼接成字符串并添加到新列表中
        rufuse_list.append(date_time_info)
    return converted_lst,rufuse_list


in_directory1 = r"D:\出口地址\联通出口1\In"
out_directory1 = r"D:\出口地址\联通出口1\Out"
num_files_to_compare = 3

in_file_num1_key = read_files(in_directory1, num_files_to_compare)
in_file_num1 = convert_to_mb(in_file_num1_key)
#in_file_num1[0]样式['129.6', '129.6', '129.6']
#in_file_num1[1]样式['Monday, 4 September 2023 at 14:05', 'Monday, 4 September 2023 at 14:05', 'Monday, 4 September 2023 at 14:05']
out_file_num1_key = read_files(out_directory1, num_files_to_compare)
out_file_num1 = convert_to_mb(out_file_num1_key)

#读取文件名称定义为采集数据时间
files_name = read_text(in_directory1, num_files_to_compare)
datetime_objects = convert_to_datetime(files_name)
files_datetimes = [dt_obj.strftime('%Y-%m-%d %H:%M:%S') for dt_obj in datetime_objects]

string_set = set(in_file_num1[1])
value = (in_file_num1[1][0])

exceptions = []  # 用于存储异常

if time_difference <= eight_minutes and time_difference >= timedelta(0):
    pass
else:
    exceptions.append(f"最新文件创建时间不在8分钟内，拉取数据可能出现问题，请登录探测机检查")

if len(string_set) == 1:
    exceptions.append(f"BGP_联通出口1在{files_datetimes[2]}、{files_datetimes[1]}、{files_datetimes[0]}三轮内刷新时间未变化均为：{value}")
else:
    pass

# 检查1出口下的In目录下的值的范围
value = float(in_file_num1[0][0])
if 0 < value < 4000:
    pass
else:
    exceptions.append(f"{files_datetimes[0]}BGP_联通出口1错误: 输入值 {value} 不在范围之内")
#防止探测时间过长，只检查判断最新文件，对第二个文件也进行判断
# value1 = float(in_file_num1[0][1])
# if 0 < value1 < 4000:
#     pass
# else:
#     exceptions.append(f"{files_datetimes[1]}BGP_联通出口1错误: 输入值 {value1} 不在范围之内")

# 检查1出口下的Out目录下的值的范围
value3 = float(out_file_num1[0][0])
if 0 < value3 < 4000:
    pass
else:
    # close_url()
    exceptions.append(f"{files_datetimes[0]}BGP_联通出口1错误: 输出值 {value3} 不在范围之内")

#防止探测时间过长，只检查判断最新文件，对第二个文件也进行判断
# value4 = float(out_file_num1[0][1])
# if 0 < value4 < 4000:
#     pass
# else:
#     # close_url()
#     exceptions.append(f"{files_datetimes[1]}BGP_联通出口1错误: 输出值 {value4} 不在范围之内")
# 如果有异常则抛出所有异常
if exceptions:
    raise Exception("；".join(str(e) for e in exceptions))
close_url()