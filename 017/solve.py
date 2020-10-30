from typing import Dict, List, Tuple, Union



Directory = Dict[str, Union[bool, 'Directory']]


def to_directory(string: str) -> Directory:
	dir = {}

	first, *lines = string.split('\n')
	current = (first, [])
	for line in lines:
		if line.startswith('\t'):
			current[1].append(line)
			continue

		dir[current[0]] = True if '.' in current[0] else {} if not (value_str := '\n'.join(vline.replace('\t', '', 1) for vline in current[1])) else to_directory(value_str)
		current = (line, [])
	dir[current[0]] = True if '.' in current[0] else {} if not (value_str := '\n'.join(vline.replace('\t', '', 1) for vline in current[1])) else to_directory(value_str)

	return dir


def longest_absolute_path(dir: Directory) -> str:
	longest = None
	remaining: List[Tuple[List[str], Directory]] = []

	def search_longest(path: List[str], subdir: Directory):
		nonlocal longest
		for name, value in subdir.items():
			if not isinstance(value, bool):
				remaining.append((path + [name], value))
			elif not longest or len(''.join(longest)) < len(''.join(path + [name])):
				longest = path + [name]

	search_longest([], dir)
	while remaining:
		search_longest(*remaining.pop())

	assert longest
	return '/'.join(longest)



def test_solve():
	assert longest_absolute_path(to_directory("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")) == 'dir/subdir2/file.ext'
	assert longest_absolute_path(to_directory("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")) == "dir/subdir2/subsubdir2/file2.ext"
