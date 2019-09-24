class CustomeError(TypeError):
    def __init__(self,message,code):
        super().__init__(f' error occured with code {code} message {message}')
        self.code = code


raise CustomeError("Ohh! error occured",500)