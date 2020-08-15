import web

render=web.template.render('templates')
urls = (   #(正则表达式,对应的类)顺序匹配
    '/source/(.*)','source',
    '/beautiful柱形图1','Beautiful_column1',
    '/boring柱形图1','Boring_column1',
    '/depressing柱形图1','Depressing_column1',
    '/lively柱形图1','Lively_column1',
    '/safety柱形图1','Safety_column1',
    '/wealthy柱形图1','Wealthy_column1',
    '/beautiful柱形图2','Beautiful_column2',
    '/boring柱形图2','Boring_column2',
    '/depressing柱形图2','Depressing_column2',
    '/lively柱形图2','Lively_column2',
    '/safety柱形图2','Safety_column2',
    '/wealthy柱形图2','Wealthy_column2',

    '/beautiful热力图1','Beautiful_warm1',
    '/boring热力图1','Boring_warm1',
    '/depressing热力图1','Depressing_warm1',
    '/lively热力图1','Lively_warm1',
    '/safety热力图1','Safety_warm1',
    '/wealthy热力图1','Wealthy_warm1',
    '/beautiful热力图2','Beautiful_warm2',
    '/boring热力图2','Boring_warm2',
    '/depressing热力图2','Depressing_warm2',
    '/lively热力图2','Lively_warm2',
    '/safety热力图2','Safety_warm2',
    '/wealthy热力图2','Wealthy_warm2',

    '/beautiful折线图','Beautiful_line',
    '/boring折线图','Boring_line',
    '/depressing折线图','Depressing_line',
    '/lively折线图','Lively_line',
    '/safety折线图','Safety_line',
    '/wealthy折线图','Wealthy_line',

    '/beautiful折线图2','Beautiful_line2',
    '/boring折线图2','Boring_line2',
    '/depressing折线图2','Depressing_line2',
    '/lively折线图2','Lively_line2',
    '/safety折线图2','Safety_line2',
    '/wealthy折线图2','Wealthy_line2',

    '/(index)','Homepage',
    '/(.*)', 'Homepage'
)

class source:
    def GET(self,name):
        print(name)
        with open('source/'+name,'rb') as f:#js、json
                contents=f.read()
        return contents

class Beautiful_column1:
    def GET(self):
        return render.beautiful_column1()

class Boring_column1:
    def GET(self):
        return render.boring_column1()

class Depressing_column1:
    def GET(self):
        return render.depressing_column1()

class Lively_column1:
    def GET(self):
        return render.lively_column1()

class Safety_column1:
    def GET(self):
        return render.safety_column1()

class Wealthy_column1:
    def GET(self):
        return render.wealthy_column1()

class Beautiful_column2:
    def GET(self):
        return render.beautiful_column2()

class Boring_column2:
    def GET(self):
        return render.boring_column2()

class Depressing_column2:
    def GET(self):
        return render.depressing_column2()

class Lively_column2:
    def GET(self):
        return render.lively_column2()

class Safety_column2:
    def GET(self):
        return render.safety_column2()

class Wealthy_column2:
    def GET(self):
        return render.wealthy_column2()

class Beautiful_warm1:
    def GET(self):
        return render.beautiful_warm1()

class Boring_warm1:
    def GET(self):
        return render.boring_warm1()

class Depressing_warm1:
    def GET(self):
        return render.depressing_warm1()

class Lively_warm1:
    def GET(self):
        return render.lively_warm1()

class Safety_warm1:
    def GET(self):
        return render.safety_warm1()

class Wealthy_warm1:
    def GET(self):
        return render.wealthy_warm1()

class Beautiful_warm2:
    def GET(self):
        return render.beautiful_warm2()

class Boring_warm2:
    def GET(self):
        return render.boring_warm2()

class Depressing_warm2:
    def GET(self):
        return render.depressing_warm2()

class Lively_warm2:
    def GET(self):
        return render.lively_warm2()

class Safety_warm2:
    def GET(self):
        return render.safety_warm2()

class Wealthy_warm2:
    def GET(self):
        return render.wealthy_warm2()
class Beautiful_line:
    def GET(self):
        return render.beautiful_line()

class Boring_line:
    def GET(self):
        return render.boring_line()

class Depressing_line:
    def GET(self):
        return render.depressing_line()

class Lively_line:
    def GET(self):
        return render.lively_line()

class Safety_line:
    def GET(self):
        return render.safety_line()

class Wealthy_line:
    def GET(self):
        return render.wealthy_line()


class Beautiful_line2:
    def GET(self):
        return render.beautiful_line2()

class Boring_line2:
    def GET(self):
        return render.boring_line2()

class Depressing_line2:
    def GET(self):
        return render.depressing_line2()

class Lively_line2:
    def GET(self):
        return render.lively_line2()

class Safety_line2:
    def GET(self):
        return render.safety_line2()

class Wealthy_line2:
    def GET(self):
        return render.wealthy_line2()
    
class Homepage:
    def GET(self,name):
        return render.homepage()

class MyApplication(web.application):# 换端口
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))
    
if __name__ == "__main__":
    app = web.application(urls, globals())
    #app = MyApplication(urls, globals())
    app.run()
