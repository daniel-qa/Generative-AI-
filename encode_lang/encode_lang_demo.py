import os,sys
import subprocess
from check_GB2312 import contains_simplified_chinese


# 执行命令并捕获输出，假设输出包含简体中文字符
command = 'dir'
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='big5')



# 输出结果
#print('Exit status:', result.returncode)
#print('Standard Output:\n\n', result.stdout)
#print('Standard Error:', result.stderr)

# 将 Big5 编码的输出重新编码为 UTF-8
output_utf8 = result.stdout.encode('utf-8', errors='replace').decode('utf-8', errors='replace')
print('Re-encoded Output (UTF-8):\n\n', output_utf8)

# 寫入 Log 檔
def append_string_to_file(string, file_path="log.txt"):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(string + '\n')


# 逐行读取 stdout
for line in output_utf8.splitlines():
    print(f"Processed line: {line}")
    
    # 檢是是否有簡體字
    if contains_simplified_chinese(line):
        print(f"字符串 '{line}' 包含简体字")
        append_string_to_file(line)
    





