from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/static')
def static_file():
    return render_template('static_file.html')


@FAI.route('/data')
def navigation():
    return render_template('navigation.html')



if __name__=='__main__':
    FAI.run(debug=True)