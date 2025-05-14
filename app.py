from flask import Flask

from utils import fetch_attendance

app = Flask(__name__)


@app.route("/verify/<libraryid>", methods=["GET"])
def verify(libraryid):
    if fetch_attendance(libraryid):
        return {"success": True, "code": "USER_VERIFIED"}
    else:
        return {"success": False, "code": "MINIMUM_ATTENDANCE_REQUIRED"}
