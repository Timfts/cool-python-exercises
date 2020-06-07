from subprocess import check_call


def generate_requirements():
    check_call(['poetry export -f requirements.txt > requirements.txt'], shell=True)
