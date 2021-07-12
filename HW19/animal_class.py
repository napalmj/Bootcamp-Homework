'''
SQL query python class for taking in existing tables and initializing new tables
'''
import pymysql

class query_class:

    def __init__(self, existingTables = [], declareNewTables = []):
        self.existingTables = existingTables
        self.declareNewTables = declareNewTables
        self.schema = 'nathaniel_palmer'
        self.database = pymysql.connect(
            host="freetrainer.cryiqqx3x1ub.us-west-2.rds.amazonaws.com",
            user="nathaniel",
            password="changeme"            
        )
        
    def getTables(self):
        return self.existingTables    

    def getDataTableData(self, dataTableName):
        columnTitles = []
        cursor = self.database.cursor()
        cursor.execute(f"SHOW COLUMNS FROM {self.schema}.{dataTableName}")
        columnParams = cursor.fetchall()
        cursor.execute(f"SELECT * FROM {self.schema}.{dataTableName}")
        bodyRow = cursor.fetchall()
        for n in range(len(columnParams)):
            columnTitles.append(columnParams[n][0])
        return [columnTitles, list(bodyRow)]

    def getCurrentTable(self, tableStr):
        if tableStr:
            return tableStr
        else:
            return self.existingTables[0]

    # def editAddRemove(self, modifyListParams = []):
    #     cursor = self.database.cursor()
    #     editParam = modifyListParams[1].lower()
    #     if modifyListParams[0] == 'add':
    #         cursor.execute(
    #             f"""ALTER TABLE {modifyListParams[2]}\
    #                 ADD COLUMN {editParam}\
    #             """
    #         )
    #     elif modifyListParams[0] == 'delete':
    #         cursor.execute(
    #             f"""ALTER TABLE {modifyListParams[2]}\
    #                 DROP COLUMN {editParam}\
    #             """
    #         )
    #     elif modifyListParams[0] == 'edit':
    #         print('edit', modifyListParams[1])
    #     else:
    #         return 'Invald Edit Param'
            
    def searchTables(self, strName):
        cursor = self.database.cursor()
        cursor.execute(
            f"""SELECT dogs.name\
                FROM dogs\
                WHERE doctors.name Like '%{strName}%'\
            """
        )
