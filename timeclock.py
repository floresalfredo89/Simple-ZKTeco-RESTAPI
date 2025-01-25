from datetime import datetime
from zk import ZK

class TimeClock:

    conn = None
    zk = object

    def __init__(self, ip='192.168.1.201', port=4370):
        """
        Initializes a new instance of TimeClock.

        Establishes a connection to the time clock device using specified IP and port.
        
        The ZK class is initialized with:
            - IP address: '192.168.1.201'
            - Port: 4370
            - Timeout: 5 seconds
            - Force UDP usage: True
        """
        self.zk = ZK(ip,port,timeout=5,force_udp=True)

    def _connect(self):
        """
        Establishes a connection to the time clock device if not already connected.

        Disables the device during communication for security or operational purposes.
        """
        if not self.conn:
            self.conn = self.zk.connect()
        self.conn.disable_device()

    def _disconnect(self):
        """
        Disconnects from the time clock device and re-enables it.

        Ensures that any active connection is properly terminated.
        """
        self.conn.enable_device()
        if self.conn:
            self.conn.disconnect()

    def set_time_device(self,date: datetime):
        """
        Sets the current time of the time clock device.

        Parameters:
            date (datetime): The new datetime to be set on the device.
        
        Returns:
            str: A string representing the current time of the device in 'YYYY-MM-DD HH:MM:SS' format
                 after setting it to the specified date and time.
        """
        self._connect()

        self.conn.set_time(self,date)
        current_time = self.conn.get_time()

        self._disconnect()
        
        return current_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_current_time(self):
        """
        Retrieves the current time from the time clock device.

        Returns:
            str: A string representing the current time of the device in 'YYYY-MM-DD HH:MM:SS' format.
        """
        self._connect()

        current_time = self.conn.get_time()
        
        self._disconnect()

        return current_time.strftime('%Y-%m-%d %H:%M:%S')

    def get_users_list(self):
        """
        Fetches a list of users registered on the time clock device.

        Returns:
            list: A list containing user data fetched from the device.
        """
        self._connect()

        users_list = self.conn.get_users()

        self._disconnect()

        return users_list

    def get_attendance_list(self):
        """
        Retrieves a log of attendance records from the time clock device.

        Returns:
            object: An object containing attendance data fetched from the device.
        """
        self._connect()

        attendance_log = self.conn.get_attendance()

        self._disconnect()

        return attendance_log