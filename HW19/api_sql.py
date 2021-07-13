from flask import Flask, request, render_template
from animal_class import query_class
from tableList import dogTables

qry = query_class(dogTables)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    
    if request.method == 'GET':
        addQueryFields = request.args.getlist('add')
        print(qry.currentColHeader)
        if addQueryFields:
            qry.editAddRemove(['add', 1, qry.currentTable, addQueryFields, qry.currentColHeader])
        
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
        # print(qry.currentColHeader)
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
    if request.method == 'GET':
        print('HI')
    return f"Hi"

# @app.route("/add", methods=['POST'])
# def add():
#     if request.method == 'POST':
#         formData = request.form
#         print(formData)
#         formName = list((formData.to_dict()).values())[0]

#     return app.redirect(app.url_for('home'))

# @app.route("/delete", methods=['GET'])
# def delete():
#     return render_template('delete.html')


