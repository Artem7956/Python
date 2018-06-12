import subprocess
import os
import shutil
from multiprocessing import Pool
from functools import partial


source_path = 'Source'
result_path = 'Result'
current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, source_path)
files = [f for f in os.listdir(file_path)]

if not os.path.exists(result_path):
    os.mkdir(result_path)
#else:
#    shutil.rmtree(result_path)
#    os.mkdir(result_path)

def convert_file(f,sf,rf):
    file_name = os.path.join(sf, f)
    result_file = os.path.join(rf, f)
    subprocess.call('convert.exe ' + '"' + file_name + '" -resize 200 ' + result_file)




if __name__ == '__main__':
     with Pool(4) as p:
         p.map(partial(convert_file,sf=file_path,rf = result_path), files)

