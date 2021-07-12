from flask import Flask, request, render_template
from animal_class import query_class
from tableList import dogTables

qry = query_class(dogTables)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    
    if request.method == 'GET':
        tableQueryString = request.args.get('table')
        currentTable = qry.getCurrentTable(tableQueryString)
        modifierQueryStringFlag = request.args.get('modify')
        if modifierQueryStringFlag: 
            modList = modifierQueryStringFlag.split('-')
            print('Modify set', modList, currentTable)
        
        dogTable = qry.getDataTableData(currentTable)
        colTitle = dogTable[0]
        rowCells = dogTable[1]
        rowLength = len(colTitle)
        rowHeight = len(rowCells)
        

    return render_template(
        'home.html',
        colTitle=colTitle,
        rowCells=rowCells,
        rowLength=rowLength,
        rowHeight=rowHeight,
        tables=qry.getTables(),
        currentTable=currentTable
        )

@app.route("/edit", methods=['GET'])
def edit():
    return render_template('edit.html')

@app.route("/add", methods=['GET'])
def add():
    return render_template('add.html')

@app.route("/delete", methods=['GET'])
def delete():
    return render_template('delete.html')


