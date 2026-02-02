VERSION = "5.0.0-dev"
PROJECT_NAME = "nts-bench"
nts_VERSION = None
current_path = None
updated_path = None
LOG_BUFFER = []


def set_nts_version(bench_path="."):
	from .utils.app import get_current_nts_version

	global nts_VERSION
	if not nts_VERSION:
		nts_VERSION = get_current_nts_version(bench_path=bench_path)
