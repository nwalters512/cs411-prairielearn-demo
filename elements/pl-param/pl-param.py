import prairielearn as pl
import lxml.html

ALLOWED_TYPES = ['string', 'int', 'float', 'boolean']

def prepare(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
    required_attribs = ['key', 'value']
    optional_attribs = ['type']
    pl.check_attribs(element, required_attribs, optional_attribs)
    key = pl.get_string_attrib(element, 'key', None)
    value = pl.get_string_attrib(element, 'value', None)
    param_type = pl.get_string_attrib(element, 'type', None)
    if param_type is not None:
        if param_type not in ALLOWED_TYPES:
            raise Exception(f'"{param_type}" is not an allowed type for the pl-param element')
        if param_type == 'int':
            value = int(value)
        elif param_type == 'float':
            value = float(value)
        elif param_type == 'boolean':
            value = bool(value)
    data['params'][key] = value
