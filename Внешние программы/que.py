import queue
from threading import Thread
import subprocess
import os
import shutil

source_path = 'Source'
result_path = 'Result'
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, source_path)


if not os.path.exists(result_path):
    os.mkdir(result_path)
else:
    shutil.rmtree(result_path)
    os.mkdir(result_path)

def convert_file(f, sf, rf):
    file_name = os.path.join(sf, f)
    result_file = os.path.join(rf, f)
    print(file_name, result_file)
    subprocess.call('convert.exe ' + '"' + file_name + '" -resize 200 ' + result_file)


def worker():
    while True:
        f = q.get()
        convert_file(f,file_path,result_path)
        q.task_done()


q = queue.Queue()

for i in range(4):
    t = Thread(target=worker)
    t.setDaemon(True)
    t.start()

files = [f for f in os.listdir(file_path)]
#print(files)
for item in files:
    #print(item)
    q.put(item)

q.join()

