import pandas as pd
import sys
import argparse

"""
Command line interface for doing things with an avocado price dataset
Copyright (c) 2019 Rowan Lindsay
"""


def run_simulate():
	# modify the argument parser for the new level
	sub_parser = argparse.ArgumentParser(prog='simulate', description='Run a Simulation')
	sub_parser.add_argument('source_file', metavar='data-file', type=str, help='file to read prices from')
	sub_args = sub_parser.parse_args(sys.argv[2:])
	print('Simulating price history...')
	print('Opening data source...')
	data = pd.read_csv(sub_args.source_file)


def primary_commands():
	return 'Possible commands: ' \
		'\n simulate	runs a simulation'


arg_parser = argparse.ArgumentParser(
	description='View and Simulate Avocado Price Data',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	epilog=primary_commands())

arg_parser.add_argument('command', metavar='command', type=str, help='procedure to execute')

# procedure table
cmd_map = {
	'simulate': run_simulate
}

if __name__ == '__main__':
	args = arg_parser.parse_args(sys.argv[1:2])
	try:
		proc = cmd_map[args.command]
		proc()
	except KeyError:
		print(primary_commands())
		sys.exit('Unrecognized command!')
