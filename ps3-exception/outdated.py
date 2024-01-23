months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Set to low
months = [v.lower()[:3] for v in months]

def check_len(m:str, d:str) -> tuple:
    if not ( int(d) > 31 or int(m) > 12):
        if len(m) < 2:
            m = "0"+m
        if len(d) < 2:
            d = "0"+d
        return (m, d)
    else:
        date_conv()

def formatted_date(m:str, d:str, y:str) -> str:
    m, d, y = (m.replace(' ',''), d.replace(' ',''), y.replace(' ',''))    
    m, d = check_len(m, d)
    return f"{y}-{m}-{d}"

def date_conv() -> str:
    while(True):
        try:
            x = input("Date: ").lower()

            if "/" in x:
                m, d, y = x.split("/")
                return formatted_date(m, d, y)

            elif x[:3] in months:
                md, y = x.split(",")
                m, d = md.split(" ")
                m = str(months.index(m[:3])+1)
                return formatted_date(m, d, y)

        except EOFError:
            return 0

        except Exception as e:
            print(e)

print(date_conv())