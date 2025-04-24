import os, sys, time, socket, hashlib, argparse
import colorama
from colorama import *
import rich
import future

stop="\033[0m"
red="\033[91;1m"
cyan="\033[96;1m"
blue="\033[94;1m"
green="\033[92;1m"
yellow="\033[93;1m"
purple="\033[95;1m"


def get_version():
    try:
        with open("./src/version", "r") as file:
            version = file.read().strip()
        return str(version)
    except FileNotFoundError:
        return "Versiya faylı tapıla bilmədi."

add=f"{purple}[{stop}+{purple}]{green} "
error=f"{purple}[{stop}-{purple}]{red} "
info=f"\033[97;1m[{purple}•\033[97;1m]{purple} "
note=f"\033[97;1m[{purple}!\033[97;1m]{purple} "
version = get_version()
kodlar = ["994", "011", "010", "995"]

def slow(F3):
    for a in F3 + '\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1./600)

def load(F3):
    for x in F3:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./600)
    for a in '\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1./600)
    


def show_menu():
    usage = f"""
İstifadə: python3 {sys.argv[0]} [SEÇİMLƏR...]
--------------------------------------------
      | SEÇİMLƏR
      |---------
            | -u <Skriptin Yenilənməsi>        | Geo-Phone skriptini daha yaxşı performans üçün yenilə
            | -c <Qurbanın Ölkə Kodu>          | Qurbanın ölkə kodunu '+' işarəsi olmadan qeyd et (məs. 994)
            | -p <Qurbanın Telefon Nömrəsi>    | Qurbanın telefon nömrəsini daxil et

      | NÜMUNƏLƏR
      |---------
            | python3 {sys.argv[0]} -u                    | Skriptin yenilənməsi
            | python3 {sys.argv[0]} -c 994 -p 501234567   | Ölkə kodu və telefon nömrəsinin qeyd edilməsi

      | ÖLKƏ KODLARI
      |---------
            | {kodlar}
"""
    return usage
    os.sys.exit()

def banner():
    os.system("clear || cls")
    return f"""{red} 
 ▄▄▄      ▒███████▒ ██▓███   █    ██  ██▓      ██████ ▓█████ {cyan}Versiya:{stop} {version}{red}
▒████▄    ▒ ▒ ▒ ▄▀░▓██░  ██▒ ██  ▓██▒▓██▒    ▒██    ▒ ▓█   ▀ 
▒██  ▀█▄  ░ ▒ ▄▀▒░ ▓██░ ██▓▒▓██  ▒██░▒██░    ░ ▓██▄   ▒███   
░██▄▄▄▄██   ▄▀▒   ░▒██▄█▓▒ ▒▓▓█  ░██░▒██░      ▒   ██▒▒▓█  ▄ 
 ▓█   ▓██▒▒███████▒▒██▒ ░  ░▒▒█████▓ ░██████▒▒██████▒▒░▒████▒
 ▒▒   ▓▒█░░▒▒ ▓░▒░▒▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░░░ ▒░ ░
  ▒   ▒▒ ░░░▒ ▒ ░ ▒░▒ ░     ░░▒░ ░ ░ ░ ░ ▒  ░░ ░▒  ░ ░ ░ ░  ░
  ░   ▒   ░ ░ ░ ░ ░░░        ░░░ ░ ░   ░ ░   ░  ░  ░     ░   
      ░  ░  ░ ░                ░         ░  ░      ░     ░  ░
          ░                                                  
{stop}"""


try:import requests, opencage, countryinfo, phonenumbers, urllib.request
except ModuleNotFoundError:
    
    slow(banner())
    slow(f"\n{note}Bağışlayın,")
    slow(f'{info}Görünür bu skriptdə bəzi tələblər çatışmır.{red}')
    slow('===========================================================')
    slow(f'        	{green}Əmr: {purple}pip3 install -r requirements.txt --break-system-packages{red}   ')
    slow('===========================================================')
    slow('\033[0m')
    os.sys.exit()

    
from countryinfo import CountryInfo
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier, timezone, geocoder, is_valid_number

def internet():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False
    
def get_remote_hash(url):
   try:
      response = urllib.request.urlopen(url)
      data = response.read()
      return hashlib.md5(data).hexdigest()
   except Exception as e:
      slow(f"{error}Zəhmət olmasa internet bağlantınızı yoxlayın{stop}")
      slow(f"")
      os.sys.exit()

def get_local_hash(script_path):
   try:
      with open(script_path, 'rb') as f:
         data = f.read()
         return hashlib.md5(data).hexdigest()
   except Exception as e:
      slow(f"{error}Yerli skript oxuyarkən xəta oldu: {e}.{stop}\n")
      os.sys.exit()


def updateus(): 
    print(banner())
    try:
        script_url = "https://github.com/thez3nith/AZPulse/raw/main/AZPulse.py"
        script_path = os.path.abspath(__file__)
        
        remote_hash = get_remote_hash(script_url)
        local_hash = get_local_hash(script_path)
        
        if remote_hash and local_hash and remote_hash == local_hash:
            time.sleep(1)
            slow(f"{error}AZPulse artıq ən son versiyadadır.{stop}\n")
            os.sys.exit()
        
        # time.sleep(1)
        slow(f"{add}Yeniləmə tapıldı...")
        time.sleep(1)
        slow(f"{add}Ən son versiya yüklənir...")
        # time.sleep(3)
        urllib.request.urlretrieve(script_url, script_path)
        slow(f"{stop}\n")
        time.sleep(1)
        slow(f"===========================================================")
        slow(f"""{info}AZPulse uğurla yeniləndi ...""")
        os.sys.exit()

    except Exception as e:
        slow(f"")
        slow(f"{error}AZPulse yenilənərkən xəta baş verdi: {e}{stop}\n")




def infoga(cncode, number):
    print(banner())
    num = f"+{cncode}{number}"
    load(f"{add}{num} nömrəsinə qarşı rekonstruksiya skanı başlayır ...")
    time.sleep(0.5)
    try:
        load(f"{info}Əsas telefon məlumatları yüklənir ...")
        time.sleep(0.5)
        try:
            phoneNumber = phonenumbers.parse(num)
            if is_valid_number(phoneNumber):
                valid_number=True
            else:
                valid_number=False
                slow(f"{error}Telefon nömrəsi etibarsız görünür!\n")
                os.sys.exit()
        except Exception as e:
            slow(f"{error}Telefon nömrəsi ayrılarkən xəta baş verdi: {e}{stop}\n")
            os.sys.exit()
        
        gc = geocoder.description_for_number(phoneNumber,"en")
        c = carrier.name_for_number(phoneNumber,"en")
        load(f"{info}Ölkə məlumatları toplanır ...")
        time.sleep(0.5)
        if not (gc and c):
            slow(f"{error}Ölkə məlumatlarını əldə etmək mümkün olmadı!")
            time.sleep(1)
        inter = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        nation = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.NATIONAL)
        e164 = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.E164)

        load(f"{info}OSINT axtarışı aparılır ...")
        time.sleep(2)
        if not (gc and c):
            slow(f"{error}OSINT axtarışı zamanı xəta baş verdi!")
            time.sleep(1)
        gc = geocoder.description_for_number(phoneNumber,"en")
        tz = timezone.time_zones_for_number(phoneNumber)
        c = carrier.name_for_number(phoneNumber,"en")

        load(f"{info}OVH Skan aparılır ...")
        time.sleep(2)
        if not (gc and c):
            slow(f"{error}OVH Skan zamanı xəta baş verdi!")
            time.sleep(1)
        local = phoneNumber.national_number
        cncode = phoneNumber.country_code

        load(f"{info}Nömrə xəritələnir ...")
        time.sleep(1)
        load(f"{info}OK! ...")
        
        act=input(f'\n{purple}[{stop}ENTER{purple}] düyməsini sıxın davam etmək üçün{stop} ')
        time.sleep(0.5)
        print(banner())

        if (gc and c):   
            gcd = gc
            country = CountryInfo(gcd)
            iso = country.iso()["alpha2"]
            print("\033[92;1m", end="\r")

            slow("===========================================================")
            slow(f"[!] {cyan}{inter.replace(' ','-')}{green} nömrəsinin yerini təyin etməyə cəhd edilir [!]")
            slow("===========================================================")

            time.sleep(2)
            slow("")
            slow(f"    {cyan}Beynəlxalq format{blue}  :>>  {green}{inter}")
            slow(f"    {cyan}Milli format{blue}       :>>  {green}{nation}")
            slow(f"    {cyan}E164 formatı{blue}      :>>  {green}{e164}")
            slow(f"    {cyan}Yerli format{blue}      :>>  {green}{local}")
            slow(f"    {cyan}Tapılan ölkə{blue}      :>>  {green}+{cncode} ({iso})")
            slow(f"    {cyan}Ölkə adı{blue}         :>>  {green}{gcd} (+{cncode})")
            slow(f"    {cyan}Vaxt zonası{blue}      :>>  {green}{tz[0]}")
            slow(f"    {cyan}Xidmət təminatçısı{blue}:>>  {green}{c}")
            slow(f"    {cyan}Doğrulama yoxlanışı{blue}:>>  {green} Tapıldı")
            
            slow(f"")

            data = country.info()
            for i, j in data.items():
                slow(f"    {cyan}{i}{blue}  :>>  {green}{j}")

            slow(f"")

            slow(f"    {cyan}Nömrə{blue}     :>>  {green}(+{cncode}) {local}")
            slow(f"    {cyan}Ölkə{blue}      :>>  {green}{gcd} ({iso})")
            slow(f"    {cyan}Yerləşmə{blue}  :>>  {green}Tapıldı")

            try:
                Key = "42c84373c47e490ba410d4132ae64fc4"
                coder = OpenCageGeocode(Key)
                query = str(gcd)

                results = coder.geocode(query)
                lat = results[0]['geometry']['lat']
                lng = results[0]['geometry']['lng']

                slow(f"    {cyan}Enlik{blue}     :>>  {green}{lat}")
                slow(f"    {cyan}Uzunluq{blue}   :>>  {green}{lng}")
                addr = coder.reverse_geocode(lat, lng)

                if addr:
                    address = addr[0]['formatted']
                    slow(f"    {cyan}Ünvan{blue}     :>>  {green}{address}")
                else:
                    slow(f"    {purple}Telefon nömrəsinə uyğun ünvan tapılmadı.")

            except Exception:
                time.sleep(1)
                slow(f"{error}Zəhmət olmasa internet bağlantınızı yoxlayın.{stop}\n")
                os.sys.exit()
                
            url=f"https://google.com/maps/place/{lat},{lng}/@{lat},{lng},16z"

            slow(f"                     ")
            act = input(f'{purple}[{stop}ENTER{purple}] Google Maps-da izləmə xəritəsini açmaq üçün [{stop}ENTER{purple}] düyməsini sıxın, ya da proqramdan çıxmaq üçün [{stop}N{purple}] düyməsini sıxın və [{stop}ENTER{purple}] düyməsini sıxın:{stop} ')
            if act.lower() == 'n':
                slow(f"{error}Proqramdan çıxılır ...")
                time.sleep(0.5)
                exit(0)
            elif act == '':
                slow(f"{info}Google Maps-da izləmə xəritəsi açılır ...")
                os.system(f"open {url}")
            else:
                slow(f"{error}Yanlış seçim, proqramdan çıxılır ...")
                exit()

            os.sys.exit()
        else:
            c = "Namə'lum"
            gc = "Namə'lum"
            gcd = gc

            print("\033[91;1m", end="\r")
            slow("===========================================================")
            slow(f"[!] {cyan}{inter.replace(' ','-')}{red} nömrəsinin yerini təyin etməyə cəhd edilir [!]")
            slow("===========================================================")
            time.sleep(3)

            slow(f"    {cyan}Beynəlxalq format{blue}  :>>  {red}{number}")
            slow(f"    {cyan}Milli format{blue}       :>>  {red}{nation}")
            slow(f"    {cyan}E164 formatı{blue}      :>>  {red}{e164}")
            slow(f"    {cyan}Yerli format{blue}      :>>  {red}{local}")
            slow(f"    {cyan}Ölkə{blue}             :>>  {red} Tapılmadı")
            slow(f"    {cyan}Vaxt zonası ID{blue}    :>>  {red}{tz[0]}")
            slow(f"    {cyan}Xidmət təminatçıları{blue} :>>  {red}{c}")
            slow(f"    {cyan}Doğrulama yoxlanışı{blue}:>>  {red} Tapılmadı")
            slow(f"")

            slow(banner())
            slow(f"\n{error}Göstərilən telefon nömrəsi etibarsızdır!.    ")
            slow("===========================================================")
            slow(f"    {stop}Zəhmət olmasa etibarlı telefon nömrəsi daxil edin.             ")
            slow(f"    Eləcə də, daxil etdiyiniz ölkə kodunun                  ")
            slow(f"    nömrəyə uyğun olduğuna əmin olun.{red}         ")
            slow(f"==========================================================={stop}")
            slow('\033[0m\n')
            os.sys.exit()
    except Exception as err:
        slow(banner())
        slow(f"\n{error}Göstərilən telefon nömrəsi etibarsızdır!.    ")
        slow("===========================================================")
        slow(f"    {stop}Zəhmət olmasa etibarlı telefon nömrəsi daxil edin.             ")
        slow(f"    Eləcə də, daxil etdiyiniz ölkə kodunun                  ")
        slow(f"    nömrəyə uyğun olduğuna əmin olun.{red}         ")
        slow(f"==========================================================={stop}")
        slow('\033[0m\n')
        os.sys.exit()


def main():
    parser = argparse.ArgumentParser( 
        description = "istifadəçilərə Azərbaycan üzrə telefon nömrələri haqqında məlumat toplamaq, izləmək və xəritələmək imkanı verən pulsuz və açıq OSINT vasitəsidir.")

    parser.add_argument( 
        "-c", "--code", 
        dest="coutry_code", 
        type=str, help='Zəhmət olmasa ölkə kodunu "+" işarəsi olmadan daxil edin. Məs: 994, 011, 010, 995 (yalnız Azərbaycan üçün)', required=False)

    parser.add_argument( 
        "-p", "--phone", 
        dest="phone_number", 
        type=str, help="Zəhmət olmasa hədəfin telefon nömrəsini daxil edin", required=False)

    parser.add_argument( 
        "-u", "--update", 
        dest="update_script",  
        action="store_true", help='AZPulse skriptini daha yaxşı performans üçün yeniləyin')

    argument = parser.parse_args()
    number = argument.phone_number
    cncode = argument.coutry_code
    update = argument.update_script

    # İnternet bağlantısını yoxlayın
    if not internet():
        slow(f"\n{error}Zəhmət olmasa internet bağlantınızı yoxlayın{stop}\n")
        os.sys.exit()

    # Yeniləmə rejimi
    if update:
        updateus()
    # Nömrə və ölkə kodu verildikdə
    elif number and cncode:
        if cncode not in kodlar:
            slow(f"\n{error}Yalnız Azərbaycan nömrələri dəstəklənir (Ölkə kodu: 994).{stop}\n")
            os.sys.exit()
        infoga(cncode, number)
    else:
        print(banner())
        print(show_menu())
    
    return argument


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        slow(f"\n{error} İstifadəçi proqramı dayandırdı!")
        load(f"{error} Proqram bağlanır ...{stop}")
        time.sleep(0.5)
        os.sys.exit()
