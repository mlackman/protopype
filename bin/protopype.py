#!/usr/bin/env python3
from bottle import static_file, route, run


@route('/')
def serve_html():
  return static_file('index.html', root='')

@route('/<filename>')
def serve(filename):
  return static_file(filename, root='')

if __name__ == '__main__':
  run(host='localhost', port=3000, debug=True, reload=True)


