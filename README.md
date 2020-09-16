![logo](https://raw.githubusercontent.com/giotto-ai/giotto-tda/master/doc/images/tda_logo.svg)

# gtda-challenge-2020
![CI](https://github.com/giotto-ai/gtda-challenge-2020/workflows/CI/badge.svg)

## Introduction
Welcome to the Giotto-tda use-cases challenge 2020. The purpose of this challenge is to create the best use-case of applied topology of the year! In order to participate to this challenge and have a chance to win, you have to submit a Jupyter Notebook to this repo (see [the section below](#submission-procedure)) with the following structure:
1. Introduction, i.e. where the problem is explained
2. Dataset, i.e. where the dataset is described
3. Analysis, i.e. where the steps of the analysis are highlighted and the central role played by [Giotto-tda](https://github.com/giotto-ai/giotto-tda) is explained
4. Short benchmark with comparable non-topological methods

Please have a look at the [example_notebook.ipynb](https://github.com/giotto-ai/gtda-challenge-2020/blob/master/example/example_notebook.ipynb) in the */example* folder.

## Subscription to the challenge
Anyone can take part to the challenge and participation is totally free: it is enough to send a PR (see [the section below](#submission-procedure)) and accept the CLA to be considered amongst the participants.

## A few rules
1. There are no constraints on the data type to be used
2. The dataset has to be public or publishable
3. The code shall run compatibly with ![Image](https://img.shields.io/badge/Python-3.8-blue.svg)
4. [Giotto-tda](https://github.com/giotto-ai/giotto-tda) has to play a central role in the analysis
5. Performance: the Jupyter notebooks will be automatically tested when the PR is submitted. Their running time shall not exceed the 15 minutes on the GitHub Actions machines (some tolerance margin can be applied to this fifth rule)
6. **For a PR to be acceptable, all the automatic tests have to pass and the CLA has to be accepted by the submitter.** An acceptable PR automatically subscribes the submitter to the challenge

## Submission procedure
1. The first step is to fork this repository
2. In the root folder of the cloned repository, in the master branch, create a new folder with your team leader's name (it is preferable if it coincides with the GitHub name of the team leader)
3. Inside the folder created at step 2, place **the unique Jupyter notebook** with the usecase (the file shall end with ```.ipynb```); the dataset and the auxilirary Python files (if needed) are also to be put in the same folder. **Large datasets (i.e. with a size larger than 10MB) shall be directly imported from external URLs or from data sharing platforms such as [OpenML](https://www.openml.org).**
4. If your project requires external ```pip installable``` libraries that are currently not amongst the [requirements.txt](https://github.com/giotto-ai/gtda-challenge-2020/blob/master/requirements.txt), you can include them at the beginning of your Jupyter notebook by adding a few lines similar to the the following ones:
```
# Install a pip package in the current Jupyter kernel
import sys
!{sys.executable} -m pip install numpy scipy torch
```

### Deadline
The final PR submission date and hour will have to take place before the 30th of October 2020 at 23:59 [CET](https://time.is/CET).

## Evaluation system
Each participant, Giotto-tda maintainer and Giotto-tda collaborator as well as the [L2F SA](https://www.giotto.ai) employees will vote (only once) on Google Form to express their preference for the three best notebooks. **The three preferences must all three be different: e.g. one cannot select the same Jupyter notebook for both first and second place. Such irregular votes will be discarded.**
*The link to the Google Form will be sent to those with voting rights soon after the 30th of October 2020.*

## Winner announcement and prizes
On the 9th of November the evaluation phase will end and the first three winners will be announced. A [Condorcet method](https://en.wikipedia.org/wiki/Condorcet_method) will be used to preapre the final classification. 
The prizes will be the following:
1. for the winner, 4000CHF
2. for the second, 1000CHF
3. for the third, 500CHF

The best three use-cases will be announced on the L2F SA social media and advertised through the web. The winner will also be contacted directly via email.

## Disclaimer
In case of irregularities, the sole and unique judge of this competition -- whose judgement is unquestionable -- will be [L2F SA](https://www.giotto.ai).

## Community
giotto-ai Slack workspace: https://slack.giotto.ai/

## Contact
maintainers@giotto.ai
