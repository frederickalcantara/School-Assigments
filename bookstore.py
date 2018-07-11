def login (un_pw):
    if not un_pw:
        return False
    else:
      username = input("Enter your username (or r to register):").lower()
      while username not in un_pw and username.lower() != 'r':
          username = input("Enter a valid username (or r to register)")
      if username.lower() == 'r':
          return False
      else:
          password = input("Enter your password: ")
          while password != un_pw[username]:
              password = input("Enter your password please:")
              print("You are now logged in")
          return True
def register (un_pw):
    un = input("Please register a new username: ").lower()
    pw = input("Enter a password of 6 characters or more: ")
    while len(pw) < 5:
        print("You did not enter a password of 6 characters of more.")
        pw = input("Enter a password of 6 characters or more:")
    un_pw[un] = pw
    print("Your login info has been created!")
    return un_pw
def menu_text():
    print("Main Menu")
    print("Press A to Add books")
    print("Press D to Delete books")
    print("Press F to Find a book")
    print("Press S to Sell a book")
    print("Press X to Log out")
def get_menu_option():
    menu_text()
    menu_select = input("Enter a command:").lower()
    while menu_select not in ('f', 'x', 'a', 'd', 's'):
        print("Error: Invalid command")
        menu_text()
        menu_select = input("Enter a command:").lower()
    return menu_select
def find(books_prices):
    options = list(books_prices.items())
    for i, (k,v) in enumerate(options):
        print("Type", i + 1, "for", k)
    num = input("Which book would you like to access")
    while not num.isnumeric() or 1 > int(num) or int(num) > len(options):
        print("Please select a number that is within the range: ")
        for i, (k,v) in enumerate(options):
            print("Select", i + 1, "for", k)
        num = input("Which book would you like to access")
    i = int(num) - 1
    title = options[i][0]
    price = str(options[i][1])
    print(title + ": $" + price)
    question = input("Anymore books you are looking for? Y or N").lower()
    while question not in ('n', 'y'):
        question = input("Press Y or N if you want to continue looking for books").lower()
    if question == 'y':
        return True, books_prices
    else:
        return False, books_prices


def add(books_prices):
    print(str(books_prices))
    newbook = input("What book would you like to add?").title()
    newcost = input("What is the cost of " + str(newbook) + "?")
    try:
        while float(newcost) < 0 or not float(newcost):
            print("Please enter a number:")
            newcost = input("What is the cost of " + str(newbook) + "?")
    except ValueError:
        newcost = input("What is the cost of " + str(newbook) + "?")
    books_prices[newbook] = newcost
    question = input("Anymore books you would like to add? Y or N").lower()
    while question not in ('y', 'n'):
        print("Please enter a valid command.")
        question = input("Anymore books you would like to add? Y or N").lower()
    if question == 'y':
        return True, books_prices
    else:
        return False, books_prices


def delete(books_prices):
    options = list(books_prices.items())
    for i, (k,v) in enumerate(options):
        print("Select", i + 1, "to delete", k)
    num = input("Which book would you like to delete")
    while not num.isnumeric() or 1 > int(num) or int(num) > len(options):
        print("Please select a number that is within the range: ")
        for i, (k,v) in enumerate(options):
            print("Select", i + 1, "for", k)
        num = input("Which book would you like to delete")
    i = int(num) - 1
    title = options[i][0]
    price = str(options[i][1])
    print(title + ": $" + price + " is now being deleted")
    options.remove(options[i])
    print(options)
    books_prices = dict(options)
    question = input("Press Y or N if you want to continue deleting books").lower()
    while question not in ('n', 'y'):
        question = input("Press Y or N if you want to continue deleting books").lower()
    if question == 'y':
        return True, books_prices
    else:
        print(books_prices)
        return False, books_prices

def sell(books_prices):
    options = list(books_prices.items())
    for i, (k,v) in enumerate(options):
        print("Select", i + 1, "to sell", k)
    num = input("Which book would you like to sell")
    while not num.isnumeric() or 1 > int(num) or int(num) > len(options):
        print("Please select a number that is within the range: ")
        for i, (k,v) in enumerate(options):
            print("Select", i + 1, "for", k)
        num = input("Which book would you like to sell")
    i = int(num) - 1
    subtotal = float(options[i][1])
    taxes = subtotal * 0.07
    tax = round(taxes, 2)
    book = options[i][0]
    shipping = 3.00
    order = [subtotal, tax, shipping]
    total = sum(order)
    print(book + " is now being sold")
    print("The subtotal is: $" + str(subtotal))
    print("The tax is: $" + str(tax))
    print("The shipping & handling cost is: $" + str(shipping))
    print("The total is: $" + str(total))
    options.remove(options[i])
    print(options)
    books_prices = dict(options)
    question = input("Press Y or N if you want to continue selling books").lower()
    while question not in ('n', 'y'):
        question = input("Press Y or N if you want to continue selling books").lower()
    if question == 'y':
        return True, books_prices
    else:
        print(books_prices)
        return False, books_prices
def main():
    has_started = True
    user_quit = False
    while not user_quit:
        if has_started:
            books = {'Games of Thrones': 50.00, 'Lord of the Rings': 25.00, 'Fantastic Beasts and Where to Find Them': 10.00}
            users = {'fred': 'luffy1'}
            valid_login = False
            has_started = False

        while not valid_login:
            valid_login = login(users)
            if not valid_login:
                users = register(users)

        menu_select = get_menu_option()
        if menu_select == 'a':
            while True:
                add_another, books = add(books)
                if add_another:
                    continue
                else:
                    break
        elif menu_select == 'f':
            while True:
                find_another, books = find(books)
                if find_another:
                    continue
                else:
                    break
        elif menu_select == 'd':
            while True:
                delete_another, books = delete(books)
                if delete_another:
                    continue
                else:
                    break
        elif menu_select == 's':
            while True:
                sell_another, books = sell(books)
                if sell_another:
                    continue
                else:
                    break
        else:
            print("Logging out")
            valid_login = False
main()