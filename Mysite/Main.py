import web
from Models import RegisterModel

urls = (
    '/', 'home',
    '/register', 'Register',
    '/postregistration', 'Postregistration'
)

render = web.template.render("Views/Templates", base="Main")

app = web.application(urls, globals())

# Classes/Routes


class home:
    def GET(self):
        return render.Home()


class Register:
    def GET(self):
        return render.Register()

class Postregistration:
    def Post(self):
        data = web.input()

        regmodel=RegisterModel.RegisterModel()
        regmodel.insert_user(data)

        return data.username

if __name__ == "__main__":
    app.run()
