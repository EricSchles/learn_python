from flask_script import Command
import code

class REPL(Command):

    def run(self):
        code.interact(local=locals())
