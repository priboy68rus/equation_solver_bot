import wolframalpha
import config

client = wolframalpha.Client(config.key)

# res = client.query("sin(x) + 2 cos(x) = -1")
keyword = "solution"

def wolfram_req(keyword, message):
    if keyword == "solution":
        return wolfram_equation(message)
    elif keyword == "plot":
        return wolfram_plot(message)
    else:
        return ""

def wolfram_equation(message):
    keyword = "solution"
    res = client.query(message)
    if int(res["@numpods"]) == 0:
        return ""
    pods_list = list(res.pods)
    ans = []
    for pod in pods_list:
        if keyword in pod["@title"].lower():
            if int(pod["@numsubpods"]) > 1:
                for subpod in pod["subpod"]:
                    ans.append(subpod["img"]["@src"])
            elif int(pod["@numsubpods"]) > 0:
                img = pod["subpod"]["img"]["@src"]
                ans.append(img)
    return ans if len(ans) else ""


def wolfram_plot(message):
    keyword = "plot"
    res = client.query(message)
    if int(res["@numpods"]) == 0:
        return ""
    pods_list = list(res.pods)
    ans = []
    for pod in pods_list:
        if keyword in pod["@title"].lower():
            
            if int(pod["@numsubpods"]) > 1:
                for subpod in pod["subpod"]:
                    ans.append(subpod["img"]["@src"])
            elif int(pod["@numsubpods"]) > 0:
                img = pod["subpod"]["img"]["@src"]
                ans.append(img)
    return ans if len(ans) else ""