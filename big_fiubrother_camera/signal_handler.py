import signal
import logging

class SignalHandler:
	stop_signal_received = False

	def __init__(self):
	      signal.signal(signal.SIGINT, self.__stop_signal_received)
	      signal.signal(signal.SIGTERM, self.__stop_signal_received)

	def __stop_signal_received(self, signum, frame):
	      self.stop_signal_received = True
	      logging.debug('Signal to stop received')


