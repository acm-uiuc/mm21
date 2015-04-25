from map import Map
from json import dump, dumps, load, loads, JSONEncoder
import pickle


class PythonObjectEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}


def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(str(dct['_python_object']))
    return dct


if __name__ == "__main__":
    # Generate Map
    m = Map(2, 2, 2)

    # Convert to JSON
    with open("json.txt", "w") as outfile:
        dump(dumps(m.convert_to_json(), cls=PythonObjectEncoder), outfile, indent=2)
    # Test load JSON
    with open("json.txt", "r") as infile:
        print loads(load(infile), object_hook=as_python_object)
    # Print graph using networkx
    # m.draw_graph()
