__version__ = '0.6.1'
__author__ = 'MIT/Feature Labs Team'


from featuretools_ta1.single_table import SingleTableFeaturization
from featuretools_ta1.multi_table import MultiTableFeaturization

PRIMITIVES = [
    SingleTableFeaturization,
    MultiTableFeaturization
]
