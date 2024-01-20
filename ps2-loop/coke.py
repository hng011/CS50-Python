def main() -> None:
    c=0
    a=50
    ch=0
    while c < 50: 
        print("Amount Due:",a-c)
        cinp = int(input("Insert Coin: "))
        match cinp:
            case 5: c+=5                
            case 10: c+=10
            case 25: c+=25
            case _ : continue    
        ch = (a-c)*-1
    print("Change Owed:",ch)    

main()