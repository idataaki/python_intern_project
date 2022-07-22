class Ticket:
    def __init__(self, id, no, chair):
        self.id = id
        self.no = no
        self.chair = chair

class plane:
    def __init__(self, c_no, start_id):
        self.c_no = c_no
        self.start_id = start_id
        self.chairs, self.all_ticket = [False for i in range(c_no)], []

    def optimal_chairs(self, c_n):
        _c_n = c_n-1
        lst = [i for i in range(len(self.chairs)) if self.chairs[i] == False]
        dist = [lst[i]-lst[i-1] for i in range(1, len(lst))]

        min_w = self.c_no+10
        window, end = 0, 0
        for i in range(len(dist)):
            window+=dist[i]
            if i+1 >= _c_n:
                if min_w > window:
                    min_w = window
                    end = i
                window -= dist[i+1 - _c_n]
        start = end - _c_n + 1
        end = end + 1
        return [lst[i] for i in range(start, end+1)]

    def buy(self, customer_name, customer_c_no):
        if customer_c_no > self.chairs.count(False):
            return -1
        id = self.start_id
        self.start_id += 1
        op_chairs = self.optimal_chairs(customer_c_no)
        for i in op_chairs:
            self.chairs[i] = True
        self.all_ticket.append(Ticket(id, customer_c_no, op_chairs))
        return id

    def info(self, id):
        return next((t for t in self.all_ticket if t.id == id), None)

    def refund(self, id):
        customer_t = next((t for t in self.all_ticket if t.id == id), None)
        if customer_t != None:
            self.all_ticket.remove(customer_t)
            for i in customer_t.chair:
                self.chairs[i] = False
            return True
        return False