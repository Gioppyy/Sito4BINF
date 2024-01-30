from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def getStudents():
    with open("studenti.txt") as file:
        students = [line.strip() for line in file.readlines()]
        
    table_data = [val for key, val in getTable().items()]
    students = [s for s in students if s not in table_data]
    return students

def getTable():
    with open("table.json") as table_file:
        table = json.load(table_file)
    return table

def addStudentToTable(name, pos):
    table = getTable()
    tableDict = dict(table)
    tableDict[pos] = name
    with open("table.json", "w") as table_file:
        json.dump(tableDict, table_file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/interrogazione-boh")
def interrogazione1():
    students = getStudents()
    tableItems = getTable().items()
    tableData = [val for key, val in tableItems]
    tableDict = dict(tableItems)
    tablePos = [key for key, val in tableDict.items() if val == "-"]
    
    return render_template("table.html", students=students, table_data=tableData, table_pos=tablePos)

@app.route("/addstudent", methods=["POST"])
def addStudent():
    if request.method == "POST":
        name = request.form.get("name")
        pos  = request.form.get("pos")
        if name != "none" and pos != "none":
            addStudentToTable(name,pos)
    return redirect("/")

if __name__ == "__main__":
    app.run()
