from flask import Flask, request
from flask_restful import Resource, Api
from board import Board
from life_counter import LifeCounter
from rules import Rules


app = Flask(__name__)
api = Api(app)


class Game(Resource):
    def post(self):
        initial_matrix = request.get_json(force=True)
        new_matrix = [[int(string) for string in inner] for inner in initial_matrix]
        board = Board(new_matrix, Rules(LifeCounter()))
        return board.next_board()


api.add_resource(Game, '/game')

if __name__ == '__main__':
    app.run(debug=True)
