import funcs

def getpairs():
	pairs=[("Postcode Text Box","Text",None),("Address 1 Text Box","Text",None),("City Text Box","Text",None),('House nr Text Box',"Text",None),('Family Name Text Box',"Text",None),("Country Combo Box","Text",None)]
	return pairs

def setpairs(lst):
	output(lst)


def output(lst):
	f = "test1.pdf"
	funcs.get_fields(f)
	dic = funcs.get_fields(f) 
	dic["Postcode Text Box"] = lst[0]#"01002"
	dic["Address 1 Text Box"] = lst[1]#"Dummy Address"
	dic["City Text Box"] = lst[2]#"City Text Box"
	dic['House nr Text Box'] = lst[3]#"120"
	dic['Family Name Text Box'] = lst[4]#"Test"
	dic['Country Combo Box'] = lst[5]#"Finland"
	#dic['Height Formatted Field'] = "150cm"
	#dic['Given Name Text Box'] = 'Daniel'
	#dic['Gender List Box'] = "Man"
	funcs.write_pdf(f, funcs.get_fields(f), "output.pdf")