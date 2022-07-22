import agency

p = agency.plane(20, 100)

while 1:
    print("\n\t\t|-----------------------|",
            "\t\t|1- book a ticket       |",
            "\t\t|2- get info of a ticket|",
            "\t\t|3- refund a ticket     |",
            "\t\t|4- exit                |",
            "\t\t|-----------------------|", sep="\n")
    try:
        cmd = int(input())
    except:
        print("undefined command!")
        continue

    if cmd == 1:
        print("5- back to main menu")
        name = input("enter your name:")
        if name == '5': continue
        n_c = int(input("enter the number of seats you want to book:"))
        if n_c == 5: continue
        id = p.buy(name, n_c)
        if id == -1:
            print(f"not enough chairs. there is {p.chairs.count(False)} free seats remained")
        else:
            print("booked successfuly. Your Ticket number is", id)

    elif cmd == 2:
        print("5- back to main menu")
        id = int(input("Enter your Ticket number you want it's info:"))
        if id == 5: continue
        ticket = p.info(id)
        if ticket != None:
            print(f"ticke number: {ticket.id}", f"number of seats for the ticket: {ticket.no}",
                  f"chairs number: {ticket.chair}", sep="\n")
        elif ticket == None:
            print("No such ticket was found")

    elif cmd == 3:
        print("5- back to main menu")
        id = int(input("enter the Ticket number you want to refund:"))
        if id == 5: continue
        if p.refund(id):
            print("refunded successfuly")
        else:
            print("Failed! please check you ticket number")

    elif cmd == 4:
        break
    else:
        print("undefined command!")