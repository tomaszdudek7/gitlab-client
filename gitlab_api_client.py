import json
import urllib.parse
import urllib.request


class GitlabApi:
    def __init__(self, url: str, token: str):
        self.__url = url
        self.__token = token
        self.__api_root = '/api/v4'

    def all_projects(self):
        print("Getting list of all projects... This make take few moments.")
        projects = []
        per_page = 100
        current_page = 1

        while True:
            current_page_projects = self.__call('GET', "projects",
                                                per_page=per_page,
                                                page=current_page
                                                )

            current_page += 1
            projects += current_page_projects

            if len(current_page_projects) == 0 or len(current_page_projects) < per_page:
                break

        return projects

    def __call(self, method, api_path, **kwargs):
        query = ''
        if kwargs:
            query = '?' + urllib.parse.urlencode(kwargs)

        request = urllib.request.Request(self.__url + self.__api_root + "/" + api_path.lstrip("/") + query)
        request.add_header('Private-Token', self.__token)
        request.method = method

        return json.loads(urllib.request.urlopen(request).read())