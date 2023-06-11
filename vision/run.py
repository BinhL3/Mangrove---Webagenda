from vision_app import app, db

if __name__ == '__main__':
    app.app_context().push()
    app.run()
    db.create_all() 