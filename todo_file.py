# -*- coding: utf-8 -*-
print "Pozdravljen v TODO urejevalnik opravil."

opravila_dict = {}
opravila_file = open("opravila.txt", "w+")

while True:
    opravilo = raw_input("Prosim vnese opravilo: ")
    status = raw_input("Ali je opravilo %s opravljeno?: (da/ne)"%opravilo)
    print "Tvoje opravilo: " + opravilo
    if status == 'da':
        opravila_dict[opravilo] = True
    else:
        opravila_dict[opravilo] = False
    novo_opravilo = raw_input("Bi rad vnesel še kakšno opravilo? (da/ne)")

    if novo_opravilo == "ne":
        break

print "\nKončana opravila: "
opravila_file.write("Končana opravila:\n")
for opravilo in opravila_dict:
    if opravila_dict[opravilo] is True:
        print "- %s"%opravilo
        opravila_file.write('- '+opravilo+'\n')
print "\nNekončana opravila: "
opravila_file.write("\nNekončana opravila:\n")
for opravilo in opravila_dict:
    if opravila_dict[opravilo] is False:
        print "x %s"%opravilo
        opravila_file.write('x ' + opravilo + '\n')
opravila_file.close()
print "\nKonec seznama"