import glob
import os
import shutil
import random
from data_process.data_config import get_train_parent

data_root = get_train_parent()+"train-img/"
files = os.listdir(data_root)
if not os.path.exists(get_train_parent()+"valid-img"):
    os.mkdir(get_train_parent()+"valid-img")
for file in files:
    train_fpaths = glob.glob(data_root + file+"/*.jpg")
    random.shuffle(train_fpaths)
    val_fpaths = train_fpaths[int(0.95*len(train_fpaths)):]
    print('val_fpaths-val data number:', len(val_fpaths))

    #split train val
    for path in val_fpaths:
        val_path = path.replace('train-img', 'valid-img')
        fold ,name = val_path.split("\\")[0],val_path.split("\\")[1]
        if not os.path.exists(fold):
            os.makedirs(fold)
        print(fold,"--------",name)
        shutil.move(path, fold+"/"+name)


