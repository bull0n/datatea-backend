def auth_required(func):
    def inner(self, info, **kwargs):
        if info.context.user.is_anonymous:
            raise Exception('Not logged in!')
        func(self, info, **kwargs)
    return inner


    