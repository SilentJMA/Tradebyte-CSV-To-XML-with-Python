# Tradebyte Panda CSV to XML Data Transformation

This Python script is designed to transform CSV data into an XML format based on a specific XML schema. It reads data from a source CSV file and generates an XML file structured according to the format of the destination XML object.

## Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system (Python 3.x recommended).
- Necessary Python modules, including `csv` and `xml.etree.ElementTree`, which are typically included with Python.
- A source CSV file containing the data to be transformed.
- The XML schema for the destination XML object, which defines the structure of the output XML.

## Usage

1. Place your source CSV file in the same directory as the Python script, or specify the file path accordingly in the code.

2. Modify the code as needed to match your specific CSV data structure and the destination XML schema. Key elements to modify include field names, XML tags, and data mapping.

3. Run the Python script using the following command:

   ```bash
   python csv_to_xml.py
   ```

4. The script will read the source CSV file, transform the data, and generate an XML file named `destination.xml` in the same directory.

## Example

Here's a simplified example of the source CSV data:

```csv
p_brand,p_name,p_text,p_comp[material],p_bullet{0},a_active,a_comp[color],a_comp[size]
BrandA,ProductA,DescriptionA,MaterialA,Bullet1,1,Red,Large
BrandB,ProductB,DescriptionB,MaterialB,Bullet2,0,Blue,Medium
```

And the corresponding simplified destination XML format:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TBCATALOG version="1.4" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://api.trade-server.net/schema/all_in_one/tb-cat_1_4_import.xsd">
  <PRODUCTDATA type="full">
    <PRODUCT>
      <P_NR>ProductA</P_NR>
      <P_NAME>
        <VALUE xml:lang="x-default">ProductA</VALUE>
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
