import re


from typing import Dict, List, Tuple, Union



Directory = Dict[str, Union[bool, 'Directory']]


def to_directory(string: str) -> Directory:
	children = re.split(r'^([a-z0-9\.]*)$', string, flags=re.MULTILINE + re.IGNORECASE)[1:]
	return {
		(key := children[i]): True if '.' in key else {} if not (value := children[i+1].replace('\n\t', '\n').strip()) else to_directory(value)
		for i in range(0, int(len(children)/2) + 1, 2)
	}


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
