from flask import Flask, request
from flask_restful import Resource, Api
from board import Board
from life_counter import LifeCounter
from rules import Rules
import sys


app = Flask(__name__)
api = Api(app)


class Game(Resource):
    def post(self):
        initial_matrix = request.get_json(force=True)
        counter = LifeCounter()
        rules = Rules(counter)
        board = Board(initial_matrix, rules)
        return board.next_board()


api.add_resource(Game, '/game')

if __name__ == '__main__':
    app.run(debug=True)
