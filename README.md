# Pixel Profile Pic
A Profile Pic generator inspired by Github's default profile picture for new users.
Pixel Profile Pic creates a square profile picture with randomly generated pixels and initials of the given name in random color in PNG format.

## Requirements
* Python 3
* Pillow 
  * Installed using: `pip install Pillow`
  * Note: Pillow is a fork of PIL and hence, is backward compatible with it.

## To run
* Go to the directory containing all the py files and font folder
* Type `python interface.py` in terminal
* Provide your given and family name when prompted eg. John Smith

## Number of unique design with the current code
* Size of Image = 660 x 660
* Size of a Pixel = 30
* Number of random colors = 256
* Blank Space size of Initial = 120 x 120
* Alphabets = 26

#### Case I (Family and Given Name/ Two Initials)
Unique design = 256 x 2^(((660-120)/30)^2) x 26 x 26 = ***5.914326e+102 unique designs***

*Example ~ John Smith*

<img src="/Examples/CaseI.PNG" width="150" align="center" >

#### Case II (Family or Given Name / One Initial)
Unique design = 256 x 2^(((660-120)/30)^2) x 26 = ***2.274741e+101 unique designs***

*Example ~ John or Jackson*

<img src="/Examples/CaseII.PNG" width="150" align="center" >


#### Case III (No Family or Given Name / Zero Initial)
Unique design = 256 x 2^((660/30)^2) = ***1.278668e+148 unique designs***

*Example ~ No name given*

<img src="/Examples/CaseIII.PNG" width="150" align="center" >

## Known Limitations
* Ignores more than two names eg. if middle name is given, takes it as the family name.
* The font used only supports English.
* The default font used when font folder is not found is a bitmapped font with no alternate sizes.
