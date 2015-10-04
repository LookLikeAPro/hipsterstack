from django.core.management.base import BaseCommand, CommandError
from subprocess import call
from app import models


class Command(BaseCommand):
	help = 'Closes the specified poll for voting'

	# def add_arguments(self, parser):
	# 	# Positional arguments
	# 	parser.add_argument('poll_id', nargs='+', type=int)

	# 	# Named (optional) arguments
	# 	parser.add_argument('--delete',
	# 		action='store_true',
	# 		dest='delete',
	# 		default=False,
	# 		help='Delete poll instead of closing it')

	def handle(self, *args, **options):
		# for poll_id in options['poll_id']:
		# 	try:
		# 		poll = Poll.objects.get(pk=poll_id)
		# 	except Poll.DoesNotExist:
		# 		raise CommandError('Poll "%s" does not exist' % poll_id)

		# 	poll.opened = False
		# 	poll.save()
		call(["echo", "fuck"])
		self.stdout.write('Successfully closed poll')
