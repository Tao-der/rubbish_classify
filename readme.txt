运行环境：
   TensorFlow2.0
   mysql
   OpenCV
   Python3.6
配置mysql:
1.下载并安装；mysql
    mysql -u root -p
    sql = "CREATE DATABASE IF NOT EXISTS db_name4"
    show databases;
    use db_name4
    show tables;
    删除表：
    drop database xxxx;
2. pip install PyMySQL -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install cryptography -i https://pypi.tuna.tsinghua.edu.cn/simple

3、把宣传视频视频放到根目录下，修改Detection.py中的第57 行，修改 self.preview_video="xxx.mp4"

4、运行 Detection.py即可检测


