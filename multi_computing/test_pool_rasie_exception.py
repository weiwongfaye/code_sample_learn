class CommandExecutionFailure(RuntimeError):
    '''
    Generic exception for when a Splunk command fails to execute.

    @ivar command: The command that failed.
    @type command: str
    @ivar code: The exit code.
    @type code: int
    @param stdout: The standard output.
    @type stdout: str
    @ivar stderr: The standard error output.
    @type stderr: str
    '''

    def __init__(self, command, code, stdout, stderr):
        '''
        Creates a new exception.

        @param command: The command that failed.
        @type command: str
        @param code: The exit code.
        @type code: int
        @param stderr: The stderr output.
        @type stderr: str
        '''
        self.command = command
        self.code = code
        self.stderr = stderr
        self.stdout = stdout
        
        # import pdb;pdb.set_trace(); 
        super(CommandExecutionFailure, self).__init__(self._error_message,command,'','')

        # the following line will not work with multi-process mode
        # https://stackoverflow.com/questions/27993567/custom-exceptions-are-not-raised-properly-when-used-in-multiprocessing-pool
        super(CommandExecutionFailure, self).__init__(self._error_message)

        # self.e_string = self._error_message

    @property
    def _error_message(self):
        '''
        The error message for this exception.

        Is built using L{command}, L{code}, L{stdout} and L{stderr}.

        @rtype: str
        '''
        message = 'Command {cmd} returned code {code}.\n'
        message += '############\nstdout: {stdout}\n'
        message += '############\nstderr: {stderr}'

        return message.format(cmd=self.command, code=self.code,
                              stdout=self.stdout, stderr=self.stderr)

    
class CouldNotStartSplunk(CommandExecutionFailure):
    '''
    Raised when a Splunk start fails.
    '''
    # def __init__(self, command,code,stdout,stderr):
    #   super(CouldNotStartSplunk, self).__init__(command,code,stdout,stderr)


import time
from multiprocessing import Pool
def run(fn) :
  raise CouldNotStartSplunk('a','b','c','d')
  print fn

if __name__ == "__main__" :
  startTime = time.time()
  testFL = [1,2,3,4,5]
  pool = Pool(10)
  pool.map(run,testFL)
  pool.close()
  pool.join()   
  endTime = time.time()
  print "time :", endTime - startTime
  # run(1)