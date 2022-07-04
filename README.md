# cvePackageChecker
Create a list of packages, with version and cvePackageChecker will scrape the internet to look for known vulnerabilities in those packages.
#OK HERE is the guide to working with this project. 
# It runs in tandem with a class I made called vendorNode which is used to keep track of the vendors. 


# Here is what the program does. 
# Given a list of packages, with the first collumn being named Package Name and the second being named 
# Version it takes the version from eachone. It needs a version. 
# Than it will look up the database CVEDETAILS to look for known vulnerabilities in the packages. 


# Here are the limitations currently you need to install panda a program to help panda read ods files, 
# beutiful soup and selenuim. Selenuim is more complicated. 
# Once those are installed and the file you want read is in the same directory, 
# you might have to edit the file name reader string. 
# Than you it will type in every version, if thier are more than 50 vendors for a product it will only look at the first 50. 
# If their are more than 50 vulnerabilities per version than it will only look at the first 50. I have never seen this before.

# !!!Secondly it reads the description to see what version the vulnerabilities is talking about. 
# Many applly to a version and the versions before. The program is written to looks for these cases.
# The program gets confused on which numbers are version numbers and just normal numbers. 
# These will be in the * category of vulnerabilities, so read that category and look with your own eyes. 
# Finally many products have multiple vendors and even as a human I could not tell which ones my company was using.
# So instead the program looks through all of them.


#Here are the commands to install everythin.If using python make sure you install it to the
# version you are using. Many operating systems pre install python, but not python 3
# pip install beautifulsoup4
# pip install selenium
# pip install pandas
# pip install odfpy
#
# For selenium you also need to prepare firefox to be run by your computer
# You can use geckodriver for this. In order to install geckodriver you need cargo
# curl https://sh.rustup.rs -sSf | sh
#
# Then install geckodriver with
# cargo install geckodriver
#
# Final note, the version of firefox cannot be the same one that comes with snap
#on ubuntu for all the linux users out their :)
