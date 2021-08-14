"""Serde method for pd.DataFrame."""

# third party
from typing import Any
import pandas as pd
from pandas.core.indexing import _LocIndexer

# relative
from syft.generate_wrapper import GenerateWrapper
from ..proto.loc_pb2 import PandasLoc as PandasLoc_PB
from syft import serialize, deserialize


def object2proto(loc: _LocIndexer) -> PandasLoc_PB:
    obj = loc.obj
    name = loc.name

    proto_name = serialize(name, to_proto=True)
    if type(obj) == pd.DataFrame:
        frame = serialize(obj, to_proto=True)
        return PandasLoc_PB(name=proto_name, frame=frame)

    if type(obj) == pd.Series:
        series = serialize(obj, to_proto=True)
        return PandasLoc_PB(name=proto_name, series=series)


def proto2object(proto: PandasLoc_PB) -> _LocIndexer:
    name = deserialize(proto.name, from_proto=True)

    # if proto.series:
    #     obj = deserialize(proto.series, from_proto=True)

    if proto.frame:
        obj = deserialize(blob=proto.frame, from_proto=True)

    return _LocIndexer(name, obj)


GenerateWrapper(
    wrapped_type=_LocIndexer,
    import_path="pandas.core.indexing._LocIndexer",
    protobuf_scheme=PandasLoc_PB,
    type_object2proto=object2proto,
    type_proto2object=proto2object,
)
