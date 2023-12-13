acronyms = {"IDK": "I Don't Know",
            "TBH": "To Be Honest",
            "SMH": "Shaking My Head"}

try:
    definition = acronyms["LOL"]
    print(definition)
except:
    print("The key does not exist")
finally:
    print("The Acronyms we have are:")
    for acronym in acronyms:
        print(acronym, ":", acronyms[acronym])

print("Program keeps running....")
