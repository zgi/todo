# -*- coding: utf-8 -*-
print "Pozdravljen v TODO urejevalnik opravil."

opravila_dict = {}

while True:
    opravilo = raw_input("Prosim vnese opravilo: ")
    status = raw_input("Ali je opravilo %s opravljeno?: (da/ne)" % opravilo)
    print "Tvoje opravilo: " + opravilo
    if status == 'da':
        opravila_dict[opravilo] = True
    else:
        opravila_dict[opravilo] = False
    novo_opravilo = raw_input("Bi rad vnesel še kakšno opravilo? (da/ne)")

    if novo_opravilo == "ne":
        break

print "\nKončana opravila: "
for opravilo in opravila_dict:
    if opravila_dict[opravilo] is True:
        print "- %s" % opravilo
print "\nNekončana opravila: "
for opravilo in opravila_dict:
    if opravila_dict[opravilo] is False:
        print "- %s" % opravilo
print "\nKonec seznama"


