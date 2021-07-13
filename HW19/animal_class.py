'''
SQL query python class for taking in existing tables and initializing new tables
'''
import pymysql

class query_class:

    def __init__(self, existingTables = [], declareNewTables = []):
        self.existingTables = existingTables
        self.declareNewTables = declareNewTables
        self.schema = 'nathaniel_palmer'
        self.currentTable = ''
        self.currentColHeader = ''
        self.currentModifyString = ''
        self.searchedData = []
        self.database = pymysql.connect(
            host="freetrainer.cryiqqx3x1ub.us-west-2.rds.amazonaws.com",
            user="nathaniel",
            password="changeme"            
        )
        
    def setCurrentTable(self, table):
        self.currentTable = table

    def setCurrentColHeader(self, col):
        self.currentColHeader = col

    def setCurrentModifyString(self, param):
        self.currentModifyString = param

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

    def editAddRemove(self, modifyListParams = [], optionString = ''):
        cursor = self.database.cursor()
        editParam = modifyListParams[0].lower()
        if editParam == 'add':
            addStr = f"""INSERT INTO nathaniel_palmer.{modifyListParams[2]} 
            (name)
            VALUES 
            ('{modifyListParams[3][1]}');"""
            cursor.execute(addStr)
        elif editParam == 'delete':
            delStr = f"""DELETE FROM nathaniel_palmer.{modifyListParams[2]} 
            WHERE {modifyListParams[2]}.id = {modifyListParams[1]};"""
            cursor.execute(delStr)
        elif editParam == 'edit':
            updateData = f"UPDATE nathaniel_palmer.{modifyListParams[2]} SET {modifyListParams[3]} = '{self.currentModifyString}' WHERE {modifyListParams[2]}.id = {modifyListParams[4]};"
            cursor.execute(updateData)
        else:
            return 'Invald Edit Param'
            
    def searchTables(self, strName = ''):
        totalSearcData = []
        cursor = self.database.cursor()
        for item in self.existingTables:
            searchStr = f"SELECT * FROM nathaniel_palmer.{item} WHERE {item}.name LIKE '%{strName}%'"
            cursor.execute(searchStr)
            totalSearcData.append(cursor.fetchall())
        self.searchedData = totalSearcData
