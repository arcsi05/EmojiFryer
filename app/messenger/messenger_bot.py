from os import getenv
import json
import logging
# from dotenv.main import load_dotenv
from starlette.responses import RedirectResponse
import requests
from typing import Optional
from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import PlainTextResponse
import hashlib
import hmac

# load_dotenv()

app = FastAPI()


# @app.get("/")
# async def docs_redirect():
#     return RedirectResponse(url='/docs')

# Logging toolbox 🔊
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("webhook")


@app.get("/webhook")
async def verify_token(
    verify_token: Optional[str] = Query(
        None, alias="hub.verify_token", regex="^[A-Za-z1-9-_]*$"
    ),
    challenge: Optional[str] = Query(
        None, alias="hub.challenge", regex="^[A-Za-z1-9-_]*$"
    ),
    mode: Optional[str] = Query(
        "subscribe", alias="hub.mode", regex="^[A-Za-z1-9-_]*$"
    ),
) -> Optional[str]:
    token = getenv("FB_VERIFY_TOKEN")
    if not token or len(token) < 8:
        logger.error(
            "🔒Token not defined. Must be at least 8 chars or numbers."
            "💡Tip: set -a; source .env; set +a"
        )
        raise HTTPException(status_code=500, detail="Webhook unavailable.")
    elif verify_token == token and mode == "subscribe":
        return PlainTextResponse(f"{challenge}")
    else:
        raise HTTPException(status_code=403, detail="Token invalid.")


@app.post("/webhook")
async def trigger_response(request: Request) -> None:
    data = await request.json()
    payload = (
        json.dumps(data, separators=(",", ":"))
        .replace("/", "\\/")
        .replace("@", "\\u0040")
        .replace("%", "\\u0025")
        .replace("<", "\\u003C")
        .encode()
    )
    print("data:")
    print(json.dumps(data, indent=4))
    app_secret = getenv("FB_APP_SECRET").encode()
    expected_signature = hmac.new(
        app_secret, payload, digestmod=hashlib.sha1
    ).hexdigest()
    signature = request.headers["x-hub-signature"][5:]
    if not hmac.compare_digest(expected_signature, signature):
        raise HTTPException(
            status_code=403, detail="Message not authenticated.")
    try:
        message = data["entry"][0]["messaging"][0]["message"]
        sender_id = data["entry"][0]["messaging"][0]["sender"]["id"]
        reply = requests.get(
            'http://localhost:4356/emojify?sentence='+message["text"]).text.strip('"')
        if message["text"]:
            request_body = {
                "recipient": {"id": sender_id},
                "message": {"text": reply},
            }
            response = requests.post(
                "https://graph.facebook.com/v12.0/me/messages?access_token="
                f'{getenv("FB_PAGE_ACCESS_TOKEN")}',
                json=request_body,
            ).json()
    except KeyError:
        logger.info("Message sent and received by recipient. ✅")
        pass
    return None
