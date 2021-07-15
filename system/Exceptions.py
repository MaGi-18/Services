class WrongParametertypeError(Exception):
    def __str__(self):
        return "Falscher Typ für den Übergabeparameter."