class StreamSupport:
    def __init__(self):
        raise NotImplementedError
    
    @staticmethod
    def stream(spliterator, parallel):
        assert spliterator is not None
        return 