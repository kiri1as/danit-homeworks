from web_development.hw5.app.DbClient import DbClient

if __name__ == '__main__':
    db_client = DbClient()
    db_client.update('users', {'name': 'kyryl', 'email': '123'}, 'null')