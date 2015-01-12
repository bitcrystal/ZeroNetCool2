# Based on http://stackoverflow.com/a/2022629

class Event(list):
	def __call__(self, *args, **kwargs):
		for f in self[:]:
			if "once" in dir(f): 
				self.remove(f)
			f(*args, **kwargs)


	def __repr__(self):
		return "Event(%s)" % list.__repr__(self)


	def once(self, func):
		func.once = True
		self.append(func)
		return self


if __name__ == "__main__":
	def say(pre, text):
		print "%s Say: %s" % (pre, text)
	onChanged = Event()
	onChanged.once(lambda pre: say(pre, "once"))
	onChanged.append(lambda pre: say(pre, "always"))
	onChanged("#1")
	onChanged("#2")
	onChanged("#3")
