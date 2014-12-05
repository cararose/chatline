from flask import Flask
app = Flask(__name__)

@app.route("/incoming_call")
def incoming_call():
    # This handles the incoming calls
    twiml = '''
            <?xml version="1.0" encoding="UTF-8"?>
            <Response>
                <Gather timeout="10" finishOnKey="*">
                    <Say>Please enter your pin number and then press star.</Say>
                </Gather>
            </Response>
            '''

    return Response(twiml, mimetype='text/xml')