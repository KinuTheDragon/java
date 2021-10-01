class AccessController:
    def __init__(self):
        raise NotImplementedError
    
    @staticmethod
    def check_permission(perm):
        return AccessController.get_context()\
                .check_permission(perm)
    
    @staticmethod
    def do_privileged(action):