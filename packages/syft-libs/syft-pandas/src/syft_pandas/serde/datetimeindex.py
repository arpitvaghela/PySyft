"""Serde method for pd.DataFrame."""

# third party
import pandas as pd
import pyarrow as pa

# relative
from syft.generate_wrapper import GenerateWrapper
from ..proto.datetime_pb2 import PandasDatetimeIndex as PandasDatetimeIndex_PB
from syft import serialize, deserialize


def object2proto(obj: pd.DatetimeIndex) -> PandasDatetimeIndex_PB:
    """Convert pd.DataFrame to PandasDataFrame_PB with pyarrow.

    Args:
        obj: target Dataframe

    Returns:
        Serialized version of Dataframe, which will be used to reconstruction.

    """
    data = pd.Series(obj._data)
    return PandasDatetimeIndex_PB(data=serialize(data, to_proto=True))


def proto2object(proto: PandasDatetimeIndex_PB) -> pd.DatetimeIndex:
    """Proto to object conversion using to return desired model.

    Args:
        proto: Serialized version of Dataframe, which will be used to reconstruction.

    Returns:
        Re-constructed dataframe.
    """
    data = deserialize(blob=proto.data, from_proto=True)

    return pd.DatetimeIndex(data, name="")


GenerateWrapper(
    wrapped_type=pd.DatetimeIndex,
    import_path="pandas.DatetimeIndex",
    protobuf_scheme=PandasDatetimeIndex_PB,
    type_object2proto=object2proto,
    type_proto2object=proto2object,
)
