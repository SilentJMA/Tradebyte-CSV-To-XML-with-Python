# Tradebyte Panda CSV to XML Data Transformation

This Python script is designed to transform CSV data into an XML format based on a specific XML schema. It reads data from a source CSV file and generates an XML file structured according to the format of the destination XML object.
More information about the xml structure can be found at the [TB.IO homepage](https://www.tradebyte.io/documentation/examples-for-product-and-order-data/).

## Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system (Python 3.x recommended). You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).
- Necessary Python modules, including `csv`, `time` and `xml.etree.ElementTree`, which are typically included with Python.
- A source CSV file containing the data to be transformed `Attached is one, but you can request a sample from your Tradebyte Solution Delivery Manager during the integration`.
- Zalando.de sign is `zade` The Tradebyte info center contains the complete channels information for Zalando(de, at, it, fr....), Log in with your account and navigate to `Manuals > Channel-specific Manuals > Data maintenance for Zalando > Quick Start Guide`.

## Usage

1. Place your source CSV file in the same directory as the Python script, or specify the file path accordingly in the code.
   ```bash
   with open('source1.csv', mode='r', newline='', encoding='utf-8-sig') as csv_file:
   ```

3. Modify the code as needed to match your specific CSV data structure and the destination XML schema. Key elements to modify include field names, XML tags, and data mapping.

4. Run the Python script using the following command:

   ```bash
   python Tradebyte_Panda_CSV_To_XML.py
   ```

5. The script will read the source CSV file, transform the data, and generate an XML file named `PandaDDMMYYYYHHMMSS.xml` `DD:Day, MM: Month, YYYY: Year, HH: Hour, MM: Minute, SS: Second`in the same directory.

## CSV Source Format

The provided CSV source format includes the following columns:

- p_brand
- p_name
- p_text
- p_supplement
- ...
- a_delivery
- a_shipping_type
- a_intrastat
- a_media[image]{0}
- a_media[image]{1}
- a_active
- a_stock

The script reads this data and maps it to corresponding XML elements.


And the corresponding simplified destination XML format:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TBCATALOG version="1.4" >
  <PRODUCTDATA type="full">
    <PRODUCT>
      <P_NR>ProductA</P_NR>
      <P_NAME>
        <VALUE xml:lang="de-DE">ProductA</VALUE>
      </P_NAME>
      <!-- Add more elements here as needed -->
    </PRODUCT>
    <!-- Add more PRODUCT elements for each CSV row -->
  </PRODUCTDATA>
</TBCATALOG>
```

## Customization

- Customize the code to match your CSV data structure and XML schema.
- Adjust XML elements, attributes, and values according to your specific requirements.
- Handle CSV columns with multiple values or complex structures as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to customize this README further based on your specific project details and requirements.
