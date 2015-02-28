import cmd
class HelloWorld(cmd.Cmd):
    """Simple command processor example."""	        
    def do_greet(self, line):
        print "hello"			        
    def do_EOF(self, line):
	return True
    def do_hello(self, person):
	if person:
            print "hi %s" % person
	else:
            print "hi"

if __name__ == '__main__':
    HelloWorld().cmdloop()
