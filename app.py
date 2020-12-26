import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message
import pygraphviz

load_dotenv()


machine = TocMachine(
    states=["user",
            "question",
            "qing",
            "honor",
            "honor_e",
            "honor_g",
            "honor_g_list",
            "honor_pa",
            "honor_par",
            "honor_par_list",
            "honor_panr",
            "honor_panr_list",
            "honor_pp",
            "honor_s",
            "honor_bro",
            "honor_bro_list",
            "honor_sis",
            "honor_sis_list",
            "honor_mc",
            "honor_mcnr",
            "honor_mcnr_list",
            "honor_mcr",
            "honor_mcr_list",
            "honor_ch",
            "honor_ch_list",
            "fsm"],
    transitions=[
        {"trigger": "advance","source": "user","dest": "question","conditions": "is_going_to_question"},
        {"trigger": "advance","source": "user","dest": "question","conditions": "is_going_to_question"},
        {"trigger": "advance","source": "user","dest": "fsm","conditions": "is_going_to_fsm"},
        {"trigger": "advance","source": "question","dest": "qing","conditions": "is_going_to_qing"},
        {"trigger": "advance","source": "qing","dest": "qing","conditions": "is_going_to_qing"},
        {"trigger": "advance","source": "user","dest": "honor","conditions": "is_going_to_honor"},
        
        {"trigger": "advance","source": "honor","dest": "honor_e","conditions": "is_going_to_honor_e"},
        {"trigger": "advance","source": "honor","dest": "honor_pp","conditions": "is_going_to_honor_pp"},
        {"trigger": "advance","source": "honor","dest": "honor_ch","conditions": "is_going_to_honor_ch"},
        
        {"trigger": "advance","source": "honor_e","dest": "honor_g","conditions": "is_going_to_honor_g"},
        {"trigger": "advance","source": "honor_e","dest": "honor_pa","conditions": "is_going_to_honor_pa"},
        {"trigger": "advance","source": "honor_e","dest": "honor","conditions": "is_going_back_to_honor"},
        
        {"trigger": "advance","source": "honor_g","dest": "honor_g_list","conditions": "is_going_to_honor_g_list"},
        {"trigger": "advance","source": "honor_g","dest": "honor_e","conditions": "is_going_back_to_honor_e"},
        
        {"trigger": "advance","source": "honor_pa","dest": "honor_panr","conditions": "is_going_to_honor_panr"},
        {"trigger": "advance","source": "honor_pa","dest": "honor_par","conditions": "is_going_to_honor_par"},
        {"trigger": "advance","source": "honor_pa","dest": "honor_e","conditions": "is_going_back_to_honor_e"},
        
        {"trigger": "advance","source": "honor_panr","dest": "honor_panr_list","conditions": "is_going_to_honor_panr_list"},
        {"trigger": "advance","source": "honor_panr","dest": "honor_pa","conditions": "is_going_back_to_honor_pa"},
        
        {"trigger": "advance","source": "honor_par","dest": "honor_par_list","conditions": "is_going_to_honor_par_list"},
        {"trigger": "advance","source": "honor_par","dest": "honor_pa","conditions": "is_going_back_to_honor_pa"},
        
        {"trigger": "advance","source": "honor_pp","dest": "honor_s","conditions": "is_going_to_honor_s"},
        {"trigger": "advance","source": "honor_pp","dest": "honor_mc","conditions": "is_going_to_honor_mc"},
        {"trigger": "advance","source": "honor_pp","dest": "honor","conditions": "is_going_back_to_honor"},
        
        {"trigger": "advance","source": "honor_s","dest": "honor_bro","conditions": "is_going_to_honor_bro"},
        {"trigger": "advance","source": "honor_s","dest": "honor_sis","conditions": "is_going_to_honor_sis"},
        {"trigger": "advance","source": "honor_s","dest": "honor_pp","conditions": "is_going_back_to_honor_pp"},
        
        {"trigger": "advance","source": "honor_bro","dest": "honor_bro_list","conditions": "is_going_to_honor_bro_list"},
        {"trigger": "advance","source": "honor_bro","dest": "honor_s","conditions": "is_going_back_to_honor_s"},
        
        {"trigger": "advance","source": "honor_sis","dest": "honor_sis_list","conditions": "is_going_to_honor_sis_list"},
        {"trigger": "advance","source": "honor_sis","dest": "honor_s","conditions": "is_going_back_to_honor_s"},

        {"trigger": "advance","source": "honor_mc","dest": "honor_mcnr","conditions": "is_going_to_honor_mcnr"},
        {"trigger": "advance","source": "honor_mc","dest": "honor_mcr","conditions": "is_going_to_honor_mcr"},
        {"trigger": "advance","source": "honor_mc","dest": "honor_pp","conditions": "is_going_back_to_honor_pp"},
        
        {"trigger": "advance","source": "honor_mcnr","dest": "honor_mcnr_list","conditions": "is_going_to_honor_mcnr_list"},
        {"trigger": "advance","source": "honor_mcnr","dest": "honor_mc","conditions": "is_going_back_to_honor_mc"},
        
        {"trigger": "advance","source": "honor_mcr","dest": "honor_mcr_list","conditions": "is_going_to_honor_mcr_list"},
        {"trigger": "advance","source": "honor_mcr","dest": "honor_mc","conditions": "is_going_back_to_honor_mc"},
        
        {"trigger": "advance","source": "honor_ch","dest": "honor_ch_list","conditions": "is_going_to_honor_ch_list"},
        {"trigger": "advance","source": "honor_ch","dest": "honor","conditions": "is_going_back_to_honor"},
        
        {"trigger": "advance","source": "user","dest": "claim","conditions": "is_going_to_claim"},
        {"trigger": "advance", "source": ["user", 
            "question",
            "qing",
            "honor",
            "honor_e",
            "honor_g",
            "honor_g_list",
            "honor_pa",
            "honor_par",
            "honor_par_list",
            "honor_panr",
            "honor_panr_list",
            "honor_pp",
            "honor_s",
            "honor_bro",
            "honor_bro_list",
            "honor_sis",
            "honor_sis_list",
            "honor_mc",
            "honor_mcnr",
            "honor_mcnr_list",
            "honor_mcr",
            "honor_mcr_list",
            "honor_ch",
            "honor_ch_list"], "dest": "user","conditions":"is_going_to_user"},
        {"trigger": "go_back", "source": "fsm", "dest": "user"},
        {"trigger": "go_back", "source": "honor_g_list", "dest": "honor_g"},
        {"trigger": "go_back", "source": "honor_panr_list", "dest": "honor_panr"},
        {"trigger": "go_back", "source": "honor_par_list", "dest": "honor_par"},
        {"trigger": "go_back", "source": "honor_bro_list", "dest": "honor_bro"},
        {"trigger": "go_back", "source": "honor_sis_list", "dest": "honor_sis"},
        {"trigger": "go_back", "source": "honor_mcnr_list", "dest": "honor_mcnr"},
        {"trigger": "go_back", "source": "honor_mcr_list", "dest": "honor_mcr"},
        {"trigger": "go_back", "source": "honor_ch_list", "dest": "honor_ch"},
        
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    show_fsm()
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
