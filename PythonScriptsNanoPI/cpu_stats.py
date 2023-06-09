import subprocess


def get_stats():
	p = subprocess.Popen("cpu_freq", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
	return [d.strip() for d in p.split("\n")]





if __name__ == '__main__':
	data = get_stats()
	print(data)
