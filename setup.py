import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = 'gapitasks',
    version = "0.0.1",
    description = 'A fork from the greatest gtasks ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'BlueBlueBlob',
    author_email = 'adrien.lesot@gmail.com',
    url = 'https://github.com/BlueBlueBlob/Gtasks2',
    license = 'MIT',
    install_requires = [
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib",
        "iso8601"
    ],
    packages= setuptools.find_packages(),
    keywords = ['google', 'tasks', 'task', 'gtasks', 'gtask']
)
