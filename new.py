from flask import Flask, render_template, request

web = Flask(__name__)


@web.route('/')
@web.route('/register')
def home():
    return render_template("register.html")

@web.route('/confirmation', methods =['POST','GET'])

def register():
    if request.method == "POST":
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phone number')
        return render_template('confirm.html',name=n, city=c,phonenumber=p)

if __name__ == "__main__":
    web.run(debug=True)
