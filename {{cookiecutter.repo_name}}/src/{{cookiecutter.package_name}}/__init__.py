{%- if cookiecutter.scm_versioning == 'yes' %}
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
{%- else %}
__version__ = '{{ cookiecutter.version }}'
{%- endif %}
{%- if cookiecutter.c_extension_support == 'cffi' %}

from .{{ cookiecutter.c_extension_module }} import ffi as _ffi
from .{{ cookiecutter.c_extension_module }} import lib as _lib


def {{ cookiecutter.c_extension_function }}(args):
    args = [_ffi.new('char[]', arg) for arg in args]
    result = _lib.{{ cookiecutter.c_extension_function }}(len(args), _ffi.new('char *[]', args))
    if result == _ffi.NULL:
        return ''
    else:
        return _ffi.string(result)
{%- elif cookiecutter.c_extension_support != 'no' %}

from .{{ cookiecutter.c_extension_module }} import {{ cookiecutter.c_extension_function }}  # noqa
{%- endif %}
