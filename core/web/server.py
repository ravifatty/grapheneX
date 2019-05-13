from flask import Flask, render_template
from core.utils.logcl import GraphenexLogger
from flask_socketio import SocketIO, emit

logger = GraphenexLogger(__name__)
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def main():
    return render_template('index.html', title="grapheneX [Web]")

def run_server(server_params=('0.0.0.0', '8080')):
    logger.info("Starting server...")
    try:
        socketio.run(app, host=server_params[0], port=int(server_params[1]), debug=False)
    except (PermissionError, ValueError):
        logger.error('Invalid host & port address. Restarting with default host and port.')
        run_server()
    except Exception as e:
        logger.error('Unable to start server: ' + str(e))
        
@socketio.on('my_event')
def handle_my_event(json):
    emit('Test Response', json)
