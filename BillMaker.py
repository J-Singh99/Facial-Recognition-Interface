def Billing(checklist, known_face_names, db):
    bill = {}
    for i in range(len(checklist)):
        if checklist[i]:
            name = known_face_names[i]
            
            for j in db:
                if name == db[j]['Name']:
                    ID = db[j]['ID']
                    print('Preparing bill for ' + name + ' :')
                    
                    Entry = {
                        'ID' : ID,
                        'Items' : []
                    }
                    
                    inp = 'Y'
                    while(inp == 'Y'):
                        Name = input('Enter Item Name : ')
                        Price = input('Enter price of Item: ')
                        Qty = input('Enter quantity of Item purchased: ')
                        Entry['Items'].append((Name, Price, Qty))
                        inp = input('Enter "Y" to enter another item.')
                        
                        bill[i] = Entry
                        print('Bill Completed')
                        print()
                        print()

    return bill

def DoCalc(ID, bill):
    for j in bill:
        try:
            print('Here')
            if bill[j]['ID'] == ID:
                
                items = bill[j]['Items']
                sum_ = 0
                
                print('Item Name => Item Price x Item Quantity = Total')
                
                for item in items:
                    item_name = item[0]
                    item_price = item[1]
                    item_quantity = item[2]
                    total = int(item_price) * int(item_quantity)
                    sum_ += total
                    
                    print(item_name, end = ' => ')
                    print(str(item_price), end = ' x ')
                    print(str(item_quantity), end = ' = ')
                    print(str(total))
                
                print('The total bill amounts up to ' + str(sum_))
                break

            else:
                print('else')
                
        except:
            print('Billing Error!!!')