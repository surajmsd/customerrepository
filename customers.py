class Customers:

    def __init__(self):
        self.customers = []

    def add_book(self,cust_name,cust_city,phone,state):
        new_customers = {}
        new_customers["custname"] = cust_name
        new_customers["custcity"] = cust_city
        new_customers["phone"]=phone
        new_customers["State"]=state
        self.customers.append(new_customers)
        print("Customer: {0}".format(new_customers))
        return json.dumps(new_customers)

    def del_book(self,phone):
        found = False
        for idx, cusr in enumerate(self.customers):
            if book["Phone"] == phone:
                index = idx
                found = True
                del self.customers[idx]
        print("books: {0}".format(json.dumps(self.customers)))
        return found

    def get_all_customers(self):
        return self.customers

    def json_list(self):
        return json.dumps(self.cusomers)
