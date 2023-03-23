#This is the file that launches the web application 

from mens_shed import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Route for handling the login page logic
#@app.route('/login', methods=['GET', 'POST'])
#def login():
 #   error = None
  #  if request.method == 'POST':
   #     if request.form['uname'] != 'test' or request.form['pword'] != 'test':
    #        error = 'Invalid Credentials. Please try again.'
     #   else:
      #      return redirect(url_for('home'))
    #return render_template('login.html', error=error)