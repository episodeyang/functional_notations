from setuptools import setup

with open("VERSION", "r") as f:
    version = f.read().strip()

setup(name="functional_notations",
      description="A Decorator Library that allows @ notation for functions",
      long_description="Abuses the @ notation of python3.5, allowing you to chain functions with the @ operator.",
      version=version,
      url="https://github.com/episodeyang/functional_notations",
      author="Ge Yang",
      author_email="ge.ike.yang@gmail.com",
      license=None,
      keywords=["functional notations", "decorator", "functional", "functional programming"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Science/Research",
          "Programming Language :: Python :: 3"
      ],
      packages=["functional_notations"],
      install_requires=[]
      )
