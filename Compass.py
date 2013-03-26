import sublime, sublime_plugin

class CompassWatchCommand(sublime_plugin.WindowCommand):
	def get_path(self, paths):
		if paths:
			return paths[0]
		elif self.window.folders():
			return self.window.folders()[0]
		else:
			sublime.error_message(__name__ + ": No folder selected")
			return False

	def run(self, paths=[]):
		path = self.get_path(paths)

		if not path:
			return

		self.window.run_command("exec", {"cmd": ["compass", "watch", path], "shell": True})
