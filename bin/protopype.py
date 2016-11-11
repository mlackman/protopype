#!/usr/bin/env python3
from bottle import static_file, route, run

def serve_static_file(filename, root):
  response = static_file(filename, root)
  response.set_header('Access-Control-Allow-Origin', '*')
  return response

@route('/')
def serve_html():
  return serve_static_file('index.html', root='')

@route('/<filename:path>')
def serve(filename):
  return serve_static_file(filename, root='')

if __name__ == '__main__':
  run(host='0.0.0.0', port=3000, debug=True, reload=True)


