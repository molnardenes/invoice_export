from lxml import etree

def xml_from_file(filepath):
    """
    Returns an lxml.etree._ElementTree object from a file
    containing a valid XML document.
    """
    try:
        return etree.parse(filepath)
    except etree.XMLSyntaxError:
        return None

def xsd_from_file(filepath):
    """
    Returns an lxml.etree.XMLSchema object from a file
    containing a valid XML document.
    """
    try:
        xml = etree.parse(filepath)
        return etree.XMLSchema(xml)
    except etree.XMLSyntaxError:
        return None

def validate(xml, xsd):
    """
    Receives an lxml.etree._ElementTree object as first parameter
    and an lxml.etree.XMLSchema object as second parameter and
    returns True or False respectively as the XSD validation of the
    XML succeeds or fails.
    """
    return xsd.validate(xml)

def validate_from_files(xmlfilepath, xsdfilepath):
    """
    Receives a string with a file path to a valid XML document 
    as first parameter and another string with a file path to a valid
    XSD document as second parameter and validates the first according 
    to the latter returning True or False respectively as the validation
    succeeds or fails.
    """
    xml = xml_from_file(xmlfilepath)
    xsd = xsd_from_file(xsdfilepath)
    return validate(xml, xsd)

def validate_with_errors(xml, xsd):
    """
    Returns a tuple with a boolean product of the XSD validation as
    the first element and the error log object as the second element.
    """
    validation = xsd.validate(xml)
    return (validation, xsd.error_log, )

def xsd_error_log_as_simple_strings(error_log):
    """
    Returns a list of errors of an XSD
    error log object.
    """    
    return [e for e in error_log]