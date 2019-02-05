# -*- coding: utf-8 -*-
print "Pozdravljen v TODO urejevalnik opravil."

seznam_opravil = []

while True:
    opravilo = raw_input("Prosim vnese opravilo: ")
    print "Tvoje opravilo: " + opravilo
    seznam_opravil.append(opravilo)

    novo_opravilo = raw_input("Bi rad vnesel še kakšno opravilo? (da/ne)")

    if novo_opravilo == "ne":
        break

print "\nVsa opravila: "
for item in seznam_opravil:
    print "- %s"%item
print "\nKonec seznama"