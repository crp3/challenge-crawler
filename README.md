# challenge-crawler
Repo containing some scraping agents

## Requirements
Python version >= 3.8
virtualenv version >= 20.14.1
poetry version >= 1.1.13

OR

Docker version >= 20.10.14

## Installation
To install the requirements for this project, just run 

` poetry install `

The command above will create a separate virtual environment for the project and install the dependencies there. In case you have any issues with your virtualenv version (e.g. having one version installed by `pip` and another version installed by `apt`), you can run 

` poetry install --no-dev `

And that will install the dependencies directly into the machine, without creating any other virtual environment.


### Installation via Docker

For this project, you can also install all you need for this project in a containerized environment. For that, just run 

`docker build . -t <IMAGE_TAG>`

That will create an image containing the environment and all necessary dependencies for the project. You can name the image tag the way you want. Locally, I chose to name it `challenge-crawler`. So the way I built it was:

`docker build . -t challenge-crawler`

## Running
Once your environment is complete, you can run this project in the following way:

`python main.py`

and select the options you want. 

To flash the information on the console, add

`--print`

To save it to a `.json` file, add

`--save_json` - this command will save the output to `machines.json`

To save it to a `.csv` file, add 

`--save_csv` - this command will save the output to `machines.csv`

All of the options are independent, so you can add multiple of the above or none. So, for instance, all of the examples below are valid.

`python main.py --print --save_json`
`python main.py --save_csv`
`python main.py --save_json --save_csv --print`
`python main.py`

### Running via Docker
The entrypoint for this docker image considers all of the options above as options. However, the output files will be generated in a containerized environment. So, if you just run

`docker run challenge-crawler` 

The output will be shown on the console, but the files will be lost, since there is no volume persistence for this image. So, in order to see the full results, one could run

`docker run -it challenge-crawler bash`

To access the bash console inside the container.
Once there, it is possible to just type 

`python main.py --print --save_json`, for example, and see the `machines.json` file there!

## Testing

To test this project, run 

`python -m unittest`

To see all modules tested, run 

`python -m unittest -v`
