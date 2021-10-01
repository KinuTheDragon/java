from abc import ABC, abstractmethod

from java.util.stream.pipeline_helper import PipelineHelper
from java.util.stream.base_stream import BaseStream
from java.util.spliterator import Spliterator


class AbstractPipeline(ABC, PipelineHelper, BaseStream):
    __MSG_STREAM_LINKED = \
        "stream has already been operated upon or closed"
    __MSG_CONSUMED = "source already consumed or closed"

    __source_stage = None
    __previous_stage = None
    _source_or_op_flags = None
    __next_stage = None
    __depth = None
    __combined_flags = None
    __source_spliterator = None
    __source_supplier = None
    __linked_or_consumed = None
    __source_any_stateful = None
    __source_close_action = None
    __parallel = None

    def __init__(self, *args):