class User:
    def __init__(self,name,engagement):
        self.name = name 
        self.engagement = engagement
        self.score = 0
    
    def __repr__(self):
        return f'<User {self.name}>'


def email_send(user):
    try:
        user.score = calculate(user.engagement)
    except KeyError:
        print("incorrect value provided to our function")
        raise
    else:
        if user.score > 500:
            send_notification(user)


def calculate(engagement):
    return engagement['clicks']*5 +engagement['hits'] *5

def send_notification(user):
    print(f'notification send to {user}')
    print("with score:"+str(user.score))


my_user = User('sagar',{'clicks':61,'hits':52})
email_send(my_user)