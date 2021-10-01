from abc import ABC, abstractmethod

class ReferencePipeline(ABC):
    @abstractmethod
    def get_source_shape(self):
        ...
    
    @abstractmethod
    def get_stream_and_op_flags(self):
        ...
    
    @abstractmethod
    def exact_output_size_if_known(self, spliterator):
        ...
    
    @abstractmethod
    def wrap_and_copy_into(self, sink, spliterator):
        ...
    
    @abstractmethod
    def copy_into(self, wrapped_sink, spliterator):
        ...
    
    @abstractmethod
    def copy_into_with_cancel(self, wrapped_sink, spliterator):
        ...
    
    @abstractmethod
    def wrap_sink(self, sink):
        ...
    
    @abstractmethod
    def wrap_spliterator(self, spliterator):
        ...
    
    @abstractmethod
    def make_node_builder(self, exact_size_if_known, generator):
        ...
    
    @abstractmethod
    def evaluate(self, spliterator, flatten, generator):
        ...