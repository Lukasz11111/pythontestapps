import pip


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

    if hasattr(pip, 'main'):
        pip.main(['uninstall', package])
    else:
        pip._internal.main(['uninstall', package])


def b():
    print("a")

# Example
if __name__ == '__main__':
    install('argadsafdshfff')
    pip.main(['install', 'argh'])
    import argh
    pip.main(['uninstall', 'argh', '-y'])
     
    
    def echo(text):
        return text

    def greeter(name, greeting='hello'):
        return greeting + ', ' + name

    # assembling:

    parser = argh.ArghParser()
    parser.add_commands([echo, greeter])

    parser.dispatch()