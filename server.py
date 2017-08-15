from sanic import Sanic
from sanic.response import json
import logging

app = Sanic()

@app.route("/")
async def test(request):
    # logging.warning(request.headers)
    user_name = request.headers['token-claim-sub']
    return json({"hello": user_name})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
