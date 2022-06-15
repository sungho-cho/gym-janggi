from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gym_janggi",
    version="0.9.24",
    author="Sungho Cho",
    author_email="didog9595@gmail.com",
    description="OpenAI Gym environment for Korean chess Janggi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sungho-cho/gym-janggi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    packages=["gym_janggi", "gym_janggi/envs"],
    python_requires=">=3.6",
    install_requires=["gym==0.23.1", "janggi==1.0.5"],
)
