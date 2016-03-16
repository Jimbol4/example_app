"""example_app base controller."""

from cement.core.controller import CementBaseController, expose
import requests
import ast

class example_BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Example app'
        arguments = [
            (['-f', '--foo'],
             dict(help='the notorious foo option', dest='foo', action='store',
                  metavar='TEXT') ),
            (['-url'],
             dict(help='the url to carry out a GET request on', dest='url', action='store',
                  metavar='TEXT') ),
            (['-payload'],
             dict(help='the payload to deliver with a request', dest='payload', action='store',
                  metavar='TEXT') ),
            (['-id'],
             dict(help='the id of the item to be updated/deleted', dest='id', action='store',
                  metavar='TEXT') ),
            ]

    @expose(hide=True)
    def default(self):
        print("Meh")
        if self.app.pargs.foo:
            print("Foo option was passed with value: %s" % self.app.pargs.foo)

    @expose(help="a great command that will do a lot")
    def command1(self):
        print("Bleh")

    #python3.5 main.py get -url='http://api.jtel6.dev.jellyfish.local/posts'
    #python3.5 main.py get -url='http://api.jtel6.dev.jellyfish.local/posts/1'
    @expose(help="make a GET request to given url")
    def get(self):
        
        if self.app.pargs.url and self.app.pargs.payload:
            r = requests.get(self.app.pargs.url, params = self.app.pargs.payload)
            return print(r.json())

        if self.app.pargs.url:
            r = requests.get(self.app.pargs.url)
            return print(r.json())

    #python3.5 main.py post -url='http://api.jtel6.dev.jellyfish.local/posts' -payload="{'title' : 'A new title', 'body' : 'This is a new body' }"
    @expose(help="make a POST request to given URL")
    def post(self):
        if self.app.pargs.url and self.app.pargs.payload:
            
            #payload = { 'title' : 'Some title', 'body': 'Some body' }
            # convert a passed dictionary to the data.
            r = requests.post(self.app.pargs.url, data=ast.literal_eval(self.app.pargs.payload))

            
            return print(r.json())

    #python3.5 main.py delete -url='http://api.jtel6.dev.jellyfish.local/posts' -id='7'
    @expose(help="make a DELETE request to the given URL")
    def delete(self):
        r = requests.delete(self.app.pargs.url + '/' + self.app.pargs.id)

        return print(r.json())

    #python3.5 main.py put -id='8' -url='http://api.jtel6.dev.jellyfish.local/posts' -payload="{'title' : 'An updated example title', 'body' : 'This is an updated body' }"
    @expose(help="make a PUT request to the given URL, to update the item with the given id")
    def put(self):
        r = requests.patch(self.app.pargs.url + '/' + self.app.pargs.id, data=ast.literal_eval(self.app.pargs.payload))

        return print(r.json())

        # If using an output handler such as 'mustache', you could also
        # render a data dictionary using a template.  For example:
        #
        #   data = dict(foo='bar')
        #   self.app.render(data, 'default.mustache')
        #
        #
        # The 'default.mustache' file would be loaded from
        # ``example_app.cli.templates``, or ``/var/lib/example_app/templates/``.
        #
