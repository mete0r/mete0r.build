from setuptools.dist import Distribution

from babel.messages.frontend import compile_catalog


__version__ = '0.0.0'


def install(dist: Distribution):
    if should_activate(dist):
        dist.cmdclass.update(compile_catalog=compile_catalog)
        build = dist.get_command_obj("build")
        build.sub_commands = [("compile_catalog", None), *build.sub_commands]


def should_activate(dist: Distribution):
    return True
