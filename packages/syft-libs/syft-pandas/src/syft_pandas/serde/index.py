"""Serde method for pd.DataFrame."""

# third party
from typing import Any
import pandas as pd

# relative
from syft.generate_wrapper import GenerateWrapper
from ..proto.index_pb2 import PandasIndex as PandasIndex_PB
from syft import serialize, deserialize

INDEX_2_STR: list[type] = [
    pd.Index,
    pd.CategoricalIndex,
    pd.Int64Index,
    pd.UInt64Index,
    pd.Float64Index,
    pd.IntervalIndex,
    pd.TimedeltaIndex,
    pd.DatetimeIndex,
    pd.PeriodIndex,
]


def object2proto(obj: Any) -> PandasIndex_PB:
    data = obj.to_series()
    return PandasIndex_PB(data=serialize(data, to_proto=True))


def proto2object(proto: PandasIndex_PB) -> Any:
    data = deserialize(blob=proto.data, from_proto=True)
    return pd.Index(data)

    # for index_type in INDEX_2_STR:
    #     import_path = "pandas." + index_type.__name__
    # print(import_path)


GenerateWrapper(
    wrapped_type=pd.DatetimeIndex,
    import_path="pandas.DatetimeIndex",
    protobuf_scheme=PandasIndex_PB,
    type_object2proto=object2proto,
    type_proto2object=proto2object,
)
