import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = 'gtasks_api',
    version = "0.0.7",
    description = 'Based on quickstart sample by Google',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'BlueBlueBlob',
    author_email = 'adrien.lesot@gmail.com',
    url = 'https://github.com/BlueBlueBlob/gtasks_api',
    license = 'MIT',
    install_requires = [
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib"
    ],
    packages= setuptools.find_packages(),
    keywords = ['google', 'tasks', 'task', 'gtasks', 'gtask']
)
