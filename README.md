# Python Verilog Code Generator <!-- omit in toc -->

![](https://img.shields.io/static/v1?message=Python&logo=python&labelColor=5c5c5c&color=1182c3&logoColor=white&label=Code) ![](https://img.shields.io/static/v1?message=Verilog&logo=V&labelColor=5c5c5c&color=1182c3&logoColor=white&label=Code) ![](https://img.shields.io/static/v1?message=Flask&logo=flask&labelColor=5c5c5c&color=1182c3&logoColor=white&label=Frame%20Work)
![](https://img.shields.io/static/v1?message=CSS&logo=css3&labelColor=5c5c5c&color=1182c3&logoColor=white&label=Style)

Writing hardware code is time-consuming. Especially when you don’t have much experience working with hardware codes. We wish to eliminate this gap between the experienced and the non-experienced. This project also tries to delve deeper, which is used for hardware description and will provide means of generating Verilog code directly from it.

This project aims to create a program that can generate Verilog code for some sequential circuit modules using python & jinja, and thereby try to build a fully-fledged Verilog code generator for both sequential circuit modules, like counters, registers, etc. Parametrizing and generalizing circuits and making it functional for n-bit operations would be the most challenging part of successfully implementing this project. The output Verilog code can be simulated in Vivado and deployed on FPGA boards to test and evaluate the effectiveness of the Verilog code generated.

## Contents <!-- omit in toc -->
- [1. Instructions](#1-instructions)
  - [1.1 Setup Virtual Environment](#11-setup-virtual-environment)
  - [1.2 Installing Dependencies](#12-installing-dependencies)
  - [1.3 Run Flask App](#13-run-flask-app)
- [2. Features](#2-features)
  - [2.1. Counters](#21-counters)
  - [2.2. Registers](#22-registers)
  - [2.3. Flip Flops](#23-flip-flops)
  - [2.4. Floating Point Arithmetic Unit](#24-floating-point-arithmetic-unit)
  - [2.5. FSMs](#25-fsms)

## 1. Instructions
It is ideal to create a virtual environment and install all the dependencies inside it. However, it would also work if the dependencies are installed globally.

### 1.1 Setup Virtual Environment

- Create a new virtual environment.     
  Go to your respective project directory first. It would be better to add the virtual environment files in the project directory itself. One could add the respective folder to .gitignore to ignore the folder while updating the github repo.

    ```bash
    python -m venv <NAME_OF_VIRTUAL_ENVIRONMENT>
    ```

- Activating the virtual environment.
  
  ```bash
   source <NAME_OF_VIRTUAL_ENVIRONMENT>/bin/activate
  ```

- Deactivating the virtual environment.     
  Once the work is done. The virtual environment can be deactivated.

  ```bash
  deactivate
  ```

### 1.2 Installing Dependencies

After the activating the virtual environment (if virtual environment is installed), all the dependencies can be installed using the requirements.txt file.

  ```bash
  pip install -r requirements.txt
  ```

### 1.3 Run Flask App

Once the dependencies are installed. The flask app can be runn using the following command.

 ```bash
 python app.py
 ```

 The web application can be accessed at <http://127.0.0.1:5000/>
 
## 2. Features
### 2.1. Counters
### 2.2. Registers
### 2.3. Flip Flops
### 2.4. Floating Point Arithmetic Unit
### 2.5. FSMs
