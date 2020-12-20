[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



[![Python][python-shield]][python-url]
[![XLRD][xlrd-shield]][xlrd-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Python Quiz Generator</h1>

  <p align="center">
    Simple tool to generate quizzes in the Python console.
    <br />
    <br />
    ·
    <a href="https://github.com/AlexAlvarez092/PY-Quiz-Generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/AlexAlvarez092/PY-Quiz-Generator/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This tool allows you to easy and quick generate quizzes. From an excel file containing the input information, it generates a couple of files: one containing plain text quiz and anothe one containing the answers.

![Key](https://github.com/AlexAlvarez092/PY-Quiz-Generator/blob/master/images/screenshots/key.png)

![Quiz](https://github.com/AlexAlvarez092/PY-Quiz-Generator/blob/master/images/screenshots/quiz.png)

### Built With

* [Python3][python-url]
* [XLRD][xlrd-url]



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Install requirements

### Installation

Do not need installation, just run quizGenerator.py file



<!-- USAGE EXAMPLES -->
## Usage

1. Fill the excel template with the raw data and properties
  - In the first sheet, put the raw data **without header**
  - In the second sheet, put configuration properties -- label already is in first column and the value goes in the second one.

2. Execute `quizGenerator.py` script in the Python3 console

### Input

Excel [file](https://github.com/AlexAlvarez092/PY-Quiz-Generator/blob/master/data.xlsx) with raw data

### Output

`./quiz.txt` file containing the generated quiz <br />
`./key.txt` file containing the answers



<!-- ROADMAP -->
## Roadmap

See the [open issues][issues-url] for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Alex Alvarez - <alexalvarez@mail.com>

Project Link: [https://github.com/AlexAlvarez092/PY-Quiz-Generator/][https://github.com/AlexAlvarez092/PY-Quiz-Generator/]

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Python][python-url]
* [XLRD][xlrd-url]




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AlexAlvarez092/PY-Quiz-Generator.svg?style=for-the-badge
[contributors-url]: https://github.com/AlexAlvarez092/PY-Quiz-Generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AlexAlvarez092/PY-Quiz-Generator.svg?style=for-the-badge
[forks-url]: https://github.com/AlexAlvarez092/PY-Quiz-Generator/network/members
[stars-shield]: https://img.shields.io/github/stars/AlexAlvarez092/PY-Quiz-Generator.svg?style=for-the-badge
[stars-url]: https://github.com/AlexAlvarez092/PY-Quiz-Generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/AlexAlvarez092/PY-Quiz-Generator.svg?style=for-the-badge
[issues-url]: https://github.com/AlexAlvarez092/PY-Quiz-Generator/issues
[license-shield]: https://img.shields.io/github/license/AlexAlvarez092/PY-Quiz-Generator.svg?style=for-the-badge
[license-url]: https://github.com/AlexAlvarez092/PY-Quiz-Generator/LICENSE.txt

[python-shield]: https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue
[python-url]: https://www.python.org/
[xlrd-shield]: https://img.shields.io/pypi/v/XLRD
[xlrd-url]: https://pypi.org/project/xlrd/

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alejandro-%C3%A1lvarez-garc%C3%ADa-365593124/
[github-followers-shield]: https://img.shields.io/github/followers/AlexAlvarez092?label=Follow&style=social
