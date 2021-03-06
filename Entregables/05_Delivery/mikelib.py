{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": 3
  },
  "orig_nbformat": 2
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Sistema\n",
    "import os,sys,inspect\n",
    "\n",
    "import requests     #Traer el fichero de internet\n",
    "import json         # Trabaja con ficheros json\n",
    "import pandas as pd # Librería para el data mining y data wrangling\n",
    "import numpy as np \n",
    "\n",
    "# visualización\n",
    "from skimage.io import imread\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib.pyplot import *\n",
    "import scipy.stats as stats\n",
    "import seaborn as sns\n",
    "from mpl_toolkits.axes_grid1 import make_axes_locatable\n",
    "\n",
    "\"\"\"\n",
    "    xmldict\n",
    "    ~~~~~~~~~~~~~~~~~~~~~~~~~\n",
    "    Convert xml to python dictionaries.\n",
    "\"\"\"\n",
    "import datetime\n",
    "\n",
    "def xml_to_dict(root_or_str, strict=True):\n",
    "    \"\"\"\n",
    "    Converts `root_or_str` which can be parsed xml or a xml string to dict.\n",
    "    \"\"\"\n",
    "    root = root_or_str\n",
    "    if isinstance(root, str):\n",
    "        import xml.etree.cElementTree as ElementTree\n",
    "        root = ElementTree.XML(root_or_str)\n",
    "    return {root.tag: _from_xml(root, strict)}\n",
    "\n",
    "def dict_to_xml(dict_xml):\n",
    "    \"\"\"\n",
    "    Converts `dict_xml` which is a python dict to corresponding xml.\n",
    "    \"\"\"\n",
    "    return _to_xml(dict_xml)\n",
    "\n",
    "# Functions below this line are implementation details.\n",
    "# Unless you are changing code, don't bother reading.\n",
    "# The functions above constitute the user interface.\n",
    "\n",
    "def _to_xml(el):\n",
    "    \"\"\"\n",
    "    Converts `el` to its xml representation.\n",
    "    \"\"\"\n",
    "    val = None\n",
    "    if isinstance(el, dict):\n",
    "        val = _dict_to_xml(el)\n",
    "    elif isinstance(el, bool):\n",
    "        val = str(el).lower()\n",
    "    else:\n",
    "        val = el\n",
    "    if val is None: val = 'null'\n",
    "    return val\n",
    "\n",
    "def _extract_attrs(els):\n",
    "    \"\"\"\n",
    "    Extracts attributes from dictionary `els`. Attributes are keys which start\n",
    "    with '@'\n",
    "    \"\"\"\n",
    "    if not isinstance(els, dict):\n",
    "        return ''\n",
    "    return ''.join(' %s=\"%s\"' % (key[1:], value) for key, value in els.iteritems()\n",
    "                   if key.startswith('@'))\n",
    "\n",
    "def _dict_to_xml(els):\n",
    "    \"\"\"\n",
    "    Converts `els` which is a python dict to corresponding xml.\n",
    "    \"\"\"\n",
    "    def process_content(tag, content):\n",
    "        attrs = _extract_attrs(content)\n",
    "        text = isinstance(content, dict) and content.get('#text', '') or ''\n",
    "        return '<%s%s>%s%s</%s>' % (tag, attrs, _to_xml(content), text, tag)\n",
    "\n",
    "    tags = []\n",
    "    for tag, content in els.iteritems():\n",
    "        # Text and attributes\n",
    "        if tag.startswith('@') or tag == '#text' or tag == '#value':\n",
    "            continue\n",
    "        elif isinstance(content, list):\n",
    "            for el in content:\n",
    "                tags.append(process_content(tag, el))\n",
    "        elif isinstance(content, dict):\n",
    "            tags.append(process_content(tag, content))\n",
    "        else:\n",
    "            tags.append('<%s>%s</%s>' % (tag, _to_xml(content), tag))\n",
    "    return ''.join(tags)\n",
    "\n",
    "def _str_to_datetime(date_str):\n",
    "    try:\n",
    "        val = datetime.datetime.strptime(date_str,  \"%Y-%m-%dT%H:%M:%SZ\")\n",
    "    except ValueError:\n",
    "        val = date_str\n",
    "    return val\n",
    "\n",
    "def _str_to_boolean(bool_str):\n",
    "    if bool_str.lower() != 'false' and bool(bool_str):\n",
    "        return True\n",
    "    return False\n",
    "\n",
    "def _from_xml(el, strict):\n",
    "    \"\"\"\n",
    "    Extracts value of xml element element `el`.\n",
    "    \"\"\"\n",
    "    val = None\n",
    "    # Parent node.\n",
    "    if len(el):\n",
    "        val = {}\n",
    "        for e in el:\n",
    "            tag = e.tag\n",
    "            v = _from_xml(e, strict)\n",
    "            if tag in val:\n",
    "                # Multiple elements share this tag, make them a list\n",
    "                if not isinstance(val[tag], list):\n",
    "                    val[tag] = [val[tag]]\n",
    "                val[tag].append(v)\n",
    "            else:\n",
    "                # First element with this tag\n",
    "                val[tag] = v\n",
    "    # Simple node.\n",
    "    else:\n",
    "        attribs = el.items()\n",
    "        # An element with attributes.\n",
    "        if attribs and strict:\n",
    "            val = dict(('@%s' % k, v) for k, v in dict(attribs).iteritems())\n",
    "            if el.text:\n",
    "                converted = _val_and_maybe_convert(el)\n",
    "                val['#text'] = el.text\n",
    "                if converted != el.text:\n",
    "                    val['#value'] = converted\n",
    "        elif el.text:\n",
    "            # An element with no subelements but text.\n",
    "            val = _val_and_maybe_convert(el)\n",
    "        elif attribs:\n",
    "            val = dict(attribs)\n",
    "    return val\n",
    "\n",
    "def _val_and_maybe_convert(el):\n",
    "    \"\"\"\n",
    "    Converts `el.text` if `el` has attribute `type` with valid value.\n",
    "    \"\"\"\n",
    "    text = el.text.strip()\n",
    "    data_type = el.get('type')\n",
    "    convertor = _val_and_maybe_convert.convertors.get(data_type)\n",
    "    if convertor:\n",
    "        return convertor(text)\n",
    "    else:\n",
    "        return text\n",
    "_val_and_maybe_convert.convertors = {\n",
    "    'boolean': _str_to_boolean,\n",
    "    'datetime': _str_to_datetime,\n",
    "    'integer': int\n",
    "}\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    \n",
    "    #currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  --> otra forma de encontrar el directorio del archivo, por favor, explicar diferencia.\n",
    "    currentdir = os.getcwd()            #path del fichero en jupiter\n",
    "    path = os.path.dirname(__file__)    #path del fichero en .py\n",
    "    parentdir = os.path.dirname(currentdir) # subir un nivel de directorios\n",
    "    sys.path.insert(0,parentdir)        #insertar el directorio en el path (necesario para poder importar librerías con 'import')\n",
    "\n",
    "    # para importar una imagen hay que ir directamente al archivo; os.sep inserta los separadores del sistema operativo correspondiente\n",
    "    image = Image.open(path + os.sep + 'img' + os.sep + 'happy.jpg')\n",
    "\n",
    "    def get_root_path(n):\n",
    "        path = os.getcwd() # para notebook ||| __file__ --> para .py\n",
    "        for i in range(n):\n",
    "            path = os.path.dirname(path)\n",
    "        print(path)\n",
    "        sys.path.append(path)\n",
    "\n",
    "    # n --> es el número de veces que se tiene que hacer os.path.dirname \n",
    "    # si en .ipynb notebook es 5 entonces en .py usando __file__ es 6. \n",
    "    get_root_path(n=5)\n",
    "\n",
    "    # Se importan las librerías de clases desde un directorio superior\n",
    "    import objects.human as ohu\n",
    "    import objects.ork as oo\n"
   ]
  }
 ]
}

import pymysql

class MySQL:

    def __init__(self, IP_DNS, USER, PASSWORD, BD_NAME, PORT):
        self.IP_DNS = IP_DNS
        self.USER = USER
        self.PASSWORD = PASSWORD
        self.BD_NAME = BD_NAME
        self.PORT = PORT
        self.SQL_ALCHEMY = 'mysql+pymysql://' + self.USER + ':' + self.PASSWORD + '@' + self.IP_DNS + ':' + str(self.PORT) + '/' + self.BD_NAME
        # 'mysql+pymysql://user:password@91.76.54.33:20001/apr_july_2021_tb'
    def connect(self):
        # Open database connection
        self.db = pymysql.connect(host=self.IP_DNS,
                                  user=self.USER, 
                                  password=self.PASSWORD, 
                                  database=self.BD_NAME, 
                                  port=self.PORT)
        # prepare a cursor object using cursor() method
        self.cursor = self.db.cursor()
        print("Connected to MySQL server [" + self.BD_NAME + "]")
        return self.db

    def close(self):
        # disconnect from server
        self.db.close()
        print("Close connection with MySQL server [" + self.BD_NAME + "]")
    
    def execute_interactive_sql(self, sql, delete=False):
        """ NO SELECT """
        result = 0
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Commit your changes in the database
            self.db.commit()
            print("Executed \n\n" + str(sql) + "\n\n successfully")
            result = 1
        except Exception as error:
            print(error)
            # Rollback in case there is any error
            self.db.rollback()
        return result
        
    def execute_get_sql(self, sql):
        """SELECT"""
        results = None
        print("Executing:\n", sql)
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = self.cursor.fetchall()
        except Exception as error:
            print(error)
            print ("Error: unable to fetch data")
        
        return results

    def generate_insert_into_people_sql(self, to_insert):
        """
        This must be modified according to the table structure
        """
        nombre = to_insert[0]
        apellidos = to_insert[1]
        direccion = to_insert[2]
        edad = to_insert[3]
        nota = to_insert[4]
        
        sql = """INSERT INTO people
            (MOMENTO, NOMBRE, APELLIDOS, DIRECCION, EDAD, NOTA)
            VALUES
            (NOW(), '""" + nombre + """', '""" + apellidos + """', '""" + direccion + """', '""" + edad + """', '""" + nota + """')"""

        sql = sql.replace("\n", "").replace("            ", " ")
        return sql