import os
from overviewer_core import util
from overviewer_core.files import FileReplacer

worlds = {}
renders = {}
execfile('config.py')

# create overviewer.js from the source js files
js_src = os.path.join(util.get_program_path(), "overviewer_core", "data", "js_src")
if not os.path.isdir(js_src):
		js_src = os.path.join(util.get_program_path(), "js_src")
with FileReplacer(os.path.join(outputdir, "overviewer.js")) as tmpfile:
		with open(tmpfile, "w") as fout:
				# first copy in js_src/overviewer.js
				with open(os.path.join(js_src, "overviewer.js"), 'r') as f:
						fout.write(f.read())
				# now copy in the rest
				for js in os.listdir(js_src):
						if not js.endswith("overviewer.js") and js.endswith(".js"):
								with open(os.path.join(js_src,js)) as f:
										fout.write(f.read())

