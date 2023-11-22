from Bio.KEGG import REST, Enzyme

request = REST.kegg_get("ec:5.4.2.2")
open("ec_5.4.2.2.txt","w").write(request.read())

records = Enzyme.parse(open("ec_5.4.2.2.txt","r"))
record = list(records)[0]
record.classname