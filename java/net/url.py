class URL:
    serial_version_UID = -7627629688361524110
    __protocol_path_prop = "java.protocol.handler.pkgs"
    __protocol = None
    __host = None
    __port = -1
    __file = None
    __query = None
    __authority = None
    __path = None
    __user_info = None
    __ref = None
    host_address = None
    handler = None
    __hash_code = -1

    def __init__(self, protocol, host, *args):
        if not (1 <= len(args) <= 3):
            raise AttributeError
        if len(args) == 1:
            file, = args
            port = -1
            handler = None
        elif len(args) == 2:
            port, file = args
            handler = None
        else:
            port, file, handler = args
        
        if handler is not None:
            sm = 