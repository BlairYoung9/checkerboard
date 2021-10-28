from flask import Flask, render_template 

app = Flask(__name__)   

@app.route('/')
def index():
    return render_template("board.html") 

@app.route('/4')
def small():
    return render_template("board2.html")

@app.route('/<int:num>/<int:num2>')
def user_picks(num,num2):
    return render_template("board3.html", num=num, num2=num2)

if __name__=="__main__":   
    app.run(debug=True)   
