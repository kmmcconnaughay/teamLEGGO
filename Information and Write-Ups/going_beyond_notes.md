# **STL Files**


## STL Files:
- Describe only the surface geometry of a 3D object without any representation of color, texture, or other attributes  
- Describe a triangulated surface by the unit normal and vertices of the triangles  
- Coordinates must be positive numbers  
- ASCII STL files and binary versions of STL exist  


**VisCAM and SolidView software packages use the two "attribute byte count" bytes at the end of every triangle to store a 15-bit RGB color:**  

- bits 0 to 4 are the intensity level for blue (0 to 31),
- bits 5 to 9 are the intensity level for green (0 to 31),
- bits 10 to 14 are the intensity level for red (0 to 31),
- bit 15 is 1 if the color is valid, or 0 if the color is not valid (as with normal STL files).

**Facet Normal:**
- Should be a unit vector pointing outwards from the solid object; can set as (0, 0, 0)  


- Use Adobe Acrobat 3D, Solidworks, MeshLab...?
