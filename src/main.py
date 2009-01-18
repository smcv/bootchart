import sys
import os
import optparse

import parsing
import gui

sys.path.insert(0, os.getcwd())

def _mk_options_parser():
	"""Make an options parser."""
	usage = "%prog [options] PATH, ..., PATH"
	version = "%prog v0.0.0"
	parser = optparse.OptionParser(usage, version=version)
	parser.add_option("-f", "--format", dest="format",
			  help="image format (...); default format ...")
	parser.add_option("-o", "--output-dir", dest="outputdir", metavar="DIR", default=".",
			  help="output directory where images are stored (default: .)")
	parser.add_option("-n", "--no-prune", action="store_true", dest="noprune", default=False,
			  help="do not prune the process tree")
	parser.add_option("-q", "--quiet", action="store_true", dest="quiet", default=False,
			  help="suppress informational messages")
	parser.add_option("--very-quiet", action="store_true", dest="veryquiet", default=False,
			  help="suppress all messages except errors")
	parser.add_option("--verbose", action="store_true", dest="verbose", default=False,
			  help="print all messages")
	return parser

def main(argv=None):
	if argv is None:
		argv = sys.argv[1:]
	
	parser = _mk_options_parser()
	opts, args = parser.parse_args(argv)
	
	if len(args) == 0:
		parser.error("insufficient arguments, expected at least one path.")
		return 2

	res = parsing.parse_log_dir(args[0], True)
	gui.show(res)
	return 0

if __name__ == '__main__':
	sys.exit(main())
