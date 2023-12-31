import csv
import xml.etree.ElementTree as ET
import time
from datetime import datetime
import os

# Define input and output folder paths
input_folder = 'input'
output_folder = 'output'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get the current Unix timestamp
current_timestamp = str(int(time.time()))

# Build the input and output file paths
input_csv_file = os.path.join(input_folder, 'source1.csv')
output_xml_file = os.path.join(output_folder, f'Panda_{current_timestamp}.xml')

# Read the source CSV data
with open(input_csv_file, mode='r', newline='', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Create the XML root element
    root = ET.Element("TBCATALOG", version="1.3", creation=current_timestamp)

    # Create PRODUCTDATA and PRODUCT elements
    product_data = ET.SubElement(root, "PRODUCTDATA", type="full")
    product = ET.SubElement(product_data, "PRODUCT")

    for row in csv_reader:
        # Create unique P_NR product number of the merchant  element
        p_nr = ET.SubElement(product, "P_NR")
        p_nr.text = row["p_nr"]

        # Create P_NAME element German Language
        p_name = ET.SubElement(product, "P_NAME")
        value = ET.SubElement(p_name, "VALUE", **{"xml:lang": "de-DE"})
        value.text = row["p_name"]
        # Create P_NAME element English Language
        value = ET.SubElement(p_name, "VALUE", **{"xml:lang": "en-US"})
        value.text = row["<en>p_name"]

        # Create P_TEXT element
        p_text = ET.SubElement(product, "P_TEXT")
        value = ET.SubElement(p_text, "VALUE", **{"xml:lang": "de-DE"})
        value.text = row["p_text"]
        value = ET.SubElement(p_text, "VALUE", **{"xml:lang": "en-US"})
        value.text = row["<en>p_text"]

        # Create P_BRAND element
        p_brand = ET.SubElement(product, "P_BRAND", identifier="name", key=row["p_brand"])

        #Create Keywords

        p_keywords = ET.SubElement(product, "P_KEYWORDS")

        # Split the 'en-US' keywords
        en_us_keywords = row["<en>p_keywords"].split(",")

        # Split the 'p_keywords' by comma and iterate through keywords
        for keyword in row["p_keywords"].split(","):
            keyword_element = ET.SubElement(p_keywords, "P_KEYWORD")

            # Add the 'de-DE' value element for the current keyword
            value_element_de = ET.SubElement(keyword_element, "VALUE", **{"xml:lang": "de-DE"})
            value_element_de.text = keyword.strip()  # Remove leading/trailing spaces

            # Check if there are corresponding 'en-US' keywords
            if en_us_keywords:
                # Add the 'en-US' value element for the current keyword
                value_element_en = ET.SubElement(keyword_element, "VALUE", **{"xml:lang": "en-US"})
                value_element_en.text = en_us_keywords.pop(0).strip()

        # Create P_COMPONENTDATA element
        p_component_data = ET.SubElement(product, "P_COMPONENTDATA")
        p_component = ET.SubElement(p_component_data, "P_COMPONENT", identifier="key", key="Materialzusammensetzung")
        value = ET.SubElement(p_component, "VALUE", **{"xml:lang": "de-DE"})
        value.text = row["p_comp[material]"]
        value = ET.SubElement(p_component, "VALUE", **{"xml:lang": "en-US"})
        value.text = row["<en>p_comp[material]"]

        # Create P_TAGS element
        p_tags = ET.SubElement(product, "P_TAGS")
        p_tag = ET.SubElement(p_tags, "P_TAG", identifier="key", key="Größenraster")
        values = ET.SubElement(p_tag, "VALUES")
        value = ET.SubElement(values, "VALUE", identifier="key", key="")

        # Add more P_TAG elements for other tags as needed

        # Create P_BULLETS element
        p_bullets = ET.SubElement(product, "P_BULLETS")
        bullet_list = row["p_bullet{0}"].split(",")
        for idx, bullet in enumerate(bullet_list):
            p_bullet = ET.SubElement(p_bullets, "P_BULLET", sort=str(idx + 10))
            value = ET.SubElement(p_bullet, "VALUE", **{"xml:lang": "de-DE"})
            value.text = bullet

        # Create P_MEDIADATA element
        p_media_data = ET.SubElement(product, "P_MEDIADATA")
        for idx in range(2):
            p_media = ET.SubElement(p_media_data, "P_MEDIA", type="image", sort=str(idx * 10 + 30))
            p_media.text = row[f"p_media[image]{{{idx}}}"]

            # Create ARTICLEDATA and ARTICLE elements
            article_data = ET.SubElement(product, "ARTICLEDATA")
            article = ET.SubElement(article_data, "ARTICLE")

            # Create A_NR element
            a_nr = ET.SubElement(article, "A_NR")
            a_nr.text = row["a_nr"]

            # Create A_ACTIVEDATA element
            a_active_data = ET.SubElement(article, "A_ACTIVEDATA")
            a_active = ET.SubElement(a_active_data, "A_ACTIVE", channel="zade")
            a_active.text = row["a_active"]

            # Create A_EAN element
            a_ean = ET.SubElement(article, "A_EAN")
            a_ean.text = row["a_ean"]

            # Create A_PROD_NR element
            a_prod_nr = ET.SubElement(article, "A_PROD_NR")
            a_prod_nr.text = row["a_prodnr"]

            # Add more elements as needed

            # Create A_VARIANTDATA element
            a_variant_data = ET.SubElement(article, "A_VARIANTDATA")
            a_variant_color = ET.SubElement(a_variant_data, "A_VARIANT", identifier="key", key="Farbe")
            value = ET.SubElement(a_variant_color, "VALUE", **{"xml:lang": "de-DE"})
            value.text = row["a_comp[color]"]
            value = ET.SubElement(a_variant_color, "VALUE", **{"xml:lang": "en-US"})
            value.text = row["<en>a_comp[color]"]

            a_variant_size = ET.SubElement(a_variant_data, "A_VARIANT", identifier="key", key="Größe")
            value = ET.SubElement(a_variant_size, "VALUE", **{"xml:lang": "de-DE"})
            value.text = row["a_comp[size]"]

            # Create A_PRICEDATA element
            a_price_data = ET.SubElement(article, "A_PRICEDATA")

            # Zalando.de sign is zade and channel id is 30 you can find the channels information in Tradebyte info center Manuals > Channel-specific Manuals > Data maintenance for Zalando > Quick Start Guide
            a_price = ET.SubElement(a_price_data, "A_PRICE", channel="zade", currency="EUR")
            a_vk = ET.SubElement(a_price, "A_VK")
            a_vk.text = row["a_vk[zade]"]
            a_vk_old = ET.SubElement(a_price, "A_VK_OLD")
            a_vk_old.text = row["a_vk_old[zade]"]
            a_uvp = ET.SubElement(a_price, "A_UVP")
            a_uvp.text = row["a_uvp[zade]"]

            # Create A_MEDIADATA element
            a_media_data = ET.SubElement(article, "A_MEDIADATA")
            for idx in range(2):
                a_media = ET.SubElement(a_media_data, "A_MEDIA", type="image", sort=str(idx * 10 + 10))
                a_media.text = row[f"a_media[image]{{{idx}}}"]

            # Create A_STOCK element
            a_stock = ET.SubElement(article, "A_STOCK")
            a_stock.text = row["a_stock"]

            # Create A_DELIVERY_TIME element
            a_delivery_time = ET.SubElement(article, "A_DELIVERY_TIME")
            a_delivery_time.text = row["a_delivery"]

            # Create an ElementTree from the root
            tree = ET.ElementTree(root)

            # Write the resulting XML to the output folder
            tree.write(output_xml_file, encoding="utf-8", xml_declaration=True)