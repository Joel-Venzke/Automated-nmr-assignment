# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# jvm.py
# Copyright (C) 2014 Fracpete (fracpete at gmail dot com)

import javabridge
import os
import glob
import logging


started = None

# logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def add_bundled_jars():
    """
     Adds the bundled jars to the JVM's classpath.
    """
    # determine lib directory with jars
    rootdir = os.path.split(os.path.dirname(__file__))[0]
    libdir = rootdir + os.sep + "lib"

    # add jars from lib directory
    for l in glob.glob(libdir + os.sep + "*.jar"):
        if l.lower().find("-src.") == -1:
            javabridge.JARS.append(str(l))


def add_weka_packages():
    """
    Adds the jars from all Weka packages to the JVM's classpath.
    """
    prefix = os.getenv("WEKA_HOME", "~")
    package_dir = os.path.expanduser(prefix + os.sep + "wekafiles" + os.sep + "packages")
    logger.debug("package_dir=" + package_dir)
    # traverse packages
    for p in os.listdir(package_dir):
        if os.path.isdir(package_dir + os.sep + p):
            directory = package_dir + os.sep + p
            logger.debug("  directory=" + directory)
            # inspect package directory
            for l in os.listdir(directory):
                if l.lower().endswith(".jar"):
                    javabridge.JARS.append(directory + os.sep + l)
                if l == "lib":
                    for m in glob.glob(directory + os.sep + "lib" + os.sep + "*.jar"):
                        javabridge.JARS.append(m)


def add_system_classpath():
    """
    Adds the system's classpath to the JVM's classpath.
    """
    if not os.environ['CLASSPATH'] is None:
        parts = os.environ['CLASSPATH'].split(os.pathsep)
        for part in parts:
            javabridge.JARS.append(part)


def start(class_path=None, bundled=True, packages=False, system_cp=False, max_heap_size=None):
    """
    Initializes the javabridge connection (starts up the JVM).
    :param class_path: the additional classpath elements to add
    :type class_path: str
    :param bundled: whether to add jars from the "lib" directory
    :type bundled: bool
    :param packages: whether to add jars from Weka packages as well
    :type packages: bool
    :param system_cp: whether to add the system classpath as well
    :type system_cp: bool
    :param max_heap_size: the maximum heap size (-Xmx parameter, eg 512m or 4g)
    :type max_heap_size: str
    """
    global started

    if not started is None:
        logger.info("JVM already running, call jvm.stop() first")
        return

    # add user-defined jars first
    if not class_path is None:
        for cp in class_path:
            logger.debug("Adding user-supplied classpath=" + cp)
            javabridge.JARS.append(cp)

    if bundled:
        logger.debug("Adding bundled jars")
        add_bundled_jars()

    if packages:
        logger.debug("Adding Weka packages")
        add_weka_packages()

    if system_cp:
        logger.debug("Adding system classpath")
        add_system_classpath()

    logger.debug("Classpath=" + str(javabridge.JARS))
    logger.debug("MaxHeapSize=" + ("default" if (max_heap_size is None) else max_heap_size))

    javabridge.start_vm(run_headless=True, max_heap_size=max_heap_size)
    javabridge.attach()
    started = True


def stop():
    """ Kills the JVM. """
    global started
    if not started is None:
        started = None
        javabridge.kill_vm()
