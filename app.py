from flask import Flask
app = Flask(__name__)

@app.route("/incoming_call")
def incoming_call():
    # This handles the incoming calls
    twiml = '''
            <?xml version="1.0" encoding="UTF-8"?>
            <Response>
                <Say voice="woman">Please leave a message after the tone.</Say>
                <Record maxLength="20" />
            </Response>
            '''

    return twiml


if __name__ == "__main__":
    app.run(debug=True)