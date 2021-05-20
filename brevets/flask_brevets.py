"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 1000, type=float)
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    # FIXME!
    # Right now, only the current time is passed as the start time
    # and control distance is fixed to 200
    # You should get these from the webpage!
    
    # Basic Logic -- Error Handlers
        #1 Check user input is valid or not, if valid
            #1.1 If user input exceed the maximum distance, then raise an error
        #2 If not valid, asking user re-enter a valid value

    # Get input from client_side
    user_input_in_km = request.args.get('km', type=str)
    if user_input_in_km.isdigit():
        if user_input_in_km > km:
            # Put everything in 1 line, if not work, have to edit them seperately.
            return flask.jsonify({"open": request.args.get("begin_date"), "close": request.args.get("begin_date"), "error_msg": "The checkPoint located at the place that exceed the maximum distance"})
    else:
        return flask.jsonify({"open": request.args.get("begin_date"), "close": request.args.get("begin_date"), "error_msg": "Please enter a valid value!"})
    
    # If data valid, then call the functions we have in acp_times to calculate.
    open_time = acp_times.open_time(km, 200, arrow.now().isoformat).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, 200, arrow.now().isoformat).format('YYYY-MM-DDTHH:mm')
    # Packing open_time and close_time in a dictionary and sent in JSON.
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)



#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
