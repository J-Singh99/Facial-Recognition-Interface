def DoCalc(ID, bill):
    for j in bill:
        try:
            if bill[j]['ID'] == ID:
                
                items = bill[j]['Items']
                sum_ = 0
                
                print('Item Name => Item Price x Item Quantity = Total')
                
                for item in items:
                    item_name = item[0]
                    item_price = item[1]
                    item_quantity = item[2]
                    total = item_price * item_quantity
                    sum_ += total
                    
                    print(item_name, end = ' => ')
                    print(str(item_price), end = ' x ')
                    print(str(item_quantity), end = ' = ')
                    print(str(total))
                
                print('The total bill amounts up to ' + str(sum_))
                break

            else:
                pass
                
        except:
            print('Billing Error!!!')


BILL = {}

Entry1 = {
	'ID' : 1,
	'Items' : [('Bears', 2, 2),
			   ('Beets', 500, 10),
			   ('Battle Star Galactica', 1500, 1),
			   ('Pepsi', 25, 4)]
}

Entry2 = {
	'ID' : 2,
	'Items' : [('Guitar', 2000, 2),
			   ('TV', 50000, 1),
			   ('Football', 500, 1),
			   ('Pepsi', 25, 4)]
}

Entry3 = {
	'ID' : 3,
	'Items' : [('White House', 10000, 1),
			   ('AK-47', 5000, 1000),
			   ('Tie', 500, 5),
			   ('Doughnut', 17, 10)]
}

Entry4 = {
	'ID' : 4,
	'Items' : [('Tesla', 1000, 2),
			   ('Falcon', 50000, 3),
			   ('Flame Thrower', 13000, 3)]
}

Entry5 = {
	'ID' : 5,
	'Items' : [('Mask', 20000, 4),
			   ('Cape', 50, 10),
			   ('Bat Mobile', 15000, 6),
			   ('Batrang', 25, 4000)]
}

BILL[1] = Entry1
BILL[2] = Entry2
BILL[3] = Entry3
BILL[4] = Entry4
BILL[5] = Entry5