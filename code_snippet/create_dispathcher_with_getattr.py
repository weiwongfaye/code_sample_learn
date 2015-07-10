import statsout
def output(data, format="text"):
     output_function = getattr(statsout, "output_%s" % format)
     return output_function(data)

if __name__ == '__main__':
	output(data = "mytestcontent",format = "text")
	output(data = "mytestcontent", format="json")
	output(data = "mytestcontent", format="html")
