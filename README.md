#Guide to using cvePackageScraper

What is cveVulnerabilityScrapper?
It is a python program that takes in a series of packages and versiosn, it then web scrapes cveVulnerabilities for any known vulnerabilities. So that you and your team can be up to date and update certain versions accordingly. Here is a link on how to get your companies used packages for projects.
https://www.cyberciti.biz/faq/check-list-installed-packages-in-centos-linux/

Make sure file being read is .ods

Limitations
  Many versions apply to packages before. Such as "prior to 3.1.0".  So cveVulnerabilityScrapper reads the version number in the any version category.  This leads to some problems where it will over pick certain versions that don't apply. These will appear in the * category
  
  If their are more than 50 vendors for a product and more than 50 vulnerabilities it will only read the first 50. I  have never seen this before just thought I would mention.



Here are the commands to install everythin.If using python make sure you install it to the
 
pip install beautifulsoup4
pip install selenium
pip install pandas
pip install odfpy

For selenium you also need to prepare firefox to be run by your computer
You can use geckodriver for this. In order to install geckodriver you need cargo

curl https://sh.rustup.rs -sSf | sh
cargo install geckodriver

Final note, the version of firefox cannot be the same one that comes with snap on ubuntu for all the linux users out their :)
