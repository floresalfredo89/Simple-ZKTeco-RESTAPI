from datetime import datetime
from zk import ZK

## This is file is for test only

class User:

    def __init__(self,uid,name,user_id):
        self.uid = uid
        self.name = name
        self.user_id = user_id

class Attendance:

    def __init__(self,uid,user_id,timestamp):
        self.uid = uid
        self.user_id = user_id
        self.timestamp = timestamp

class TimeClock:

    def set_time_device(self):
        return "2024-01-24 10:11:12"

    def get_current_time(self):
        return "2025-01-24 14:20:10"

    def get_users_list(self):

        return [User(1,'Jair',1),User(2,'Sara',2)]

    def get_attendance_list(self):

        return [Attendance(1,1,'2025-01-24 08:10:05'),Attendance(2,2,'2025-01-24 08:12:25')]