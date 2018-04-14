import funcs

f = "test1.pdf"
funcs.get_fields(f)
dic = funcs.get_fields(f) 
dic["Postcode Text Box"] = "01002"
dic["Address 1 Text Box"] = "Dummy Address"
dic["City Text Box"] = "City Text Box"
dic['House nr Text Box'] = "120"
dic['Family Name Text Box'] = "Test"
dic['Country Combo Box'] = "Finland"
dic['Height Formatted Field'] = "150cm"
dic['Given Name Text Box'] = 'Daniel'
dic['Gender List Box'] = "Man"
funcs.write_pdf(f, funcs.get_fields(f), "output.pdf")