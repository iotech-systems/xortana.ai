#!/usr/bin/env python3

import flask
import setproctitle
from picamera import PiCamera


APP_NAME = "xor/cam_proxy"
TCP_PORT: int = 9092
FLASK_APP = flask.Flask(APP_NAME
   , static_url_path=""
   , static_folder="www"
   , template_folder="www/templates")


# -- app rounds --
@FLASK_APP.route("/")
def idx():
   return FLASK_APP.send_static_file("idx.html")


@FLASK_APP.route("/get/cam/<cam_id>", methods=["GET"])
def read_cam(cam_id: str):
   return f"{cam_id}"


# -- -- -- -- [ entry point ] -- -- -- --
if __name__ == "__main__":
   setproctitle.setproctitle(APP_NAME)
   FLASK_APP.run(host="0.0.0.0", port=TCP_PORT, debug=True)
