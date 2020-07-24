class Request:
    def __init__(self, request):
        self.request_id = request[0]
        self.request_date = request[1]
        self.request_status = request[2]
        self.request_type = request[3]
        self.rental_start_date = request[4]
        self.rental_period = request[5]
        self.UserID = request[6]
        self.PropertyID = request[7]
