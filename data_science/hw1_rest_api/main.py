from resource import create_app

game_resource = create_app()

if __name__ == "__main__":
    game_resource.run(port=8080)