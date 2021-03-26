class Settings:
    class __Settings:
        def __init__(self):
            setup(self)

    settings = None
    def __init__(self):
        if not getattr(Settings, "settings", None):
            Settings.settings = Settings.__Settings()

    def __getattr__(self, name):
        return getattr(self.settings, name)

    def __setattr__(self, name, value):
        if name == 'settings':
            self.__dict__[name] = value
        else:
            setattr(self.settings, name, value)

def setup(module):
    '''
        This will import modules config_default and config and move their variables
        into current module (variables in config have higher priority than config_default).
        Thanks to this, you can import settings anywhere in the application and you'll get
        actual application settings.

        This config is related to server side. You don't need config.py if you
        want to use client part only.
    '''

    def read_values(cfg):
        for varname in cfg.__dict__.keys():
            if varname.startswith('__'):
                continue

            value = getattr(cfg, varname)
            yield (varname, value)

    import config_default

    try:
        import config
    except ImportError:
        # Custom config not presented, but we can still use defaults
        config = None

    for name,value in read_values(config_default):
        setattr(module, name, value)

    changes = {}
    if config:
        for name,value in read_values(config):
            if value != getattr(module, name, None):
                changes[name] = value
            setattr(module, name, value)

    if module.DEBUG and changes:
        print ("----------------")
        print ("Custom settings:")
        for k, v in changes.items():
            if 'passw' in k.lower():
                print (k, ": ********")
            else:
                print (k, ":", v)
        print ("----------------")

s = Settings()