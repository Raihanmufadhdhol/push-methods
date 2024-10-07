#membuat class order
class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount

    def calculate_tax(self, tax_rate):
        tax = self.total_amount * tax_rate
        return tax

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Order Date: {self.order_date}")
        print(f"Total Amount: {self.total_amount}")
        
class OrderProcessor:
    def __init__(self):
        self.list_order = []
        
    def add_order(self, order):
        self.list_order.append(order)
        
    def calculate_total_revenue(self):
        total_revenue = sum(order.total_amount for order in self.list_order) # menghitung total pendapatan untuk semua pesanan
        return total_revenue
    
    def calculate_total_tax(self, tax_rate):
        total_tax = sum(order.calculate_tax(tax_rate) for order in self.list_order) # menghitung total pajak untuk semua pesanan
        return total_tax
    
    def display_orders(self):
        for order in self.list_order:
            order.display_order()
            print("-" * 30)
           
if __name__ == "__main__":
    order1 = Order("001", "Wilson", "08 September 2024", 50000)
    order2 = Order("002", "Miguel", "10 September 2024", 106000)
    order3 = Order("003", "Rado", "11 September 2024", 700000)
    
    #membuat objek oderprosessor
    processor = OrderProcessor()
    
    # menambahkan pesanan ke dalam orderprosessor
    processor.add_order(order1)
    processor.add_order(order2)
    processor.add_order(order3)
    
    #menampilkan detail semua pesanan
    print(f"\nOrder Details:")
    processor.display_orders()
    
    # menghitung dan menampilkan total pendapatan
    total_revenue = processor.calculate_total_revenue()
    print(f"Total Revenue: {total_revenue}")
    
    #menghitung dan menampilkan total pajak dengan tarid pajak 10%
    total_tax = processor.calculate_total_tax(0.1)
    print(f"Total Tax (at {0.1*100}%): {total_tax:.2f}")