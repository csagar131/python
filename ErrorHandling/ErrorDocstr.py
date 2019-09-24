class RuntimeWithCode(TypeError):
    '''
    if anything wrong will happen throws an error here
    '''
    def __init__(self,message,code):
        super().__init__(f' error occured with code {code} message {message}')
        self.code = code


err  = RuntimeWithCode("hey there error",500)
print(err.__doc__)