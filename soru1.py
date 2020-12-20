import re

def hepsiASCIIMi(dizge):
    return all(ord(k) < 128 for k in dizge)

def ePostaGeçerliMi(adres):
    if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z", adres, re.IGNORECASE):
        if (hepsiASCIIMi(adres)):
            return True
        else:
            return False
    return False

def main():
    email = input ("Lütfen bir e posta adresi giriniz: ")

    if (ePostaGeçerliMi(email)):
        print('Girilen adres geçerli')
    else:
        print('Girilen adres geçersiz')

if __name__ == "__main__":
    main()