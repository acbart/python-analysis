
__all__ = ['Submission']


class Submission:
    """
    Simple class for holding information about the student's submission.

    Examples:
        A very simple example of creating a Submission with a single file::

            >>> Submission({'answer.py': "a = 0"})

    Attributes:
        files (`dict` mapping `str` to `str`): Dictionary of filenames mapped to their contents, emulating
            a file system.
        main_file (str): The entry point file that will be considered the main file.
        main_code (str): The actual code to run; if None, then defaults to the code of the main file.
            Useful for tools that want to change the currently active code (e.g., Source's sections) or
            run additional commands (e.g., Sandboxes' call).
        user (dict): Additional information about the user.
        assignment (dict): Additional information about the assignment.
        course (dict): Additional information about the course.
        execution (dict): Additional information about the results of previously executing the students' code.
    """

    def __init__(self, files=None, main_file='answer.py', main_code=None,
                 user=None, assignment=None, course=None, execution=None):
        self.files = files
        self.main_file = main_file
        if main_code is None:
            self.main_code = self.files[self.main_file]
        else:
            self.main_code = main_code
        self._original_main_code = self.main_code
        self.user = user
        self.assignment = assignment
        self.course = course
        self.execution = execution
