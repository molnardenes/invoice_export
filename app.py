from bottle import route, run, template, request, redirect, static_file, get
import time
import validate
import os


@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@route('/')
def main(): 
    return template('main.tpl')

@route('/goback', method='POST')
def gotomain():
    return redirect('/')

@route('/upload', method='POST')
def do_upload():    
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename) 
    timestr = time.strftime("%Y%m%d%H%M%S")    
    filename = name + '_' + timestr + ext
    upload.save(filename)

    xsd = validate.xsd_from_file('23_2014_szamlasema.xsd')      
    xml = validate.xml_from_file(filename)

    os.remove(filename)

    error_log = validate.validate_with_errors(xml, xsd)
    errors = validate.xsd_error_log_as_simple_strings(error_log[1])
    
    return template('result.tpl', errors=errors)

run(host='0.0.0.0', port=8080, debug=True)
