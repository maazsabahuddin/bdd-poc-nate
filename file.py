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

    success_ratio = get_success_ratio(passed_sites)
    automation_result_file.write(f"\nPassed sites: {len(passed_sites)}\n") if log_flag else None
    automation_result_file.write(f"Failed sites: {len(failed_sites)}\n") if log_flag else None
    automation_result_file.write(f"Total sites: {len(sites)}\n") if log_flag else None
    automation_result_file.write(f"Success rate: {success_ratio}\n\n") if log_flag else None
    automation_result_file.write(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n") if log_flag else None
    log_site(_site="Result", message="Automation")
    print(_result_sites)
    print(f"Passed sites: {len(passed_sites)}")
    print(f"Failed sites: {len(failed_sites)}")
    print(f"Total sites: {len(sites)}")
    print(f"Success rate: {success_ratio}")
    close_file(automation_result_file)


def get_success_ratio(passed_sites):
    from app import sites
    return str(_format_percentage((len(passed_sites) / len(sites)) * 100))+"%"


def _format_percentage(value):
    return '{:.2f}'.format(float(value))
