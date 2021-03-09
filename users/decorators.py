def auth_required(func):
    def inner(self, info, **kwargs):
        if info.context.user.is_anonymous:
            raise Exception('Not logged in!')
        return func(self, info, **kwargs)
    return inner


    