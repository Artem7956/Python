import subprocess
import os
import shutil

source_path = 'Source'
result_path = 'Result'
current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, source_path)
files = [f for f in os.listdir(file_path)]

if not os.path.exists(result_path):
    os.mkdir(result_path)
else:
    shutil.rmtree(result_path)
    os.mkdir(result_path)


for i in files:
     file_name = os.path.join(file_path, i)
     result_file = os.path.join(result_path, i)
     subprocess.call('convert.exe ' + '"' + file_name + '" -resize 200 ' + result_file)
