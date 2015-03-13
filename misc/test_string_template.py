from string import Template

template = Template('The president of $state is $name')
message = template.substitute(state='USA', name='Obama')
print '1.',message
message = template.substitute(state='France', name='Sarkozy')
print '2.',message

try:
 	# will raise an exception
  	message = template.substitute(state='England')
except Exception as e:
 	print 'I cannot fill the placeholder',e
	#  original name placeholder will be used
   	message = template.safe_substitute(state='England') 

   	print '3.',message
