from datetime import datetime
from flask import Flask, request, jsonify

from timeclock import TimeClock

timeclock = TimeClock()
app = Flask(__name__)

@app.route('/api/get_users', methods=['GET'])
def get_users():
    """
    Endpoint to retrieve the list of users.

    Returns a JSON with a list of users, each represented by their UID, name, and user ID.
    
    Returns:
        JSON: A JSON object containing user details in 'users_list'.
              In case of an error, returns an error message and status 503.
    """
    try:
        users_list = timeclock.get_users_list()
        users = []

        for u in users_list:
            user = {
                "uid": u.uid,
                "name": u.name,
                "user_id": u.user_id
            }
            users.append(user)
        
        return jsonify(data={'users_list': users},status=200, mimetype='application/json')
    
    except Exception as e:
        return jsonify(data={'message': format(e)},status=503, mimetype='application/json')
    
    
@app.route('/api/get_attendance', methods=['GET'])
def get_attendance():
    """
    Endpoint to retrieve the attendance log.

    Returns a JSON with a list of attendance records, each containing UID, user ID, and timestamp.
    
    Returns:
        JSON: A JSON object containing an 'attendance' list with detailed records.
              In case of an error, returns a JSON object with an error message and status 503.
    """
    try:
        attendance_log = timeclock.get_attendance_list()
        attendance_records = []

        for r in attendance_log:
            record = {
                "uid": r.uid,
                "user_id": r.user_id,
                "timestamp": r.timestamp
            }
            attendance_records.append(record)
        
        return jsonify(data={'attendance': attendance_records},status=200, mimetype='application/json')
    
    except Exception as e:
        return jsonify(data={'message': format(e)},status=503, mimetype='application/json')
    

@app.route('/api/get_time', methods=['GET'])
def get_time():
    """
    Endpoint to retrieve the current time.

    Returns a JSON with the current clock time.
    
    Returns:
        JSON: A JSON object containing 'current time'.
              In case of an error, returns an error message and status 503.
    """
    try:
        current_time = timeclock.get_current_time()
    
        return jsonify(data={'current time': current_time},status=200, mimetype='application/json')
    except Exception as e:
        return jsonify(data={'message': format(e)},status=503, mimetype='application/json')

    
@app.route('/api/set_time', methods=['POST'])
def set_time():
    """
    Endpoint to retrieve the clock's status.

    Returns a JSON with the clock's status information.
    
    Returns:
        JSON: A JSON object containing 'clock_status'.
              In case of an error, returns an error message and status 503.
    """
    try:
        new_time = request.get_json()

        new_time = datetime.strptime(new_time["time"],'%Y-%m-%d %H:%M:%S')

        current_time = timeclock.set_time_device(new_time)
    
        return jsonify(data={'current time': current_time},status=201, mimetype='application/json')
    except Exception as e:
        return jsonify(data={'message': format(e)},status=503, mimetype='application/json')
    

if __name__ == '__main__':
    from waitress import serve
    serve(app,host='0.0.0.0',port=8080)
