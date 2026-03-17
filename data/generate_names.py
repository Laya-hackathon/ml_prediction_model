import pandas as pd
import random

first_names = [
    "Aoife", "Ciara", "Niamh", "Sinead", "Orla", "Grainne", "Maeve", "Roisin",
    "Aisling", "Caoimhe", "Siobhan", "Deirdre", "Fionnuala", "Clodagh", "Eimear",
    "Sorcha", "Brigid", "Nuala", "Saoirse", "Blathnaid", "Liadh", "Muireann",
    "Seamus", "Conor", "Ciarán", "Patrick", "Liam", "Sean", "Eoin", "Declan",
    "Cathal", "Padraig", "Fergus", "Ronan", "Cormac", "Darragh", "Tadhg", "Fionn",
    "Oisin", "Ruairi", "Brendan", "Dermot", "Killian", "Tiernan", "Donnacha",
    "Kevin", "Colm", "Noel", "Barry", "Brian"
]

last_names = [
    "Murphy", "Kelly", "O'Brien", "Walsh", "Smith", "O'Sullivan", "O'Connor",
    "McCarthy", "Byrne", "Ryan", "O'Neill", "O'Reilly", "Doyle", "Brennan",
    "Burke", "Collins", "Campbell", "Clarke", "Johnston", "Moore", "Fitzgerald",
    "Gallagher", "Flynn", "Kavanagh", "Connolly", "Daly", "Kennedy", "Lynch",
    "Murray", "Quinn", "Nolan", "Dunne", "Boyle", "Farrell", "Reilly", "Foley",
    "Sheridan", "Hennessy", "Maguire", "Donnelly", "Flanagan", "Higgins", "Power",
    "Mullen", "Whelan", "Cullen", "Lawlor", "Hogan", "Keenan", "Doherty"
]

user_ids = [f"U{str(i).zfill(5)}" for i in range(1, 2001)]

rows = []
for uid in user_ids:
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f"{first.lower().replace('\'', '')}.{last.lower().replace('\'', '')}@email.ie"
    rows.append({"user_id": uid, "first_name": first, "last_name": last, "email": email})

out = pd.DataFrame(rows)
out.to_csv("user_names.csv", index=False)
print(f"Generated {len(out)} rows → user_names.csv")

# Generate SQL UPDATE file
with open("update_names.sql", "w") as f:
    for r in rows:
        first = r["first_name"].replace("'", "''")
        last = r["last_name"].replace("'", "''")
        email = r["email"]
        f.write(f"UPDATE users_backup SET first_name='{first}', last_name='{last}', email='{email}' WHERE user_id='{r['user_id']}';\n")
print("Generated update_names.sql")
