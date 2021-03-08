from setuptools import setup, find_packages
import os
import subprocess

project_version = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
assert "." in project_version

assert os.path.isfile("django-upstorage-backend/version.py")
with open("django-upstorage-backend/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{project_version}\n")


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


# Setting up
setup(
    name="django-upstorage-backend",
    version=project_version,
    author="Sakib (Florian Dedov)",
    author_email="<mail@neuralnine.com>",
    long_description_content_type="text/markdown",
    long_description=read_file('README.md'),
    description='Custom Storage For UpStorage.',
    packages=find_packages(),
    url='https://github.com/QuackCoding/DjangoUpStorageBackend',
    package_data={'UpStorageApiClient': ['VERSION']},
    install_requires=['UpStorageApiClient'],
    keywords=['python', 'storage', 'api', 'upstorage', 'django-upstorage-backend'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
