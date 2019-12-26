# phishdetect-python

This is a Python3 library to easily interact with a [PhishDetect Node](https://github.com/phishdetect/phishdetect-node) API server.

## Installation

It can be installed with:

	pip3 install phishdetect

Or by downloading directly from the GitHub repository:

	pip3 install --upgrade https://github.com/phishdetect/phishdetect-python/archive/master.zip

## Quickstart

Firstly, we instantiate a `PhishDetect` object:

```python
import phishdetect

# You have to specify the base host of your PhishDetect Node (including the schema).
# The API key is optional, although it is required by some admin-level APIs.
pd = phishdetect.PhishDetect(host="https://your-server.com", api_key="your-api-key")
```

From the `PhishDetect` instance we can now access some models to interact with various records. For example:

```python
# To fetch all recent indicators:
iocs = pd.indicators.fetch_recent()

# To fetch all recent events:
events = pd.events.fetch()
# To fetch only a selection:
events = pd.events.fetch(limit=10, offset=10)

# To interact with users:
pending = pd.users.get_pending()
active = pd.users.get_active()
pd.users.activate(api_key="user-api-key")
pd.users.deactivate(api_key="user-api-key")

# To download raw messages shared with the Node:
messages = pd.raw.fetch(limit=10, offset=10)
for entry in messages:
	msg = pd.raw.details(uuid=entry["uuid"])
```

For a complete reference, run:

	pydoc3 -b phishdetect

## License

This library is released under [MIT License](LICENSE) and is copyrighted by [Claudio Guarnieri](https://nex.sx/).
