from get_api import fetch_api

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

HELP_STRING = """
Ange ett år och fält
Exempelvis 1965 fysik
Fält att välja mellan:
fysik
kemi
litteratur
ekonomi
fred
medicin

Write Q to exit program
"""

fields = {"fysik": "phy",
          "kemi": "che",
          "litteratur": "lit",
          "ekonomi": "eco",
          "fred": "pea",
          "medicin": "med"}



#  10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input
# TODO 15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern inte skickas med till apiet och vi får då alla priser det året



def print_nobelwinners(res):
    '''
    Prints out information about the nobel-prize winners
    :param res: Iterable
    '''
    for prize in res["nobelPrizes"]:
        peng = prize["prizeAmount"]
        idagpeng = prize["prizeAmountAdjusted"]
        print(f"{prize['categoryFullName']['se']} prissumma: {peng} SEK")
        print(f"Dagens värde: {idagpeng}\n")

        for name_info in prize["laureates"]:
            print(f"{name_info['knownName']['en']} prissumma: {float(peng / 3)} dagens värde: {float(idagpeng / 3)}")
            print("Prissumma: " + "{:.3f}".format(float(peng / 3)))
            print("Dagens värde: " + "{:.3f}".format(float(idagpeng / 3)))
            print(f"{name_info['motivation']['en']}")
            andel = name_info['portion']
            print(andel)
            print('-' * 80)


def run():
    print(HELP_STRING)

    while True:

        # 5p Skriv bara ut hjälptexten en gång när programmet startar inte efter varje gång användaren matat in en fråga
        #      Förbättra hjälputskriften så att användaren vet vilka fält, exempelvis kemi som finns att välja på

        #  5p Gör så att det finns ett sätt att avsluta programmet, om användaren skriver Q så skall programmet stängas av
        #      Beskriv i hjälptexten hur man avslutar programmet

        #  5p Gör så att hjälptexten skrivs ut om användaren skriver h eller H

        user_input = input(">")
        if user_input == 'Q':
            break
        elif user_input == 'H' or 'h':
            print(HELP_STRING)

        try:
            year, field = user_input.split()

            parameter = fields[field]
            print(parameter)

            parameter = {"nobelPrizeYear": int(year), "nobelPrizeCategory": parameter}

            res = fetch_api(parameter)
            #  5p Lägg till någon typ av avskiljare mellan pristagare, exempelvis --------------------------

            # TODO 20p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera mottagare, skriv ut både i dåtidens pengar och dagens värde
            #   Skriv ut med tre decimalers precision. exempel 534515.123
            #   Skapa en funktion som hanterar uträkningen av prispengar och skapa minst ett enhetestest för den funktionen
            #   Tips, titta på variabeln andel
            # Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i dåtidens penningvärde

            print_nobelwinners(res)
        except ValueError:
            print('Wrong input. Enter a year and field separated by space.')





if __name__ == '__main__':
    run()
