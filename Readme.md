# Muhammad Asad Waseem Codefolio

## Table of Content

- [Muhammad Asad Waseem Codefolio](#muhammad-asad-waseem-codefolio)
  - [Table of Content](#table-of-content)
  - [Introduction](#introduction)
  - [Directory Tree](#directory-tree)
  - [Algorithms](#algorithms)
  - [Python Basics](#python-basics)
  - [Control Structures](#control-structures)
  - [Data Structures](#data-structures)
  - [Date Time Module](#date-time-module)
  - [Enums Generators and Iterators](#enums-generators-and-iterators)
  - [File Handling](#file-handling)
  - [Functional Programming](#functional-programming)
  - [Lambda Functions](#lambda-functions)
  - [Object Oriented Programming](#object-oriented-programming)
  - [Operation System (OS) Module](#operation-system-os-module)
  - [Pickling Unpickling](#pickling-unpickling)
  - [Pytests](#pytests)
  - [Regular Expressions](#regular-expressions)
  - [Recursion](#recursion)
  - [100 Days of Python](#100-days-of-python)
  - [Bash](#bash)
  - [Batch](#batch)
  - [Natural Language Processing](#natural-language-processing)
  - [Database](#database)
  - [Console Programs](#console-programs)
  - [Covid-19 Project](#covid-19-project)
  - [Geopy Library](#geopy-library)
  - [Json](#json)
  - [Mobile Application Development](#mobile-application-development)
    - [Kivy](#kivy)
    - [Beeware](#beeware)
  - [Request Library](#request-library)
  - [Web Frameworks](#web-frameworks)
    - [Flask](#flask)
    - [Django](#django)
    - [API Development](#api-development)
      - [Fast API](#fast-api)
      - [Flask-Restful](#flask-restful)
      - [Django-Restful](#django-restful)
  - [Scrappers and Crawlers](#scrappers-and-crawlers)
  - [Projects](#projects)
  - [Notes](#notes)

## Introduction

Hey there, this is my codefolio/portfolio for my Software Engineering skills using python as a programming Language.  
This repository contains all the Subject and related exercises I could find on the internet, along with my notes and small projects.  
To learn more about me and this repository please consult [About page](https://github.com/rx290/PythonPortfolio/blob/main/About.md).  
To get to know what methods have been used throughout this repository use [Method Glossary page](https://github.com/rx290/PythonPortfolio/blob/main/Method%20Glossary.md).  
To know more about the projects listed below see [Project Description Page](https://github.com/rx290/PythonPortfolio/blob/main/ProjectDescriptions.md).  

## Directory Tree

<details>
<summary>  Directory Tree  </summary>

    |   About.md
    |   Method Glossary.md
    |   ProjectDescriptions.md
    |   Readme.md
    |
    +---100 Days of Python
    |   +---Day1
    |   |       BandNameGenerator.py
    |   |
    |   +---Day10-Calculator
    |   |       calculator.py
    |   |
    |   +---Day12-Number_guessing_game
    |   |       ngg.py
    |   |
    |   +---Day13-FizzBuzz
    |   |       app.py
    |   |
    |   +---Day15-Coffee_Machine
    |   |       app.py
    |   |
    |   +---Day2
    |   |       BMI.py
    |   |       time_calculator.py
    |   |       TipCalculator.py
    |   |
    |   +---Day3
    |   |       BMI_2.0.py
    |   |       love_counter.py
    |   |       odd_or_even.py
    |   |       pizza_app.py
    |   |       rollercoaster_ticket_booth.py
    |   |       treassure_hunter.py
    |   |
    |   +---Day4
    |   |       FizzBuzz.py
    |   |       height_calculator.py
    |   |       password_generator.py
    |   |       Reboorg_Challenge.py
    |   |       sum_of_all_even_number_under_100.py
    |   |       treassure_mapping.py
    |   |       who's_Paying.py
    |   |
    |   +---Day5
    |   |       function_ex_1.py
    |   |       prime_or_not.py
    |   |
    |   +---Day7-Hangman
    |   |       hangman.py
    |   |
    |   \---Day8-Cease Cipher
    |           app.py
    |
    +---Algorithms
    |   +---Heap Queue
    |   |       explanation.md
    |   |       Problem_1.py
    |   |       Problem_10.py
    |   |       Problem_11.py
    |   |       Problem_12.py
    |   |       Problem_13.py
    |   |       Problem_14.py
    |   |       Problem_15.py
    |   |       Problem_16.py
    |   |       Problem_17.py
    |   |       Problem_18.py
    |   |       Problem_19.py
    |   |       Problem_2.py
    |   |       Problem_20.py
    |   |       Problem_21.py
    |   |       Problem_22.py
    |   |       Problem_23.py
    |   |       Problem_24.py
    |   |       Problem_25.py
    |   |       Problem_26.py
    |   |       Problem_27.py
    |   |       Problem_28.py
    |   |       Problem_29.py
    |   |       Problem_3.py
    |   |       Problem_4.py
    |   |       Problem_5.py
    |   |       Problem_6.py
    |   |       Problem_7.py
    |   |       Problem_8.py
    |   |       Problem_9.py
    |   |
    |   +---Searching
    |   |   +---Binary Searching
    |   |   |       Problem_1.py
    |   |   |       Problem_10.py
    |   |   |       Problem_11.py
    |   |   |       Problem_12.py
    |   |   |       Problem_13.py
    |   |   |       Problem_14.py
    |   |   |       Problem_15.py
    |   |   |       Problem_16.py
    |   |   |       Problem_17.py
    |   |   |       Problem_18.py
    |   |   |       Problem_19.py
    |   |   |       Problem_2.py
    |   |   |       Problem_20.py
    |   |   |       Problem_3.py
    |   |   |       Problem_4.py
    |   |   |       Problem_5.py
    |   |   |       Problem_6.py
    |   |   |       Problem_7.py
    |   |   |       Problem_8.py
    |   |   |       Problem_9.py
    |   |   |
    |   |   +---Linear Searching
    |   |   |       Problem_1.py
    |   |   |       Problem_10.py
    |   |   |       Problem_11.py
    |   |   |       Problem_12.py
    |   |   |       Problem_13.py
    |   |   |       Problem_2.py
    |   |   |       Problem_3.py
    |   |   |       Problem_4.py
    |   |   |       Problem_5.py
    |   |   |       Problem_6.py
    |   |   |       Problem_7.py
    |   |   |       Problem_8.py
    |   |   |       Problem_9.py
    |   |   |
    |   |   +---Sequentioal Search
    |   |   |       Problem_1.py
    |   |   |
    |   |   \---Ternary Searching
    |   |           Problem_1.py
    |   |           Problem_2.py
    |   |           Problem_3.py
    |   |           Problem_4.py
    |   |           Problem_5.py
    |   |           Problem_6.py
    |   |
    |   \---Sorting
    |       |   Bitonic_Sort.py
    |       |   Bogosort sort.py
    |       |   Cocktail shaker sort.py
    |       |   Comb Sort.py
    |       |   Cycle Sort.py
    |       |   Gnome sort.py
    |       |   Merge-insertion sort.py
    |       |   Natural Sort.py
    |       |   Odd even transposition sort.py
    |       |   Odd-even Transpostion sort 2.py
    |       |   Odd-even Transpostion sort paraallel.py
    |       |   Pancake Sort.py
    |       |   Patience sorting.py
    |       |   Pigeonhole sorting.py
    |       |   Problem_8.py
    |       |   Shell_sort.py
    |       |   Standard Sort.py
    |       |   Stooge Sort.py
    |       |   Tim Sort.py
    |       |   Time Sort.py
    |       |   Topological Sort.py
    |       |   Tree Sort.py
    |       |   Wiggle Sort.py
    |       |
    |       +---Bubble Sort
    |       |       Problem_1.py
    |       |       Problem_2.py
    |       |
    |       +---Bucket Sort
    |       |       Problem_1.py
    |       |
    |       +---Counting Sort
    |       |       Counting_sort.py
    |       |
    |       +---Heap Sort
    |       |       Problem_1.py
    |       |       Problem_2.py
    |       |       Problem_3.py
    |       |       Problem_4.py
    |       |       Problem_5.py
    |       |
    |       +---Insertion Sort
    |       |       Problem_1.py
    |       |       Problem_2.py
    |       |
    |       +---Merge Sort
    |       |       Problem_1.py
    |       |       Problem_10.py
    |       |       Problem_11.py
    |       |       Problem_12.py
    |       |       Problem_13.py
    |       |       Problem_14.py
    |       |       Problem_15.py
    |       |       Problem_16.py
    |       |       Problem_17.py
    |       |       Problem_18.py
    |       |       Problem_19.py
    |       |       Problem_2.py
    |       |       Problem_20.py
    |       |       Problem_3.py
    |       |       Problem_4.py
    |       |       Problem_5.py
    |       |       Problem_6.py
    |       |       Problem_7.py
    |       |       Problem_8.py
    |       |       Problem_9.py
    |       |
    |       +---Quick Sort
    |       |       Multikey_quick_sort.py
    |       |       Problem_1.py
    |       |       Random Pivot Quick Sort.py
    |       |       Recusive Quick Sort.py
    |       |
    |       +---Radix Sort
    |       |       Problem_1.py
    |       |
    |       \---Selection Sort
    |               Problem_1.py
    |
    +---Bash
    |       Script_To_Make_New_Files.sh
    |
    +---Basics [Completed]
    |       Problem_1.py
    |       Problem_10.py
    |       Problem_11.py
    |       Problem_12.py
    |       Problem_13.py
    |       Problem_14.py
    |       Problem_15.py
    |       Problem_2.py
    |       Problem_3.py
    |       Problem_4.py
    |       Problem_5.py
    |       Problem_6.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Batch
    |       Script_To_Create_Multiple_Files.bat
    |
    +---Console_Programs
    |       Body_Mass_index.py
    |       Contact_Book.py
    |       Guess_The_Number.py
    |       Intro.md
    |       Password_Generator.py
    |       rock_paper_sissors.py
    |       Youtube_video_downloader.py
    |
    +---Control Structures [Completed]
    |       Create_Case_in_python.py
    |       Problem_1.py
    |       Problem_10.py
    |       Problem_11.py
    |       Problem_12.py
    |       Problem_13.py
    |       Problem_14.py
    |       Problem_15.py
    |       Problem_16.py
    |       Problem_17.py
    |       Problem_18.py
    |       Problem_19.py
    |       Problem_2.py
    |       Problem_20.py
    |       Problem_21.py
    |       Problem_22.py
    |       Problem_23.py
    |       Problem_3.py
    |       Problem_4.py
    |       Problem_5.py
    |       Problem_6.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Covid-19 Project
    |       info.md
    |       Problem_1.py
    |       Problem_10.py
    |       Problem_11.py
    |       Problem_12.py
    |       Problem_13.py
    |       Problem_14.py
    |       Problem_2.py
    |       Problem_3.py
    |       Problem_4.py
    |       Problem_5.py
    |       Problem_6.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Data Structures
    |   +---Arrays, List
    |   |       Problem_1.py
    |   |       Problem_10.py
    |   |       Problem_11.py
    |   |       Problem_12.py
    |   |       Problem_13.py
    |   |       Problem_14.py
    |   |       Problem_15.py
    |   |       Problem_2.py
    |   |       Problem_3.py
    |   |       Problem_4.py
    |   |       Problem_5.py
    |   |       Problem_6.py
    |   |       Problem_7.py
    |   |       Problem_8.py
    |   |       Problem_9.py
    |   |
    |   +---Collection
    |   |       Problem_1.py
    |   |       Problem_10.py
    |   |       Problem_11.py
    |   |       Problem_12.py
    |   |       Problem_13.py
    |   |       Problem_14.py
    |   |       Problem_15.py
    |   |       Problem_16.py
    |   |       Problem_17.py
    |   |       Problem_18.py
    |   |       Problem_19.py
    |   |       Problem_2.py
    |   |       Problem_20.py
    |   |       Problem_21.py
    |   |       Problem_22.py
    |   |       Problem_23.py
    |   |       Problem_24.py
    |   |       Problem_25.py
    |   |       Problem_26.py
    |   |       Problem_27.py
    |   |       Problem_28.py
    |   |       Problem_29.py
    |   |       Problem_3.py
    |   |       Problem_30.py
    |   |       Problem_31.py
    |   |       Problem_32.py
    |   |       Problem_33.py
    |   |       Problem_34.py
    |   |       Problem_35.py
    |   |       Problem_36.py
    |   |       Problem_4.py
    |   |       Problem_5.py
    |   |       Problem_6.py
    |   |       Problem_7.py
    |   |       Problem_8.py
    |   |       Problem_9.py
    |   |
    |   +---Dict
    |   |       Problem_1.py
    |   |       Problem_10.py
    |   |       Problem_11.py
    |   |       Problem_12.py
    |   |       Problem_13.py
    |   |       Problem_14.py
    |   |       Problem_15.py
    |   |       Problem_16.py
    |   |       Problem_17.py
    |   |       Problem_18.py
    |   |       Problem_19.py
    |   |       Problem_2.py
    |   |       Problem_20.py
    |   |       Problem_21.py
    |   |       Problem_22.py
    |   |       Problem_23.py
    |   |       Problem_24.py
    |   |       Problem_25.py
    |   |       Problem_26.py
    |   |       Problem_27.py
    |   |       Problem_28.py
    |   |       Problem_29.py
    |   |       Problem_3.py
    |   |       Problem_30.py
    |   |       Problem_31.py
    |   |       Problem_32.py
    |   |       Problem_33.py
    |   |       Problem_34.py
    |   |       Problem_35.py
    |   |       Problem_36.py
    |   |       Problem_37.py
    |   |       Problem_38.py
    |   |       Problem_39.py
    |   |       Problem_4.py
    |   |       Problem_40.py
    |   |       Problem_41.py
    |   |       Problem_42.py
    |   |       Problem_43.py
    |   |       Problem_44.py
    |   |       Problem_45.py
    |   |       Problem_46.py
    |   |       Problem_47.py
    |   |       Problem_48.py
    |   |       Problem_49.py
    |   |       Problem_5.py
    |   |       Problem_50.py
    |   |       Problem_51.py
    |   |       Problem_52.py
    |   |       Problem_53.py
    |   |       Problem_54.py
    |   |       Problem_55.py
    |   |       Problem_56.py
    |   |       Problem_57.py
    |   |       Problem_58.py
    |   |       Problem_59.py
    |   |       Problem_6.py
    |   |       Problem_60.py
    |   |       Problem_61.py
    |   |       Problem_62.py
    |   |       Problem_63.py
    |   |       Problem_64.py
    |   |       Problem_65.py
    |   |       Problem_66.py
    |   |       Problem_67.py
    |   |       Problem_68.py
    |   |       Problem_69.py
    |   |       Problem_7.py
    |   |       Problem_70.py
    |   |       Problem_71.py
    |   |       Problem_72.py
    |   |       Problem_73.py
    |   |       Problem_74.py
    |   |       Problem_75.py
    |   |       Problem_76.py
    |   |       Problem_77.py
    |   |       Problem_78.py
    |   |       Problem_79.py
    |   |       Problem_8.py
    |   |       Problem_80.py
    |   |       Problem_81.py
    |   |       Problem_82.py
    |   |       Problem_83.py
    |   |       Problem_84.py
    |   |       Problem_85.py
    |   |       Problem_9.py
    |   |
    |   +---Heaps
    |   |       Problem_ 26.py
    |   |       Problem_ 27.py
    |   |       Problem_ 28.py
    |   |       Problem_ 29.py
    |   |       Problem_1.py
    |   |       Problem_10.py
    |   |       Problem_11.py
    |   |       Problem_12.py
    |   |       Problem_13.py
    |   |       Problem_14.py
    |   |       Problem_15.py
    |   |       Problem_16.py
    |   |       Problem_17.py
    |   |       Problem_18.py
    |   |       Problem_19.py
    |   |       Problem_2.py
    |   |       Problem_20.py
    |   |       Problem_21.py
    |   |       Problem_22.py
    |   |       Problem_23.py
    |   |       Problem_24.py
    |   |       Problem_25.py
    |   |       Problem_3.py
    |   |       Problem_4.py
    |   |       Problem_5.py
    |   |       Problem_6.py
    |   |       Problem_7.py
    |   |       Problem_8.py
    |   |       Problem_9.py
    |   |
    |   +---Linked Lists
    |   |   |   Problem_1.py
    |   |   |   Problem_10.py
    |   |   |   Problem_11.py
    |   |   |   Problem_12.py
    |   |   |   Problem_13.py
    |   |   |   Problem_14.py
    |   |   |   Problem_2.py
    |   |   |   Problem_3.py
    |   |   |   Problem_4.py
    |   |   |   Problem_5.py
    |   |   |   Problem_6.py
    |   |   |   Problem_7.py
    |   |   |   Problem_8.py
    |   |   |   Problem_9.py
    |   |   |
    |   |   \---Implementation
    |   |           LinkList.py
    |   |
    |   +---Lists
    |   |       Problem_1.py
    |   |       Problem_2.py
    |   |       Problem_3.py
    |   |       Problem_4.py
    |   |       Problem_5.py
    |   |       Problem_6.py
    |   |       Problem_7.py
    |   |       Problem_8.py
    |   |       Problem_9.py
    |   |
    |   +---Queue
    |   |       Problem_1.py
    |   |       Problem_2.py
    |   |       Problem_3.py
    |   |       Problem_4.py
    |   |
    |   +---Sets
    |   |       Problem_1.py
    |   |       Problem_2.py
    |   |       Problem_3.py
    |   |       Problem_4.py
    |   |
    |   +---Stack
    |   |       Problem_1.py
    |   |       Problem_2.py
    |   |
    |   +---Trees
    |   |   \---Binary Seart Tree
    |   |           Problem_1.py
    |   |           Problem_2.py
    |   |           Problem_3.py
    |   |           Problem_4.py
    |   |           Problem_5.py
    |   |           Problem_6.py
    |   |
    |   \---Tupples
    |           Problem_1.py
    |           Problem_10.py
    |           Problem_11.py
    |           Problem_12.py
    |           Problem_13.py
    |           Problem_14.py
    |           Problem_15.py
    |           Problem_16.py
    |           Problem_17.py
    |           Problem_18.py
    |           Problem_19.py
    |           Problem_2.py
    |           Problem_20.py
    |           Problem_21.py
    |           Problem_3.py
    |           Problem_4.py
    |           Problem_5.py
    |           Problem_6.py
    |           Problem_7.py
    |           Problem_8.py
    |           Problem_9.py
    |
    +---Database
    |   +---Firebase
    |   |   \---Firebase_Admin
    |   |           Firebase_Conn_and_CRUD.py
    |   |           sample_data.json
    |   |
    |   +---Mongodb
    |   |       Problem_1.py
    |   |       Problem_10.py
    |   |       Problem_2.py
    |   |       Problem_3.py
    |   |       Problem_4.py
    |   |       Problem_5.py
    |   |       Problem_6.py
    |   |       Problem_7.py
    |   |       Problem_8.py
    |   |       Problem_9.py
    |   |       Readme.md
    |   |
    |   +---Mysql
    |   |       Problem_1.3.py
    |   |       Problem_1.5.py
    |   |       Problem_1.py
    |   |       Problem_10.py
    |   |       Problem_11.py
    |   |       Problem_2.py
    |   |       Problem_3.py
    |   |       Problem_4.py
    |   |       Problem_5.py
    |   |       Problem_6.py
    |   |       Problem_7.py
    |   |       Problem_8.py
    |   |       Problem_9.py
    |   |       requirement.txt
    |   |
    |   \---Sqlite
    |       |   Problem_1.py
    |       |   Problem_10.py
    |       |   Problem_11.py
    |       |   Problem_12.py
    |       |   Problem_13.py
    |       |   Problem_2.py
    |       |   Problem_3.py
    |       |   Problem_4.py
    |       |   Problem_5.py
    |       |   Problem_6.py
    |       |   Problem_7.py
    |       |   Problem_8.py
    |       |   Problem_9.py
    |       |
    |       \---db
    |               product_database.db
    |               Sqlite_backup.db
    |
    +---Date Time
    |       Problem_1.py
    |       Problem_10.py
    |       Problem_11.py
    |       Problem_12.py
    |       Problem_13.py
    |       Problem_14.py
    |       Problem_15.py
    |       Problem_16.py
    |       Problem_17.py
    |       Problem_18.py
    |       Problem_19.py
    |       Problem_2.py
    |       Problem_20.py
    |       Problem_21.py
    |       Problem_22.py
    |       Problem_23.py
    |       Problem_24.py
    |       Problem_25.py
    |       Problem_26.py
    |       Problem_27.py
    |       Problem_28.py
    |       Problem_29.py
    |       Problem_3.py
    |       Problem_30.py
    |       Problem_31.py
    |       Problem_32.py
    |       Problem_33.py
    |       Problem_34.py
    |       Problem_35.py
    |       Problem_36.py
    |       Problem_37.py
    |       Problem_38.py
    |       Problem_39.py
    |       Problem_4.py
    |       Problem_40.py
    |       Problem_41.py
    |       Problem_42.py
    |       Problem_43.py
    |       Problem_44.py
    |       Problem_45.py
    |       Problem_46.py
    |       Problem_47.py
    |       Problem_48.py
    |       Problem_49.py
    |       Problem_5.py
    |       Problem_50.py
    |       Problem_51.py
    |       Problem_52.py
    |       Problem_53.py
    |       Problem_54.py
    |       Problem_55.py
    |       Problem_56.py
    |       Problem_57.py
    |       Problem_58.py
    |       Problem_59.py
    |       Problem_6.py
    |       Problem_60.py
    |       Problem_61.py
    |       Problem_62.py
    |       Problem_63.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Enums Generators and Iterators
    |   +---Enums
    |   |       Problem_1.py
    |   |       Problem_2.py
    |   |       Problem_3.py
    |   |       Problem_4.py
    |   |       Problem_5.py
    |   |
    |   \---Generator and Iterators
    |           Problem_1.py
    |           Problem_10.py
    |           Problem_11.py
    |           Problem_12.py
    |           Problem_13.py
    |           Problem_14.py
    |           Problem_15.py
    |           Problem_16.py
    |           Problem_17.py
    |           Problem_18.py
    |           Problem_19.py
    |           Problem_2.py
    |           Problem_20.py
    |           Problem_21.py
    |           Problem_22.py
    |           Problem_23.py
    |           Problem_24.py
    |           Problem_25.py
    |           Problem_26.py
    |           Problem_27.py
    |           Problem_28.py
    |           Problem_29.py
    |           Problem_3.py
    |           Problem_30.py
    |           Problem_31.py
    |           Problem_32.py
    |           Problem_33.py
    |           Problem_34.py
    |           Problem_35.py
    |           Problem_36.py
    |           Problem_37.py
    |           Problem_38.py
    |           Problem_39.py
    |           Problem_4.py
    |           Problem_40.py
    |           Problem_41.py
    |           Problem_42.py
    |           Problem_43.py
    |           Problem_44.py
    |           Problem_5.py
    |           Problem_6.py
    |           Problem_7.py
    |           Problem_8.py
    |           Problem_9.py
    |
    +---FastAPI
    |   |   Api_demo.py
    |   |   Readme.md
    |   |   requirements.txt
    |   |
    |   \---__pycache__
    |           Api_demo.cpython-38.pyc
    |
    +---File Handling
    |   +---CSV
    |   |       Problem_1.py
    |   |       Problem_10.py
    |   |       Problem_11.py
    |   |       Problem_2.py
    |   |       Problem_3.py
    |   |       Problem_4.py
    |   |       Problem_5.py
    |   |       Problem_6.py
    |   |       Problem_7.py
    |   |       Problem_8.py
    |   |       Problem_9.py
    |   |
    |   +---file_handling_basic
    |   |       DestinationFile.txt
    |   |       Problem_1.py
    |   |       Problem_10.py
    |   |       Problem_11.py
    |   |       Problem_12.py
    |   |       Problem_13.py
    |   |       Problem_14.py
    |   |       Problem_15.py
    |   |       Problem_2.py
    |   |       Problem_3.py
    |   |       Problem_4.py
    |   |       Problem_5.py
    |   |       Problem_6.py
    |   |       Problem_7.py
    |   |       Problem_8.py
    |   |       Problem_9.py
    |   |       sample.txt
    |   |       sample1.txt
    |   |
    |   \---File_handling_conceptual
    |           Problem_1.py
    |           Problem_10.py
    |           Problem_11.py
    |           Problem_12.py
    |           Problem_13.py
    |           Problem_14.py
    |           Problem_15.py
    |           Problem_16.py
    |           Problem_17.py
    |           Problem_18.py
    |           Problem_2.py
    |           Problem_3.py
    |           Problem_4.py
    |           Problem_5.py
    |           Problem_6.py
    |           Problem_7.py
    |           Problem_8.py
    |           Problem_9.py
    |
    +---Flask
    |   |   Authentication.md
    |   |   CSS.md
    |   |   Design_Architecture.md
    |   |   Django.md
    |   |   Flask.md
    |   |   HTML.md
    |   |
    |   +---Flask_Restful
    |   |   \---Simple_Crud
    |   |       |   app.py
    |   |       |
    |   |       \---api
    |   |               Task.py
    |   |               TaskById.py
    |   |               __init.py
    |   |
    |   \---Flask_WebApps
    |       \---Simple_Crud_WebApp
    |           |   app.py
    |           |   Create.html
    |           |   models.py
    |           |   Readme.md
    |           |   students.db
    |           |
    |           +---templates
    |           |       Create.html
    |           |       header.html
    |           |       Temp.html
    |           |
    |           \---__pycache__
    |                   app.cpython-310.pyc
    |                   models.cpython-310.pyc
    |
    +---Functional Programming
    |   |   Problem_1.py
    |   |   Problem_10.py
    |   |   Problem_11.py
    |   |   Problem_12.py
    |   |   Problem_13.py
    |   |   Problem_14.py
    |   |   Problem_2.py
    |   |   Problem_3.py
    |   |   Problem_4.py
    |   |   Problem_5.py
    |   |   Problem_6.py
    |   |   Problem_7.py
    |   |   Problem_8.py
    |   |   Problem_9.py
    |   |
    |   \---Calling Methods
    |       +---Caling by value
    |       |       Problem_1.py
    |       |       Problem_10.py
    |       |       Problem_11.py
    |       |       Problem_2.py
    |       |       Problem_3.py
    |       |       Problem_4.py
    |       |       Problem_5.py
    |       |       Problem_6.py
    |       |       Problem_7.py
    |       |       Problem_8.py
    |       |       Problem_9.py
    |       |
    |       \---Calling by refrence
    |               Problem_12.py
    |               Problem_13.py
    |               Problem_14.py
    |               Problem_15.py
    |
    +---GeoPy
    |       Problem_1.py
    |       Problem_2.py
    |       Problem_3.py
    |       Problem_4.py
    |       Problem_5.py
    |       Problem_6.py
    |       Problem_7.py
    |
    +---Json
    |       Problem_1.py
    |       Problem_2.py
    |       Problem_3.py
    |       Problem_4.py
    |       Problem_5.py
    |       Problem_6.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Kivy_Learnings
    +---Lambda Functions
    |       Problem_1.py
    |       Problem_10.py
    |       Problem_11.py
    |       Problem_12.py
    |       Problem_13.py
    |       Problem_14.py
    |       Problem_15.py
    |       Problem_16.py
    |       Problem_17.py
    |       Problem_18.py
    |       Problem_19.py
    |       Problem_2.py
    |       Problem_20.py
    |       Problem_21.py
    |       Problem_22.py
    |       Problem_23.py
    |       Problem_24.py
    |       Problem_25.py
    |       Problem_26.py
    |       Problem_27.py
    |       Problem_28.py
    |       Problem_29.py
    |       Problem_3.py
    |       Problem_30.py
    |       Problem_31.py
    |       Problem_32.py
    |       Problem_33.py
    |       Problem_34.py
    |       Problem_35.py
    |       Problem_36.py
    |       Problem_37.py
    |       Problem_38.py
    |       Problem_39.py
    |       Problem_4.py
    |       Problem_40.py
    |       Problem_41.py
    |       Problem_42.py
    |       Problem_43.py
    |       Problem_44.py
    |       Problem_45.py
    |       Problem_46.py
    |       Problem_47.py
    |       Problem_48.py
    |       Problem_49.py
    |       Problem_5.py
    |       Problem_50.py
    |       Problem_51.py
    |       Problem_52.py
    |       Problem_6.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Machine Learning
    |   |   Models.md
    |   |
    |   +---.ipynb_checkpoints
    |   |       Video game sales prediction-checkpoint.ipynb
    |   |
    |   +---Music Genre Prediction
    |   |       genre-prediction.joblib
    |   |       intro.md
    |   |       music dataset.zip
    |   |       Music Prediction.ipynb
    |   |       music.csv
    |   |       visual-rep-Music-Recommender.dot
    |   |
    |   \---Video Game Sales Prediction
    |           archive.zip
    |           vgsales.csv
    |           Video game sales prediction.ipynb
    |
    +---Map Function
    |       Problem_1.py
    |       Problem_10.py
    |       Problem_11.py
    |       Problem_12.py
    |       Problem_13.py
    |       Problem_14.py
    |       Problem_15.py
    |       Problem_16.py
    |       Problem_17.py
    |       Problem_2.py
    |       Problem_3.py
    |       Problem_4.py
    |       Problem_5.py
    |       Problem_6.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Natural Language Processing
    |   \---NLTK
    |       +---Corpus
    |       |       Problem_1.py
    |       |       Problem_10.py
    |       |       Problem_11.py
    |       |       Problem_12.py
    |       |       Problem_13.py
    |       |       Problem_2.py
    |       |       Problem_3.py
    |       |       Problem_4.py
    |       |       Problem_5.py
    |       |       Problem_6.py
    |       |       Problem_7.py
    |       |       Problem_8.py
    |       |       Problem_9.py
    |       |
    |       \---Tokenization
    |               Problem_1.py
    |               Problem_2.py
    |               Problem_3.py
    |               Problem_4.py
    |               Problem_5.py
    |               Problem_6.py
    |               Problem_7.py
    |               Problem_8.py
    |               Problem_9.py
    |
    +---Notes
    |       classes.md
    |       DB.md
    |       Django.md
    |       excel_notes.md
    |       flask.md
    |       Interview_questions_prac.md
    |       postgresql.md
    |       postgresql_datawrapper.md
    |       python.md
    |       Python_mistakes_to_avoid.md
    |       Scrapy.md
    |
    +---OOP
    |   \---Class
    |       +---Basic Application
    |       |       Problem_1.py
    |       |       Problem_10.py
    |       |       Problem_11.py
    |       |       Problem_12.py
    |       |       Problem_2.py
    |       |       Problem_3.py
    |       |       Problem_4.py
    |       |       Problem_5.py
    |       |       Problem_6.py
    |       |       Problem_7.py
    |       |       Problem_8.py
    |       |       Problem_9.py
    |       |
    |       \---Basic Exercises
    |               Problem_1.py
    |               Problem_10.py
    |               Problem_11.py
    |               Problem_12.py
    |               Problem_2.py
    |               Problem_3.py
    |               Problem_4.py
    |               Problem_5.py
    |               Problem_6.py
    |               Problem_7.py
    |               Problem_8.py
    |               Problem_9.py
    |
    +---OS
    |       Problem_1.py
    |       Problem_10.py
    |       Problem_11.py
    |       Problem_12.py
    |       Problem_13.py
    |       Problem_14.py
    |       Problem_15.py
    |       Problem_16.py
    |       Problem_17.py
    |       Problem_18.py
    |       Problem_2.py
    |       Problem_3.py
    |       Problem_4.py
    |       Problem_5.py
    |       Problem_6.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Pickling_Unpickling
    |       Problem_1.py
    |       Problem_10.py
    |       Problem_11.py
    |       Problem_12.py
    |       Problem_13.py
    |       Problem_14.py
    |       Problem_15.py
    |       Problem_2.py
    |       Problem_3.py
    |       Problem_4.py
    |       Problem_5.py
    |       Problem_6.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Projects
    |   |   Project List.md
    |   |
    |   +---ContactBook
    |   |   |   .gitignore
    |   |   |   manage.py
    |   |   |   ReadMe.md
    |   |   |   requirements.txt
    |   |   |
    |   |   \---ContactBook
    |   |           asgi.py
    |   |           settings.py
    |   |           urls.py
    |   |           wsgi.py
    |   |           __init__.py
    |   |
    |   +---CRM
    |   |   |   .gitignore
    |   |   |   manage.py
    |   |   |   requirements.txt
    |   |   |
    |   |   +---djCRM
    |   |   |       asgi.py
    |   |   |       settings.py
    |   |   |       urls.py
    |   |   |       wsgi.py
    |   |   |       __init__.py
    |   |   |
    |   |   +---leads
    |   |   |   |   admin.py
    |   |   |   |   apps.py
    |   |   |   |   forms.py
    |   |   |   |   models.py
    |   |   |   |   tests.py
    |   |   |   |   urls.py
    |   |   |   |   views.py
    |   |   |   |   __init__.py
    |   |   |   |
    |   |   |   +---migrations
    |   |   |   |       0001_initial.py
    |   |   |   |       __init__.py
    |   |   |   |
    |   |   |   \---templates
    |   |   |       \---leads
    |   |   |               lead_create.html
    |   |   |               lead_details.html
    |   |   |
    |   |   \---templates
    |   |           lead_details.html
    |   |           lead_list.html
    |   |
    |   \---WebChatApp
    |       |   intro.md
    |       |   requirements.txt
    |       |
    |       \---Source
    |               index.html
    |               main.py
    |
    +---Pytest
    |   |   PyTest Notes.md
    |   |   pytest.ini
    |   |   test_api.py
    |   |   test_fixtures.py
    |   |   test_parameterized.py
    |   |   test_sample_cases.py
    |   |   test_suite_sample.py
    |   |
    |   \---__pycache__
    |           sample_TestCase.cpython-38-pytest-7.1.3.pyc
    |           sample_TestSuite.cpython-38-pytest-7.1.3.pyc
    |           sample_TestSuite.cpython-38.pyc
    |           test_api.cpython-38-pytest-7.1.3.pyc
    |           test_fixtures.cpython-38-pytest-7.1.3.pyc
    |           test_parameterized.cpython-38-pytest-7.1.3.pyc
    |           test_suite_sample.cpython-38-pytest-7.1.3.pyc
    |
    +---RE
    |       Problem_1.py
    |       Problem_10.py
    |       Problem_11.py
    |       Problem_12.py
    |       Problem_13.py
    |       Problem_14.py
    |       Problem_15.py
    |       Problem_16.py
    |       Problem_17.py
    |       Problem_18.py
    |       Problem_19.py
    |       Problem_2.py
    |       Problem_20.py
    |       Problem_21.py
    |       Problem_22.py
    |       Problem_23.py
    |       Problem_24.py
    |       Problem_25.py
    |       Problem_26.py
    |       Problem_27.py
    |       Problem_28.py
    |       Problem_29.py
    |       Problem_3.py
    |       Problem_30.py
    |       Problem_31.py
    |       Problem_32.py
    |       Problem_33.py
    |       Problem_34.py
    |       Problem_35.py
    |       Problem_36.py
    |       Problem_37.py
    |       Problem_38.py
    |       Problem_39.py
    |       Problem_4.py
    |       Problem_40.py
    |       Problem_41.py
    |       Problem_42.py
    |       Problem_43.py
    |       Problem_44.py
    |       Problem_45.py
    |       Problem_46.py
    |       Problem_47.py
    |       Problem_48.py
    |       Problem_49.py
    |       Problem_5.py
    |       Problem_50.py
    |       Problem_51.py
    |       Problem_52.py
    |       Problem_53.py
    |       Problem_54.py
    |       Problem_55.py
    |       Problem_56.py
    |       Problem_6.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Recursion
    |       Problem_1.py
    |       Problem_10.py
    |       Problem_11.py
    |       Problem_2.py
    |       Problem_3.py
    |       Problem_4.py
    |       Problem_5.py
    |       Problem_6.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Requests
    |       Problem_1.py
    |       Problem_2.py
    |       Problem_3.py
    |       Problem_4.py
    |       Problem_5.py
    |       Problem_6.py
    |       Problem_7.py
    |       Problem_8.py
    |       Problem_9.py
    |
    +---Web
    |       Project_1.py
    |       Project_10.py
    |       Project_11.py
    |       Project_12.py
    |       Project_2.py
    |       Project_3.py
    |       Project_4.py
    |       Project_5.py
    |       Project_6.py
    |       Project_7.py
    |       Project_8.py
    |       Project_9.py
    |
    \---Web scrapers
        +---BeautifulSoap_Project
        |       beautiful_soup.md
        |       main.py
        |       requirements.txt
        |       sample.py
        |
        +---BeautifulSoup
        |       Problem_1.py
        |       Problem_10.py
        |       Problem_11.py
        |       Problem_12.py
        |       Problem_13.py
        |       Problem_14.py
        |       Problem_15.py
        |       Problem_16.py
        |       Problem_17.py
        |       Problem_18.py
        |       Problem_19.py
        |       Problem_2.py
        |       Problem_20.py
        |       Problem_21.py
        |       Problem_22.py
        |       Problem_23.py
        |       Problem_24.py
        |       Problem_25.py
        |       Problem_26.py
        |       Problem_27.py
        |       Problem_28.py
        |       Problem_29.py
        |       Problem_3.py
        |       Problem_30.py
        |       Problem_31.py
        |       Problem_32.py
        |       Problem_33.py
        |       Problem_34.py
        |       Problem_35.py
        |       Problem_36.py
        |       Problem_4.py
        |       Problem_5.py
        |       Problem_6.py
        |       Problem_7.py
        |       Problem_8.py
        |       Problem_9.py
        |
        \---scrapy_project
            \---lightNovel_Scraper
                |   scrapy.cfg
                |
                \---lightNovel_Scraper
                    |   items.py
                    |   middlewares.py
                    |   pipelines.py
                    |   settings.py
                    |   __init__.py
                    |
                    +---spiders
                    |   |   LN_Scraper.py
                    |   |   __init__.py
                    |   |
                    |   \---__pycache__
                    |           LN_Scraper.cpython-39.pyc
                    |           __init__.cpython-39.pyc
                    |
                    \---__pycache__
                            items.cpython-39.pyc
                            settings.cpython-39.pyc
                            __init__.cpython-39.pyc
</details>

## Algorithms

<details>
<summary>  List of Algorithms  </summary>

    - Heap Queue
    - Searching
      - Binary Search
      - Linear Search
      - Sequential Search
      - Ternary Search
    - Sorting
      - Bubble Sort
      - Bucket Sort
      - Counting sort
      - Heap sort
      - Insertion sort
      - Merge sort
      - Quick sort
      - Radix sort
      - Selection sort
    - Backtracking
  
</details>

## Python Basics

## Control Structures

## Data Structures

## Date Time Module

## Enums Generators and Iterators

## File Handling

## Functional Programming

## Lambda Functions

## Object Oriented Programming

## Operation System (OS) Module

## Pickling Unpickling

## Pytests

## Regular Expressions

## Recursion

## 100 Days of Python

## Bash

## Batch

## Natural Language Processing

## Database

## Console Programs

## Covid-19 Project

## Geopy Library

## Json

## Mobile Application Development

### Kivy

### Beeware

## Request Library

## Web Frameworks

### Flask

### Django

### API Development

#### Fast API

#### Flask-Restful

#### Django-Restful

## Scrappers and Crawlers

## Projects

## Notes
