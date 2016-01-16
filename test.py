import pint
import numpy as np

ureg = pint.UnitRegistry()

l = np.arange(10)

two = 2 * ureg('')

## These all work just fine
# l + two
# l += two
# l *= two
# l ** two

# This does not work when 'two' has a __numpy_ufunc__ method!
l **= two
