# La Réunion DataCup Challenge 2024 - ESI'Flipside

The [Reunion Island DataCup Challenge (Réunion DataCup Challenge)](https://data.regionreunion.com/p/page-reunion-datacup-challenge) is a unique event in which every data analysis and manipulations skills are put under the spot : extraction, processing, models and visualizers... Hosted by the Reunion Island Region (La Région Réunion), *La Réunion DataCup Challenge* is part of a framework of collaboration and cooperation with local data producers willing to open, share and valuate their data. Partners' themes are varied : from the preservation of resources to the economy, or even the concerns of local authorities and their inhabitants.

The main goal of this second edition is to keep gathering a community around local open-data and also to initiate sustainable projects et useful to as many people as possible.

## ESI'Flipside

Our team has chosen the challenge **The right address** bringed by **EDF and Réunion THD**

This challenge is part of a context where many public and private organizations have lists of addresses that, collected over time, are rarely checked or updated. As a result, the quality of this information is gradually deteriorating, making it difficult to use them efficiently. This challenge consists of comparing the source address data with existing repositories, identifying incorrect data and give possible solutions to correct them.

Its objective here is to design a prototype tool to help correct an address file. This tool, based on a comparison with data from the BAN (National Address Base) and ARCEP, will not only detect differences between sources and repositories, but also suggest relevant corrections. In addition, a statistical analysis of the quality of the source data and a cartographic visualization of the addresses will also be included in the prototype.

## **Documentation**

Our solution addresses the problem of the quality and updating of address databases, often collected over time without regular monitoring. It consists of cross-referencing address databases with those provided by authorities and the government and proposing data updates based on a range of conditions. This solution is aimed at all organizations or communities that would like to enhance their address database in an accessible and easy manner.


### **Installation**

You can find the instructions to install our application in our [Installation Guide](/INSTALL.md)

### **Usage**

Our solution is aimed to be open-source, accessible to everyone, including companies that need to create an address database. First of all, once the application is deployed, users will be able to access a site that allows them to take as input a CSV file containing at least a column for each specificity of an address (number, name, coordinates, longitudes & latitudes) and the city concerned. The site will therefore be able to analyze this file by comparing it with the CSV file of the National Address Database (BAN) that it can retrieve using the API linked to the site containing the addresses of France (https://adresse.data.gouv.fr).\
\
The result of this comparison will be the same CSV file with the corrections applied by the autonomous backend of the site, which will allow users to save time.

### **Contributing**

If you wish to contribute to this project, please follow the [recommendations](/CONTRIBUTING.md).

### **Licence**

The code is published under [MIT Licence](/LICENSE).

The data referenced in this README and in the installation guide is published under <a href="https://www.etalab.gouv.fr/wp-content/uploads/2018/11/open-licence.pdf">Open Licence 2.0</a>.
