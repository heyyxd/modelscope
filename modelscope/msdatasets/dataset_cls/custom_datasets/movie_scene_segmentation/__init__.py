# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .movie_scene_segmentation_dataset import MovieSceneSegmentationDataset
else:
    _import_structure = {
        'movie_scene_segmentation_dataset': ['MovieSceneSegmentationDataset'],
    }
    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )