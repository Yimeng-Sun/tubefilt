# tubefilt
This repo is for code related to construction of lossy dielectric filters (low-pass filters) for cryogenic applications. This type of filter, described by Wollack, Chuss, Rostem, and U-Yen at http://ntrs.nasa.gov/search.jsp?R=20140010491 (http://dx.doi.org/10.1063/1.4869038, PDF: http://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20140010491.pdf), is commonly referred to as a metal powder filter. While multiple geometries are possible for this class of filter, this code focuses on the coaxial cylindrical type. 

What this code will do:
- Calculate the outer diameter of the inner coaxial conductor, in inches and in nearest American Wire Gauge, given an outer coaxial conductor inner diameter, the relative dielectric constant of the material in the filter, and a target impedance to be matched.
- Calculate the resulting impedance of the coaxial filter, given the diameter of the suggested nearest AWG size, i.e. the impedance mismatch incurred by using the nearest available AWG size.

What you will need to use this code:
- Mathematica (Python coming soon)
- Inner diameter of outer conductor (e.g. the ID of a copper tube)
- Dielectric material of known relative dielectric constant, and knowledge of the relative dielectric constant's dependence on frequency, or at least a value of relative dielectric constant for your frequency of interest. Documentation on Emerson & Cuming "Eccosorb" is available at http://www.eccosorb.com/. Custom mixtures of metal and powder, or metal and Stycast 2850FT are also common.


