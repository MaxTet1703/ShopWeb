
class DataMixIn:

    def get_redirect_url(self):

        if self.request.user.is_superuser:
            return "administrator/"
        elif self.request.user.is_cooker:
            return "employee/"
        return 'homepage/'

