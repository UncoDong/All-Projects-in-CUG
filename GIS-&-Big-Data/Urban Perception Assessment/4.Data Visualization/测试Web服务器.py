import web
urls = (
    '/upper/(.*)', 'upper',
    '/lower/(.*)', 'lower'
)
app = web.application(urls, globals())
class upper:
    def GET(self, text):
        print('input:' + text)
        return text.upper()

class lower:
    def GET(self, text):
        print('input:' + text)
        return text.lower()

if __name__ == "__main__":
    app.run()
