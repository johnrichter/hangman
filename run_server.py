from application import db, create_app


app = create_app()


if __name__ == '__main__':
    print('Database location:', db.engine)
    app.run()


# Webpages
#  index/root view
#  login
#  game page
#  ability to log out
#  if time: win/loss records per user view

# Functions
#  Database handler
#  login
#  logout
#  connection/session manager to update clients of the game status

