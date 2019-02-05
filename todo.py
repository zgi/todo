# -*- coding: utf-8 -*-
print "Pozdravljen v TODO urejevalnik opravil."

while True:
    opravilo = raw_input("Prosim vnesi opravilo: ")
    print "Tvoje opravilo: " + opravilo

    novo_opravilo = raw_input("Bi rad vnesel še kakšno opravilo? (da/ne)")

    if novo_opravilo == "ne":
        break

print "Hvala in čau"
