import json
        

class handler:
    """
    A class to handle searching and retrieving information about Algerian Wilayas and Communes.
    """

    def searchByCode(self, wilayaCode):
        """
        Search for a Wilaya by its code.
        
        :param wilayaCode: int: The code of the Wilaya to search for.
        :return: dict: The information of the Wilaya.
        :raises Exception: If the Wilaya code is not valid.
        """
        if wilayaCode <= 0 or wilayaCode > 58 or wilayaCode is None:
            raise Exception("Wilaya code is not valid!")
        
        with open('wilaya\Wilaya_Of_Algeria.json', 'r', encoding='utf8') as w:
            data = json.load(w)

        return data[wilayaCode-1]
    

    def searchByName(self, name):
        """
        Search for a Wilaya by its name.
        
        :param name: str: The name of the Wilaya to search for.
        :return: dict: The information of the Wilaya.
        :raises Exception: If the Wilaya name is not valid.
        """
        if name is None:
            raise Exception("Wilaya name is not valid!")
        
        with open('wilaya\Wilaya_Of_Algeria.json', 'r', encoding='utf8') as w:
            data = [wilaya for wilaya in json.load(w) if wilaya['name'].lower() == name.lower()]
            
        return data[0]
    

    def getBaladiyat(self, wilayaCode):
        """
        Get all Baladiyat for a given Wilaya code.
        
        :param wilayaCode: int: The code of the Wilaya.
        :return: list: A list of Baladiyat for the Wilaya.
        :raises Exception: If the Wilaya code is not valid.
        """
        if wilayaCode <= 0 or wilayaCode > 58 or wilayaCode is None:
            raise Exception("Wilaya code is not valid!")
        
        with open('wilaya\Commune_Of_Algeria.json', 'r', encoding='utf8') as w:
            data = [baladiya for baladiya in json.load(w) if baladiya['wilaya_id'] == str(wilayaCode)]
            
        return data
    

    def searchBaladiya(self, baladiyaName):
        """
        Search for a Baladiya by its name.
        
        :param baladiyaName: str: The name of the Baladiya to search for.
        :return: dict: The information of the Baladiya.
        :raises Exception: If the Baladiya name is not valid or not found.
        """
        if baladiyaName is None:
            raise Exception("Baladiya name code is not valid!")
        
        with open('wilaya\Commune_Of_Algeria.json', 'r', encoding='utf8') as w:
            data = [baladiya for baladiya in json.load(w) if baladiya['name'].lower() == baladiyaName.lower() or baladiyaName.lower() in baladiya['name'].lower()]
        
        try:
            return data[0]
        except:
            return []