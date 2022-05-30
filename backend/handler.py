import json

from loot_of_lima_solver.game import StandardGame


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}


def solve(event, context):
    game = StandardGame()
    game.solve()
    body = {
        "iterations": f"{game._iteration_count}",
        "solution": f"{game.get_result()}",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
