# -*- coding: utf-8 -*-

import multiprocessing
import os

from glob import glob
from distutils.util import strtobool

bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"
accesslog = "-"
access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' (%({host}i)s) in %(L)ss"  # noqa: E501
timeout = 60 # seconds (note that increasing doesn't really help; needs more root cause analysis)

workers = int(os.getenv("WEB_CONCURRENCY", multiprocessing.cpu_count() * 2))
threads = int(os.getenv("PYTHON_MAX_THREADS", 20))

reload = bool(strtobool(os.getenv("WEB_RELOAD", "false")))

if reload:
    reload_extra_files = glob('/app/allthethings/translations/**/*.mo', recursive=True)
