"""
Out of the box, Python's json module can't dump dataclasses.

Here's a workaround, thanks to:
    https://stackoverflow.com/a/51286749/2071807
"""
import dataclasses
import json


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def json_dump_class(*args, **kwargs):
    return json.dumps(*args, **kwargs, cls=EnhancedJSONEncoder)
