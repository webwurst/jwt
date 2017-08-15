from sanic import Sanic
from sanic.response import json
# import sanic.response
# sanic.request.Request

import logging

app = Sanic()

@app.route("/")
async def test(request):
    print(request.headers)
    logging.warning(request.headers)

    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    # app.run(log_config=LOGGING)
