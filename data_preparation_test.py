import glob
import os
import shutil
import random
from data_process.data_config import get_train_parent

data_root = get_train_parent()+"valid-img/"
files = os.listdir(data_root)
if not os.path.exists(get_train_parent()+"test-img"):
    os.mkdir(get_train_parent()+"test-img")
for file in files:
    val_fpaths = glob.glob(data_root + file+"/*.jpg")
    random.shuffle(val_fpaths)
    test_fpaths = val_fpaths[int(0.5*len(val_fpaths)):]
    print('test_fpaths- data number:',len(test_fpaths))

    #split val test
    for path in test_fpaths:
        val_path = path.replace('valid-img', 'test-img')
        fold ,name = val_path.split("\\")[0],val_path.split("\\")[1]
        if not os.path.exists(fold):
            os.makedirs(fold)
        print(fold,"--------",name)
        shutil.move(path, fold+"/"+name)

     
