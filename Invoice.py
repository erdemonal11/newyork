from datetime import datetime


class Invoice:
     

    def __init__(self,
                 sender_name,
                 recipient_name,
                 sender_address,
                 recipient_address,
                 sender_email,
                 recipient_email):
        
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        
        self.date = datetime.now()
        self.cost = 0
        self.items = []
        self.comments = []

    def add_item(self, name, price, tax):
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }
        self.items.append(item)

    def calculate_total(self, discount):
        total = 0
        for item in self.items:
            price = item["price"]
            tax = item["tax"]
            total += price + price * tax
        total *= 1 - discount / 100   
        return total

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments(self):
        return "\n".join(self.comments)


if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, .1)
    invoice.add_item("Equipment Rental", 1000, .1)
    invoice.add_item("Fear Tax", 340, 0.0)

  
    invoice.add_comment("Additional charges due to complexity.")
    invoice.add_comment("Discount applied for repeat customer.")

    invoice_total = invoice.calculate_total(20)
    print("Invoice Total:", invoice_total)
    
 
    print("\nComments:\n", invoice.get_comments())
