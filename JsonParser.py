import json


class JsonParser:
    """
    this class to handle anything related to json file
    """

    def convert_json_to_python(self, par_json_file):
        """
        this function to convert any json file format to dictionary
        :param jsonfile:
        :return: dictionary contains json file data
        """
        with open(par_json_file) as json_file:
            data_dic = json.load(json_file)
        return data_dic
