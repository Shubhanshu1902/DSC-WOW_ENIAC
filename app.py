#Author:-ENIAC 
#Project Name:-ENIAC:Calculator cum Converter
#Team Member:-  Shubhanshu Agrawal  github:-Shubhanshu1902
#           :-  Sheersh Jindal      github:-SheershJindal
#           :-  Kshitiz Agrawal     github:-Kshitiz1403
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def app1():
    return render_template("index.html")

@app.route("/calc")#,methods=['POST'])
def calc():
    return render_template("calc.html")

@app.route("/sendCalc", methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']
    num1 = num1.strip()
    num1 = ''.join(i for i in num1 if i.isdigit())
    num2 = num2.strip()
    num2 = ''.join(i for i in num2 if i.isdigit())

    if num1 == '' or num2 == '':
        return render_template('calc.html')    

    elif operation=="add":
        result=float(num1)+float(num2)
        return render_template('calc.html',result=result)

    elif operation=="subtract":
        result=float(num1)-float(num2)
        return render_template('calc.html',result=result)

    elif operation=="multiply":
        result=float(num1)*float(num2)
        return render_template('calc.html',result=result)

    elif operation=="divide":
        result=float(num1)/float(num2)
        return render_template('calc.html',result=result) 

    else:
        return render_template("calc.html")

@app.route("/binary")
def binary():
    return render_template("binary.html")

@app.route("/sendBinary",methods=['POST'])
def converter():
    num = request.form['num']
    inputOperation = request.form['input-operation']
    outputOperation = request.form['output-operation']
    num = num.strip()
    num = ''.join(i for i in num if i.isdigit())
    if num == '':
        return render_template('binary.html')    

    elif inputOperation == "Binary":
        if outputOperation=="Decimal":
            result=int(num,2)
            return render_template('binary.html',result=result)

        elif outputOperation=="Hexadecimal":
            result=int(num,2)
            result=hex(result)
            return render_template('binary.html',result=result)

        elif outputOperation=="Octal":
            result=int(num,2)
            result=oct(result)
            return render_template('binary.html',result=result)

        else:
            return render_template('binary.html')

    elif inputOperation == "Decimal":
        num=int(num)
        if outputOperation=="Binary":
            result=bin(num)
            return render_template('binary.html',result=result)
   
        elif outputOperation=="Hexadecimal":
            result=hex(num)
            return render_template('binary.html',result=result)
        
        elif outputOperation=="Octal":
            result=oct(num)
            return render_template('binary.html',result=result)
        
        else:
            return render_template('binary.html')

    elif inputOperation == "Hexadecimal":
        num=int(num,16)
        if outputOperation=="Binary":
            result=bin(num)
            return render_template('binary.html',result=result)

        elif outputOperation=="Decimal":
            result=num
            return render_template('binary.html',result=result)

        elif outputOperation=="Octal":
            result=oct(num)
            return render_template('binary.html',result=result)

        else:
            return render_template('binary.html')

    elif inputOperation == "Octal":
        num=int(num,8)
        if outputOperation=="Binary":
            result=bin(num)
            return render_template('binary.html',result=result)

        elif outputOperation=="Decimal":
            result=num
            return render_template('binary.html',result=result)

        elif outputOperation=="Hexadecimal":
            result=hex(num)
            return render_template('binary.html',result=result)

        else:
            return render_template('binary.html')

    else:
        return render_template("binary.html")

if __name__ == "__main__":
    app.run(debug=True)