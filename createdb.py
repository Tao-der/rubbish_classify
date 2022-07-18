import pymysql

class ObjectDB():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='123456', charset='utf8mb4')
        self.cursor = self.conn.cursor()
    def createDb(self):
        sql = "CREATE DATABASE IF NOT EXISTS rubbish"
        self.cursor.execute(sql)
        self.cursor.execute("use rubbish")

    def createTable(self):
        sql_2 = '''CREATE TABLE `rubbishinfo` ( 
                 `id`   INT AUTO_INCREMENT, 
                 `category` TEXT(100) , 
                 `weight` TEXT(100) , 
                 `nums` TEXT(100) ,  
                 `status` TEXT(100),
                 PRIMARY KEY (`id`)
               ) ENGINE=InnoDB;
               '''
        try:
            self.cursor.execute(sql_2)
            print("创建数据库成功")
        except Exception as e:
            print("创建数据库结果：case%s" % e)
        finally:
            pass
            # cursor.close()
            # db.close()

    def selectAll(self,catregory):
        if catregory == None:
            sql = """SELECT * FROM rubbishinfo ;"""
        else:
            sql = """SELECT * FROM rubbishinfo WHERE catregory = '%s';""" % (str(catregory))
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print("查询出错：case%s" % e)
            return None

    def insertInto(self,catregory,weight,nums,status):
        sql = "INSERT INTO  rubbishinfo VALUES(%s,%s,%s,%s,%s)"
        params = [(0,catregory,weight,nums,status)]
        try:
            self.cursor.executemany(sql,params)
            self.conn.commit()
            print("有",self.cursor.rowcount,"插入数据成功")
        except Exception as e:
            print("插入数据失败：case%s"%e)
            self.conn.rollback()
        finally:
            pass

    def updataInfo(self,id,weight,nums,status):
        sql = """UPDATE rubbishinfo SET weight = '%s', nums = '%s', status = '%s' WHERE idshow = '%s';""" % (str(id))
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("有",self.cursor.rowcount,"更新数据成功")
        except Exception as e:
            print("更新数据失败：case%s"%e)
            self.conn.rollback()
        finally:
            pass
            # cursor.close()
            # db.close()

    def clearDb(self,id= None):
        if id is None:
            sql = """DELETE FROM rubbishinfo"""
        else:
            sql = """DELETE FROM rubbishinfo WHERE ID = %s""" % (int(id))
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("删除数据成功")

        except Exception as e:
            print("删除数据失败：case%s" % e)
            self.conn.rollback()
        # finally:
        #     self.cursor.close()
        #     self.conn.close()

    def deleteDb(self, idshow=None):
        if idshow is None:
            sql = """DELETE FROM rubbishinfo"""
        else:
            sql = """DELETE FROM rubbishinfo  WHERE idshow = '%s';""" % (str(idshow))
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("删除数据成功")
            return  True

        except Exception as e:
            print("删除数据失败：case%s" % e)
            self.conn.rollback()
            return False
if __name__ == "__main__":
    objectDB = ObjectDB()
    try:
        #
        objectDB.createDb()
        objectDB.createTable()
        objectDB.clearDb(None)
        #objectDB.insertInto("1","2","3","4")
    except Exception as e:
        pass
    finally:
        objectDB.cursor.close()
        objectDB.conn.close()
