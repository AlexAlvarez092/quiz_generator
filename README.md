[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/AlexAlvarez092/PY-Quiz-Generator>
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Python Quiz Generator</h3>

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

<img src="tree/master/README/screenshots/key.png" alt="Key" width="600" height="400> <br />

<img src="tree/master/README/screenshots/quiz.png" alt="Quiz" width="600" height="400">

### Built With

* [Python3](https://www.python.org/download/releases/3.0/)
* [XLRD](https://pypi.org/project/xlrd/)


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

Excel [file](https://github.com/AlexAlvarez092/PY-Quiz-Generator/data.xlsx) with raw data

### Output

`./quiz.txt` file containing the generated quiz <br />
`./key.txt` file containing the answers


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/AlexAlvarez092/PY-Quiz-Generator/issues) for a list of proposed features (and known issues).



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

Project Link: [https://github.com/AlexAlvarez092/PY-Quiz-Generator/issues](https://github.com/AlexAlvarez092/PY-Quiz-Generator/issues)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Python3 Documentation](https://www.python.org/doc/)
* [XLRD Documentation](https://pypi.org/project/xlrd/)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/AlexAlvarez092/PY-Quiz-Generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/AlexAlvarez092/PY-Quiz-Generator/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/AlexAlvarez092/PY-Quiz-Generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/AlexAlvarez092/PY-Quiz-Generator/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/AlexAlvarez092/PY-Quiz-Generator/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alejandro-%C3%A1lvarez-garc%C3%ADa-365593124/
