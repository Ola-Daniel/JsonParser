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

    def convert_python_to_json(self, par_data_dic, par_json_file=""):
        """
        this function converts dictionary of data to json string and store it in json file
        json file pass provided if not it only returns the json string
        :param par_data_dic:
        :param par_json_file:
        :return: json string/ json file
        """
        if par_json_file:
            with open(par_json_file, "w") as outfile:
                return json.dump(par_data_dic, outfile)
        else:
            return json.dump(par_data_dic)

    def get_json_value(self, par_value, par_json_file):
        """
        this function gets specific dictionary key value from json file
        :param par_value:
        :param par_json_file:
        :return: value result
        """
        data_dic = self.convert_json_to_python(par_json_file)
        return data_dic[par_value]
