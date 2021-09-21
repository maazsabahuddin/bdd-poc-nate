# Python imports
import datetime

# Framework imports


def open_file(name, mod):
    """
    :param name:
    :param mod:
    :return:
    """
    if not (name and mod):
        return
    return open(name, mod)


def close_file(f):
    f.close()


def erase_file_content():
    f = open_file(name="result.txt", mod="w")
    close_file(f)
    return True


def read_file_and_append_result():
    from app import log_site, sites, log_flag

    f = open_file(name="result.txt", mod="r")
    content = f.read()
    first_line = content.splitlines()[0]
    passed_sites = first_line.split(",")
    passed_sites.pop()
    close_file(f)

    automation_result_file = open_file(name="automation_result.txt", mod="a")
    if erase_file_content():
        current_datetime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        automation_result_file.write(f"Date and Time: {current_datetime} \n") if log_flag else None

    _result_sites = {}
    failed_sites = set(sites.keys()) - set(passed_sites)

    for _site in passed_sites:
        automation_result_file.write(f"Site: {_site} - PASSED\n") if log_flag else None
        _result_sites.update({_site: "PASSED"})

    for _site in failed_sites:
        automation_result_file.write(f"Site: {_site} - FAILED\n") if log_flag else None
        _result_sites.update({_site: "FAILED"})

    automation_result_file.write("\n") if log_flag else None
    log_site(_site="Result", message="Automation")
    print(_result_sites)
    close_file(automation_result_file)
