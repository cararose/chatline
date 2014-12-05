from flask import Flask, Response
app = Flask(__name__)

@app.route("/incoming_call")
def incoming_call():
    # This handles the incoming calls
    twiml = '''<?xml version="1.0" encoding="UTF-8"?>
                <Response>
                    <Say>Hello. You have reached a robot. Don't worry, I'm a singing robot, not a stabbing robot.</Say>
                </Response>
            '''

    return Response(twiml, mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True)
