class Session:
    def __init__(self, session_id, start_time, end_time, status="scheduled"):
        self.session_id = session_id
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def start_session(self):
        self.status = "ongoing"
        return "Session started."

    def end_session(self):
        self.status = "completed"
        return "Session ended."