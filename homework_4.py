def yil_dogru_mu(year):
    if year != 2017 and year != 2018:
        return False
    return True

# function to validate the month input
def ay_dogru_mu(year, month):
    if year == 2017 and (month < 1 or month > 12):
        return False
    elif year == 2018 and month != 1:
        return False

    

    return True


def main():
    yil = int(input("Enter the year: "))
    while not yil_dogru_mu(yil):
        yil = int(input("Enter the year: "))
    ay = int(input("Enter the month: "))
    while not ay_dogru_mu(yil, ay):
        ay = int(input("Enter the month: "))

    if ay == 9:
        ay = "09"

    elif ay == 8:
        ay = "08"

    elif ay == 7:
        ay = "07"

    elif ay == 6:
        ay = "06"

    elif ay == 5:
        ay = "05"

    elif ay == 4:
        ay = "04"

    elif ay == 3:
        ay = "03" 

    elif ay == 2:
        ay = "02"

    elif ay == 1:
        ay = "01"
    tum_sarkilar = en_pop_sarkilari(yil, ay)
    while tum_sarkilar:
        besten_singen = tum_sarkilar.pop(0)
        print(f"NEW SUGGESTION: {besten_singen['name']}, {besten_singen['artist']} (Total stream number in this month: {besten_singen['streams']})")
        wanna_horen = input("Do you want to listen this song (enter either yes or no): ")
        if wanna_horen.upper() == "YES":
            print(f"Enjoy {besten_singen['name']}, {besten_singen['artist']}. Here is the url for you: {besten_singen['url']}")
            break
        while wanna_horen.upper() != "NO" and wanna_horen.upper() != "YES":
            wanna_horen = input("Do you want to listen this song (enter either yes or no): ")
            if wanna_horen.upper() == "NO" or wanna_horen.upper() == "YES":
                break
def en_pop_sarkilari(year, month):
    sarki_verisi = {}
    with open("turkiye_spotify_data.txt") as file:
        for line in file:
            kutup = line.strip().split("\t")
            yayin = kutup[5]
            if yayin[:4] == str(year) and yayin[5:7] == str(month):
                sarki_adi = kutup[1]
                sanatci = kutup[2]
                izlenme = int(kutup[3])
                link = kutup[4]
                key = sarki_adi + " ^ " + sanatci
                if key in sarki_verisi:
                    sarki_verisi[key]["streams"] += izlenme
                else:
                    sarki_verisi[key] = {"streams": izlenme, "url": link}
    en_populer_sarkilar = []
    for song in sorted(sarki_verisi.items(), key=lambda x: x[1]["streams"], reverse=True):
        en_populer_sarkilar.append({"name":song[0].split("^")[0].strip(),"artist":song[0].split("^")[1].strip(),"streams":song[1]["streams"],"url":song[1]["url"]})
    return en_populer_sarkilar

if __name__ == "__main__":
    main()
