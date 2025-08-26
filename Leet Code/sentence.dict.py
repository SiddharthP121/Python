details={
    "S1":{
    "name":"Nisha",
    "age":28,
    "email":"nisha.jaiswal@anudip.org",
    "certifications":["OCJP","OCJA","AWS System Associate"]
    },
    "S2":{
    "name":"Nishant",
    "age":26,
    "email":"nishant.harde@anudip.org",
    "certifications":["OCJA","AWS System Associate"]
    }
}

# Nisha , 28, has been certified in [OCJP,OCJA, AWS System Associate]

for keys, values in details.items():
    certs = ', '.join(values['certifications'])
    print(f"{values['name']}, {values['age']}, has been certified in {certs}")

