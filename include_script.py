#!/usr/bin/env python2

import commands
import subprocess
import sys
from string import Template

url = sys.argv[1].split(' ')[0]
script_name = sys.argv[1].split(' ')[1]
tab_id = commands.getoutput("./bin/chrome-cli info").split('\n')[0].split(': ')[1]

include_script_template = Template("\"\
    var script = document.createElement('script');\
    script.setAttribute('src','$url');\
    document.head.appendChild(script);\
\"")

success_script_template = Template("\"\
    console.log('imported: $script_name')\
\"")

chrome_command_template = Template("./bin/chrome-cli execute $script -t $tab_id")

include_script = include_script_template.substitute(url=url)
success_script = success_script_template.substitute(script_name=script_name)
chrome_include_command = chrome_command_template.substitute(script=include_script, tab_id=tab_id)
chrome_success_command = chrome_command_template.substitute(script=success_script, tab_id=tab_id)

commands.getoutput(chrome_include_command)
commands.getoutput(chrome_success_command)
