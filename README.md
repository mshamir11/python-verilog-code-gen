

## Python Verilog Code Generator


Writing hardware code is time-consuming. Especially when you don’t have much experience working with hardware codes. We wish to eliminate this gap between the experienced and the non-experienced. This project also tries to delve deeper, which is used for hardware description and will provide means of generating Verilog code directly from it.

This project aims to create a program that can generate Verilog code for some sequential circuit modules using python & jinja, and thereby try to build a fully-fledged Verilog code generator for both sequential circuit modules, like counters, registers, etc. Parametrizing and generalizing circuits and making it functional for n-bit operations would be the most challenging part of successfully implementing this project. The output Verilog code can be simulated in Vivado and deployed on FPGA boards to test and evaluate the effectiveness of the Verilog code generated.

