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

# packages.py
# Copyright (C) 2014 Fracpete (fracpete at gmail dot com)

import javabridge
import weka.core.jvm as jvm
from weka.core.classes import JavaObject


class Package(JavaObject):
    """
    Wrapper for the org.pentaho.packageManagement.Package class.
    """

    def __init__(self, jobject):
        """
        Initializes the wrapper.
        :param jobject: the java Package instance to wrap
        :type jobject: JB_Object
        """
        self.enforce_type(jobject, "org.pentaho.packageManagement.Package")
        super(Package, self).__init__(jobject)

    def get_name(self):
        """
        Returns the name of the package.
        :return: the name
        :rtype: str
        """
        return javabridge.call(self.jobject, "getName", "()Ljava/lang/String;")

    def get_url(self):
        """
        Returns the URL of the package.
        :return: the url
        :rtype: str
        """
        return str(JavaObject(javabridge.call(self.jobject, "getPackageURL", "()Ljava/net/URL;")))

    def get_dependencies(self):
        """
        Returns the dependencies of the package.
        :return: the list of Dependency objects
        :rtype: list of Dependency
        """
        result = []
        dependencies = javabridge.get_collection_wrapper(
            javabridge.call(self.jobject, "getDependencies", "()Ljava/util/List;"))
        for dependency in dependencies:
            result.append(Dependency(dependency))
        return result

    def get_metadata(self):
        """
        Returns the meta-data.
        :return: the meta-data dictionary
        :rtype: dict
        """
        return javabridge.get_dictionary_wrapper(
            javabridge.call(self.jobject, "getPackageMetaData", "()Ljava/util/Map;"))

    def is_installed(self):
        """
        Returns whether the package is installed.
        :return: whether installed
        :rtype: bool
        """
        return javabridge.call(self.jobject, "isInstalled", "()Z")

    def install(self):
        """
        Installs the package.
        """
        return javabridge.call(self.jobject, "install", "()V")


class PackageConstraint(JavaObject):
    """
    Wrapper for the org.pentaho.packageManagement.PackageConstraint class.
    """

    def __init__(self, jobject):
        """
        Initializes the wrapper.
        :param jobject: the java PackageConstraint instance to wrap
        :type jobject: JB_Object
        """
        self.enforce_type(jobject, "org.pentaho.packageManagement.PackageConstraint")
        super(PackageConstraint, self).__init__(jobject)

    def set_package(self, pkge):
        """
        Sets the package.
        :param pkge: the package
        :type pkge: Package
        """
        javabridge.call(self.jobject, "setPackage", "(Lorg/pentaho/packageManagement/Package;)V", pkge.jobject)

    def get_package(self):
        """
        Returns the package.
        :return: the package
        :rtype: Package
        """
        return Package(javabridge.call(self.jobject, "getPackage", "()Lorg/pentaho/packageManagement/Package;"))

    def check_constraint(self, pkge=None, constr=None):
        """
        Checks the constraing.
        :param pkge: the package to check
        :type pkge: Package
        :param constr: the package constraint to check
        :type constr: PackageConstraint
        """
        if not pkge is None:
            return javabridge.call(
                self.jobject, "checkConstraint", "(Lorg/pentaho/packageManagement/Package;)Z", pkge.jobject)
        if not constr is None:
            return javabridge.call(
                self.jobject, "checkConstraint", "(Lorg/pentaho/packageManagement/PackageConstraint;)Z", pkge.jobject)
        raise Exception("Either package or package constraing must be provided!")


class Dependency(JavaObject):
    """
    Wrapper for the org.pentaho.packageManagement.Dependency class.
    """

    def __init__(self, jobject):
        """
        Initializes the wrapper.
        :param jobject: the java Dependency instance to wrap
        :type jobject: JB_Object
        """
        self.enforce_type(jobject, "org.pentaho.packageManagement.Dependency")
        super(Dependency, self).__init__(jobject)

    def set_source(self, pkge):
        """
        Sets the source package.
        :param pkge: the package
        :type pkge: Package
        """
        javabridge.call(
            self.jobject, "setSource", "(Lorg/pentaho/packageManagement/Package;)V", pkge.jobject)

    def get_source(self):
        """
        Returns the source package.
        :return: the package
        :rtype: Package
        """
        return Package(
            javabridge.call(self.jobject, "getSource", "()Lorg/pentaho/packageManagement/Package;"))

    def set_target(self, constr):
        """
        Sets the target package constraint.
        :param constr: the package constraint
        :type constr: Package
        """
        javabridge.call(
            self.jobject, "setTarget", "(Lorg/pentaho/packageManagement/PackageConstraint;)V", constr.jobject)

    def get_target(self):
        """
        Returns the target package constraint.
        :return: the package constraint
        :rtype: PackageConstraint
        """
        return PackageConstraint(
            javabridge.call(self.jobject, "getTarget", "()Lorg/pentaho/packageManagement/PackageConstraint;"))


def establish_cache():
    """
    Establishes the package cache if necessary.
    """
    javabridge.static_call(
        "weka/core/WekaPackageManager", "establishCacheIfNeeded", "([Ljava/io/PrintStream;)Ljava/lang/Exception;", [])


def get_all_packages():
    """
    Returns a list of all packages.
    :return: the list of packages
    :rtype: list
    """
    establish_cache()
    result = []
    pkgs = javabridge.get_collection_wrapper(
        javabridge.static_call(
            "weka/core/WekaPackageManager", "getAllPackages", "()Ljava/util/List;"))
    for pkge in pkgs:
        result.append(Package(pkge))
    return result


def get_available_packages():
    """
    Returns a list of all packages that aren't installed yet.
    :return: the list of packages
    :rtype: list
    """
    establish_cache()
    result = []
    pkgs = javabridge.get_collection_wrapper(
        javabridge.static_call(
            "weka/core/WekaPackageManager", "getAvailablePackages", "()Ljava/util/List;"))
    for pkge in pkgs:
        result.append(Package(pkge))
    return result


def get_installed_packages():
    """
    Returns a list of the installed packages.
    :return: the list of packages
    :rtype: list
    """
    establish_cache()
    result = []
    pkgs = javabridge.get_collection_wrapper(
        javabridge.static_call(
            "weka/core/WekaPackageManager", "getInstalledPackages", "()Ljava/util/List;"))
    for pkge in pkgs:
        result.append(Package(pkge))
    return result


def install_package(pkge, version="Latest"):
    """
    The list of packages to install.
    :param pkge: the name of the repository package, a URL (http/https) or a zip file
    :type pkge: str
    :param version: in case of the repository packages, the version
    :type version: str
    :return: whether successfully installed
    :rtype: bool
    """
    establish_cache()
    if pkge.startswith("http://") or pkge.startswith("https://"):
        url = javabridge.make_instance(
            "java/net/URL", "(Ljava/lang/String;)V", javabridge.get_env().new_string_utf(pkge))
        return not javabridge.static_call(
            "weka/core/WekaPackageManager", "installPackageFromURL",
            "(Ljava/net/URL;[Ljava/io/PrintStream;)Ljava/lang/String;", url, []) is None
    elif pkge.lower().endswith(".zip"):
        return not javabridge.static_call(
            "weka/core/WekaPackageManager", "installPackageFromArchive",
            "(Ljava/lang/String;[Ljava/io/PrintStream;)Ljava/lang/String;", pkge, []) is None
    else:
        return javabridge.static_call(
            "weka/core/WekaPackageManager", "installPackageFromRepository",
            "(Ljava/lang/String;Ljava/lang/String;[Ljava/io/PrintStream;)Z", pkge, version, [])


def uninstall_package(name):
    """
    Uninstalls a package.
    :param name: the name of the package
    :type name: str
    :return: whether successfully uninstalled
    :rtype: bool
    """
    establish_cache()
    javabridge.static_call(
        "weka/core/WekaPackageManager", "uninstallPackage",
        "(Ljava/lang/String;Z[Ljava/io/PrintStream;)V", name, True, [])


def is_installed(name):
    """
    Checks whether a package with the name is already installed.
    :param name: the name of the package
    :type name: str
    :return: whether the package is installed
    :rtype: bool
    """
    pkgs = get_installed_packages()
    for pkge in pkgs:
        if pkge.get_name() == name:
            return True
    return False

if __name__ == "__main__":
    jvm.start()
    try:
        print("Establish cache")
        print("===============")
        establish_cache()

        print("All packages")
        print("============")
        packages = get_all_packages()
        for pkg in packages:
            print(pkg.get_name())
            print("  url: " + pkg.get_url())
            print("")

        print("Available packages")
        print("==================")
        packages = get_available_packages()
        p = packages[0]
        for pkg in packages:
            print(pkg.get_name())
            print("  url: " + pkg.get_url())
            print("")

        print("Installed packages")
        print("==================")
        packages = get_installed_packages()
        for pkg in packages:
            print(pkg.get_name())
            print("  url: " + pkg.get_url())
            print("")

        print("Install/Uninstall")
        print("=================")
        print("Install: " + p.get_name())
        print(install_package(p.get_url()))

        print("Uninstall: " + p.get_name())
        uninstall_package(p.get_name())
    except Exception, e:
        print(e)
    finally:
        jvm.stop()
