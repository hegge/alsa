#! /usr/bin/python
# -*- Python -*-

import os

ROOT = os.path.abspath(os.getcwd())
USER = os.getenv('USER')
VERBOSE = False
GERRORS = 0
TMPDIR = '/dev/shm/alsatool'
SMTP_SERVER = 'localhost'
GIT_KERNEL_MERGE = 'v2.6.33'
GIT_DRIVER_MERGE = 'v1.0.22'
GIT_MERGE_REPOS = [
        ('git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux-2.6.git', 'master', 'linux-2.6', 'http://www.kernel.org/pub/scm/linux/kernel/git/torvalds/linux-2.6.git'),
        ('git://git.alsa-project.org/alsa-kernel.git', 'fixes', 'perex-fixes', 'http://git.alsa-project.org/http/alsa-kernel.git'),
        ('git://git.alsa-project.org/alsa-kernel.git', 'devel', 'perex-devel', 'http://git.alsa-project.org/http/alsa-kernel.git'),
        ('git://git.kernel.org/pub/scm/linux/kernel/git/tiwai/sound-2.6.git', 'topic/misc', 'tiwai-topic-misc', 'http://www.kernel.org/pub/scm/linux/kernel/git/tiwai/sound-2.6.git'),
        ('git://git.kernel.org/pub/scm/linux/kernel/git/tiwai/sound-2.6.git', 'topic/hda', 'tiwai-topic-hda', 'http://www.kernel.org/pub/scm/linux/kernel/git/tiwai/sound-2.6.git'),
        ('git://git.kernel.org/pub/scm/linux/kernel/git/tiwai/sound-2.6.git', 'topic/asoc', 'tiwai-topic-asoc', 'http://www.kernel.org/pub/scm/linux/kernel/git/tiwai/sound-2.6.git')
]
REPOSITORIES = [
        'alsa', 'alsa-driver', 'alsa-kmirror', 'alsa-lib', 'alsa-utils',
        'alsa-tools', 'alsa-firmware', 'alsa-oss', 'alsa-plugins',
        'alsa-python'
]        
ALSA_FILES = (
	'Documentation/sound/alsa/',
	'sound/',
	'include/sound/'
)
NOT_ALSA_FILES = (
	'sound/oss/',
)
ALSA_TRANSLATE = {
        'Documentation/DocBook/alsa-driver-api.tmpl': 'Documentation/DocBook/alsa-driver-api.tmpl',
        'Documentation/sound/alsa/':        'Documentation/',
        'include/sound/':                   'include/',
        'sound/':                           ''
}
ALSA_RTRANSLATE = {}
for i in ALSA_TRANSLATE:
  ALSA_RTRANSLATE[ALSA_TRANSLATE[i]] = i
