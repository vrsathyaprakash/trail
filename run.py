from learncrypto import create_app

app = create_app()
app.app_context().push()

if __name__ == '__main__':
    aapp.run(debug=False)