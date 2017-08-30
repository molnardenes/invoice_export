from bottle import route, run, template, request, redirect, static_file, get
import time
import validate
import os

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@route('/')
def main(message=None): 
    return template('main.tpl', message=message)

@route('/goback', method='POST')
def gotomain():
    return redirect('/')

@route('/upload', method='POST')
def do_upload():    
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)     
    filename = _generate_filename(name, ext)
    upload.save(filename)

    xsd = validate.xsd_from_file('23_2014_szamlasema.xsd')      
    xml = validate.xml_from_file(filename)
    os.remove(filename)

    if xsd is None:        
        return template('main.tpl', message="Something went wrong processing the scheme definition.")
    elif xml is None:
        return template('main.tpl', message="Something went wrong processing the XML file. Are you sure it is in correct format?") 
    
    errors = _check_for_errors(xml, xsd)
    
    return template('result.tpl', errors=errors)

def _generate_filename(name, ext):
    timestamp = time.strftime("%Y%m%d%H%M%S")
    return f'{name}_{timestamp}{ext}'

def _check_for_errors(xml, xsd):
    error_log = validate.validate_with_errors(xml, xsd)
    return validate.xsd_error_log_as_simple_strings(error_log[1])

run(host='0.0.0.0', port=8080, debug=True)
