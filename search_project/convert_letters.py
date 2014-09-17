
print"Copy string here:  "
backbone = raw_input()
#print backbone
backbone.split()
#print backbone
characteristic = []
for let in backbone:
	if let == "A":
		characteristic.append("Ala");
	if let == "R":
		characteristic.append("Arg");
	if let == "N":
		characteristic.append("Asn");
	if let == "D":
		characteristic.append("Asp");
	if let == "B":
		characteristic.append("Asx");
	if let == "C":
		characteristic.append("Cys");
	if let == "Q":
		characteristic.append("Gln");
	if let == "E":
		characteristic.append("Glu");
	if let == "G":
		characteristic.append("Gly");
	if let == "H":
		characteristic.append("His");
	if let == "I":
		characteristic.append("Ile");
	if let == "L":
		characteristic.append("Leu");
	if let == "K":
		characteristic.append("Lys");
	if let == "M":
		characteristic.append("Met");
	if let == "F":
		characteristic.append("Phe");
	if let == "P":
		characteristic.append("Pro");
	if let == "S":
		characteristic.append("Ser");
	if let == "T":
		characteristic.append("Thr");
	if let == "W":
		characteristic.append("Trp");
	if let == "Y":
		characteristic.append("Tyr");
	if let == "V":
		characteristic.append("Val");

print "Your characteristic is:  "
line = ""
for item in characteristic:
	line = line+item+" "
print str(line)
