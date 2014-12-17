from pipeline.storage import PipelineStorage
from pipeline.storage import GZIPMixin


class GZIPCachedStorage(GZIPMixin, PipelineStorage):
    pass
