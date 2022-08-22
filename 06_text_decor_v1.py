# function text_decor to add symbols for decoration around statements
# parameters are the text that needs to be decorated and the symbol it is decorated with
# this function returns an empty string
def text_decor(text, symbol):
    text = "{}".format(text)
    up_down = symbol * len(text)
    print(up_down)
    print(text)
    print(up_down)
    return ""


# main routine******************************************
text_decor("Welcome to the General Knowledge Quiz!", "★")  # print decoration with stars
print()
text_decor("Correct!", "✓")  # print decoration with ticks
print()
text_decor("Incorrect!", "✕")  # print decoration with crosses
