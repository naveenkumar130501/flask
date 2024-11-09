from flask import Flask,render_template
app=Flask(__name__)

# static route

@app.route("/")

def hello():
    courses=["C",'C++'"JAVA","PYTHON","MYSQL"]
    is_loged = True
    return render_template("index.html" ,user_course=courses , verify=is_loged)

@app.route("/about")

def about():
    return render_template("about.html",about_user="age 22")

# dinamic route

@app.route("/users/<input>")

def getting(input):
    # return "<h1>welcome {}</h1>".format(input)

    arr=[1,2,3,"apple"]
    dic={
        "name":"naveen",
        "age":22,
        "sex":"male"
    }
    return render_template("users.html",user_input=input.upper() , user_list=arr , user_dic=dic)

if __name__ == "__main__":
    app.run(debug=True)

