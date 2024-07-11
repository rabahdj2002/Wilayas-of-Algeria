### Module Description: Algerian Location Handler

This Python module provides functionality for searching and retrieving information about Algerian Wilayas (provinces) and their respective Communes (municipalities). The module reads data from JSON files containing detailed information about Wilayas and Communes and provides methods to access this information based on specific criteria.

#### Features:

1. **Search by Wilaya Code**:
   - Method: `searchByCode(wilayaCode)`
   - Description: Retrieves information about a Wilaya based on its unique code.
   - Parameters: 
     - `wilayaCode` (int): The code of the Wilaya to search for.
   - Returns: A dictionary containing information about the Wilaya.
   - Raises: Exception if the provided code is invalid or out of range.

2. **Search by Wilaya Name**:
   - Method: `searchByName(name)`
   - Description: Retrieves information about a Wilaya based on its name.
   - Parameters: 
     - `name` (str): The name of the Wilaya to search for.
   - Returns: A dictionary containing information about the Wilaya.
   - Raises: Exception if the provided name is invalid or not found.

3. **Get Baladiyat (Communes) of a Wilaya**:
   - Method: `getBaladiyat(wilayaCode)`
   - Description: Retrieves a list of all Baladiyat (Communes) within a specified Wilaya.
   - Parameters: 
     - `wilayaCode` (int): The code of the Wilaya.
   - Returns: A list of dictionaries, each containing information about a Baladiya.
   - Raises: Exception if the provided code is invalid or out of range.

4. **Search for a Baladiya by Name**:
   - Method: `searchBaladiya(baladiyaName)`
   - Description: Retrieves information about a Baladiya based on its name.
   - Parameters: 
     - `baladiyaName` (str): The name of the Baladiya to search for.
   - Returns: A dictionary containing information about the Baladiya.
   - Raises: Exception if the provided name is invalid or not found.

### Installation:

To use this module, you need to download the wilaya file containing the Wilaya and Commune data and import it using:

```
from wilaya import handler
```

#### Usage Example:

```python
# Import the handler class from the module
from wilaya import handler

# Create an instance of the handler class
handler_instance = handler()

# Search for a Wilaya by its code
wilaya_info_by_code = handler_instance.searchByCode(16)
print(wilaya_info_by_code)

# Search for a Wilaya by its name
wilaya_info_by_name = handler_instance.searchByName("Alger")
print(wilaya_info_by_name)

# Get all Baladiyat for a given Wilaya code
baladiyat_list = handler_instance.getBaladiyat(16)
print(baladiyat_list)

# Search for a Baladiya by its name
baladiya_info_by_name = handler_instance.searchBaladiya("Ouled Fayet")
print(baladiya_info_by_name)
```



### Summary:

This module is a handy tool for accessing and processing information about Algerian Wilayas and Communes. It simplifies the process of retrieving data based on codes or names, making it useful for applications requiring geographical data handling within Algeria.