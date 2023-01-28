from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/hai')
def hai():
    return 'This is flask first view function'

@FAI.route('/wish/<name>')
def wish(name):
    return f'Hello how r u MR/MS {name}'

@FAI.route('/first')
def first():
    return render_template('first.html')

if __name__=='__main__':
    FAI.run(debug=True,host='192.168.1.35',port=5001)