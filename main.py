from website import create_app

# create and configure the app in __init__.py
app = create_app() 

#Running our Flask application using app.run method
if __name__ == '__main__':
    app.run(debug=True)
