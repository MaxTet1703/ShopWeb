
class DataMixIn:

    def get_redirect_url(self):

        if self.request.user.is_superuser:
            return "administrator/"
        print("Хаха неправильно")
        return "homepage/"

