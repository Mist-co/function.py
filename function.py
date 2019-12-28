def mcd(a, b):
    """mcd() calcola il massimo comun divisore di due interi (o stringhe di cifre)"""
    try:
        resto = int(a) % int(b)
        while resto != 0:
            a = b
            b = resto
            resto = a % b
        return b
    except (TypeError):
        print("La funzione mcd() gestisce due interi, non le liste: consultare gcd() per una lista.")
    except (ValueError):
        print("La funzione gcd() non gestisce le stringhe di caratteri, ma di cifre.")
        
def gcd(a):
    """gcd() calcola il massimo comun divisore tra tutti i valori interi (o stringhe di cifre) di una lista"""
    try:
        c = int(a[0])
        for d in range(1, len(a)):
            c = mcd(c, int(a[d]))
        return c
    except (TypeError):
        print("La funzione gcd() gestisce le liste, non gli interi: consultare mcd() per due interi.")
    except (IndexError):
        print("L'oggetto passato alla funcione gcd() non risponde ai requisiti: forse è vuota?")
    except (ValueError):
        print("La funzione gcd() non gestisce le stringhe di caratteri, ma di cifre.")        
    

def mcm(a, b):
    """mcm() calcola il minimo comune multiplo di due interi (o stringhe di cifre)"""
    try:
        temp = mcd(int(a), int(b))
        if temp:
            return (int(a) // temp * int(b))
        else:
            return 0
    except (TypeError):
        print("La funzione mcm() gestisce due interi, non le liste: consultare lcm() per una lista.")
    except (ValueError):
        print("La funzione mcm() non gestisce le stringhe di caratteri, ma di cifre.")

def lcm(a):
    """lcm() calcola il minimo comune multiplo tra tutti i valori interi (o stringhe di cifre) di una lista"""
    try:
        c = int(a[0])
        for d in range(1, len(a)):
            c = mcm(c, int(a[d]))
        return c
    except (TypeError):
        print("La funzione lcm() gestisce le liste, non gli interi: consultare mcm() per due interi.")
    except (IndexError):
        print("L'oggetto passato alla funcione lcm() non risponde ai requisiti: forse è vuota?")
    except (ValueError):
        print("La funzione lcm() non gestisce le stringhe di caratteri, ma di cifre.")

def invstr(a):
    """invstr() restituisce la stringa di caratteri (o di cifre) inversa a quella data"""
    try:
        a = str(a)
        return a[::-1]
    except (TypeError):
        print("La funzione invstr() non gestisce gli interi: consultare invint() per gli interi.")

def invint(a):
    """invint() restituisce un intero (anche come stringa di cifre) inverso a quello dato"""
    try:
        T = int(a)
        R = 0
        while T > 0:
            R = R * 10 + (T % 10);
            T //= 10;
        return R;
    except (TypeError):
        print("La funzione invint() non gestisce le stringhe o liste di numeri: consultare invstr() per le stringhe.")

def get(path_file, tipo = 'int', sep = ' '):
    """get() prende il percorso del file e restituisce una lista dei dati contenuti in esso.
tipo = 'int' restituisce una lista di interi
tipo = 'str' restituisce una lista di stringhe
'sep' è il valore che la funzione sfrutterà per prelevare i valori
(predefinito -sempre- '\\n')"""
    try:
        data = []
        dati = ""
        file = open(path_file, 'r')
        raw_input = file.read()
        if raw_input != '':
            raw_length = len(raw_input)
            file.seek(0)
            while raw_length != 0:
                dato = file.read(1)
                raw_length -= 1
                if raw_length == 0 and dato != '\n':
                    dati = dati + dato
                    if tipo == 'int':
                        data.append(int(dati))
                    elif tipo == 'str':
                        data.append(dati)
                    else:
                        error = tipo + " non è un tipo accettabile"
                        return error
                    dati = ""
                elif dato == sep or dato == '\n':
                    if tipo == 'int':
                        data.append(int(dati))
                    elif tipo == 'str':
                        data.append(dati)
                    else:
                        error = tipo + " non è un tipo accettabile"
                        return error
                    dati = ""
                else:
                    dati = dati + dato
            file.close()
            return data
        else:
            return None
    except (OSError):
        if tipo=='str':
            print("Il file non esiste o non è accessibile: controlla il percorso")
        elif tipo=='int':
            print(-1)
    except (ValueError):
        print("Se il file contiene stringhe imposta tipo su 'str': possibile problema di conversione") 
