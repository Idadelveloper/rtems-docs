#
# RTEMS Project Documentation
#

from sys import path
from os.path import abspath
path.append(abspath('common'))

import waflib
import waf as docs_waf

version = '4.11 (branch)'

build_all = ['user',
             'rsb',
             'c-user',
             'bsp-howto',
             'posix-users',
             'filesystem',
             'networking',
             'shell',
             'cpu-supplement',
             'develenv',
             'eclipse']

building = build_all

def options(opt):
    docs_waf.cmd_options(opt)

def configure(conf):
    conf.env.VERSION = version
    for b in building:
        conf.recurse(b)
    conf.env['BUILD_FROM_TOP'] = 'yes'

def catalogue(ctx):
    docs_waf.xml_catalogue(ctx, building)

def coverpage_js(ctx):
    js = None
    xml = None
    for f in ctx.inputs:
        if f.abspath().endswith('.js'):
            with open(f.abspath()) as i:
                js = i.read()
        elif f.abspath().endswith('.xml'):
            with open(f.abspath()) as i:
                xml = i.read()
    xml = xml.replace('\n', ' \\\n');
    with open(ctx.outputs[0].abspath(), 'w') as o:
        o.write(js.replace('@CATALOGUE', xml))

def build(ctx):
    for b in building:
        ctx.recurse(b)

    #
    # Build the catalogue, coverpage.js and install.
    #
    ctx(rule = catalogue,
        target = 'catalogue.xml',
        source = ['wscript', 'common/waf.py'])
    ctx.install_files('${PREFIX}', 'catalogue.xml')
    ctx(rule = coverpage_js,
        target = 'coverpage.js',
        source = ['wscript', 'catalogue.xml', 'common/html-coverpage/coverpage.js'])
    ctx.install_as('${PREFIX}/coverpage.js', 'coverpage.js')
    #
    # Install the static content.
    #
    ctx.install_as('${PREFIX}/index.html', 'common/html-coverpage/coverpage.html')
    static_dir = ctx.path.find_dir('common/html-coverpage/static')
    ctx.install_files('${PREFIX}/static',
                      static_dir.ant_glob('**'),
                      cwd = static_dir,
                      relative_trick = True)

def install(ctx):
    for b in building:
        ctx.recurse(b)
