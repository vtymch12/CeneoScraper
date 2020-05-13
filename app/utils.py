

#funkcja do usuwania znaków formatujacych
def remove_whitespaces(string):
    try:
        return string.replace("\n", ", ").replace("\r", ", ")
    except AttributeError:
        pass
