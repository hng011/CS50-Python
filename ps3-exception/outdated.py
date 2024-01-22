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

def check_len(m, d) -> tuple:
    if not ( int(d) > 31 or int(m) > 12):
        if len(m) < 2:
            m = "0"+m
        if len(d) < 2:
            d = "0"+d
        return (m, d)
    else:
        date_conv()

def remove_wp(m, d, y):
    return (m.replace(' ',''), d.replace(' ',''), y.replace(' ',''))

def date_conv() -> str:
    while(True):
        try:
            x = input("Date: ").lower()

            if "/" in x:
                m, d, y = x.split("/")
                m, d, y = remove_wp(m, d, y)
                m, d = check_len(m, d)
                return f"{y}-{m}-{d}"

            elif x[:3] in months:
                dm, y = x.split(",")
                m, d = dm.split(" ")
                m, d, y = remove_wp(m, d, y)
                m = str(months.index(m[:3])+1)
                m, d = check_len(m, d)
                return f"{y}-{m}-{d}"

        except EOFError:
            return 0

        except Exception as e:
            print(e)

print(date_conv())
