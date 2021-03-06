#!/usr/bin/python3.2
# Skript: EingabeValidierung.py
# Erstellt durch Lukas Grimm (ombre@ombre.ch)
# Im Modul 122 an der Gibb

# Regex importieren
import re

# Variablen Definieren
Name = input('"Name Vorname" = ')
Str = input('"Strasse HausNr." = ')
PlzOrt = input('"PLZ Ort" = ')
Email = input('"Email" = ')
Geb = input('Geburtsdatum "DD.MM.YYYY" = ')
PC = input('Postkonto NR. =')

print("Ihre Daten werden Überprüft:")


#Überprüfen der Eingabe, bei Fehler nachfragen bis korrekt: (weniger strickte Lösungen im Kommentar)
while True:
  if re.match('^[A-Z]{1}[a-z]*\s{1}[A-Z]{1}[a-z]*$', Name): #('^\w+(\s\w+)+$', name)
    break
  Name = input('Name Vorname = ')

while True:
  if re.match('^([a-zA-Z])*\s{1}[0-9]{1,}$', Str): #('^(\w+(\s|\-|\'))+\d+[a-z]?$', adr)
    break
  Str = input('Strasse HausNr. = ')

while True:
  if re.match('[0-9]{4}\s{1}([A-Za-z])*$', PlzOrt): #('^\d{4}((\s|\-|\')\w+)+$', cty)
    break
  PlzOrt = input('Plz Ort = ')

while True:
  if re.match('^[a-zA-Z0-9-_.]+@[a-zA-Z0-9-.]+\.[a-zA-Z]{2,}', Email): #('^[a-zA-zZ0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', mail)
    break
  Email = input('Email = ')

while True:
  if re.match('([0-9]{1,2}(.|/)){2}(19|20)[0-9]{2}$', Geb): #('^\d{2}\.\d{2}\.\d{4}$', birth)
    break
  Geb = input('Geburtsdatum "DD.MM.YYYY" = ')

while True:
  if re.match('^[0-9]{1,2}-[0-9]{2,15}-[0-9]{1,2}$', PC): #('^\d{1-2}\-\d{4,}\-\d$', pc)
    break
  PC = input('Postkonto Nr. =')

print("Alle Daten sind korrekt, danke und auf Wiedersehen")
