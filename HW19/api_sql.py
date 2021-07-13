from flask import Flask, request, render_template
from animal_class import query_class
from tableList import dogTables

qry = query_class(dogTables)

app = Flask(__name__)



@app.route("/", methods=['GET'])
def home():
    if request.method == 'GET':
        addQueryParams = request.args.getlist('add')
        print(qry.currentColHeader)
        if addQueryParams:
            qry.editAddRemove(['add', 1, qry.currentTable, addQueryParams, qry.currentColHeader])

        editQueryParams = request.args.get('modify')
        if editQueryParams:
            modList = editQueryParams.split('-')
            print(modList)
            qry.editAddRemove(modList)

        tableQueryString = request.args.get('table')
        currentTable = qry.getCurrentTable(tableQueryString)
        qry.setCurrentTable(currentTable)
        deleteQueryStringFlag = request.args.get('modify')
        if deleteQueryStringFlag:
            modList = deleteQueryStringFlag.split('-')
            qry.editAddRemove(modList)
        
        dogTable = qry.getDataTableData(currentTable)
        colTitle = dogTable[0]
        qry.setCurrentColHeader(colTitle)
        qry.setCurrentModifyString(request.args.get('editSubmit'))

        rowCells = dogTable[1]
        rowLength = len(colTitle)
        rowHeight = len(rowCells)
        
        if request.args.get('search'):
            qry.searchTables(request.args.get('search'))
        else:
            qry.searchedData.clear()

    return render_template(
        'home.html',
        colTitle=colTitle,
        rowCells=rowCells,
        rowLength=rowLength,
        rowHeight=rowHeight,
        tables=qry.getTables(),
        currentTable=currentTable,
        searchedData=qry.searchedData
        )
