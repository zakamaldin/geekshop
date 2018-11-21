from django.shortcuts import redirect


class AdminGroupRequired:
    redirect_url = ''

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(
                [
                    'mainapp.add_product',
                    'mainapp.change_product',
                    'mainapp.delete_product',
                    'mainapp.add_productcategory',
                    'mainapp.change_productcategory',
                    'mainapp.delete_productcategory',

                ]
        ):
            return super(AdminGroupRequired, self).dispatch(request, *args, **kwargs)
        return redirect(self.redirect_url)
