import json
import os

_DATA_DIR = os.path.dirname(os.path.abspath(__file__))
_cache = {}

WILAYA_COUNT = 58


def _load(filename):
    if filename not in _cache:
        path = os.path.join(_DATA_DIR, filename)
        with open(path, encoding="utf-8") as f:
            _cache[filename] = json.load(f)
    return _cache[filename]


def _wilayas():
    return _load("Wilaya_Of_Algeria.json")


def _communes():
    return _load("Commune_Of_Algeria.json")


def _validate_wilaya_code(wilaya_code):
    """Return the code as int, or raise ValueError."""
    if isinstance(wilaya_code, bool) or (
        isinstance(wilaya_code, float) and not wilaya_code.is_integer()
    ):
        raise ValueError("Wilaya code is not valid!")
    try:
        code = int(wilaya_code)
    except (TypeError, ValueError):
        raise ValueError("Wilaya code is not valid!") from None
    if code < 1 or code > WILAYA_COUNT:
        raise ValueError("Wilaya code is not valid!")
    return code


def _validate_name(name, kind):
    if not isinstance(name, str) or not name.strip():
        raise ValueError(f"{kind} name is not valid!")
    return name.strip()


class handler:
    """
    A class to handle searching and retrieving information about Algerian Wilayas and Communes.
    """

    def searchByCode(self, wilayaCode):
        """
        Search for a Wilaya by its code.

        :param wilayaCode: int: The code of the Wilaya to search for.
        :return: dict: The information of the Wilaya.
        :raises ValueError: If the Wilaya code is not valid.
        """
        code = _validate_wilaya_code(wilayaCode)

        for wilaya in _wilayas():
            if int(wilaya["id"]) == code:
                return wilaya

        raise ValueError("Wilaya code is not valid!")

    def searchByName(self, name):
        """
        Search for a Wilaya by its name.

        :param name: str: The name of the Wilaya to search for.
        :return: dict: The information of the Wilaya.
        :raises ValueError: If the Wilaya name is not valid or not found.
        """
        name = _validate_name(name, "Wilaya")

        matches = [
            wilaya
            for wilaya in _wilayas()
            if wilaya["name"].lower() == name.lower()
        ]
        if not matches:
            raise ValueError(f"Wilaya '{name}' not found!")
        return matches[0]

    def getBaladiyat(self, wilayaCode):
        """
        Get all Baladiyat for a given Wilaya code.

        :param wilayaCode: int: The code of the Wilaya.
        :return: list: A list of Baladiyat for the Wilaya.
        :raises ValueError: If the Wilaya code is not valid.
        """
        code = _validate_wilaya_code(wilayaCode)

        return [
            baladiya
            for baladiya in _communes()
            if int(baladiya["wilaya_id"]) == code
        ]

    def searchBaladiya(self, baladiyaName):
        """
        Search for a Baladiya by its name.

        :param baladiyaName: str: The name of the Baladiya to search for.
        :return: dict: The information of the Baladiya.
        :raises ValueError: If the Baladiya name is not valid or not found.
        """
        name = _validate_name(baladiyaName, "Baladiya")

        matches = [
            baladiya
            for baladiya in _communes()
            if baladiya["name"].lower() == name.lower()
            or name.lower() in baladiya["name"].lower()
        ]
        if not matches:
            raise ValueError(f"Baladiya '{name}' not found!")
        return matches[0]
