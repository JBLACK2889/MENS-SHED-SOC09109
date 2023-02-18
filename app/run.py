#This is the file that launches the web application 

from mens_shed import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)