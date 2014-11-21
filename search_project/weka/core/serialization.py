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

# serialization.py
# Copyright (C) 2014 Fracpete (fracpete at gmail dot com)

import javabridge
import logging
from weka.core.classes import JavaObject

# logging setup
logger = logging.getLogger(__name__)


def read(filename):
    """
    Reads the serialized object from disk. Caller must wrap object in appropriate Python wrapper class.
    :param filename: the file with the serialized object
    :type filename: str
    :return: the JB_Object
    :rtype: JB_Object
    """
    return javabridge.static_call(
        "Lweka/core/SerializationHelper;", "read",
        "(Ljava/lang/String;)Ljava/lang/Object;",
        filename)


def read_all(filename):
    """
    Reads the serialized objects from disk. Caller must wrap objects in appropriate Python wrapper classes.
    :param filename: the file with the serialized objects
    :type filename: str
    :return: the list of JB_OBjects
    :rtype: list
    """
    array = javabridge.static_call(
        "Lweka/core/SerializationHelper;", "readAll",
        "(Ljava/lang/String;)[Ljava/lang/Object;",
        filename)
    if array is None:
        return None
    else:
        return javabridge.get_env().get_object_array_elements(array)


def write(filename, jobject):
    """
    Serializes the object to disk. JavaObject instances get automatically unwrapped
    :param filename: the file to serialize the object to
    :type filename: str
    :param jobject: the object to serialize
    :type jobject: JB_Object or JavaObject
    """
    if isinstance(jobject, JavaObject):
        jobject = jobject.jobject
    javabridge.static_call(
        "Lweka/core/SerializationHelper;", "write",
        "(Ljava/lang/String;Ljava/lang/Object;)V",
        filename, jobject)


def write_all(filename, jobjects):
    """
    Serializes the list of objects to disk. JavaObject instances get automatically unwrapped
    :param filename: the file to serialize the object to
    :type filename: str
    :param jobjects: the list of objects to serialize
    :type jobjects: list
    """
    array = javabridge.get_env().make_object_array(len(jobjects), javabridge.get_env().find_class("java/lang/Object"))
    for i in xrange(len(jobjects)):
        obj = jobjects[i]
        if isinstance(obj, JavaObject):
            obj = obj.jobject
        javabridge.get_env().set_object_array_element(array, i, obj)
    javabridge.static_call(
        "Lweka/core/SerializationHelper;", "writeAll",
        "(Ljava/lang/String;[Ljava/lang/Object;)V",
        filename, array)
