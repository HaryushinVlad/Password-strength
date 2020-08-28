import urwid

def is_very_long(password):
    return len(password) > 12

def has_digit(password):
    return any(symbol.isdigit() for symbol in password)

def has_letters(password):
    return any(symbol.isalpha() for symbol in password)

def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)

def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)

def has_symbols(password):
    return any(not symbol.isdigit() and not symbol.isalpha() for symbol in password)

def doesnt_consist_of_symbols(password):
    return any(symbol.islower() or symbol.isalpha() for symbol in password)

def count_rating(password):
    checks = [is_very_long, has_digit, has_letters, has_upper_letters, has_lower_letters, has_symbols, doesnt_consist_of_symbols]
    rating = 0
    
    for score in checks:
        if score(password):
            rating += 2
    return rating

def on_ask_change(edit, password):
    reply.set_text("Рейтинг этого пароля: %s" % count_rating(password))

if __name__ == "__main__":
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
    password = input(ask)