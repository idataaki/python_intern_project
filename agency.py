class Ticket:
    def __init__(self, id, no, chair):
        self.id = id
        self.no = no
        self.chair = chair

class Plane:
    def __init__(self, c_no, start_id):
        self.c_no = c_no
        self.start_id = start_id
        self.chairs = [False for i in range(c_no)]
        self.all_ticket = []

    def get_free_seats(self):
        return [i for i in range(len(self.chairs)) if self.chairs[i] == False]

    def get_free_seats_dist(self, lst):
        return [lst[i] - lst[i - 1] for i in range(1, len(lst))]

    def find_nearest_seats(self, c_n, dist):
        _c_n = c_n-1
        min_w = self.c_no + 10
        window, end = 0, 0
        for i in range(len(dist)):
            window += dist[i]
            if i + 1 >= _c_n:
                if min_w > window:
                    min_w = window
                    end = i
                window -= dist[i + 1 - _c_n]
        start = end - _c_n + 1
        end = end + 2
        return start, end

    def select_seats(self, c_n):
        lst = self.get_free_seats()
        dist = self.get_free_seats_dist(lst)
        start, end = self.find_nearest_seats(c_n, dist)
        return [lst[i] for i in range(start, end)]

class Agency:
    def __init__(self, plane):
        self.plane = plane

    def assign_id(self):
        id = self.plane.start_id
        self.plane.start_id += 1
        return id

    def fill_seats(self, op_chairs):
        for i in op_chairs:
            self.plane.chairs[i] = True

    def refund_seats(self, ticket):
        self.plane.all_ticket.remove(ticket)
        for i in ticket.chair:
            self.plane.chairs[i] = False

    def buy(self, customer_name, customer_c_no):
        if customer_c_no > len(self.plane.get_free_seats()):
            return -1
        id = self.assign_id()
        op_chairs = self.plane.select_seats(customer_c_no)
        self.fill_seats(op_chairs)
        self.plane.all_ticket.append(Ticket(id, customer_c_no, op_chairs))
        return id

    def get_info(self, id):
        return next((t for t in self.plane.all_ticket if t.id == id), None)

    def refund(self, id):
        customer_t = next((t for t in self.plane.all_ticket if t.id == id), None)
        if customer_t != None:
            self.refund_seats(customer_t)
            return True
        return False